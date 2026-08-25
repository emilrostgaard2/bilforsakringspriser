# -*- coding: utf-8 -*-
"""Uppskattade prisspann per modell.

═══════════════════════════════════════════════════════════════════
   LÄS DET HÄR INNAN NI ÄNDRAR NÅGOT
═══════════════════════════════════════════════════════════════════

VAD DET HÄR ÄR
Ett uppskattat spann per modell, framräknat ur publicerade
marknadssiffror och modellens prisklass. Det är en uppskattning, inte
en offert och inte en insamlad siffra — och det står utskrivet vid
varje tabell.

VAD DET INTE ÄR
Det är inte vår egen prisinsamling. Den ligger i data.PRIS och är
fortfarande tom. När den fylls i tar de riktiga siffrorna över och
uppskattningarna försvinner automatiskt från modellsidorna.

VARFÖR SPANN OCH INTE EXAKTA PRISER
Ett exakt "från 549 kr/mån" på en modell vi inte offererat vore ett
påhittat tal med falsk precision. Ett spann visar samma sak — var i
skalan modellen ligger — utan att låtsas om en noggrannhet som inte
finns. Det är också vad som går att stå för om någon frågar hur vi
räknat.

ANKARE (publicerade siffror, med källa)
  Snittpremie över alla nivåer      451 kr/mån   Zmarta, 2025
  Snittpremie i annan mätning       472 kr/mån   Försäkras.se, 2026
  Trafikförsäkring, spann       169–335 kr/mån   Tryggvi, 2026
  Halvförsäkring, lägsta            260 kr/mån   Försäkras.se, 2026
  Helförsäkring, lägsta             347 kr/mån   Försäkras.se, 2026
  Helförsäkring, exempel            695 kr/mån   Bästabilförsäkringen, 2026
  Helförsäkring V70, spann      350–900 kr/mån   BilKoll, 2026

METOD
Spannen nedan är satta så att marknadens publicerade lägsta och högsta
värden ryms i klasserna, och modellerna placerats i klass efter
ersättningsvärde och drivlina — de två faktorer som väger tyngst i
bolagens egna modeller. Klassindelningen är vår bedömning och redovisas
öppet på /redaktionell-metod/.

NÄR NI FÅR EGNA SIFFROR
Fyll i data.PRIS. Modellsidor och märkessidor byter automatiskt från
uppskattat spann till insamlat pris, och metodrutan byts mot källrutan.
"""

# ─── Prisklasser ───────────────────────────────────────────────────
# (halv_låg, halv_hög, hel_låg, hel_hög) i kronor per månad.
KLASSER = {
    'budget':    (230, 330, 330, 500),
    'volym':     (280, 400, 450, 650),
    'stor':      (340, 470, 560, 800),
    'premium':   (380, 520, 620, 900),
    'elbil':     (310, 440, 500, 740),
    'elbil-stor': (390, 540, 650, 950),
    'prestanda': (400, 560, 680, 980),
}

KLASS_TEXT = {
    'budget': 'Låg prisklass — lågt ersättningsvärde och god delstillgång',
    'volym': 'Volymklass — stort bestånd och väldokumenterad skadestatistik',
    'stor': 'Stor bil — högre ersättningsvärde och dyrare karossdelar',
    'premium': 'Premiumklass — högt ersättningsvärde och ofta krav på stöldskydd',
    'elbil': 'Elbil — batteriets värde och certifierad verkstad väger in',
    'elbil-stor': 'Stor elbil — högt ersättningsvärde och begränsat verkstadsnät',
    'prestanda': 'Prestandaversion — effektklassen väger tyngst',
}

# ─── Modeller med egen sida ────────────────────────────────────────
MODELLKLASS = {
    # Volvo
    'xc60': 'volym', 'xc40': 'volym', 'v60': 'volym', 'v90': 'stor',
    'xc90': 'premium', 's60': 'volym', 's90': 'stor',
    'ex30': 'elbil', 'ex40': 'elbil', 'v70': 'budget',
    # Tesla
    'model-3': 'elbil', 'model-y': 'elbil', 'model-s': 'elbil-stor',
    'model-x': 'elbil-stor',
    # XPeng
    'g6': 'elbil', 'g9': 'elbil-stor', 'p7': 'elbil', 'x9': 'elbil-stor',
    # Cupra
    # Audi
    'a4': 'volym', 'a6': 'stor', 'a3': 'volym', 'q3': 'volym', 'q5': 'stor',
    'q7': 'premium', 'q4-e-tron': 'elbil', 'q6-e-tron': 'elbil-stor',
    'a6-e-tron': 'elbil-stor', 'e-tron-gt': 'prestanda',
    # Polestar
    'polestar-2': 'elbil', 'polestar-3': 'elbil-stor', 'polestar-4': 'elbil-stor',
    # Zeekr
    'x': 'elbil', '001': 'elbil-stor', '7x': 'elbil',
    # Hyundai
    'kona': 'volym', 'tucson': 'volym', 'ioniq-5': 'elbil', 'ioniq-6': 'elbil',
    'inster': 'elbil', 'santa-fe': 'stor', 'bayon': 'budget', 'i20': 'budget',
    'i10': 'budget', 'ioniq-9': 'elbil-stor',
    # Volkswagen
    'golf': 'volym', 'passat': 'stor', 'tiguan': 'volym', 'polo': 'budget',
    'id4': 'elbil', 'id3': 'elbil', 'id7': 'elbil-stor', 'id-buzz': 'elbil-stor',
    'tayron': 'stor', 't-roc': 'volym', 'touran': 'volym',
    # Skoda
    'octavia': 'volym', 'superb': 'stor', 'kodiaq': 'stor', 'karoq': 'volym',
    'fabia': 'budget', 'scala': 'budget', 'kamiq': 'volym', 'enyaq': 'elbil',
    'elroq': 'elbil', 'yeti': 'budget',
    # Cupra
    'formentor': 'volym', 'born': 'elbil', 'leon': 'prestanda',
    'tavascan': 'elbil', 'terramar': 'stor', 'ateca': 'volym',
}

# ─── Fallback per märkesgrupp ──────────────────────────────────────
# Används för modeller utan egen sida, alltså raderna på märkessidorna.
GRUPPKLASS = {
    'budget': 'budget', 'volym': 'volym', 'premium': 'premium',
    'elbil': 'elbil', 'sport': 'prestanda', 'lyx': 'premium',
}

# Modellnamn som avslöjar eldrift även på märken med förbränningsmotorer.
EL_ORD = ('id.', 'ioniq', 'ev', 'e-tron', 'eqa', 'eqb', 'eqc', 'eqe', 'eqs',
          'born', 'zoe', 'leaf', 'ariya', 'mg4', 'atto', 'dolphin', 'seal',
          'recharge', 'ex30', 'ex40', 'ex90', 'i4', 'ix', 'enyaq')


def klass_for(modellslug=None, modellnamn=None, grupp=None):
    """Placerar en modell i prisklass. Egen sida går före gissning."""
    if modellslug and modellslug in MODELLKLASS:
        return MODELLKLASS[modellslug]
    if modellnamn:
        n = modellnamn.lower()
        if any(o in n for o in EL_ORD):
            return 'elbil'
    return GRUPPKLASS.get(grupp, 'volym')


def spann(klass, niva):
    """Returnerar '280–400 kr/mån' eller '—' om klassen är okänd."""
    v = KLASSER.get(klass)
    if not v:
        return '—'
    lo, hi = (v[0], v[1]) if niva == 'halv' else (v[2], v[3])
    return f'{lo}\u2013{hi}\u00a0kr/mån'


def ar_spann(klass, niva):
    v = KLASSER.get(klass)
    if not v:
        return '—'
    lo, hi = (v[0], v[1]) if niva == 'halv' else (v[2], v[3])
    return (f'{lo * 12:,}\u2013{hi * 12:,}\u00a0kr'.replace(',', '\u00a0'))


VAGLEDANDE = [
 'Spannen är uppskattade utifrån publicerade marknadssiffror och modellens prisklass, inte '
 'insamlade offerter.',
 'Beloppen är uppskattningar byggda på publicerade marknadssiffror. De är inte offerter och '
 'inte insamlade priser.',
 'Spannen bygger på publicerade marknadssiffror kombinerade med modellens prisklass. Ingen '
 'offert ligger bakom.',
 'Siffrorna är framräknade ur publicerade marknadsuppgifter, inte hämtade hos bolagen.',
 'Uppskattningen utgår från marknadens publicerade spann och modellens prisklass.',
 'Beloppen visar storleksordning, inte pris. De bygger på publicerade marknadssiffror.',
 'Spannen är beräknade, inte offererade. Underlaget är publicerade marknadssiffror.',
]


def metodruta(kort=False, i=0):
    """Ska stå under varje tabell som visar uppskattade spann."""
    if kort:
        return (f'<p class="jf-not"><strong>Priserna är vägledande.</strong> '
                f'{VAGLEDANDE[i % len(VAGLEDANDE)]} Ditt eget pris beror på ålder, '
                f'bostadsort, körsträcka och skadefria år. '
                f'<a href="/redaktionell-metod/">Så räknar vi</a>.</p>')
    return ('<div class="src"><p><strong>Priserna är vägledande och uppskattade.</strong> '
            'Spannen bygger på publicerade marknadssiffror från Zmarta, Försäkras.se, '
            'Tryggvi och BilKoll, kombinerade med modellens prisklass utifrån '
            'ersättningsvärde och drivlina. De är alltså inte offerter och inte insamlade '
            'priser — vår egen insamling pågår och publiceras separat när den är klar. '
            'Ditt eget pris kan hamna både under och över spannet beroende på ålder, '
            'bostadsort, körsträcka och antal skadefria år. '
            '<a href="/redaktionell-metod/">Läs hela metoden</a>.</p></div>')
