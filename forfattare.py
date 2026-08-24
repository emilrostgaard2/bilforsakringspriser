# -*- coding: utf-8 -*-
"""Författarruta och E-E-A-T-uppgifter.

VARFÖR TEXTEN SER UT SOM DEN GÖR
Google belönar inte påstådd expertis — den belönar tydlighet om vem som
står bakom och vad den personen faktiskt kan. Att utge sig för att vara
försäkringsexpert utan att vara det är både en trovärdighetsrisk och,
på en sajt om finansiella produkter, en juridisk risk.

Texten nedan säger därför rakt ut vad kompetensen består i (insamling,
jämförelse, källredovisning) och vad den inte består i (rådgivning om
enskilda försäkringar). Det är den ärliga versionen — och i praktiken
den starkare, eftersom den går att stå för.

JURIDIK
Sajten förmedlar inga försäkringar och står inte under
Finansinspektionens tillsyn. Det ska stå någonstans, eftersom
försäkringsdistribution är tillståndspliktig verksamhet i Sverige och
läsaren annars kan tro att sajten är en förmedlare. Ändra inte bort den
raden utan att först ha kollat vad ni faktiskt gör.

FAKTAGRANSKARE
Fyll i GRANSKARE när ni knutit en svensk fackperson till sajten — en
försäkringsrådgivare, jurist eller ekonomijournalist som läser igenom
sakinnehållet. Rutan renderas automatiskt när fältet inte är tomt.
Det är den enskilt största E-E-A-T-förbättringen som återstår.
"""

FORFATTARE = {
    'namn': 'Emil Rostgaard Clausen',
    'roll': 'Grundare och redaktör',
    'bild': '/assets/forfattare-emil.webp',
    'bild2x': '/assets/forfattare-emil@2x.webp',
    'sida': '/om-oss/',
    'kort': 'Jag arbetar med sökmotoroptimering och driver jämförelsesajter — '
            'inte med försäkringar.',
    'text': (
        'Jag är inte försäkringsrådgivare och har ingen bakgrund i försäkringsbranschen. '
        'Det jag kan är att samla in uppgifter, ställa dem mot varandra på ett sätt som '
        'faktiskt går att jämföra, och redovisa var varje siffra kommer ifrån. '
        'Bilförsäkring hamnade jag i för att jag tyckte att det var orimligt svårt att '
        'få ett rakt svar på vad en försäkring kostar — och för att jag driver '
        'motsvarande jämförelsesajter i Danmark sedan flera år.'),
    'gor': [
        'Samlar in priser och villkor på samma jämförelseprofil hos alla bolag',
        'Redovisar källa och datum för varje siffra som publiceras',
        'Skriver om hur försäkringarna fungerar, utifrån bolagens egna villkor',
    ],
    'gor_inte': [
        'Ger inte råd om vilken försäkring just du ska välja',
        'Förmedlar och säljer inga försäkringar',
        'Gör inga bedömningar av enskilda skadeärenden',
    ],
}

# Lämna tomt tills en faktagranskare är på plats. Fyll i namn, titel och
# vad personen granskat — aldrig ett namn utan att personen läst texten.
GRANSKARE = {'namn': '', 'titel': '', 'text': ''}


def ruta():
    """Kompakt författarruta sist på varje sida.

    Medvetet liten: den ska svara på vem som står bakom, inte ta plats
    från innehållet. Den fullständiga beskrivningen ligger på /om-oss/."""
    f = FORFATTARE

    granskad = ''
    if GRANSKARE['namn']:
        granskad = (f'<span class="fb-gr">Faktagranskad av {GRANSKARE["namn"]}, '
                    f'{GRANSKARE["titel"]}.</span> ')

    return (
        '<div class="wrap narrow"><div class="fb">'
        f'<img class="fb-bild" src="{f["bild"]}" '
        f'srcset="{f["bild"]} 1x, {f["bild2x"]} 2x" width="44" height="44" '
        f'alt="{f["namn"]}" loading="lazy" decoding="async">'
        '<div class="fb-txt">'
        f'<p class="fb-namn">{f["namn"]} <span>&middot; {f["roll"]}</span></p>'
        f'<p class="fb-kort">{granskad}Jag arbetar med sökmotoroptimering och '
        'driver jämförelsesajter — inte med försäkringar. Jag samlar in, jämför '
        f'och redovisar källor. <a href="{f["sida"]}">Om sajten</a></p>'
        '<p class="fb-jur">Bilförsäkringspriser.se förmedlar inga försäkringar och '
        'står inte under Finansinspektionens tillsyn. Innehållet är allmän information, '
        'inte rådgivning i ett enskilt ärende. Oberoende vägledning får du kostnadsfritt '
        'hos <a href="https://www.konsumenternas.se/" rel="nofollow noopener" '
        'target="_blank">Konsumenternas Försäkringsbyrå</a>.</p>'
        '</div></div></div>')

def schema(bas):
    """Person-objektet till author i Article-schemat."""
    f = FORFATTARE
    return {
        '@type': 'Person',
        'name': f['namn'],
        'url': bas + f['sida'],
        'image': bas + f['bild2x'],
        'jobTitle': f['roll'],
        'description': f['kort'],
        'knowsAbout': ['Bilförsäkring', 'Prisjämförelse', 'Sökmotoroptimering'],
        'worksFor': {'@type': 'Organization', 'name': 'Bilförsäkringspriser.se',
                     'url': bas + '/'},
    }
