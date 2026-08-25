# -*- coding: utf-8 -*-
"""Den stora jämförelsetabellen — filter, priser och utfällbara detaljer.

VAD DEN GÖR
Listar samtliga bolag med pris per skyddsnivå, oberoende betyg och en
utfällbar detaljvy med bedömning, villkorsfakta, omfattningsmatris,
självrisker och tilläggsförsäkringar.

TRE SAKER SOM SKILJER DEN FRÅN KONKURRENTERNAS
1. Underlaget redovisas. Där en siffra saknas står "—" och en rad om
   varför, i stället för ett påhittat "från"-pris.
2. Omfattningsmatrisen är märkt som branschstandard, inte som bolagets
   exakta villkor, tills någon läst just det bolagets villkor.
3. Sorteringen bygger på publicerade betyg, inte på vem som betalar
   mest i provision. Ordningen ändras inte av ett affiliateavtal.

TEKNIK
Detaljvyn är <details>/<summary> — den fungerar utan JavaScript och
innehållet finns i HTML från början, alltså indexerbart. Filtren är
progressiv förbättring: utan JS visas alla tre priskolumnerna, vilket
är det fullständiga läget.

FYLL PÅ
Priser i data.PRIS, självrisker i data.SJALVRISK, villkorsfakta i
data.VILLKOR, tillägg i data.TILLAGG. Allt slår igenom automatiskt.
"""
from companies import BOLAG
import data
import kort

NIVAER = [('alla', 'Alla'), ('trafik', 'Trafik'),
          ('halv', 'Halvförsäkring'), ('hel', 'Helförsäkring')]

# Bolag med egen logotyp. Övriga får en monogramplatta.
LOGOTYPER = {'gofido', 'dina-forsakringar', 'ica-forsakring'}

AFF = {p['slug']: p.get('aff', '') for p in kort.PARTNERS}


def _logo(b):
    if b['slug'] in LOGOTYPER:
        return (f'<div class="jf-logo"><img src="/assets/logotyper/{b["slug"]}.webp" '
                f'alt="{b["namn"]}" width="104" height="30" loading="lazy" '
                f'decoding="async"></div>')
    ord_ = b['namn'].replace('-', ' ').split()
    initialer = (ord_[0][0] + ord_[1][0]) if len(ord_) > 1 else ord_[0][:2]
    initialer = initialer.upper()
    return f'<div class="jf-logo"><span class="jf-mono">{initialer}</span></div>'


def _punkter(b):
    """Tre korta punkter ur bolagets egna fakta — unika per bolag."""
    ut = []
    if b.get('kons'):
        ut.append(f'Villkorsbetyg {str(b["kons"]).replace(".", ",")} av 5')
    for rubrik, _ in b.get('fakta', [])[:3]:
        ut.append(rubrik)
    if b.get('typ'):
        ut.append(b['typ'] + ' bolag')
    return ut[:3]


def _betygsruta(b):
    tp = data.TRUSTPILOT.get(b['slug'], {})
    if tp.get('betyg'):
        antal = f'{tp["antal"]:,}'.replace(',', '\u00a0') + ' omd.' if tp.get('antal') else ''
        return (f'<div class="jf-betyg"><strong>{data.betyg(tp["betyg"])}</strong>'
                f'<span>av 5</span><small>{antal}<br>Trustpilot</small></div>')
    if b.get('kons'):
        return (f'<div class="jf-betyg"><strong>{data.betyg(b["kons"])}</strong>'
                f'<span>av 5</span><small>Konsumenternas<br>villkorsbetyg</small></div>')
    if b.get('ski'):
        return (f'<div class="jf-betyg"><strong>{data.betyg(b["ski"])}</strong>'
                f'<span>av 100</span><small>Kundnöjdhet<br>SKI</small></div>')
    return ('<div class="jf-betyg tom"><strong>—</strong>'
            '<small>Deltar inte i de<br>oberoende mätningarna</small></div>')


def _prisrad(niva, etikett, belopp):
    v = data.kr(belopp, per_manad=True) if belopp else '—'
    txt = f'Från {v}/mån' if belopp else '—'
    return (f'<div class="jf-pris" data-niva="{niva}">'
            f'<span>{etikett}</span><strong>{txt}</strong></div>')


def _bock(v):
    return '<span class="ja">&#10003;</span>' if v else '<span class="nej">&ndash;</span>'


def _detaljer(b):
    s = b['slug']
    v = data.VILLKOR.get(s, {})
    sr = data.SJALVRISK.get(s, {})
    tl = data.TILLAGG.get(s, {})

    passar = ''.join(f'<li>{x}</li>' for x in b.get('passar', [])[:3])
    passar_ej = ''.join(f'<li>{x}</li>' for x in b.get('passar_ej', [])[:3])

    villkor = ''.join(
        f'<div><span>{namn}</span><strong>{v.get(nyckel) or "Uppgift saknas"}</strong></div>'
        for nyckel, namn in (('bindningstid', 'Bindningstid'),
                             ('maskin', 'Maskinskada gäller till'),
                             ('verkstad', 'Verkstadsval')))

    moment = ''.join(
        f'<tr><th scope="row">{namn}</th><td>{_bock(t)}</td><td>{_bock(h)}</td>'
        f'<td>{_bock(he)}</td></tr>' for namn, t, h, he in data.MOMENT)

    sjalvrisk = ''.join(
        f'<div><span>{namn}</span><strong>{data.kr(sr.get(nyckel))}</strong></div>'
        for nyckel, namn in data.SJALVRISK_NAMN)

    tillagg = ''.join(
        f'<div><span>{namn}</span><strong>'
        f'{"Ja" if tl.get(nyckel) else ("Nej" if tl.get(nyckel) is False else "—")}'
        f'</strong></div>' for nyckel, namn in data.TILLAGG_NAMN)

    return f'''<details class="jf-det"><summary><span class="jf-sum-a">Visa detaljer</span>
<span class="jf-sum-b">Dölj detaljer</span></summary><div class="jf-det-in">

<h4>Vår bedömning</h4>
<p>{b["sammanfattning"]}</p>
<div class="jf-tva">
<div><h5>Passar dig som</h5><ul class="jf-ja">{passar}</ul></div>
<div><h5>Passar mindre bra om</h5><ul class="jf-nej">{passar_ej}</ul></div>
</div>

<h4>Villkor i korthet</h4>
<div class="jf-fakta">{villkor}</div>

<h4>Vad som ingår per nivå</h4>
<div class="tbl"><table class="jf-matris"><thead><tr><th scope="col">Moment</th>
<th scope="col">Trafik</th><th scope="col">Halv</th><th scope="col">Hel</th></tr></thead>
<tbody>{moment}</tbody></table></div>
<p class="jf-not">Tabellen visar standardomfattningen på den svenska marknaden. Enskilda
bolag kan avvika på enstaka moment — läs alltid villkoren innan du tecknar.</p>

<h4>Självrisker</h4>
<div class="jf-fakta">{sjalvrisk}</div>

<h4>Tilläggsförsäkringar</h4>
<div class="jf-fakta">{tillagg}</div>

<p class="jf-mer"><a href="/forsakringsbolag/{s}/">Läs hela genomgången av {b["namn"]}
&#8594;</a></p>
</div></details>'''


def _rad(b, i):
    s = b['slug']
    p = data.PRIS.get(s, {})
    punkter = ''.join(f'<li>{x}</li>' for x in _punkter(b))
    priser = (_prisrad('trafik', 'Trafik', p.get('trafik'))
              + _prisrad('halv', 'Halv', p.get('halv'))
              + _prisrad('hel', 'Hel', p.get('hel')))

    if AFF.get(s):
        cta = (f'<a class="jf-cta" href="{AFF[s]}" rel="sponsored nofollow noopener" '
               f'target="_blank">Se ditt pris &#8594;</a>')
        under = '<span class="jf-under">Annonslänk</span>'
    else:
        cta = f'<a class="jf-cta" href="/forsakringsbolag/{s}/">Läs om {b["namn"]} &#8594;</a>'
        under = '<span class="jf-under">Vår genomgång</span>'

    sortvarden = ' '.join(f'data-{n}="{p.get(n) or 0}"' for n in ('trafik', 'halv', 'hel'))
    return f'''<article class="jf-rad" {sortvarden}>
<div class="jf-topp">
{_logo(b)}
<div class="jf-namn"><h3>{b["namn"]} bilförsäkring</h3><ul>{punkter}</ul></div>
<div class="jf-priser">{priser}</div>
{_betygsruta(b)}
<div class="jf-cta-kol">{cta}{under}</div>
</div>
{_detaljer(b)}
</article>'''


def sektion(rubrik='Jämför alla bolag', ingress=None):
    ordnade = sorted(BOLAG, key=lambda b: -((b.get('kons') or 0) * 20 + (b.get('ski') or 0)))
    rader = ''.join(_rad(b, i) for i, b in enumerate(ordnade))
    knappar = ''.join(
        f'<button type="button" class="jf-filt{" pa" if n == "alla" else ""}" '
        f'data-niva="{n}" aria-pressed="{"true" if n == "alla" else "false"}">{t}</button>'
        for n, t in NIVAER)

    if ingress is None:
        ingress = ('Samtliga bolag med oberoende betyg, villkor och självrisker. Fäll ut '
                   'ett bolag för att se vad som ingår på varje nivå.')

    saknas = ''
    if not data.har_priser():
        saknas = ('<div class="warn"><strong>Priserna samlas in.</strong> Vi publicerar '
                  'inga "från"-priser förrän vi hämtat dem själva på samma bil och '
                  'förarprofil hos varje bolag. Tills dess står det streck. '
                  '<a href="/redaktionell-metod/">Så går insamlingen till</a>.</div>')

    return f'''<section class="sec jf-sek"><div class="wrap">
<h2>{rubrik}</h2>
<p class="jf-ing">{ingress}</p>
{saknas}
<div class="jf-filter" role="group" aria-label="Filtrera på skyddsnivå">{knappar}</div>
<div class="jf-lista" id="jf-lista">{rader}</div>
<p class="jf-fot">Sorterat på oberoende betyg, inte på ersättning. Priser avser
{data.PROFIL_TEXT}. Senast kontrollerad: {data.UPPDATERAD_TEXT}.</p>
</div></section>'''
