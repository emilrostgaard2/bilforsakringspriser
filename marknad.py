# -*- coding: utf-8 -*-
"""Publicerade prisuppgifter från andra källor — med angiven källa.

VARFÖR DEN HÄR FILEN FINNS OCH VARFÖR DEN ÄR SKILD FRÅN data.py
Siffrorna här är INTE våra. De är hämtade ur andra sajters publicerade
prisexempel och redovisas som citat, med källa, datum och den profil
källan själv uppger. De ligger därför i en egen tabell, tydligt märkt,
och de flyter aldrig in i data.PRIS, i rankningen eller i strukturerad
data. Vår egen jämförelse förblir tom tills vi hämtat den själva.

DET HÄR ÄR SKILLNADEN SOM GÖR DET LAGLIGT OCH TROVÄRDIGT
Att citera enstaka publicerade uppgifter med källhänvisning är
journalistik. Att kopiera en hel pristabell och presentera den som sin
egen är dels upphovsrättsligt tveksamt (katalogskydd, 49 § URL), dels
vilseledande enligt marknadsföringslagen — särskilt eftersom källornas
profiler skiljer sig från vår. Ordet "uppskattat" räddar inte det.

REGLER OM DU LÄGGER TILL FLER
  • Aldrig fler än ett par uppgifter per källa. Tar du hela tabellen
    har du kopierat en databas.
  • Alltid profil, källa, url och datum. Saknas något: ta inte med den.
  • Skriv aldrig om uppgiften så att den ser ut att vara vår.
  • Gå igenom listan vid varje uppdatering. Priser åldras fort, och en
    felaktig siffra med vårt namn på är värre än ingen siffra alls.
"""

# Varje post: vad uppgiften avser, bolag, belopp, källans egen profil.
PRISEXEMPEL = [
    {'vad': 'Lägsta trafikförsäkring i källans prisexempel', 'bolag': 'Hedvig',
     'belopp': '169 kr/mån', 'profil': 'Källans egen jämförelseprofil',
     'kalla': 'Tryggvi', 'url': 'https://tryggvi.se/bilforsakring/', 'datum': 'juli 2026'},

    {'vad': 'Högsta trafikförsäkring i samma prisexempel', 'bolag': 'Trygg-Hansa',
     'belopp': '335 kr/mån', 'profil': 'Källans egen jämförelseprofil',
     'kalla': 'Tryggvi', 'url': 'https://tryggvi.se/bilforsakring/', 'datum': 'juli 2026'},

    {'vad': 'Halvförsäkring i källans prisexempel', 'bolag': 'Hedvig',
     'belopp': '232 kr/mån', 'profil': 'Källans egen jämförelseprofil',
     'kalla': 'Börskollen', 'url': 'https://www.borskollen.se/forsakring/bil/basta',
     'datum': 'augusti 2026'},

    {'vad': 'Billigaste trafikförsäkring i källans undersökning', 'bolag': 'Hedvig',
     'belopp': '170 kr/mån', 'profil': 'Volvo XC60, man 31 år, Göteborg, 2 000 mil/år',
     'kalla': 'Försäkras.se', 'url': 'https://www.xn--frskras-7wa3n.se/',
     'datum': 'augusti 2026'},

    {'vad': 'Dyraste i samma undersökning', 'bolag': 'Trygg-Hansa',
     'belopp': '292 kr/mån', 'profil': 'Volvo XC60, man 31 år, Göteborg, 2 000 mil/år',
     'kalla': 'Försäkras.se', 'url': 'https://www.xn--frskras-7wa3n.se/',
     'datum': 'augusti 2026'},

    {'vad': 'Helförsäkring, lägsta i källans prisexempel', 'bolag': 'Premiva',
     'belopp': 'från 549 kr/mån',
     'profil': 'Volvo XC40 2019, Göteborg, förare 36 år, 1 500 mil/år',
     'kalla': 'Billigastbilförsäkring.se',
     'url': 'https://xn--billigastbilfrskring-pzb70b.se/', 'datum': 'augusti 2026'},

    {'vad': 'Helförsäkring i källans prisexempel', 'bolag': 'Gofido',
     'belopp': '695 kr/mån', 'profil': 'Källans egen jämförelseprofil',
     'kalla': 'Bästabilförsäkringen.se',
     'url': 'https://xn--bstabilfrskringen-qqbj17a.se/', 'datum': 'augusti 2026'},

    {'vad': 'Genomsnittligt månadspris enligt bolagets egen statistik', 'bolag': 'Hedvig',
     'belopp': 'omkring 510 kr/mån', 'profil': 'Bolagets egen kundstatistik för 2026',
     'kalla': 'Billigastbilförsäkring.se, med hänvisning till Hedvig',
     'url': 'https://xn--billigastbilfrskring-pzb70b.se/jamfor-bilforsakring/',
     'datum': 'augusti 2026'},
]

# Marknadsgenomsnitt — inte per bolag, utan för marknaden som helhet.
GENOMSNITT = [
    {'vad': 'Genomsnittlig bilförsäkring, samtliga nivåer',
     'belopp': '5 406 kr/år (451 kr/mån)',
     'underlag': 'Försäkringar förmedlade via jämförelsetjänsten under 2025',
     'kalla': 'Zmarta', 'url': 'https://www.zmarta.se/forsakring/bilforsakring',
     'datum': '2025'},

    {'vad': 'Genomsnittlig trafikförsäkring', 'belopp': '190 kr/mån',
     'underlag': 'Källans egna prisexempel',
     'kalla': 'Försäkringsguiden',
     'url': 'https://www.xn--frskringsguiden-2kb71a.se/fordon/bilforsakring/',
     'datum': 'juni 2026'},
]

# Oberoende betyg — primärkällor, inte prisjämförelsesajter.
BETYG = [
    {'vad': 'Högst betyg, stor- och tilläggsprodukter', 'bolag': 'Trygg-Hansa Stor',
     'varde': '4,8 av 5', 'kalla': 'Konsumenternas Försäkringsbyrå',
     'url': 'https://www.konsumenternas.se/konsumentstod/jamforelser/'
            'fordons---batforsakringar/jamfor-bilforsakringar/', 'datum': 'augusti 2026'},

    {'vad': 'Högst betyg, trafikförsäkring', 'bolag': 'ICA Försäkring',
     'varde': '4,8 av 5', 'kalla': 'Konsumenternas Försäkringsbyrå',
     'url': 'https://www.konsumenternas.se/konsumentstod/jamforelser/'
            'fordons---batforsakringar/jamfor-bilforsakringar/', 'datum': 'augusti 2026'},
]

# Kundnöjdhet ur Konsumenternas jämförelse 2026-05-18. Primärkälla.
# OBS: skiljer sig från siffrorna i companies.py, som avser en annan
# mätning. Stäm av och välj en källa innan lansering.
KUNDNOJDHET_2026 = [
    ('Svedea', 77.1), ('If', 75.4), ('Folksam', 74.9),
    ('Länsförsäkringar', 74.7), ('Volvia', 74.5), ('Trygg-Hansa', 68.9),
]
KUNDNOJDHET_KALLA = {
    'kalla': 'Konsumenternas Försäkringsbyrå, jämförelse av bilförsäkringar',
    'url': 'https://www.konsumenternas.se/konsumentstod/jamforelser/'
           'fordons---batforsakringar/jamfor-bilforsakringar/',
    'datum': '18 maj 2026'}

SWIPE = '<p class="swipe">&larr; Dra i sidled för att se alla kolumner</p>'


def _kalla(p):
    return f'<a href="{p["url"]}" rel="nofollow noopener" target="_blank">{p["kalla"]}</a>'


def disclaimer():
    return ('<div class="warn"><strong>Detta är andras siffror, inte våra.</strong> '
            'Uppgifterna nedan är hämtade ur andra sajters publicerade prisexempel och '
            'redovisas med källa och datum. Varje källa använder sin egen bil och '
            'förarprofil, vilket betyder att beloppen inte är jämförbara med varandra — '
            'och inte med vår egen jämförelseprofil. De visas för att ge en '
            'storleksordning, ingenting annat. Vår egen prisinsamling publiceras separat '
            'när den är klar.</div>')


def prisexempel_tabell():
    rader = ''.join(
        f'<tr><th scope="row">{p["bolag"]}</th><td>{p["belopp"]}</td>'
        f'<td>{p["vad"]}</td><td>{p["profil"]}</td>'
        f'<td>{_kalla(p)}, {p["datum"]}</td></tr>' for p in PRISEXEMPEL)
    return ('<div class="tbl"><table><caption>Publicerade prisexempel hos andra '
            'jämförelsesajter</caption><thead><tr><th scope="col">Bolag</th>'
            '<th scope="col">Belopp</th><th scope="col">Avser</th>'
            '<th scope="col">Källans profil</th><th scope="col">Källa</th></tr></thead>'
            f'<tbody>{rader}</tbody></table></div>{SWIPE}')


def genomsnitt_tabell():
    rader = ''.join(
        f'<tr><th scope="row">{g["vad"]}</th><td>{g["belopp"]}</td>'
        f'<td>{g["underlag"]}</td><td>{_kalla(g)}, {g["datum"]}</td></tr>'
        for g in GENOMSNITT)
    return ('<div class="tbl"><table><caption>Marknadsgenomsnitt enligt publicerade '
            'källor</caption><thead><tr><th scope="col">Uppgift</th>'
            '<th scope="col">Belopp</th><th scope="col">Underlag</th>'
            f'<th scope="col">Källa</th></tr></thead><tbody>{rader}</tbody></table></div>{SWIPE}')


def betyg_tabell():
    rader = ''.join(
        f'<tr><th scope="row">{b["bolag"]}</th><td>{b["varde"]}</td>'
        f'<td>{b["vad"]}</td><td>{_kalla(b)}, {b["datum"]}</td></tr>' for b in BETYG)
    k = KUNDNOJDHET_KALLA
    rader += ''.join(
        f'<tr><th scope="row">{namn}</th><td>{str(v).replace(".", ",")} av 100</td>'
        f'<td>Kundnöjdhet</td><td>{_kalla(k)}, {k["datum"]}</td></tr>'
        for namn, v in KUNDNOJDHET_2026)
    return ('<div class="tbl"><table><caption>Oberoende betyg och kundnöjdhet</caption>'
            '<thead><tr><th scope="col">Bolag</th><th scope="col">Värde</th>'
            '<th scope="col">Avser</th><th scope="col">Källa</th></tr></thead>'
            f'<tbody>{rader}</tbody></table></div>{SWIPE}')
