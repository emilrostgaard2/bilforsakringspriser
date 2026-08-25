# -*- coding: utf-8 -*-
"""Modellsidor — /bilmarken/<märke>/<modell>/.

UNIKHET ÄR HELA POÄNGEN MED DEN HÄR FILEN
Modellsidor är den sidtyp som lättast blir mallutfyllnad, och Google är
hårdast mot just den. Tre saker håller isär sidorna:

1. Allt bärande innehåll kommer ur modeller.py och är skrivet per modell.
2. Rubriker, sektionsordning, ingresser och FAQ-formuleringar roteras
   med olika modulotal, så att två modeller aldrig får samma kombination.
3. Titel, metabeskrivning och H1 byggs av modellens eget 'kort'-fält.

Innan ni lägger till fler märken: kör kontrollen i README under
"dubblettkoll". Går två modellsidor över 40 procent gemensamma meningar
är något fel — då är det modeller.py som är för tunt ifyllt, inte
generatorn som är trasig.

ORDLÄNGD
En modellsida landar på omkring 1 400–1 800 ord med den här strukturen.
Vill ni längre än så ska det komma av mer modellspecifikt underlag i
modeller.py, aldrig av fler generiska stycken — utfyllnad som återkommer
på alla sidor sänker samtliga.
"""
from modeller import MODELLER
from modeller_extra import PRISER, SPANN, EXTRA, META
from brands import MARKEN
import data
import kort

MARKE = {m['slug']: m for m in MARKEN}

AGARE_H2 = ['Vem kör en {b}?', 'Så används en {b} — och varför det spelar roll',
            'Ägarprofilen bakom premien', 'Vilka kör den här bilen?',
            'Bilens vardag avgör priset']
SYSKON_H2 = ['Jämför {m}-modellerna mot varandra', 'Övriga {m}-modeller och deras premie',
             'Hur ligger resten av {m}-utbudet?', 'Andra {m} att jämföra med',
             '{m}-modellerna sida vid sida']
JAMFOR_H2 = ['{b} jämfört med konkurrenterna', 'Hur står sig {b} mot alternativen?',
             '{b} mot liknande bilar', 'Premien i jämförelse med klassen',
             'Vad kostar konkurrenterna?']

H2 = [
    {'pris': 'Vad kostar det att försäkra en {b}?',
     'styr': 'Det här styr premien på din {b}',
     'niva': 'Vilken skyddsnivå passar en {b}?',
     'skada': 'Skadorna som drabbar {b} oftast',
     'villkor': 'Villkoren du bör läsa extra noga',
     'byta': 'Så sänker du priset på din {b}'},
    {'pris': '{b} — prisbild och jämförelse',
     'styr': 'Varför just den här modellen prissätts som den gör',
     'niva': 'Trafik, halv eller hel till en {b}?',
     'skada': 'Vanliga skadeärenden på {b}',
     'villkor': 'Fyra villkorsposter som skiljer bolagen åt',
     'byta': 'Fyra sätt att få ned premien'},
    {'pris': 'Försäkringspris för {b}',
     'styr': 'Premiefaktorerna som väger tyngst här',
     'niva': 'Rätt skyddsnivå utifrån bilens värde',
     'skada': 'Vad som faktiskt går sönder på en {b}',
     'villkor': 'Det som avgör vid en skada',
     'byta': 'Det som ger mest tillbaka på premien'},
    {'pris': 'Premien på en {b} — så ser bilden ut',
     'styr': 'Modellens egna premiedrivare',
     'niva': 'Skyddsnivå för {b} år för år',
     'skada': 'Skadebilden på {b}',
     'villkor': 'Villkorsfrågor att ställa innan du tecknar',
     'byta': 'Konkreta åtgärder som sänker priset'},
    {'pris': 'Kostnaden för en {b}-försäkring',
     'styr': 'Vad bolagen tittar på hos den här modellen',
     'niva': 'När räcker halvförsäkring till en {b}?',
     'skada': 'De ärenden som återkommer',
     'villkor': 'Läs det här innan du väljer bolag',
     'byta': 'Så förhandlar du ned premien'},
]

ORDNING = [
    ['agare', 'styr', 'skada', 'jamfor', 'niva', 'villkor', 'byta'],
    ['agare', 'niva', 'styr', 'jamfor', 'skada', 'villkor', 'byta'],
    ['agare', 'skada', 'styr', 'niva', 'jamfor', 'villkor', 'byta'],
    ['agare', 'styr', 'niva', 'jamfor', 'villkor', 'skada', 'byta'],
    ['agare', 'jamfor', 'styr', 'skada', 'niva', 'villkor', 'byta'],
    ['agare', 'niva', 'jamfor', 'styr', 'villkor', 'skada', 'byta'],
    ['agare', 'skada', 'jamfor', 'niva', 'styr', 'villkor', 'byta'],
]

BYTA_PUNKTER = [
 [('Ange rätt körsträcka', 'Den vanligaste felkällan i offerten, och den som ger mest '
   'tillbaka när den rättas.'),
  ('Kontrollera att bonusen är registrerad', 'Skadefria år följer dig men överförs inte '
   'automatiskt vid byte av bolag.'),
  ('Se över självrisken', 'Höj bara om mellanskillnaden går ihop inom tre år.'),
  ('Betala per år', 'Månadsbetalning innehåller normalt ett påslag.')],
 [('Räkna om skyddsnivån varje år', 'Bilens värde sjunker, premien gör det inte av sig '
   'själv.'),
  ('Stryk dubbla tillägg', 'Rättsskydd och assistans finns ofta redan i hemförsäkringen.'),
  ('Jämför sex veckor före huvudförfallodagen', 'Då hinner uppsägningen igenom i tid.'),
  ('Be ditt nuvarande bolag matcha', 'Med en skriftlig konkurrentoffert är det en '
   'förhandling, inte en förfrågan.')],
 [('Uppdatera var bilen står nattetid', 'Garage eller carport sänker premien direkt hos de '
   'flesta bolag.'),
  ('Kontrollera vem som är huvudsaklig brukare', 'Fel uppgift kan sänka ersättningen vid '
   'skada.'),
  ('Ta bort tillägg du aldrig använt', 'Gå igenom förra årets villkor rad för rad.'),
  ('Hämta minst tre offerter', 'Spridningen mellan bolagen är störst på mindre vanliga '
   'modeller.')],
 [('Meddela ändrad adress', 'Postnumret är en av de tyngre faktorerna och uppdateras inte '
   'automatiskt.'),
  ('Se över antalet förare', 'En yngre extraförare kan kosta mer än den används.'),
  ('Välj bort hyrbil om du har två bilar', 'Momentet är värt mindre när du har en reservbil '
   'hemma.'),
  ('Samla försäkringarna', 'Samlingsrabatt finns hos de flesta — men jämför totalen, inte '
   'rabatten.')],
 [('Kontrollera årsmodell och utrustning i offerten', 'Fel utrustningsnivå ger fel '
   'ersättningsvärde och fel premie.'),
  ('Höj självrisken medvetet', 'Bara om du klarar beloppet den dag det smäller.'),
  ('Fråga efter tyst prishöjning', 'Premien kan ha stigit vid förnyelsen utan att du märkt '
   'det.'),
  ('Byt vid rätt tillfälle', 'Bilköp, flytt och aviserad höjning ger rätt att byta direkt.')],
]

PRIS_ING = [
 'Premien räknas fram ur din bil, din ålder, ditt postnummer och din körsträcka. Tabellen '
 'visar vår jämförelseprofil — ditt eget pris kan ligga både över och under.',
 'Siffrorna gäller en och samma förarprofil hos varje bolag, vilket är det enda sättet att '
 'ställa modeller mot varandra. Byt profil och hela bilden förskjuts.',
 'Ett modellpris är alltid ett medelvärde av mycket olika förare. Använd tabellen för '
 'storleksordningen, inte för att förutse din egen premie.',
 'Vi publicerar bara priser vi hämtat själva på samma villkor hos varje bolag. Saknas '
 'siffran står det streck i stället för en gissning.',
 'Skillnaden mellan billigaste och dyraste bolag på samma bil är ofta större än skillnaden '
 'mellan två helt olika modeller. Det är därför jämförelsen lönar sig.',
 'Tabellen är en utgångspunkt, inte ett bud. Två grannar med samma bil kan få priser som '
 'skiljer med tusenlappar beroende på bonus och ålder.',
 'Priset följer bilens ersättningsvärde, inte dess nypris. På begagnade exemplar är det '
 'skillnaden som förvånar flest.',
 'Ingen prislista kan ersätta en offert på registreringsnumret. Tabellen visar var i '
 'prisskalan modellen brukar hamna.',
 'Nivåerna bygger på varandra, så jämför alltid samma nivå mellan bolagen. Ett lågt pris på '
 'halvförsäkring säger ingenting om helförsäkringen.',
 'Bolagen viktar samma faktorer olika. Därför är spridningen på en enskild modell större än '
 'branschgenomsnittet antyder.',
]

STYR_ING = [
 'Utöver din egen profil är det de här egenskaperna hos bilen som bolagen räknar på.',
 'Bilens tekniska data avgör en stor del av premien redan innan din profil vägs in.',
 'Det här är vad som står i bolagets modelldata när premien beräknas.',
 'Karosstyp, drivlina och ersättningsvärde är de tre faktorer som styr mest hos modellen.',
 'Bolagen prissätter modellen utifrån hur den brukar användas och vad den brukar kosta att '
 'laga.',
 'Innan din ålder och ditt postnummer vägs in ligger modellens egen riskprofil till grund.',
 'De här uppgifterna hämtas ur fordonsregistret och avgör grundpremien.',
 'Modellens egenskaper sätter ramen — din profil avgör var inom ramen du hamnar.',
 'Det som skiljer den här bilen från andra i samma prisklass står i tabellen nedan.',
 'Så här ser modellens riskprofil ut i bolagens ögon.',
]

NIVA_ING = [
 'Valet av nivå ska följa bilens värde, inte vanan. Räkna om varje år.',
 'Frågan är enkel: vad skulle du förlora om bilen totalskadades i en olycka du själv '
 'orsakat? Det är precis vad halvförsäkring inte täcker.',
 'Nivån bör omprövas vid varje förnyelse. Bilen tappar i värde, premien gör det inte av sig '
 'själv.',
 'Skillnaden mellan halv och hel är vagnskadedelen — och den är den dyraste delen av '
 'premien.',
 'Ju lägre marknadsvärde, desto mindre kan vagnskadedelen betala ut. Där går gränsen.',
 'Rätt nivå beror på bilens ålder, var den står nattetid och hur mycket du klarar att '
 'betala själv vid en skada.',
 'De flesta behåller helförsäkringen för länge. Räkna på det i stället för att förnya '
 'automatiskt.',
 'Vagnskadegarantin gör att nya bilar klarar sig med halvförsäkring de första åren.',
 'Är bilen värd mindre än självrisken plus några tiotusen kronor är helförsäkring sällan '
 'motiverad.',
 'Nivåvalet är den enskilt största posten du själv styr över i premien.',
]

SKADA_ING = [
 'Skadebilden skiljer sig mer mellan modeller än de flesta tror, och den avgör vilka moment '
 'som faktiskt kommer till användning.',
 'Vilka skador en modell drabbas av avgör vilken nivå som är värd pengarna.',
 'Bolagen prissätter utifrån vad som brukar hända, inte vad som kan hända.',
 'Det är återkommande småskador, inte de stora olyckorna, som styr premien mest.',
 'Statistiken bakom premien handlar om frekvens lika mycket som om belopp.',
 'En modell med många billiga skador kan kosta mer att försäkra än en med få dyra.',
 'Skadetypen avgör vilken självrisk du faktiskt kommer att betala.',
 'Var bilen står och hur den används formar skadebilden mer än körstilen.',
 'Det här mönstret är hämtat ur hur ärenden på modellen brukar se ut.',
 'Känner du igen skadetypen vet du också vilket moment du inte bör välja bort.',
]

VILLKOR_ING = [
 'Två offerter med samma pris kan skilja med tusenlappar den dag något händer. Här skiljer '
 'sig bolagen mest.',
 'Priset är ena halvan. Den andra är vad som faktiskt står i villkoren.',
 'Det är de här posterna som avgör utfallet vid en skada — inte årspremien.',
 'Innan du väljer bolag: läs de fem raderna nedan i varje offert.',
 'Villkoren är det som skiljer en billig försäkring från en dålig.',
 'De här posterna kostar ingenting att jämföra och kan bli dyra att missa.',
 'Skillnaderna mellan bolagen ligger sällan i priset och nästan alltid här.',
 'Kontrollera det här i offerten, inte i marknadsföringen.',
 'Fem frågor som avgör om två offerter över huvud taget är jämförbara.',
 'Den som bara jämför årspremien jämför halva försäkringen.',
]

BYTA_ING = [
 'Ordningen är avsiktlig — de två första ger nästan alltid mest, och kostar dig ingenting i '
 'skydd.',
 'Börja uppifrån. Effekten avtar snabbt längre ned i listan.',
 'Fyra åtgärder som går att göra i dag, utan att försämra skyddet.',
 'Det här är åtgärder som fungerar. Rabattkoder och kampanjer är sällan värda tiden.',
 'De flesta kan sänka premien utan att byta bolag — det här är hur.',
 'Rätta felaktiga uppgifter först, förhandla sedan.',
 'Två av punkterna nedan handlar om att offerten ska stämma, inte om att pruta.',
 'Gå igenom listan innan du hämtar nya offerter, annars jämför du på fel underlag.',
 'Åtgärderna är sorterade efter vad de brukar ge, inte efter hur enkla de är.',
 'Ingen av punkterna kräver att du säger upp något.',
]

SYSKON_ING = [
 'Samma märke, men olika skadebild och olika ersättningsvärden.',
 'Modellerna delar verkstadsnät och delkatalog — men inte premie.',
 'Vad kostar de andra bilarna i utbudet? Så här ser bredden ut.',
 'Karosstyp och drivlina förskjuter premien mer än märket gör.',
 'Byter du modell inom märket följer inte premien med.',
 'Jämför gärna mot syskonmodellerna innan du bestämmer dig för bil.',
 'Utbudet spänner över flera prisklasser och därmed flera premienivåer.',
 'Samma tillverkare, olika riskprofiler.',
 'Här är resten av utbudet, med länk till varje modellsida.',
 'Skillnaden mellan två modeller från samma märke kan vara större än mellan två märken.',
]

FAQ_PRIS = [
 'Priset beräknas individuellt och kan skilja med flera tusen kronor mellan bolagen för '
 'exakt samma bil. Begär offert på registreringsnumret hos minst tre bolag.',
 'Det finns inget fast pris för en modell. Ålder, postnummer, skadefria år och körsträcka '
 'påverkar mer än vilken bil du kör.',
 'Premien sätts på dig och bilen tillsammans. Två personer med samma modell kan ha dubbelt '
 'så stor skillnad i pris beroende på bostadsort och bonus.',
 'Vi publicerar inga påhittade från-priser. Vår egen insamling pågår, och tills den är klar '
 'står det streck i tabellen.',
 'Räkna med att spridningen mellan bolagen är stor. Det är därför tre offerter är minimum.',
 'Modellen sätter ramen, din profil avgör priset inom den. Hämta offert på '
 'registreringsnumret.',
 'Årsmodell och utrustningsnivå påverkar mer än många tror, eftersom de styr '
 'ersättningsvärdet.',
 'Priset följer marknadsvärdet. Är bilen begagnad blir premien lägre än siffror för nya '
 'exemplar antyder.',
 'Bolagen viktar faktorerna olika, vilket gör att ingen är billigast för alla.',
 'Jämför på samma nivå och samma självrisk, annars jämför du inte samma sak.',
]

def _desc(b, slug, kort):
    """Metabeskrivning som ryms i sökresultatet utan att kapas."""
    klausul = META.get(slug) or kort.rstrip('.')
    text = (f'Vad kostar försäkring till {b}? Se prisexempel för {klausul}, '
            f'rätt skyddsnivå och villkoren som avgör.')
    if len(text) > 155:
        text = f'{b} försäkring: prisexempel för {klausul}, rätt skyddsnivå och villkor.'
    return text


def _tbl(caption, kol, rader, swipe=False):
    th = ''.join(f'<th scope="col">{k}</th>' for k in kol)
    tr = ''.join('<tr><th scope="row">' + r[0] + '</th>'
                 + ''.join(f'<td>{c}</td>' for c in r[1:]) + '</tr>' for r in rader)
    s = '<p class="swipe">&larr; Dra i sidled för att se alla kolumner</p>' if swipe else ''
    return (f'<div class="tbl"><table><caption>{caption}</caption><thead><tr>{th}</tr></thead>'
            f'<tbody>{tr}</tbody></table></div>{s}')


def _sektion(nyckel, m, mod, b, i, syskon):
    h = H2[i % len(H2)].get(nyckel, '').replace('{b}', b)
    p = data.PRIS

    if nyckel == 'pris':
        e = EXTRA.get(mod['slug'], {})
        cit = PRISER.get(mod['slug'])
        if cit:
            rader = [[c['bolag'], c['belopp'], c['vad'], c['profil'],
                      f'{c["kalla"]}, {c["datum"]}'] for c in cit]
            tabell = _tbl(f'Publicerade prisuppgifter för {b}',
                          ['Bolag', 'Belopp', 'Avser', 'Källans profil', 'Källa'],
                          rader, swipe=True)
            kalltext = (f'<p class="jf-not">Uppgifterna kommer från andra sajters '
                        f'publicerade prisexempel och redovisas med källa och datum. Varje '
                        f'källa använder sin egen profil, vilket gör att beloppen inte är '
                        f'jämförbara med varandra. Vår egen insamling på en och samma profil '
                        f'pågår.</p>')
        else:
            rader = [[x['niva'], x['spann'], f'{x["kalla"]}, {x["datum"]}'] for x in SPANN]
            tabell = _tbl('Marknadens publicerade prisspann',
                          ['Nivå', 'Spann', 'Källa'], rader)
            kalltext = (f'<p class="jf-not">Vi har inte hittat publicerade prisuppgifter för '
                        f'specifikt {b}. I stället visas marknadens spann med källa. Det är '
                        f'ärligare än att räkna fram en siffra och kalla den ett pris — och '
                        f'det säger dig var i skalan du bör hamna.</p>')
        return (f'<h2>{h}</h2>'
                f'<p class="direkt">{e.get("direktsvar", "")}</p>'
                + tabell + kalltext
                + f'<p>{PRIS_ING[i % len(PRIS_ING)]}</p>')

    if nyckel == 'agare':
        e = EXTRA.get(mod['slug'], {})
        rub = AGARE_H2[i % len(AGARE_H2)].replace('{b}', b)
        return f'<h2>{rub}</h2><p>{e.get("agare", "")}</p>'

    if nyckel == 'jamfor':
        e = EXTRA.get(mod['slug'], {})
        rub = JAMFOR_H2[i % len(JAMFOR_H2)].replace('{b}', b)
        return f'<h2>{rub}</h2><p>{e.get("jamfor", "")}</p>'

    if nyckel == 'styr':
        rader = [['Drivlina', mod['drivlina']],
                 ['Karosstyp', mod['typ'].capitalize()],
                 ['Årsmodeller', mod['ar']],
                 ['Reservdelsläge', 'Delas med övriga ' + m['namn'] + '-modeller'],
                 ['Ersättningsvärde', mod['varde']]]
        punkter = ''.join(f'<li>{x}</li>' for x in mod['punkter'])
        return (f'<h2>{h}</h2><p>{STYR_ING[i % len(STYR_ING)]}</p>'
                + _tbl(f'{b} — modellens egna premiefaktorer', ['Faktor', 'Betydelse'], rader)
                + f'<ul>{punkter}</ul>')

    if nyckel == 'niva':
        rader = [['Under 3 år', 'Halvförsäkring räcker om vagnskadegarantin gäller',
                  'Garantin täcker vagnskadedelen'],
                 ['3–8 år', 'Helförsäkring', 'Marknadsvärdet motiverar vagnskadedelen'],
                 ['8–12 år', 'Räkna på det', 'Jämför premien mot bilens värde'],
                 ['Över 12 år', 'Ofta halvförsäkring', 'Vagnskadedelen betalar sällan ut '
                  'mer än den kostar']]
        return (f'<h2>{h}</h2><p>{NIVA_ING[i % len(NIVA_ING)]} {mod["niva"]}</p>'
                + _tbl(f'Skyddsnivå för {b} efter ålder',
                       ['Bilens ålder', 'Rimlig nivå', 'Motivering'], rader, swipe=True)
                + f'<p>Läs mer om skillnaden mellan '
                  f'<a href="/halvforsakring/">halvförsäkring</a> och '
                  f'<a href="/helforsakring/">helförsäkring</a>, eller om hur '
                  f'<a href="/sjalvrisk/">självrisken</a> påverkar vad som faktiskt '
                  f'betalas ut.</p>')

    if nyckel == 'skada':
        return (f'<h2>{h}</h2><p>{SKADA_ING[i % len(SKADA_ING)]}</p>'
                f'<p>{mod["skada"]}</p>'
                + _tbl(f'Vilken nivå som täcker vad på en {b}',
                       ['Skadetyp', 'Trafik', 'Halv', 'Hel'],
                       [['Skada på annans bil eller egendom', 'Ja', 'Ja', 'Ja'],
                        ['Stöld och inbrott', 'Nej', 'Ja', 'Ja'],
                        ['Brand', 'Nej', 'Ja', 'Ja'],
                        ['Glas och stenskott', 'Nej', 'Ja', 'Ja'],
                        ['Viltolycka', 'Nej', 'Ja', 'Ja'],
                        ['Egen vållad krock', 'Nej', 'Nej', 'Ja'],
                        ['Parkeringsskada utan motpart', 'Nej', 'Nej', 'Ja'],
                        ['Skadegörelse', 'Nej', 'Nej', 'Ja']], swipe=True))

    if nyckel == 'villkor':
        return (f'<h2>{h}</h2><p>{VILLKOR_ING[i % len(VILLKOR_ING)]}</p>'
                + _tbl('Att kontrollera i offerten',
                       ['Post', 'Varför den spelar roll här'],
                       [['Glassjälvrisk', 'Skillnaden mellan lagning och byte, och '
                         'kalibrering av kameran bakom rutan'],
                        ['Hyrbilsdagar', 'Väntetid på delar drabbar dig direkt'],
                        ['Maskinskada', 'Gäller bara upp till en viss ålder och körsträcka'],
                        ['Verkstadsval', 'Fritt val eller anvisad verkstad'],
                        ['Djurkollision', 'Om självrisken reduceras vid viltolycka']])
                + f'<p>En fullständig genomgång av samtliga självrisktyper finns på sidan om '
                  f'<a href="/sjalvrisk/">självrisk</a>.</p>')

    if nyckel == 'byta':
        punkter = BYTA_PUNKTER[i % len(BYTA_PUNKTER)]
        rader = [[t, b_] for t, b_ in punkter]
        return (f'<h2>{h}</h2><p>{BYTA_ING[i % len(BYTA_ING)]}</p>'
                + _tbl('Åtgärder i prioritetsordning', ['Åtgärd', 'Varför'], rader)
                + f'<p>Hela regelverket för när du får byta står under '
                  f'<a href="/byta-bilforsakring/">byta bilförsäkring</a>.</p>')
    return ''


def _syskontabell(m, mod, syskon):
    rader = [[f'<a href="/bilmarken/{m["slug"]}/{s["slug"]}/">{m["namn"]} {s["namn"]}</a>',
              s['typ'].capitalize(), s['drivlina'], '—']
             for s in syskon if s['slug'] != mod['slug']]
    return _tbl(f'Andra {m["namn"]}-modeller',
                ['Modell', 'Typ', 'Drivlina', 'Helförsäkring'], rader, swipe=True)


def sidor():
    ut = []
    for marke_slug, lista in MODELLER.items():
        m = MARKE[marke_slug]
        for i, mod in enumerate(lista):
            b = f'{m["namn"]} {mod["namn"]}'
            mod_extra = EXTRA.get(mod['slug'], {})
            ordning = ORDNING[i % len(ORDNING)]
            kroppar = ''.join(_sektion(k, m, mod, b, i, lista) for k in ordning)

            faq = [
                mod['fraga'],
                (f'Vad kostar bilförsäkring till {b}?', FAQ_PRIS[i % len(FAQ_PRIS)]),
                (f'Behöver jag helförsäkring på min {b}?',
                 mod['niva'] + ' Räkna alltid på bilens marknadsvärde minus självrisken — '
                 'det är den summan vagnskadedelen kan betala ut.'),
                (f'Vilket bolag är billigast för {b}?',
                 'Det varierar med förarprofilen. Ett bolag som är billigast för en '
                 '25-åring i Malmö kan vara dyrast för en 60-åring i Umeå. Jämför alltid '
                 'på ditt eget registreringsnummer.'),
                (f'Påverkar {mod["typ"]}-formatet premien?',
                 f'Ja, indirekt. Karosstypen styr både vilka skador som är vanliga och vad '
                 f'en reparation kostar. {mod["skada"].split(".")[0]}.'),
            ]

            ut.append({
                'slug': f'bilmarken/{m["slug"]}/{mod["slug"]}',
                'key': True,
                'title': f'{b} försäkring — pris, villkor och jämförelse {data.UPPDATERAD[:4]}',
                # Metabeskrivning: kapas vid ordgräns så att den aldrig slutar
                # mitt i ett ord, och håller sig under 155 tecken.
                'desc': _desc(b, mod['slug'], mod['kort']),
                'eyebrow': f'{m["namn"]} · {mod["typ"].capitalize()}',
                'h1': f'{b} försäkring',
                'lead': mod['kort'] + ' ' + mod['vinkel'].split('.')[0] + '.',
                'checks': mod['punkter'],
                'card_t': f'Se vad din {b} kostar',
                'sticky': f'Jämför försäkring till {b}',
                'bild': f'/bilder/{m["slug"]}.webp' if m['slug'] else None,
                'body': (
                    f'<section class="sec"><div class="wrap narrow">'
                    f'<div class="note"><p><strong>Kort sagt.</strong> {mod["vinkel"]}</p>'
                    f'</div>'
                    + _sektion('pris', m, mod, b, i, lista)
                    + '</div></section>'
                    # Bolagen direkt under prisavsnittet — det är där läsaren är
                    # när frågan "vad kostar det" precis besvarats.
                    + kort.sektion(
                        f'Bolag att begära offert från till {b}',
                        None, ['ica-forsakring', 'dina-forsakringar', 'gofido'],
                        smal=True, kompakt=True)
                    + f'<section class="sec"><div class="wrap narrow">'
                    + kroppar
                    + f'<h2>{SYSKON_H2[i % len(SYSKON_H2)].replace("{m}", m["namn"])}</h2>'
                    + f'<p>{SYSKON_ING[i % len(SYSKON_ING)]}</p>'
                    + _syskontabell(m, mod, lista)
                    + f'<h2>{mod_extra.get("lang", ("", ""))[0]}</h2>'
                    + f'<p class="direkt">{mod_extra.get("lang", ("", ""))[1]}</p>'
                    + f'<div class="cta"><h2>Se priset på din {b}</h2>'
                      f'<p>Ange registreringsnumret så hämtas bilens uppgifter '
                      f'automatiskt.</p><div class="cta-inner">{{PLATE}}</div></div>'
                      f'</div></section>'),
                'faq_h2': f'Vanliga frågor om försäkring till {b}',
                'faq': faq,
                'rel': [(f'/bilmarken/{m["slug"]}/', f'{m["namn"]} bilförsäkring'),
                        ('/bilmarken/', 'Alla bilmärken'),
                        ('/halvforsakring/', 'Halvförsäkring'),
                        ('/helforsakring/', 'Helförsäkring'),
                        ('/jamfor-bilforsakring/', 'Så jämför du offerter')],
            })
    return ut
