# -*- coding: utf-8 -*-
"""Centralt datalager — ALLA siffror på sajten hämtas härifrån.

═══════════════════════════════════════════════════════════════════
   DET HÄR ÄR DEN ENDA FIL DU BEHÖVER FYLLA I FÖRE LANSERING
═══════════════════════════════════════════════════════════════════

Ingen siffra finns hårdkodad i någon sidmall. Fyller du i PRIS och
TRUSTPILOT nedan slår de igenom på samtliga sidor, i topplistan, i
rankningen, i tabellerna och i strukturerad data — automatiskt.

Så länge ett värde är None renderas det som "—" och sidan skriver
själv ut att underlaget saknas. Sajten ljuger alltså aldrig om vad
den vet, oavsett hur långt insamlingen kommit.

INSAMLINGSMETOD (följ den, annars går siffrorna inte att jämföra)
1. Hämta offert på EXAKT samma bil och profil hos varje bolag.
   Profilen står i PROFIL nedan och publiceras på /redaktionell-metod/.
2. Notera datum och källa per bolag i KALLA.
3. Priserna anges i kronor per år, inklusive skatt, utan nykundsrabatt.
   Nykundsrabatt gäller normalt bara år ett och gör jämförelsen falsk.
4. Trustpilot: betyg och antal omdömen samma dag som priserna hämtas.
5. Uppdatera UPPDATERAD till dagens datum när insamlingen är klar.
"""

# ─── Datum ─────────────────────────────────────────────────────────
# Syns på varje sida ("Senast kontrollerad"), i schema.org dateModified
# och som lastmod i sitemap.xml. Höj vid varje faktisk genomgång.
UPPDATERAD = '2026-08-24'
UPPDATERAD_TEXT = 'augusti 2026'

# ─── Jämförelseprofil ──────────────────────────────────────────────
PROFIL = {
    'alder': 40,
    'korstracka': '1 500 mil per år',
    'ort': 'ort utanför storstad',
    'skadefria': 6,
    'sjalvrisk': '4 000 kr',
    'bil': 'Volvo V60, 2019, bensin',      # ← ange den bil ni faktiskt offererar
}
PROFIL_TEXT = (f'{PROFIL["alder"]} år, {PROFIL["korstracka"]}, {PROFIL["ort"]}, '
               f'{PROFIL["skadefria"]} skadefria år och {PROFIL["sjalvrisk"]} i självrisk')

# ─── Priser per bolag, kronor per år ───────────────────────────────
# Nyckeln måste matcha slug i companies.py. None = ej insamlat ännu.
PRIS = {
    'folksam':              {'trafik': None, 'halv': None, 'hel': None},
    'lansforsakringar':     {'trafik': None, 'halv': None, 'hel': None},
    'if':                   {'trafik': None, 'halv': None, 'hel': None},
    'trygg-hansa':          {'trafik': None, 'halv': None, 'hel': None},
    'gjensidige':           {'trafik': None, 'halv': None, 'hel': None},
    'dina-forsakringar':    {'trafik': None, 'halv': None, 'hel': None},
    'hedvig':               {'trafik': None, 'halv': None, 'hel': None},
    'ica-forsakring':       {'trafik': None, 'halv': None, 'hel': None},
    'svedea':               {'trafik': None, 'halv': None, 'hel': None},
    'gofido':               {'trafik': None, 'halv': None, 'hel': None},
    'moderna-forsakringar': {'trafik': None, 'halv': None, 'hel': None},
    'paydrive':             {'trafik': None, 'halv': None, 'hel': None},
    'watercircles':         {'trafik': None, 'halv': None, 'hel': None},
    'volvia':               {'trafik': None, 'halv': None, 'hel': None},
    'aktsam':               {'trafik': None, 'halv': None, 'hel': None},
    'evoli':                {'trafik': None, 'halv': None, 'hel': None},
}

# ─── Trustpilot ────────────────────────────────────────────────────
# 'betyg' 1.0–5.0, 'antal' antal omdömen. Hämta samma dag som priserna.
TRUSTPILOT = {slug: {'betyg': None, 'antal': None} for slug in PRIS}

# ─── Källa och datum per bolag ─────────────────────────────────────
# Fyll i när ni hämtat siffrorna. Publiceras på /redaktionell-metod/
# och är den enskilt viktigaste E-E-A-T-signalen på hela sajten.
KALLA = {slug: {'hamtad': None, 'kalla': None} for slug in PRIS}

# ─── Självrisker per bolag ─────────────────────────────────────────
# Kräver ingen offert — står i respektive bolags villkor och kan
# fyllas i direkt. Gör det först: tabellen blir unik på marknaden.
SJALVRISK = {slug: {'trafik': None, 'vagn': None, 'glas': None,
                    'stold': None, 'maskin': None} for slug in PRIS}

# ─── Orter ─────────────────────────────────────────────────────────
# 'index' = premien i procent av riksgenomsnittet (100 = snitt).
# Fyll i när ni offererat samma bil på ett postnummer i varje ort.
ORTER = {
    'stockholm': {'namn': 'Stockholm', 'index': None, 'lan': 'Stockholms län'},
    'goteborg':  {'namn': 'Göteborg',  'index': None, 'lan': 'Västra Götaland'},
    'malmo':     {'namn': 'Malmö',     'index': None, 'lan': 'Skåne'},
}


# ─── Hjälpfunktioner ───────────────────────────────────────────────
def kr(v, per_manad=False):
    """Formaterar ett belopp, eller tankstreck om det saknas."""
    if v is None:
        return '—'
    if per_manad:
        v = round(v / 12)
    return f'{v:,}'.replace(',', '\u00a0') + '\u00a0kr'


def betyg(v):
    return str(v).replace('.', ',') if v is not None else '—'


def har_priser():
    """True först när minst ett bolag har ett insamlat pris."""
    return any(p['hel'] or p['halv'] or p['trafik'] for p in PRIS.values())


def har_trustpilot():
    return any(t['betyg'] for t in TRUSTPILOT.values())


def saknas_ruta(vad='priserna'):
    """Ärlig upplysning i stället för påhittade siffror."""
    return ('<div class="warn"><strong>Underlag saknas ännu.</strong> '
            f'Vi publicerar {vad} först när de är insamlade på samma '
            'jämförelseprofil hos samtliga bolag. Tomma fält betyder att '
            'siffran inte är verifierad — inte att den är noll. '
            '<a href="/redaktionell-metod/">Så samlar vi in dem</a>.</div>')


def profil_ruta():
    return ('<div class="src"><p><strong>Jämförelseprofil.</strong> Alla priser avser '
            f'{PROFIL_TEXT}. Bil: {PROFIL["bil"]}. Ändras en förutsättning ändras priset — '
            'ofta mycket. <a href="/redaktionell-metod/">Så räknar vi</a>.</p></div>')


def kontrollerad():
    return (f'<p class="checked">Senast kontrollerad: {UPPDATERAD_TEXT}. '
            f'Vi går igenom priser och villkor löpande.</p>')


# ─── Villkorsfakta per bolag ───────────────────────────────────────
# Står i bolagens villkor och kräver ingen offert. Fyll i efter hand —
# tomma fält visas som "Uppgift saknas" och sidan påstår ingenting.
#   bindningstid : t.ex. 'Ingen' eller '12 månader'
#   maskin       : t.ex. '8 år eller 12 000 mil'
#   verkstad     : 'Fritt val' / 'Anvisad verkstad' / 'Fritt val mot tillägg'
VILLKOR = {slug: {'bindningstid': None, 'maskin': None, 'verkstad': None}
           for slug in PRIS}

# ─── Tilläggsförsäkringar ──────────────────────────────────────────
# True = ingår som valbart tillägg, False = erbjuds inte, None = okänt.
TILLAGG = {slug: {'allrisk': None, 'vagassistans': None, 'hyrbil': None,
                  'lagre_sjalvrisk': None, 'djur': None, 'parkeringsskada': None}
           for slug in PRIS}

TILLAGG_NAMN = [('allrisk', 'Allrisk / drulle'), ('vagassistans', 'Vägassistans'),
                ('hyrbil', 'Hyrbil'), ('lagre_sjalvrisk', 'Lägre självrisk'),
                ('djur', 'Självriskreducering djur'), ('parkeringsskada', 'Parkeringsskada')]

# ─── Standardomfattning på den svenska marknaden ───────────────────
# Så här ser uppdelningen ut hos i princip alla bolag. Enskilda villkor
# kan avvika, och det skrivs ut i tabellen — men strukturen är stabil
# nog att publicera, och den är samma information som ligger till grund
# för sidorna om trafik-, halv- och helförsäkring.
MOMENT = [
    ('Trafikskada',          True,  True,  True),
    ('Stöld och inbrott',    False, True,  True),
    ('Brand',                False, True,  True),
    ('Glas',                 False, True,  True),
    ('Maskin och elektronik', False, True, True),
    ('Räddning och bärgning', False, True, True),
    ('Rättsskydd',           False, True,  True),
    ('Kristerapi',           False, True,  True),
    ('Allrisk / drulle',     False, False, False),
    ('Vagnskada',            False, False, True),
]

SJALVRISK_NAMN = [('trafik', 'Trafik'), ('vagn', 'Vagnskada'), ('glas', 'Glasskada'),
                  ('stold', 'Stöld'), ('maskin', 'Maskinskada')]


# ─── Insamlade siffror ─────────────────────────────────────────────
# insamlat.py skapas av insamling/importera.py och skriver över
# platshållarna ovan. Finns filen inte kör sajten vidare på tomma
# värden — inget går sönder, allt renderas som "—".
try:
    import insamlat
    for _namn in ('PRIS', 'TRUSTPILOT', 'SJALVRISK', 'KALLA'):
        _ny = getattr(insamlat, _namn, None)
        if _ny:
            for _slug, _v in _ny.items():
                globals()[_namn].setdefault(_slug, {}).update(
                    {k: v for k, v in _v.items() if v is not None})
except ImportError:
    pass
