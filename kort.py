# -*- coding: utf-8 -*-
"""Jämförelsekorten under hero på startsidan.

═══════════════════════════════════════════════════════════════════
   INNAN NI PUBLICERAR: LÄS DET HÄR
═══════════════════════════════════════════════════════════════════

AFFILIATELÄNKAR
Fältet 'aff' är tomt för alla partners. Så länge det är tomt pekar
knappen på bolagets egen sida hos oss, och inget markeras som
sponsrat — vilket är korrekt, eftersom det inte är det ännu.

När Adtraction godkänt er: lägg in spårlänken i 'aff'. Då byter
knappen automatiskt till partnerlänken och får rel="sponsored
nofollow noopener". Gör det inte manuellt i HTML.

    'aff': 'https://track.adtraction.com/t/t?a=...&url=...'

MÄRKNING ÄR INTE VALFRI
Marknadsföringslagen kräver att reklam går att känna igen som reklam.
Google kräver rel="sponsored" eller "nofollow" på betalda länkar.
Båda sköts av koden nedan så länge ni lägger länken i 'aff'-fältet
och inte någon annanstans. Raden om ersättning ovanför korten ska
ligga kvar och vara synlig utan att man scrollar förbi den.

ETIKETTERNA MÅSTE GÅ ATT BELÄGGA
Varje 'badge' hänvisar till något kontrollerbart: ett betyg från
Konsumenternas Försäkringsbyrå, en siffra ur companies.py eller en
citerad uppgift i marknad.py. Skriv aldrig "Bäst i test" — vi har
inte gjort något test, och påståendet är både felaktigt och i strid
med reglerna om vilseledande marknadsföring.

PRISERNA
Hämtas ur data.PRIS. Är de tomma visas "—" och prisblocket får en
förklarande rad i stället. Skriv aldrig in ett pris här i filen.
"""
import data

PARTNERS = [
    {
        'slug': 'ica-forsakring',
        'namn': 'ICA Försäkring',
        'logo': '/assets/logotyper/ica-forsakring.webp',
        'badge': 'Högst betyg på trafikförsäkring',
        'badge_typ': 'guld',
        'text': 'Fick högsta betyg, 4,8 av 5, för sin trafikförsäkring i Konsumenternas '
                'Försäkringsbyrås jämförelse. Bonus på ICA-kortet vid köp av försäkring, '
                'vilket gör den intressant om du redan handlar där.',
        'taggar': ['Konsumenternas 4,8 av 5', 'Bonus på ICA-kortet', 'Öppen för alla'],
        'sida': '/forsakringsbolag/ica-forsakring/',
        'aff': '',
    },
    {
        'slug': 'dina-forsakringar',
        'namn': 'Dina Försäkringar',
        'logo': '/assets/logotyper/dina-forsakringar.webp',
        'badge': 'Högst kundnöjdhet',
        'badge_typ': 'silver',
        'text': 'Ligger högst av samtliga bolag i vår sammanställning av kundnöjdhet. '
                'Lokalt förankrade bolag med egna kontor, vilket märks i handläggningen '
                'när något faktiskt har hänt.',
        'taggar': ['Högst kundnöjdhet', 'Lokala kontor', 'Personlig handläggning'],
        'sida': '/forsakringsbolag/dina-forsakringar/',
        'aff': '',
    },
    {
        'slug': 'gofido',
        'namn': 'Gofido',
        'logo': '/assets/logotyper/gofido.webp',
        'badge': 'Låg premie i publicerade prisexempel',
        'badge_typ': 'blaa',
        'text': 'Återkommer bland de lägsta premierna i andra jämförelsesajters '
                'publicerade prisexempel. Digitalt bolag utan kontor — allt sköts på '
                'nätet, vilket är en del av förklaringen till prisbilden.',
        'taggar': ['Ofta lägst i prisexempel', 'Helt digitalt', 'Villkorsbetyg 4,1 av 5'],
        'sida': '/forsakringsbolag/gofido/',
        'aff': '',
    },
]

# Jämförelsetjänst, inte försäkringsbolag. Visas separat så att det inte
# ser ut som att den konkurrerar om samma sak.
TJANST = {
    'namn': 'Zmarta',
    'logo': '/assets/logotyper/zmarta.webp',
    'text': 'Jämförelsetjänst som hämtar offerter från flera bolag i ett formulär. '
            'Täcker bara anslutna bolag och får provision av dem — använd den som ett '
            'av flera underlag, inte som hela marknaden.',
    'taggar': ['Flera offerter i ett formulär', 'Endast anslutna bolag'],
    'aff': '',
}

BADGE_IKON = {'guld': '\u2605', 'silver': '\u25cf', 'blaa': '\u25be'}


def _knapp(p, text='Se din pris'):
    """Partnerlänk om den finns, annars vår egen bolagssida."""
    if p.get('aff'):
        return (f'<a class="pk-cta" href="{p["aff"]}" '
                f'rel="sponsored nofollow noopener" target="_blank">{text} \u2192</a>')
    return f'<a class="pk-cta" href="{p["sida"]}">Läs om {p["namn"]} \u2192</a>'


def _pris(slug):
    p = data.PRIS.get(slug, {})
    trafik, hel = p.get('trafik'), p.get('hel')
    if trafik or hel:
        return (f'<div class="pk-pris"><div><span>Trafik från</span>'
                f'<strong>{data.kr(trafik)}</strong><small>per år</small></div>'
                f'<div><span>Hel från</span><strong>{data.kr(hel)}</strong>'
                f'<small>per år</small></div></div>')
    return ('<div class="pk-pris tom"><p>Pris visas när vår egen insamling är klar. '
            '<a href="/redaktionell-metod/">Så gör vi den</a></p></div>')


def _tagg(t):
    return f'<span class="pk-tagg">{t}</span>'


def kort(ordning=None, kompakt=False):
    lista = PARTNERS
    if ordning:
        index = {p['slug']: p for p in PARTNERS}
        lista = [index[x] for x in ordning if x in index]
    ut = []
    for p in lista:
        taggar = ''.join(_tagg(t) for t in p['taggar'])
        if kompakt:
            # Kompakt läge för djupa sidor: samma kort utan de långa
            # beskrivningarna. Modulen ska inte lägga fyrahundra ord
            # identisk text på hundra modellsidor.
            ut.append(f'''<article class="pk kompakt">
<div class="pk-in">
<div class="pk-logo"><img src="{p['logo']}" alt="{p['namn']}" width="120" height="34"
 loading="lazy" decoding="async"></div>
<div class="pk-txt"><h3>{p['namn']}</h3><p class="pk-badge-in">{p['badge']}</p>
<div class="pk-taggar">{taggar}</div></div>
<div class="pk-hoger">{_knapp(p)}</div>
</div></article>''')
            continue
        ut.append(f'''<article class="pk">
<p class="pk-badge {p['badge_typ']}">{BADGE_IKON[p['badge_typ']]} {p['badge']}</p>
<div class="pk-in">
<div class="pk-logo"><img src="{p['logo']}" alt="{p['namn']}" width="120" height="34"
 loading="lazy" decoding="async"></div>
<div class="pk-txt"><h3>{p['namn']}</h3><p>{p['text']}</p>
<div class="pk-taggar">{taggar}</div></div>
<div class="pk-hoger">{_pris(p['slug'])}{_knapp(p)}
<a class="pk-lank" href="{p['sida']}">Läs vår genomgång</a></div>
</div></article>''')

    if kompakt:
        return ''.join(ut)

    t = TJANST
    taggar = ''.join(_tagg(x) for x in t['taggar'])
    knapp = (f'<a class="pk-cta" href="{t["aff"]}" rel="sponsored nofollow noopener" '
             f'target="_blank">Jämför hos {t["namn"]} \u2192</a>' if t.get('aff')
             else '<a class="pk-cta" href="/jamfor-bilforsakring/">Så jämför du själv \u2192</a>')
    ut.append(f'''<article class="pk tjanst">
<p class="pk-badge grå">Jämförelsetjänst</p>
<div class="pk-in">
<div class="pk-logo"><img src="{t['logo']}" alt="{t['namn']}" width="120" height="34"
 loading="lazy" decoding="async"></div>
<div class="pk-txt"><h3>{t['namn']}</h3><p>{t['text']}</p>
<div class="pk-taggar">{taggar}</div></div>
<div class="pk-hoger">{knapp}</div>
</div></article>''')
    return ''.join(ut)


def sektion(rubrik='Bolag att börja med', ingress=None, ordning=None,
            smal=False, kompakt=False):
    """Kortsektionen. Varje sida skickar in egen rubrik och ingress.

    Korten är samma modul på flera sidor — det är en komponent, inte
    brödtext. Rubrik, ingress och ordning varieras ändå per sida, dels
    för att texten ska passa sammanhanget, dels för att sidorna inte ska
    dela stycken med varandra."""
    sponsrat = any(p.get('aff') for p in PARTNERS) or bool(TJANST.get('aff'))
    upplysning = (
        '<p class="pk-upp"><strong>Så finansieras sajten.</strong> '
        + ('Vissa länkar nedan är annonslänkar. Klickar du på dem kan vi få ersättning '
           'av bolaget, vilket inte påverkar vilket pris du får. Ordningen bygger på '
           'kriterierna i vår '
           if sponsrat else
           'Vi har i dag inga annonsavtal med bolagen nedan, och länkarna går till våra '
           'egna genomgångar. Ordningen bygger på kriterierna i vår ')
        + '<a href="/redaktionell-metod/">redaktionella metod</a>, inte på ersättning.</p>')

    if kompakt and ingress is None:
        ingress = 'Tre bolag med olika profil att begära offert från.'
    if ingress is None:
        ingress = ('Tre bolag som utmärker sig på var sin punkt — betyg, kundnöjdhet och '
                   'pris. Etiketterna hänvisar till betyg från Konsumenternas '
                   'Försäkringsbyrå och till publicerade prisexempel, aldrig till egna '
                   'omdömen.')

    wrap = 'wrap narrow' if smal else 'wrap'
    klass = 'sec pk-sek smal' if smal else 'sec pk-sek'

    return f'''<section class="{klass}"><div class="{wrap}">
<h2>{rubrik}</h2>
<p class="pk-ing">{ingress} Hela marknaden finns under
<a href="/forsakringsbolag/">försäkringsbolag</a>.</p>
{upplysning}
<div class="pk-lista">{kort(ordning, kompakt)}</div>
<p class="pk-fot">Priserna avser {data.PROFIL_TEXT}. En annan profil ger ett annat pris —
begär alltid egen offert. Senast kontrollerad: {data.UPPDATERAD_TEXT}.</p>
</div></section>'''
