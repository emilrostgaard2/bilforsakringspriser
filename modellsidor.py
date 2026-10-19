# -*- coding: utf-8 -*-
"""Modellsidor — /bilmarken/<märke>/<modell>/.

UNIKHET ÄR HELA POÄNGEN MED DEN HÄR FILEN
Modellsidor är den sidtyp som lättast blir mallutfyllnad. Tidigare
versioner bar tolv generiska block (nivåtabell år för år, självrisk-
räkneexempel, checklista, villkorstabell, åtgärdslista, generisk FAQ)
som stod på alla sidor och gjorde att två slumpvisa modellsidor delade
ungefär en tredjedel av sin text. De blocken är borta. Regeln är nu:

1. Varje stycke i brödtexten ska komma ur modellens egna fält i
   modeller*.py / modeller_extra*.py, eller vara en mening som byggs av
   de fälten (segment, drivlina, årsmodeller, prisklass, syskon).
2. Allmän kunskap som gäller alla bilar står på guidesidorna. Här länkas
   den med en mening, den skrivs inte av.
3. FAQ innehåller bara frågor vars svar kommer ur modelldata.

Mät efter varje större ändring: 5-ordsshinglar på <main>-texten,
Jaccard per modellpar. Mål: snitt under 0,15 och inget par över 0,35.

ANNONSKORTEN
Dina Försäkringars regler förbjuder ord som bäst, billigast, trygg,
säker, heltäckande, rankning/betyg och rådgivning i anslutning till
deras annons. Därför står korten direkt efter prisuppgiften och en
neutral övergångsmening, följda av en faktatabell — och källtabellen
med andra sajters namn ligger längst ned, långt från korten.
"""
from modellkatalog import MODELLER
from modeller_extra import PRISER, SPANN, EXTRA as _E1, META as _META1
from modeller_extra_2 import EXTRA_2 as _E2
from modeller_extra_skoda import EXTRA_SKODA as _E3
from modeller_extra_vw import EXTRA_VW as _E4
from modeller_extra_4 import EXTRA_4 as _E5
from modeller_extra_audi import EXTRA_AUDI as _E6
from modeller_extra_peugeot import EXTRA_PEUGEOT as _E7
from modeller_extra_bmw import EXTRA_BMW as _E8
from modeller_extra_kia import EXTRA_KIA as _E9
from modeller_extra_toyota import EXTRA_TOYOTA as _E10
from modeller_extra_mercedes import EXTRA_MERCEDES as _E11

EXTRA = {**_E1, **_E2, **_E3, **_E4, **_E5, **_E6, **_E7, **_E8, **_E9, **_E10, **_E11}
META = {**_META1,
        **{k: v['meta'] for k, v in _E2.items() if v.get('meta')},
        **{k: v['meta'] for k, v in _E3.items() if v.get('meta')},
        **{k: v['meta'] for k, v in _E4.items() if v.get('meta')},
        **{k: v['meta'] for k, v in _E5.items() if v.get('meta')},
        **{k: v['meta'] for k, v in _E6.items() if v.get('meta')},
        **{k: v['meta'] for k, v in _E7.items() if v.get('meta')},
        **{k: v['meta'] for k, v in _E8.items() if v.get('meta')},
        **{k: v['meta'] for k, v in _E9.items() if v.get('meta')},
        **{k: v['meta'] for k, v in _E10.items() if v.get('meta')},
        **{k: v['meta'] for k, v in _E11.items() if v.get('meta')}}
from brands import MARKEN
import data
import kort
import uppskattning as upp

MARKE = {m['slug']: m for m in MARKEN}


# ─── Namn ─────────────────────────────────────────────────────────
def namn(m, mod):
    """'Polestar 2' ska inte bli 'Polestar Polestar 2'."""
    if mod['namn'].lower().startswith(m['namn'].lower()):
        return mod['namn']
    return f'{m["namn"]} {mod["namn"]}'


import re as _re

# Fält ur datamodulerna som visas på sidan. Flera modeller (tvillingar
# som GLE/X5, Picanto/i10) har fått nästan identiska stycken med bara
# namnet utbytt. En mening vars 5-ordsshinglar till minst hälften redan
# förekommit hos en tidigare modell i katalogen visas bara på den första
# sidan. Inget skrivs om — meningar stryks bara där de är dubbletter.
_TEXTFALT = ('direktsvar', 'agare', 'teknik', 'jamfor', 'kostnad', 'vinkel', 'skada', 'varde',
             'niva')
_DUBBEL_GRANS = 0.5
_GOLV_ORD = 260
_GOLV_ORDNING = ('teknik', 'agare', 'vinkel', 'skada', 'jamfor', 'varde', 'niva', 'kostnad',
                 'direktsvar', 'fraga_svar', 'lang_svar', 'lang2_svar')


def _shinglar(t):
    w = _re.findall(r'\w+', t.lower())
    return {' '.join(w[k:k + 5]) for k in range(len(w) - 4)}


def _normalisera(t, ord_):
    for o in sorted(ord_, key=len, reverse=True):
        if o:
            t = _re.sub(r'(?<!\w)' + _re.escape(o) + r'(?!\w)', 'MODELL', t, flags=_re.I)
    return t


def _rensa_dubbletter():
    sett = set()
    ut = {}
    for marke_slug, lista in MODELLER.items():
        mn = MARKE[marke_slug]['namn']
        for mod in lista:
            e = EXTRA.get(mod['slug'], {})
            ord_ = {mn, mod['namn'], f'{mn} {mod["namn"]}', mod['slug'].replace('-', ' ')}
            falt = {}
            nya = set()
            kallor = {k: (e.get(k) if k in e else mod.get(k, '')) for k in _TEXTFALT}
            for par in ('lang', 'lang2'):
                if e.get(par):
                    kallor[par + '_svar'] = e[par][1]
            kallor['fraga_svar'] = mod['fraga'][1]
            for k, text in kallor.items():
                if not text:
                    falt[k] = []
                    continue
                delar = []
                for mening in _re.split(r'(?<=[.!?])\s+', text.strip()):
                    s = _shinglar(_normalisera(mening, ord_))
                    dubbel = bool(s) and len(s & sett) / len(s) >= _DUBBEL_GRANS
                    delar.append([mening, not dubbel, s])
                falt[k] = delar
            # Golv: blir sidan för tunn återställs strukna meningar i
            # prioritetsordning tills golvet nås. Tvillingmodeller får då
            # viss överlappning, men ingen sida töms.
            ord_kvar = lambda: sum(len(m_[0].split()) for d in falt.values() for m_ in d if m_[1])
            for k in _GOLV_ORDNING:
                for m_ in falt.get(k, []):
                    if ord_kvar() >= _GOLV_ORD:
                        break
                    m_[1] = True
            for d in falt.values():
                for m_ in d:
                    if m_[1]:
                        nya |= m_[2]
            sett |= nya
            ut[mod['slug']] = {k: ' '.join(m_[0] for m_ in d if m_[1]) for k, d in falt.items()}
    return ut


def _v(pool, i, mult=1, add=0):
    return pool[(i * mult + add) % len(pool)]


# ─── Rubriker (korta, roterade) ───────────────────────────────────
PRIS_H2 = ['Vad kostar det att försäkra en {b}?', '{b} — prisbild', 'Försäkringspris för {b}',
           'Premien på en {b}', 'Kostnaden för en {b}-försäkring']
STYR_H2 = ['{b} i bolagens modelldata', 'Det här styr premien på din {b}',
           'Varför {b} prissätts som den gör', 'Modellens egna premiedrivare',
           'Vad bolagen tittar på hos {b}']
AGARE_H2 = ['Vem kör en {b}?', 'Så används en {b}', 'Ägarprofilen bakom premien',
            'Vilka kör den här bilen?', 'Bilens vardag avgör priset']
TEKNIK_H2 = ['Reparationsbilden för {b}', 'Vad som gör en {b} dyr eller billig att laga',
             'Under plåten — det som kostar vid en skada', 'Teknik, verkstad och skadebild',
             'Skadorna och reparationerna på {b}']
JAMFOR_H2 = ['{b} jämfört med konkurrenterna', 'Hur står sig {b} mot alternativen?',
             '{b} mot liknande bilar', 'Premien i jämförelse med klassen',
             'Vad kostar konkurrenterna?']
SYSKON_H2 = ['Jämför {m}-modellerna', 'Övriga {m}-modeller och deras premie',
             'Hur ligger resten av {m}-utbudet?', 'Andra {m} att jämföra med',
             '{m}-modellerna sida vid sida']
NIVA_H2 = ['Vilken skyddsnivå passar en {b}?', 'Halv- eller helförsäkring på {b}?',
           'Rätt skyddsnivå för {b}', 'Värdet och skyddsnivån', 'När räcker halvförsäkring?']
KOSTNAD_H2 = ['{b} i den totala ägarkostnaden', 'Var försäkringen hamnar bland bilkostnaderna',
              'Vad {b} kostar utöver premien', 'Försäkringen som andel av driftkostnaden',
              'Helhetsbilden av vad bilen kostar']
KALLA_H2 = ['Källor till prisuppgifterna', 'Prisexempel och källor', 'Varifrån siffrorna kommer',
            'Publicerade prisexempel med källa']

KALLA_INGEN = [
 'Vi har inte hittat publicerade prisuppgifter för specifikt {b}, så spannet bygger på '
 'marknadens siffror och modellens prisklass.',
 'Modellspecifika prisexempel för {b} saknas i de källor vi gått igenom. Spannet är därför '
 'härlett ur marknadens nivåer och prisklassen.',
 'För {b} finns ännu inga publicerade exempel med angiven profil. Uppskattningen vilar på '
 'marknadsnivåerna nedan.',
 'Ingen av källorna redovisar {b} separat, och spannet utgår i stället från prisklassen och '
 'de marknadsnivåer som listas här.',
]

FORE_KORT = [
 'Här nedan visas två bolag som tar emot offertförfrågningar på {b}.',
 'Två bolag där du kan begära offert på {b} följer här.',
 'Nedan finns två bolag som offererar {b} på registreringsnumret.',
 'Offert på {b} kan begäras hos bolagen nedan.',
 'Bolagen nedan tar emot förfrågningar om försäkring av {b}.',
]

KLASS_MENING = [
 'Spannet utgår från att {b} placeras i {k}: {t}.',
 'Vi placerar {b} i {k} — {t}.',
 '{b} hamnar i {k} i vår uppskattning, vilket betyder {t}.',
 'Klassningen av {b} är {k}, eftersom modellen har {t}.',
]

BEG_FLERA = [
 'Köper du {b} begagnad finns den som {d}, så kontrollera att offerten anger rätt drivlina '
 'och årsmodell — de styr ersättningsvärdet. ',
 'En begagnad {b} kan vara {d}; fel drivlina i offerten ger fel ersättningsvärde. ',
 'Eftersom {b} säljs som {d} är drivlinan det första att stämma av i offerten vid ett '
 'begagnatköp. ',
]
BEG_EN = [
 'Köper du {b} begagnad: ange din egen körsträcka, inte bilens historik. ',
 'Vid köp av en begagnad {b} är det din körsträcka som ska stå i offerten, inte den '
 'föregående ägarens. ',
 'Den begagnade {b}:ns mätarställning påverkar inte din premie — din egen körsträcka gör. ',
]

VINKEL_H2 = ['Så prissätts {b}', 'Premien på {b} i korthet', 'Varför {b} kostar det den gör',
             'Det som skiljer {b} i premie', 'Vad bolagen räknar med på {b}']

# Ord som inte får stå i anslutning till Dina Försäkringars annons.
_FORBJUDET = _re.compile(r'(?<!\w)(bäst\w*|billigast\w*|trygg\w*|säker(t|a|het\w*)?|heltäck\w*|'
                         r'rank\w*|rating\w*|betyg\w*|välj\w*|rekommender\w*)(?!\w)', _re.I)

KLASS_NAMN = {
    'budget': 'låg prisklass', 'volym': 'volymklassen', 'stor': 'klassen för stora bilar',
    'premium': 'premiumklassen', 'elbil': 'elbilsklassen', 'elbil-stor': 'klassen för stora elbilar',
    'prestanda': 'prestandaklassen',
}

# Varierade ankartexter mot jämförelsesidorna — aldrig samma exakta
# fras på alla sidor.
JMF_LANK = [
 ('/billigaste-bilforsakringen/', 'vilka bolag som brukar ligga lågt i pris',
  'Vill du se {a} på en standardprofil, oavsett bilmodell, finns det samlat i en egen genomgång.'),
 ('/basta-bilforsakringen/', 'jämförelsen av bolagen',
  'Hur bolagen skiljer sig i villkor och service, oberoende av bil, står i {a}.'),
 ('/billigaste-bilforsakringen/', 'genomgången av låga premier',
  'Vilka faktorer som ger lägst premie generellt beskrivs i {a}.'),
 ('/basta-bilforsakringen/', 'bolagens villkor sida vid sida',
  'Prisskillnaden mellan två modeller säger inget om villkoren — se {a}.'),
 ('/billigaste-bilforsakringen/', 'hur prisbilden ser ut mellan bolagen',
  'För {a} på en och samma profil finns en separat sida.'),
 ('/basta-bilforsakringen/', 'vår översikt över bolagen',
  'Villkor, självrisker och skadehantering per bolag finns i {a}.'),
]
MARKE_LANK = [
 'Hela {m}-utbudet med prisklass per modell finns på <a href="/bilmarken/{s}/">sidan om {m}</a>.',
 'Märkets övriga modeller och det som gäller {m} generellt står på '
 '<a href="/bilmarken/{s}/">{m}-sidan</a>.',
 'Mer om hur bolagen ser på märket finns under <a href="/bilmarken/{s}/">försäkring för {m}</a>.',
 'Samtliga modeller vi gått igenom finns samlade på <a href="/bilmarken/{s}/">märkessidan för {m}</a>.',
]


def _start_slut(ar):
    """'2017–' → (2017, None), '2007–2016' → (2007, 2016)."""
    delar = ar.replace('-', '–').split('–')
    try:
        s = int(delar[0])
    except ValueError:
        return None, None
    e = int(delar[1]) if len(delar) > 1 and delar[1].strip().isdigit() else None
    return s, e


def _ar_mening(b, mod, nu, i=0):
    """Byggs av årsmodellerna: ålder i dag och garantiläge i årtal."""
    s, e = _start_slut(mod['ar'])
    if s is None:
        return ''
    gr = nu - 3
    if e:
        return _v([
            f'{b} tillverkades {s}–{e}, så de yngsta exemplaren är i dag {nu - e} år och de äldsta '
            f'{nu - s}. Vagnskadegarantin har gått ut på samtliga.',
            f'Med tillverkning {s}–{e} är varje {b} på marknaden minst {nu - e} år gammal, och '
            f'ingen omfattas längre av tillverkarens vagnskadegaranti.',
        ], i, 1, s)
    if nu - s <= 2:
        return _v([
            f'Generationen kom {s}, så i stort sett varje {b} i trafik är registrerad efter {gr} '
            f'och kan fortfarande ha tillverkarens vagnskadegaranti — kontrollera datum för första '
            f'registrering innan du betalar för helförsäkring.',
            f'Eftersom {b} funnits sedan {s} är de flesta exemplar yngre än tre år. Gäller '
            f'vagnskadegarantin täcker den normalt det helförsäkringen annars gör.',
        ], i, 1, s)
    if nu - s <= 6:
        return _v([
            f'Med generationsstart {s} har en {b} registrerad {gr} eller senare normalt kvar '
            f'vagnskadegarantin, medan exemplar från {s if gr - 1 == s else f"{s}–{gr - 1}"} '
            f'behöver eget vagnskadeskydd.',
            f'En {b} från {s} är i dag {nu - s} år. Bilar registrerade från {gr} kan ha kvar '
            f'garantin; äldre exemplar har det inte.',
        ], i, 1, s)
    return _v([
        f'{b} har sålts sedan {s}, så begagnatmarknaden rymmer bilar från {nu - s} år ned till '
        f'nya. Räkna på det enskilda exemplarets marknadsvärde, inte modellens nypris.',
        f'Äldsta exemplaren av den här generationen är från {s}, alltså {nu - s} år gamla, och '
        f'värdet skiljer sig därför mycket mellan två {b} till salu.',
    ], i, 1, s)


def _guide_mening(b, klass, mod, i):
    el = klass.startswith('elbil') or ('eldriven' in mod['drivlina']
                                         and ',' not in mod['drivlina']
                                         and ' och ' not in mod['drivlina'])
    if el:
        return _v([
            f'Det som gäller eldrivna bilar generellt, oavsett märke, finns i '
            f'<a href="/bilforsakring-elbil/">försäkring för elbil</a>.',
            f'Batteri, laddkabel och verkstadskrav för elbilar i allmänhet tas upp i '
            f'<a href="/bilforsakring-elbil/">genomgången av elbilsförsäkring</a>.',
            f'Mer om hur bolagen ser på elbilar som grupp finns på '
            f'<a href="/bilforsakring-elbil/">sidan om elbilsförsäkring</a>.',
        ], i, 1, len(b))
    if klass in ('premium', 'prestanda', 'stor'):
        if (i + len(b)) % 2:
            return (f'Går en {b} på leasing gäller avtalets krav på skyddsnivå, se '
                    f'<a href="/leasingbil-forsakring/">försäkring av leasingbil</a>.')
        return (f'Vad vagnskadedelen omfattar på en bil i {KLASS_NAMN[klass]} beskrivs under '
                f'<a href="/helforsakring/">helförsäkring</a>.')
    if klass == 'budget':
        return _v([
            f'Är du under 25 och funderar på {b} som första bil står det som påverkar priset '
            f'för unga under <a href="/bilforsakring-ung-forare/">bilförsäkring för unga förare</a>.',
            f'{b} är en vanlig första bil — vad som gäller för förare under 25 finns i '
            f'<a href="/bilforsakring-ung-forare/">guiden för unga förare</a>.',
        ], i, 1, len(b))
    return _v([
        f'Skillnaden mellan nivåerna står under <a href="/halvforsakring/">halvförsäkring</a> '
        f'och <a href="/helforsakring/">helförsäkring</a>.',
        f'Vad som ingår i varje nivå beskrivs på sidorna om '
        f'<a href="/halvforsakring/">halvförsäkring</a> och <a href="/helforsakring/">helförsäkring</a>.',
    ], i, 1, len(b))


def _tbl(caption, kol, rader, swipe=False):
    th = ''.join(f'<th scope="col">{k}</th>' for k in kol)
    tr = ''.join('<tr><th scope="row">' + r[0] + '</th>'
                 + ''.join(f'<td>{c}</td>' for c in r[1:]) + '</tr>' for r in rader)
    s = '<p class="swipe">&larr; Dra i sidled för att se alla kolumner</p>' if swipe else ''
    return (f'<div class="tbl"><table><caption>{caption}</caption><thead><tr>{th}</tr></thead>'
            f'<tbody>{tr}</tbody></table></div>{s}')


def _kalla(c):
    """Källa som länk när modulen lagrar en URL, annars som text."""
    if c.get('url'):
        return f'<a href="{c["url"]}" rel="nofollow noopener">{c["kalla"]}</a>, {c["datum"]}'
    return f'{c["kalla"]}, {c["datum"]}'


def _syskon(m, mod, lista, klass_av, n=4):
    """Högst fyra syskon: samma prisklass först, sedan närmast i listan."""
    idx = next(j for j, s in enumerate(lista) if s['slug'] == mod['slug'])
    andra = [(j, s) for j, s in enumerate(lista) if s['slug'] != mod['slug']]
    andra.sort(key=lambda t: (klass_av[t[1]['slug']] != klass_av[mod['slug']], abs(t[0] - idx)))
    return [s for _, s in andra[:n]]


# ─── Titel och beskrivning ────────────────────────────────────────
TITEL_MALL = [
 '{b} försäkring {ar} — pris, villkor och jämförelse',
 '{b} försäkring {ar} — prisspann och skyddsnivå',
 '{b} försäkring {ar} — pris, skadebild och villkor',
 '{b} försäkring {ar} — vad kostar den?',
 '{b} försäkring {ar} — jämför pris och självrisk',
 '{b} försäkring {ar} — pris, värde och rätt nivå',
 '{b} försäkring {ar} — premie och reparationer',
]
TITEL_RESERV = ['{b} försäkring {ar} — pris och villkor', '{b} försäkring {ar} — pris',
                '{b} försäkring {ar}', '{b} försäkring']


def _titel(b, i, ar):
    """Första mallen som ryms inom 60 tecken vinner. Rotationen börjar
    på olika ställen per sida så att titlarna inte blir likformiga."""
    n = len(TITEL_MALL)
    kand = [TITEL_MALL[(i * 3 + k) % n] for k in range(n)] + TITEL_RESERV
    for t in kand:
        t = t.replace('{b}', b).replace('{ar}', ar)
        if len(t) <= 60:
            return t
    return b[:60]


DESC_MALL = [
 'Vad kostar försäkring till {b}? {k}. Se uppskattat prisspann, rätt skyddsnivå, '
 'reparationsbilden och hur modellen står sig mot konkurrenterna.',
 '{b}: {k}. Prisspann för halv- och helförsäkring, vad som gör bilen dyr eller billig '
 'att laga och vilka modeller den jämförs med.',
 'Så mycket kostar det att försäkra {b} — {k}. Prisspann, skadebild, ägarprofil och '
 'när halvförsäkring räcker.',
 'Försäkra {b}? {k}. Här är prisspannet per nivå, vad som styr premien och hur {b} '
 'ligger mot liknande bilar.',
 '{b} försäkring: {k}. Uppskattat pris per nivå, reparationer som kostar och vad värdet '
 'betyder för skyddsnivån.',
 'Prisbild för {b} — {k}. Vad halv- och helförsäkring brukar kosta, vanliga skador och '
 'jämförelse med syskonmodellerna.',
 'Vad bör du betala för att försäkra {b}? {k}. Prisspann, premiedrivare, skadebild och '
 'rätt skyddsnivå efter bilens ålder.',
]


def _desc(b, slug, kortf, mod, i):
    """120–155 tecken. Kortas vid ordgräns, fylls på med modelldata."""
    k = (META.get(slug) or kortf).rstrip('.')
    text = _v(DESC_MALL, i, 5, 4).replace('{b}', b).replace('{k}', k)
    if len(text) > 155:
        text = text[:154].rsplit(' ', 1)[0].rstrip(',.—– ') + '.'
    if len(text) < 120:
        till = f' {mod["typ"].capitalize()} med {mod["drivlina"]}.'
        text = (text + till) if len(text + till) <= 155 else text
    if len(text) < 120:
        till = ' Med källor och uppskattat prisspann.'
        text = (text + till)[:155]
    return text


# ─── Sidan ────────────────────────────────────────────────────────
def _sida(m, mod, b, i, lista, klass_av, nu):
    e = EXTRA.get(mod['slug'], {})
    r = REN.get(mod['slug'], {})
    klass = klass_av[mod['slug']]
    h = lambda pool, mult, add: _v(pool, i, mult, add).replace('{b}', b).replace('{m}', m['namn'])
    cit = PRISER.get(mod['slug'])

    # 1. Pris — modellens direktsvar och uppskattat spann. Källtabellen
    #    med andra sajters namn står längst ned, långt från annonskorten.
    pris = (f'<h2>{h(PRIS_H2, 3, 1)}</h2>'
            + (f'<p class="direkt">{r["direktsvar"]}</p>' if r.get('direktsvar') else '')
            + _tbl(f'Uppskattat prisspann för {b}', ['Nivå', 'Per månad', 'Per år'],
                   [['<a href="/halvforsakring/">Halvförsäkring</a>',
                     upp.spann(klass, 'halv'), upp.ar_spann(klass, 'halv')],
                    ['<a href="/helforsakring/">Helförsäkring</a>',
                     upp.spann(klass, 'hel'), upp.ar_spann(klass, 'hel')]])
            + upp.metodruta(kort=True, i=i)
            + '<p>' + _v(KLASS_MENING, i, 7, len(mod['slug'])).replace('{b}', b)
              .replace('{k}', KLASS_NAMN.get(klass, klass))
              .replace('{t}', upp.KLASS_TEXT.get(klass, '').split(' — ')[-1])
            + ' ' + ('Prisexemplen för just den här modellen' if cit else 'Källorna')
            + _v([' står längst ned på sidan.', ' finns i slutet av sidan.',
                  ' redovisas sist, med datum.'], i, 1, len(m['slug'])) + '</p>'
            )

    kort_sek = kort.sektion(f'Bolag att begära offert från till {b}', None,
                            ['dina-forsakringar', 'gofido'], smal=True, kompakt=True)

    # 2. Modelldata — första meningen efter korten är rena fakta.
    s_, e_ = _start_slut(mod['ar'])
    ar_txt = (f'{s_}–{e_}' if e_ else f'sedan {s_}') if s_ else mod['ar']
    styr = (f'<h2>{h(STYR_H2, 5, 2)}</h2>'
            f'<p>{b} är en {mod["typ"]} med {mod["drivlina"]}, i nuvarande generation på '
            f'svenska marknaden {ar_txt}.</p>'
            + _tbl(f'{b} — uppgifter som påverkar premien', ['Faktor', 'För den här modellen'],
                   [['Drivlina', mod['drivlina'].capitalize()],
                    ['Karosstyp', mod['typ'].capitalize()],
                    ['Årsmodeller', mod['ar']],
                    ['Prisklass i vår uppskattning', upp.KLASS_TEXT.get(klass, '—')]])
            + '<p>' + _v(FORE_KORT, i, 5, len(m['slug'])).replace('{b}', b) + '</p>')
    vinkel = (f'<h2>{h(VINKEL_H2, 3, 2)}</h2><p>{r["vinkel"]}</p>' if r.get('vinkel') else '')

    agare = f'<h2>{h(AGARE_H2, 3, 1)}</h2><p>{r["agare"]}</p>' if r.get('agare') else ''
    teknik = (f'<h2>{h(TEKNIK_H2, 7, 3)}</h2>'
              + (f'<p>{r["teknik"]}</p>' if r.get('teknik') else '')
              + (f'<p>{r["skada"]}</p>' if r.get('skada') else ''))

    jl = _v(JMF_LANK, i, 5, sum(map(ord, m['slug'])))
    jamfor = (f'<h2>{h(JAMFOR_H2, 5, 2)}</h2>'
              + (f'<p>{r["jamfor"]}</p>' if r.get('jamfor') else '')
              + '<p>' + jl[2].replace('{a}', f'<a href="{jl[0]}">{jl[1]}</a>') + '</p>')

    sys_ = _syskon(m, mod, lista, klass_av)
    samma = sum(1 for s in lista if klass_av[s['slug']] == klass) - 1
    sys_rader = [[f'<a href="/bilmarken/{m["slug"]}/{s["slug"]}/">{namn(m, s)}</a>',
                  s['typ'].capitalize(), upp.spann(klass_av[s['slug']], 'halv'),
                  upp.spann(klass_av[s['slug']], 'hel')] for s in sys_]
    syskon = ''
    if sys_rader:
        intro = (f'Av de {len(lista)} {m["namn"]}-modeller vi gått igenom ligger '
                 + (f'{samma} till i samma prisklass som {b}.' if samma > 0 else
                    f'ingen annan i samma prisklass som {b}.'))
        syskon = (f'<h2>{h(SYSKON_H2, 3, 2)}</h2><p>{intro} '
                  + _v(MARKE_LANK, i, 3, 1).replace('{m}', m['namn']).replace('{s}', m['slug'])
                  + '</p>'
                  + _tbl(f'{b} och närmaste {m["namn"]}-modeller — uppskattat spann',
                         ['Modell', 'Typ', 'Halvförsäkring', 'Helförsäkring'], sys_rader,
                         swipe=True))

    flera = ',' in mod['drivlina'] or ' och ' in mod['drivlina']
    begagnat = (_v(BEG_FLERA, i, 3, len(mod['slug'])) if flera else
                _v(BEG_EN, i, 3, len(mod['slug']))).replace('{b}', b).replace('{d}', mod['drivlina'])
    niva = (f'<h2>{h(NIVA_H2, 7, 3)}</h2>'
            + (f'<p>{r["varde"]}</p>' if r.get('varde') else '') +
            
            f'<p>{_ar_mening(b, mod, nu, i)}</p>'
            f'<p>{begagnat}'
            + _v(['Reglerna vid ägarbyte står under <a href="/byta-bilforsakring/">byta '
                  'bilförsäkring</a>. ',
                  'Hur bytet går till beskrivs på <a href="/byta-bilforsakring/">sidan om att '
                  'byta försäkring</a>. ',
                  'Vad som gäller när försäkringen ska börja står under '
                  '<a href="/byta-bilforsakring/">byte av bilförsäkring</a>. '], i, 7, 2)
            + f'{_guide_mening(b, klass, mod, i)}</p>')

    kostnad = f'<h2>{h(KOSTNAD_H2, 3, 4)}</h2><p>{r["kostnad"]}</p>' if r.get('kostnad') else ''

    # Ordningen: pris → modelldata → annonskort → roterade avsnitt. Det
    # första avsnittet efter korten måste vara fritt från orden Dina
    # Försäkringar inte tillåter nära sin annons; källorna står sist.
    mitt = [agare, teknik, jamfor, vinkel, niva, kostnad, syskon]
    rot = (i * 2 + len(m['slug'])) % 4
    mitt = mitt[rot:] + mitt[:rot]
    # Rena avsnitt läggs först tills minst ~900 tecken text står mellan
    # korten och första förekomsten av ett otillåtet ord.
    mitt = [a for a in mitt if a]
    rena = [a for a in mitt if not _FORBJUDET.search(_re.sub(r'<[^>]+>', ' ', a))]
    fram, n = [], 0
    for a in rena:
        if n >= 900:
            break
        fram.append(a)
        n += len(_re.sub(r'<[^>]+>', ' ', a))
    mitt = fram + [a for a in mitt if a not in fram]

    cta = (f'<div class="cta"><h2>Se priset på din {b}</h2>'
           f'<p>Ange registreringsnumret så hämtas bilens uppgifter automatiskt.</p>'
           f'<div class="cta-inner">{{PLATE}}</div></div>')

    if cit:
        kall = _tbl(f'Publicerade prisexempel för {b}',
                    ['Bolag', 'Belopp', 'Avser', 'Källans profil', 'Källa'],
                    [[c['bolag'], c['belopp'], c['vad'], c['profil'], _kalla(c)] for c in cit],
                    swipe=True)
        kall_txt = ('Uppgifterna kommer från andra sajters publicerade prisexempel. Varje '
                    'källa använder sin egen profil, så beloppen går inte att jämföra rakt av.')
    else:
        kall = ''
        lista_k = '; '.join(f'{x["niva"].lower()} {x["spann"]} ({_kalla(x)})' for x in SPANN)
        kall_txt = (_v(KALLA_INGEN, i, 3, len(mod['slug'])).replace('{b}', b)
                    + f' Marknadens publicerade siffror: {lista_k}.')
    kallor = f'<h2>{h(KALLA_H2, 1, 0)}</h2><p class="jf-not">{kall_txt}</p>' + kall

    return ('<section class="sec"><div class="wrap narrow">' + pris + styr + '</div></section>'
            + kort_sek
            + '<section class="sec"><div class="wrap narrow">' + ''.join(mitt)
            + cta + kallor + '</div></section>')


REN = _rensa_dubbletter()


def sidor():
    ut = []
    nu = int(data.UPPDATERAD[:4])
    for marke_slug, lista in MODELLER.items():
        m = MARKE[marke_slug]
        klass_av = {s['slug']: upp.klass_for(s['slug'], s['namn'], m['grupp']) for s in lista}
        for i, mod in enumerate(lista):
            b = namn(m, mod)
            e = EXTRA.get(mod['slug'], {})

            # FAQ: bara frågor vars svar kommer ur modelldata. 3–4 frågor.
            r = REN.get(mod['slug'], {})
            faq = [(mod['fraga'][0], r.get('fraga_svar') or mod['fraga'][1])]
            for nyckel in ('lang', 'lang2'):
                par = e.get(nyckel)
                if par and par[0] and r.get(nyckel + '_svar'):
                    faq.append((par[0], r[nyckel + '_svar']))
            for fraga, nyckel in ((f'Behöver jag helförsäkring på min {b}?', 'niva'),
                                  (f'Vilka skador är vanligast på en {b}?', 'skada'),
                                  (f'Hur håller {b} värdet?', 'varde'),
                                  (f'Vad kostar en {b} utöver försäkringen?', 'kostnad'),
                                  (f'Hur står sig {b} mot liknande bilar?', 'jamfor')):
                if len(faq) >= 4:
                    break
                if r.get(nyckel):
                    faq.append((fraga, r[nyckel]))

            ut.append({
                'slug': f'bilmarken/{m["slug"]}/{mod["slug"]}',
                'key': True,
                'title': _titel(b, i, data.UPPDATERAD[:4]),
                'desc': _desc(b, mod['slug'], mod['kort'], mod, i),
                'eyebrow': f'{m["namn"]} · {mod["typ"].capitalize()}',
                'h1': f'{b} försäkring',
                'lead': mod['kort'],
                'checks': mod['punkter'],
                'card_t': f'Se vad din {b} kostar',
                'sticky': f'Jämför försäkring till {b}',
                'body': _sida(m, mod, b, i, lista, klass_av, nu),
                'faq_h2': f'Vanliga frågor om försäkring till {b}',
                'faq': faq,
                'rel': [(f'/bilmarken/{m["slug"]}/', f'{m["namn"]} bilförsäkring'),
                        ('/bilmarken/', 'Alla bilmärken'),
                        ('/basta-bilforsakringen/', 'Bästa bilförsäkringen'),
                        ('/helforsakring/', 'Helförsäkring'),
                        ('/jamfor-bilforsakring/', 'Så jämför du offerter')],
            })
    return ut
