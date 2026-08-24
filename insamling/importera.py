#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Läser in prisunderlag.csv och skriver insamlat.py, som data.py plockar upp.

KÖR SÅ HÄR
    cd insamling && python3 importera.py

Skriptet validerar innan det skriver. Hittar det något orimligt säger det
till och avbryter — det är billigare att fånga en felskrivning här än att
upptäcka den när sidan ligger ute.

VALIDERINGAR
  • Okänd bolagsslug            → avbryter
  • Hel < halv, eller halv < trafik → avbryter (nivåerna bygger på varandra)
  • Premie utanför 500–40 000 kr/år → avbryter (troligen månadspris eller nolla för mycket)
  • Trustpilot utanför 1,0–5,0  → avbryter
  • Pris utan datum och källa   → avbryter (E-E-A-T kräver spårbarhet)
"""
import csv
import os
import sys

HAR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HAR))
from companies import BOLAG                                    # noqa: E402

GILTIGA = {b['slug'] for b in BOLAG}
FEL = []


def tal(v, rad, falt, heltal=True):
    v = (v or '').strip().replace(' ', '').replace('\u00a0', '').replace(',', '.')
    if not v:
        return None
    try:
        return int(round(float(v))) if heltal else round(float(v), 1)
    except ValueError:
        FEL.append(f'{rad}: {falt} är inte ett tal ("{v}")')
        return None


def main():
    pris, trust, sjalv, kalla = {}, {}, {}, {}

    with open(os.path.join(HAR, 'prisunderlag.csv'), encoding='utf-8-sig') as f:
        for r in csv.DictReader(f, delimiter=';'):
            slug = (r['bolag_slug'] or '').strip()
            if not slug:
                continue
            if slug not in GILTIGA:
                FEL.append(f'{slug}: okänd bolagsslug — finns inte i companies.py')
                continue

            t = tal(r['trafik_kr_ar'], slug, 'trafik')
            h = tal(r['halv_kr_ar'], slug, 'halv')
            he = tal(r['hel_kr_ar'], slug, 'hel')

            for namn, v in (('trafik', t), ('halv', h), ('hel', he)):
                if v is not None and not (500 <= v <= 40000):
                    FEL.append(f'{slug}: {namn} = {v} kr/år ligger utanför rimligt '
                               f'intervall — är det ett månadspris?')
            if h is not None and t is not None and h < t:
                FEL.append(f'{slug}: halvförsäkring ({h}) billigare än trafik ({t})')
            if he is not None and h is not None and he < h:
                FEL.append(f'{slug}: helförsäkring ({he}) billigare än halv ({h})')

            datum = (r['hamtad_datum'] or '').strip()
            kall = (r['kalla_url'] or '').strip()
            if any(v is not None for v in (t, h, he)) and not (datum and kall):
                FEL.append(f'{slug}: pris angivet utan hämtat datum och källa')

            tb = tal(r['trustpilot_betyg'], slug, 'trustpilot_betyg', heltal=False)
            if tb is not None and not (1.0 <= tb <= 5.0):
                FEL.append(f'{slug}: trustpilot_betyg = {tb} ligger utanför 1,0–5,0')

            pris[slug] = {'trafik': t, 'halv': h, 'hel': he}
            trust[slug] = {'betyg': tb, 'antal': tal(r['trustpilot_antal'], slug, 'antal')}
            sjalv[slug] = {k: tal(r[f'sjalvrisk_{k}'], slug, f'sjalvrisk_{k}')
                           for k in ('trafik', 'vagn', 'glas', 'stold', 'maskin')}
            kalla[slug] = {'hamtad': datum or None, 'kalla': kall or None}

    if FEL:
        print('\nAVBRYTER — rätta det här först:\n')
        for f in FEL:
            print('  •', f)
        print()
        sys.exit(1)

    ut = ['# -*- coding: utf-8 -*-',
          '"""GENERERAD FIL — skriv inte här.',
          '',
          'Skapad av insamling/importera.py utifrån prisunderlag.csv.',
          'Redigera CSV:n och kör om skriptet i stället.',
          '"""', '']
    for namn, d in (('PRIS', pris), ('TRUSTPILOT', trust),
                    ('SJALVRISK', sjalv), ('KALLA', kalla)):
        ut.append(f'{namn} = {{')
        for slug, v in d.items():
            ut.append(f'    {slug!r}: {v!r},')
        ut.append('}')
        ut.append('')

    mal = os.path.join(os.path.dirname(HAR), 'insamlat.py')
    open(mal, 'w', encoding='utf-8').write('\n'.join(ut))

    n_pris = sum(1 for v in pris.values() if v['hel'])
    n_tp = sum(1 for v in trust.values() if v['betyg'])
    n_sr = sum(1 for v in sjalv.values() if any(v.values()))
    print(f'\nSkrev insamlat.py')
    print(f'  Priser (helförsäkring): {n_pris} av {len(GILTIGA)} bolag')
    print(f'  Trustpilot:             {n_tp} av {len(GILTIGA)} bolag')
    print(f'  Självrisker:            {n_sr} av {len(GILTIGA)} bolag')
    print('\nKör nu:  cd .. && python3 build.py')
    if n_pris >= 5 and n_tp >= 5:
        print('\nUnderlaget räcker nu för att topplistan ska publiceras med '
              'placeringssiffror.')


if __name__ == '__main__':
    main()
