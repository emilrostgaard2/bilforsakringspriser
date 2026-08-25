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

AGARE_H2 = ['Vem kör en {b}?', 'Så används en {b} — och varför det spelar roll',
            'Ägarprofilen bakom premien', 'Vilka kör den här bilen?',
            'Bilens vardag avgör priset']
SYSKON_H2 = ['Jämför {m}-modellerna mot varandra', 'Övriga {m}-modeller och deras premie',
             'Hur ligger resten av {m}-utbudet?', 'Andra {m} att jämföra med',
             '{m}-modellerna sida vid sida']
TILLAGG_H2 = ['Vilka tillägg är värda pengarna på en {b}?', 'Tilläggen som lönar sig här',
              'Vad du bör lägga till — och vad du kan stryka', 'Tilläggsförsäkringar för {b}',
              'Extraskydden som faktiskt används']
TILLAGG_ING = [
 'Tillägg säljs som en klumpsumma men bör väljas ett i taget. Det avgörande är inte vad de '
 'kostar utan hur sannolikt det är att just du får användning för dem.',
 'De flesta betalar för minst ett tillägg de aldrig kommer att använda, och saknar ett de '
 'skulle ha haft nytta av. Vilka det är beror på bilen.',
 'Ett tillägg är värt sin premie när sannolikheten att det används är rimlig i förhållande '
 'till kostnaden. Här är hur den kalkylen ser ut för den här modellen.',
 'Gå igenom tilläggen mot bilens faktiska skadebild i stället för mot vad de heter.',
 'Skadebilden avgör vilka tillägg som betalar sig. Den skiljer sig mer mellan modeller än '
 'mellan bolag.',
 'Det finns inget tillägg som är rätt för alla. Det finns däremot tillägg som är fel för den '
 'här bilen.',
 'Innan du väljer till: fråga vad som redan ingår. Dubbelt skydd är den vanligaste onödiga '
 'kostnaden i en bilförsäkring.',
]
SLUT_RAKNA = [
 'Beloppen är räkneexempel på självrisken, inte prisuppgifter. Poängen är proportionen '
 'mellan vad du betalar varje år och vad försäkringen kan betala tillbaka.',
 'Siffrorna illustrerar självriskens effekt, inget annat. Det är förhållandet mellan premie '
 'och möjlig ersättning som avgör nivån.',
 'Tabellen visar hur självrisken äter av ersättningen. Sätt den summan mot vad '
 'vagnskadedelen kostar per år.',
 'Räkneexemplen säger inget om priset, bara om vad som blir kvar när självrisken dragits.',
 'Det är skillnaden mellan årspremien och den möjliga ersättningen som avgör om '
 'vagnskadedelen är värd att behålla.',
 'Jämför den möjliga utbetalningen med vad vagnskadedelen kostar under fem år. Då blir '
 'valet tydligt.',
 'Beloppen är exempel. Metoden — värde minus självrisk — är densamma oavsett bil.',
]
SLUT_CHECK = [
 'Det är den skadetypen din offert i praktiken ska klara, och därför väger villkoren tyngre '
 'än de sista hundralapparna i premie.',
 'Offerten ska matcha den skadebilden. Ett lägre pris på sämre villkor är ingen besparing.',
 'Kontrollera att offerten faktiskt täcker det som brukar hända den här bilen.',
 'Villkoren avgör utfallet vid just den typen av ärende. Priset avgör bara vad du betalar '
 'under tiden ingenting händer.',
 'Det är mot den skadebilden offerten ska mätas, inte mot marknadens genomsnitt.',
 'Väg villkoren mot den vanligaste skadan, inte mot den värsta tänkbara.',
 'Den skadetypen är den mest sannolika. Se till att den är ordentligt täckt.',
]
SLUT_TILLAGG = [
 'Det är skälet till att tilläggen bör väljas efter bilen och inte efter vad paketet råkar '
 'heta hos bolaget.',
 'Välj tillägg efter bilens skadebild, inte efter paketets namn.',
 'Ett tilläggspaket är sällan optimerat för din bil. Plocka delarna själv.',
 'Bolagens paket är byggda för genomsnittsbilen. Din är inte det.',
 'Gå efter vad bilen faktiskt råkar ut för, inte efter vad tillägget heter.',
 'Det är bilens egenskaper som avgör vilka tillägg som betalar sig.',
 'Namnet på paketet säger ingenting om vad du behöver.',
]
SLUT_BEGAGNAT = [
 'Det är den siffran vagnskadedelen utgår från vid en totalskada, och därmed den som avgör '
 'om helförsäkring är motiverad.',
 'Marknadsvärdet i dag är det enda som räknas vid en totalskada — inte nypriset.',
 'Ersättningen bygger på vad bilen är värd nu. Låt det styra skyddsnivån.',
 'Vagnskadedelen kan aldrig betala mer än marknadsvärdet minus självrisken.',
 'Det är dagens värde, inte köpeskillingen, som avgör vad försäkringen kan ge tillbaka.',
 'Skyddsnivån ska följa värdet, och värdet ändras varje år.',
 'Räkna på dagens värde varje gång försäkringen förnyas.',
]
SLUT_SPANN = [
 'Det är ärligare än att räkna fram en siffra och kalla den ett pris — och det säger dig var '
 'i skalan du bör hamna.',
 'Vi redovisar hellre spannet med källa än en uträknad siffra utan grund.',
 'Ett spann med källa är mer användbart än ett påhittat exakt belopp.',
 'Så vet du var i skalan bilen bör hamna, utan att vi gissar åt dig.',
 'Marknadens spann säger mer om storleksordningen än ett enskilt framräknat tal skulle göra.',
 'Vi publicerar det vi kan belägga och skriver ut resten.',
 'Spannet är hämtat med källa. Din egen offert är det enda exakta svaret.',
]
PROFIL_ING = [
 'Utöver bilen väger din egen profil tyngre än de flesta tror. Bostadsorten sätts på '
 'postnummernivå, inte på kommun, och skillnaden mellan två adresser i samma stad kan vara '
 'större än mellan två landsändar.',
 'Bilen sätter ramen, men det är din profil som avgör var inom ramen du hamnar. Postnumret '
 'väger tyngst av det du inte kan ändra, körsträckan av det du kan.',
 'Två personer med samma bil kan betala dubbelt så mycket som varandra. Skillnaden ligger '
 'nästan alltid i ålder, bonus och var bilen står nattetid.',
 'Premien är en produkt av bil och förare. Modellen förklarar sällan mer än halva '
 'skillnaden mellan två offerter.',
 'Det som avgör din premie utöver modellen är tre uppgifter du själv lämnar: adress, '
 'körsträcka och antal skadefria år.',
 'Bolagen räknar på bilen och på dig samtidigt. Den delen du styr över är större än den '
 'delen bilen står för.',
 'Din egen profil förklarar oftare skillnaden mellan två offerter än vilken bil det gäller.',
]
GARANTI_ING = [
 'Nya bilar har normalt vagnskadegaranti i tre år från första registrering, och under den '
 'tiden räcker halvförsäkring — garantin täcker det som annars är vagnskadedelen.',
 'De första tre åren har en ny bil normalt vagnskadegaranti från tillverkaren. Då behövs '
 'ingen helförsäkring, eftersom garantin gör samma jobb.',
 'Vagnskadegarantin följer med nya bilar i tre år och gör helförsäkring överflödig under '
 'den perioden. Halvförsäkring räcker.',
 'Är bilen under tre år gammal täcker tillverkarens vagnskadegaranti normalt det '
 'helförsäkringen annars gör.',
 'Under garantitiden betalar du för ett skydd du redan har om du väljer helförsäkring. '
 'Kontrollera datumet för första registrering.',
 'Tillverkarens vagnskadegaranti gäller i regel tre år och gör att halvförsäkring räcker '
 'så länge.',
 'Nybilsgarantin på vagnskada löper tre år. Många tecknar helförsäkring ändå, utan att '
 'behöva det.',
]
SUMMA_H2 = ['Sammanfattning — {b} och försäkringen', 'Det viktigaste om {b} i korthet',
            'Slutsats: så försäkrar du en {b}', '{b} — sammanfattat',
            'Kort sammanfattning innan du väljer']
SUMMA_ING = [
 'Om du bara tar med dig tre saker från den här sidan, ta med de här.',
 'Sammanfattat i tre punkter, i den ordning de påverkar din premie.',
 'Det här är vad som faktiskt avgör vad du betalar för den här bilen.',
 'Tre slutsatser, hämtade ur allt ovan.',
 'Kortversionen för dig som ska hämta offert i dag.',
 'Det viktigaste, destillerat.',
 'Tre saker att ha med när du ringer bolaget.',
]
BEGAGNAT_H2 = ['Köper du {b} begagnad?', 'Vad du bör kontrollera vid begagnatköp',
               'Begagnad {b} — försäkringen vid ägarbytet', 'Att tänka på vid köp av begagnad {b}',
               'Ägarbytet och försäkringen']
BEGAGNAT_ING = [
 'Försäkringsplikten börjar den dag du står som ägare, inte den dag du hämtar bilen. Det är '
 'den vanligaste och dyraste missen vid ett begagnatköp.',
 'Vid ett ägarbyte upphör säljarens försäkring automatiskt. Din egen måste börja gälla samma '
 'dag, annars är bilen oförsäkrad.',
 'Ett begagnatköp är också ett tillfälle att byta bolag — du får teckna nytt utan att vänta '
 'på huvudförfallodagen.',
 'Den som köper begagnat får en bil med historik men bygger sin egen premie från noll av den '
 'historiken.',
 'Bilens tidigare körsträcka följer med i annonsen men inte in i din offert. Din egen '
 'körsträcka är den som ska anges.',
 'Vid köp av begagnad bil finns tre datum som måste stämma: ägarbytet, försäkringens start '
 'och den gamla försäkringens slut.',
 'Ett ägarbyte är den enklaste tidpunkten att göra rätt från början, eftersom ingenting är '
 'låst ännu.',
]
CHECK_H2 = ['Checklista innan du tecknar till din {b}', 'Det här ska du kontrollera i offerten',
            'Nio punkter att gå igenom för {b}', 'Innan du skriver på — {b}',
            'Vad du bör fråga bolaget om']
CHECK_ING = [
 'Gå igenom listan med offerten framför dig. De tre första punkterna gäller just den här '
 'modellen, resten gäller alla bilar men glöms oftast bort.',
 'De tre översta punkterna är specifika för modellen. De tre nedersta är sådant som gäller '
 'alla bilar och ändå missas i nio offerter av tio.',
 'Punkterna är sorterade med det modellspecifika först. Ta listan med dig när du ringer '
 'bolaget — det tar fem minuter och avgör vad du faktiskt får.',
 'Här är vad som skiljer en bra offert från en billig på just den här bilen.',
 'Den här listan är skillnaden mellan att jämföra pris och att jämföra försäkring.',
 'Kontrollera punkterna i varje offert, inte bara i den du lutar åt. Annars jämför du inte '
 'samma sak.',
 'Tre modellspecifika punkter och tre allmänna. Alla sex kostar ingenting att kontrollera.',
]
RAKNA_H2 = ['Räkna på om helförsäkring lönar sig', 'Lönar sig vagnskadedelen på din {b}?',
            'Så räknar du ut rätt skyddsnivå', 'Vad du faktiskt får ut vid en totalskada',
            'Premien mot vad försäkringen kan betala']
RAKNA_ING = [
 'Vagnskadedelen ersätter bilens marknadsvärde minus självrisken — inte vad du betalade och '
 'inte vad en likvärdig bil kostar hos en handlare.',
 'Frågan är enkel att räkna på: hur mycket kan försäkringen betala ut, och hur mycket kostar '
 'den delen per år?',
 'Ersättningen vid totalskada bygger på marknadsvärdet, och det är ofta lägre än ägaren tror.',
 'Sätt vad vagnskadedelen kostar per år mot vad den skulle betala ut. Kalkylen avgör nivån.',
 'Det här är den enda beräkning som verkligen behövs för att välja skyddsnivå.',
 'Vagnskadedelen är den dyraste delen av premien. Räkna på vad den kan ge tillbaka.',
 'Marknadsvärdet minus självrisken är hela ersättningen vid totalskada. Börja där.',
]
TEKNIK_H2 = ['Tekniken som avgör reparationskostnaden', 'Vad som gör en {b} dyr eller billig att laga',
             'Under plåten — det som kostar vid en skada', 'Reparationsbilden för {b}',
             'Teknik, verkstad och delar']
KOSTNAD_H2 = ['{b} i den totala ägarkostnaden', 'Var försäkringen hamnar bland dina bilkostnader',
              'Vad {b} kostar utöver premien', 'Försäkringen som andel av driftkostnaden',
              'Helhetsbilden av vad bilen kostar']
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
    ['agare', 'teknik', 'styr', 'skada', 'jamfor', 'rakna', 'niva', 'tillagg', 'kostnad', 'begagnat', 'checklista', 'villkor', 'byta', 'summa'],
    ['agare', 'niva', 'teknik', 'styr', 'jamfor', 'skada', 'rakna', 'tillagg', 'begagnat', 'kostnad', 'villkor', 'checklista', 'byta', 'summa'],
    ['agare', 'skada', 'teknik', 'styr', 'rakna', 'niva', 'tillagg', 'jamfor', 'begagnat', 'checklista', 'villkor', 'kostnad', 'byta', 'summa'],
    ['agare', 'teknik', 'niva', 'rakna', 'styr', 'tillagg', 'jamfor', 'kostnad', 'begagnat', 'villkor', 'skada', 'checklista', 'byta', 'summa'],
    ['agare', 'jamfor', 'teknik', 'styr', 'skada', 'niva', 'rakna', 'begagnat', 'tillagg', 'kostnad', 'checklista', 'villkor', 'byta', 'summa'],
    ['agare', 'niva', 'rakna', 'jamfor', 'teknik', 'tillagg', 'styr', 'villkor', 'begagnat', 'skada', 'kostnad', 'checklista', 'byta', 'summa'],
    ['agare', 'skada', 'jamfor', 'teknik', 'rakna', 'tillagg', 'niva', 'styr', 'checklista', 'begagnat', 'kostnad', 'villkor', 'byta', 'summa'],
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

TITEL_MALL = [
 '{b} försäkring — pris, villkor och jämförelse {ar}',
 'Försäkring {b} {ar} — vad kostar den och vad ingår?',
 '{b} bilförsäkring {ar} — prisspann, skyddsnivå och villkor',
 'Vad kostar försäkring till {b}? Pris och villkor {ar}',
 '{b} försäkring {ar} — jämför pris, självrisk och skydd',
 'Bilförsäkring {b} — så mycket kostar den {ar}',
 '{b} — försäkringspris, rätt nivå och villkoren {ar}',
 'Försäkra {b} {ar} — prisspann, tillägg och jämförelse',
 '{b} bilförsäkring — pris, skadebild och villkor {ar}',
 'Vad kostar det att försäkra {b}? Guide {ar}',
]

DESC_MALL = [
 'Vad kostar försäkring till {b}? Se prisspann för {k}, rätt skyddsnivå och villkoren '
 'som avgör.',
 '{b} är {k}. Se uppskattat prisspann, vilken nivå som passar och vad du bör kontrollera '
 'i offerten.',
 'Så mycket kostar det att försäkra {b} — {k}. Prisspann, skadebild och villkor att jämföra.',
 'Prisspann, skyddsnivå och villkor för {b}, {k}. Plus vilka tillägg som är värda pengarna.',
 'Ska du försäkra {b}? Se vad {k} kostar, vilken nivå som räcker och var bolagen skiljer sig.',
 '{b} — {k}. Uppskattat prisspann per nivå, vanliga skador och tre bolag att jämföra.',
 'Guide till försäkring för {b}, {k}: prisspann, självrisk, tillägg och rätt skyddsnivå.',
 'Vad bör du betala för att försäkra {b}? Prisspann för {k} plus villkoren som avgör.',
 'Allt om bilförsäkring till {b} — {k}. Pris, skadebild, tillägg och jämförelse.',
 '{b}: se prisspann, vilken nivå bilen behöver och vad du ska fråga bolaget om. {k}.',
]


def _titel(b, i, ar):
    return TITEL_MALL[(i * 7 + 5) % len(TITEL_MALL)].replace('{b}', b).replace('{ar}', ar)


def _desc(b, slug, kort, i):
    """Metabeskrivning: roterande mall plus modellens egen klausul.

    Tio mallar gånger unika klausuler ger beskrivningar som varken är
    identiska eller uppenbart mallade. Kapas alltid under 155 tecken,
    och aldrig mitt i ett ord."""
    k = (META.get(slug) or kort).rstrip('.')
    text = DESC_MALL[(i * 5 + 4) % len(DESC_MALL)].replace('{b}', b).replace('{k}', k)
    if len(text) > 155:
        text = text[:152].rsplit(' ', 1)[0].rstrip(',.') + '.'
    return text


def _tbl(caption, kol, rader, swipe=False):
    th = ''.join(f'<th scope="col">{k}</th>' for k in kol)
    tr = ''.join('<tr><th scope="row">' + r[0] + '</th>'
                 + ''.join(f'<td>{c}</td>' for c in r[1:]) + '</tr>' for r in rader)
    s = '<p class="swipe">&larr; Dra i sidled för att se alla kolumner</p>' if swipe else ''
    return (f'<div class="tbl"><table><caption>{caption}</caption><thead><tr>{th}</tr></thead>'
            f'<tbody>{tr}</tbody></table></div>{s}')


def _sektion(nyckel, m, mod, b, i, syskon):
    h = H2[(i * 3 + 3) % len(H2)].get(nyckel, '').replace('{b}', b)
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
            k = upp.klass_for(mod['slug'], mod['namn'], m['grupp'])
            rader = [['<a href="/halvforsakring/">Halvförsäkring</a>',
                      upp.spann(k, 'halv'), upp.ar_spann(k, 'halv')],
                     ['<a href="/helforsakring/">Helförsäkring</a>',
                      upp.spann(k, 'hel'), upp.ar_spann(k, 'hel')]]
            tabell = (_tbl(f'Uppskattat prisspann för {b}',
                           ['Nivå', 'Per månad', 'Per år'], rader)
                      + upp.metodruta(kort=True, i=i)
                      + _tbl('Marknadens publicerade siffror',
                             ['Nivå', 'Spann', 'Källa'],
                             [[x['niva'], x['spann'], f'{x["kalla"]}, {x["datum"]}']
                              for x in SPANN]))
            kalltext = (f'<p class="jf-not">Vi har inte hittat publicerade prisuppgifter för '
                        f'specifikt {b}. I stället visas marknadens spann med källa. '
                        f'{SLUT_SPANN[(i * 3 + 3) % len(SLUT_SPANN)]}</p>')
        return (f'<h2>{h}</h2>'
                f'<p class="direkt">{e.get("direktsvar", "")}</p>'
                + tabell + kalltext
                + f'<p>{PRIS_ING[(i * 3 + 1) % len(PRIS_ING)]}</p>')

    if nyckel == 'agare':
        e = EXTRA.get(mod['slug'], {})
        rub = AGARE_H2[(i * 3 + 1) % len(AGARE_H2)].replace('{b}', b)
        return f'<h2>{rub}</h2><p>{e.get("agare", "")}</p>'

    if nyckel == 'jamfor':
        e = EXTRA.get(mod['slug'], {})
        rub = JAMFOR_H2[(i * 5 + 2) % len(JAMFOR_H2)].replace('{b}', b)
        return f'<h2>{rub}</h2><p>{e.get("jamfor", "")}</p>'

    if nyckel == 'summa':
        rub = SUMMA_H2[(i * 7 + 1) % len(SUMMA_H2)].replace('{b}', b)
        e = EXTRA.get(mod['slug'], {})
        forsta = (e.get('jamfor', '').split('. ')[0] + '.') if e.get('jamfor') else ''
        return (f'<h2>{rub}</h2><p>{SUMMA_ING[(i * 5 + 7) % len(SUMMA_ING)]}</p>'
                f'<p><strong>Vad som styr premien.</strong> {mod["vinkel"]}</p>'
                f'<p><strong>Vilken nivå du bör välja.</strong> {mod["niva"]} '
                f'{mod["varde"]}</p>'
                f'<p><strong>Det som avgör vid en skada.</strong> '
                f'{(e.get("teknik", "").split(". ")[0] + ".") if e.get("teknik") else ""} '
                f'{mod["punkter"][0]} är den enskilda uppgift som oftast förklarar varför '
                f'två offerter på samma bil skiljer sig åt, och den står i villkoren — inte '
                f'i priset.</p>'
                f'<p><strong>Var du bör jämföra.</strong> {forsta} Hämta offert på '
                f'registreringsnumret hos minst tre bolag, på samma skyddsnivå och samma '
                f'självrisk — annars jämför du inte samma sak. Hur du gör det steg för steg '
                f'står under <a href="/jamfor-bilforsakring/">jämför bilförsäkring</a>, och '
                f'de generella prisfaktorerna finns på sidan om '
                f'<a href="/billigaste-bilforsakringen/">billigaste bilförsäkringen</a>.</p>')

    if nyckel == 'tillagg':
        rub = TILLAGG_H2[(i * 3 + 5) % len(TILLAGG_H2)].replace('{b}', b)
        el = 'el' in mod['drivlina'] or 'eldriven' in mod['typ']
        rader = [
            ['Hyrbil', 'Ofta ja' if el else 'Beror på om du har tillgång till en andra bil',
             'Väntetid på delar är den vanligaste orsaken till att bilen står stilla'],
            ['Allrisk eller drulle', 'Ja på nyare bilar',
             'Täcker feltankning, nyckelförlust och skador i kupén — inget av det ingår annars'],
            ['Lägre självrisk', 'Räkna på det',
             'Lönar sig bara om skillnaden i premie är mindre än sänkningen av självrisken'],
            ['Vägassistans', 'Kontrollera först',
             'Ingår ofta redan via nybilsgaranti eller medlemskap'],
            ['Självriskreducering vid djurkollision',
             'Ja om du kör på landsväg', 'Viltolyckor är den skada som oftast ger ett större '
             'belopp utanför tätort'],
        ]
        return (f'<h2>{rub}</h2><p>{TILLAGG_ING[(i * 7 + 6) % len(TILLAGG_ING)]} {mod["skada"]}</p>'
                + _tbl(f'Tillägg bedömda för {b}',
                       ['Tillägg', 'Värt pengarna?', 'Motivering'], rader, swipe=True)
                + f'<p>{mod["punkter"][2] if len(mod["punkter"]) > 2 else mod["punkter"][0]} '
                  f'{SLUT_TILLAGG[(i * 5 + 4) % len(SLUT_TILLAGG)]}</p>')

    if nyckel == 'begagnat':
        rub = BEGAGNAT_H2[(i * 5 + 3) % len(BEGAGNAT_H2)].replace('{b}', b)
        return (f'<h2>{rub}</h2><p>{BEGAGNAT_ING[(i * 3 + 7) % len(BEGAGNAT_ING)]}</p>'
                + _tbl(f'Ägarbyte steg för steg — {b}',
                       ['Steg', 'Vad du gör', 'Varför'],
                       [['1', 'Teckna försäkring med startdatum samma dag som ägarbytet',
                         'Försäkringsplikten börjar vid ägarbytet, inte vid hämtningen'],
                        ['2', 'Ange din egen körsträcka', 'Bilens historik är irrelevant för '
                         'din premie och kan göra den för dyr'],
                        ['3', 'Begär intyg på dina skadefria år',
                         'Bonusen följer dig men överförs inte automatiskt'],
                        ['4', 'Kontrollera utrustningsnivån i offerten',
                         'Utrustningen styr ersättningsvärdet och därmed premien'],
                        ['5', 'Välj skyddsnivå efter bilens värde i dag',
                         'Inte efter vad den kostade ny']], swipe=True)
                + f'<p>{mod["varde"]} {SLUT_BEGAGNAT[(i * 7 + 5) % len(SLUT_BEGAGNAT)]} '
                  f'Reglerna kring ägarbyte och byte av bolag står samlade under '
                  f'<a href="/byta-bilforsakring/">byta bilförsäkring</a>.</p>')

    if nyckel == 'checklista':
        rub = CHECK_H2[(i * 5 + 1) % len(CHECK_H2)].replace('{b}', b)
        e = EXTRA.get(mod['slug'], {})
        rader = [[p, 'Modellspecifikt'] for p in mod['punkter']]
        rader += [['Kontrollera hyrbilsdagar', 'Väntetid på delar drabbar dig direkt'],
                  ['Jämför glassjälvrisken vid byte, inte bara vid lagning',
                   'Skillnaden är större än de flesta tror'],
                  ['Ange din egen körsträcka, inte bilens historik',
                   'Felaktig uppgift kan sänka ersättningen']]
        return (f'<h2>{rub}</h2><p>{CHECK_ING[(i * 3 + 6) % len(CHECK_ING)]}</p>'
                + _tbl(f'Checklista före tecknandet — {b}',
                       ['Punkt', 'Varför'], rader)
                + f'<p>{mod["skada"]} {SLUT_CHECK[(i * 3 + 2) % len(SLUT_CHECK)]}</p>')

    if nyckel == 'rakna':
        rub = RAKNA_H2[(i * 7 + 2) % len(RAKNA_H2)].replace('{b}', b)
        return (f'<h2>{rub}</h2>'
                f'<p>{RAKNA_ING[(i * 5 + 6) % len(RAKNA_ING)]} {mod["varde"]}</p>'
                + _tbl(f'Vad vagnskadedelen kan betala ut på en {b}',
                       ['Marknadsvärde', 'Vid 4 000 kr självrisk', 'Vid 8 000 kr självrisk'],
                       [['50 000 kr', '46 000 kr', '42 000 kr'],
                        ['100 000 kr', '96 000 kr', '92 000 kr'],
                        ['200 000 kr', '196 000 kr', '192 000 kr'],
                        ['400 000 kr', '396 000 kr', '392 000 kr']])
                + f'<p>{mod["niva"]} {SLUT_RAKNA[(i * 7 + 1) % len(SLUT_RAKNA)]}</p>')

    if nyckel == 'teknik':
        e = EXTRA.get(mod['slug'], {})
        rub = TEKNIK_H2[(i * 7 + 3) % len(TEKNIK_H2)].replace('{b}', b)
        return f'<h2>{rub}</h2><p>{e.get("teknik", "")}</p>'

    if nyckel == 'kostnad':
        e = EXTRA.get(mod['slug'], {})
        rub = KOSTNAD_H2[(i * 3 + 4) % len(KOSTNAD_H2)].replace('{b}', b)
        return f'<h2>{rub}</h2><p>{e.get("kostnad", "")}</p>'

    if nyckel == 'styr':
        rader = [['Drivlina', mod['drivlina']],
                 ['Karosstyp', mod['typ'].capitalize()],
                 ['Årsmodeller', mod['ar']],
                 ['Reservdelsläge', 'Delas med övriga ' + m['namn'] + '-modeller'],
                 ['Ersättningsvärde', mod['varde']]]
        punkter = ''.join(f'<li>{x}</li>' for x in mod['punkter'])
        return (f'<h2>{h}</h2><p>{STYR_ING[(i * 5 + 2) % len(STYR_ING)]}</p>'
                + _tbl(f'{b} — modellens egna premiefaktorer', ['Faktor', 'Betydelse'], rader)
                + f'<ul>{punkter}</ul>'
                + f'<p>{PROFIL_ING[(i * 5 + 5) % len(PROFIL_ING)]} Läs mer under '
                  f'<a href="/bilforsakring-stockholm/">bilförsäkring i '
                  f'Stockholm</a>. Körsträckan anges i intervall, och ligger du strax över en '
                  f'gräns kan en ärlig justering nedåt ge en tydlig sänkning. Skadefria år är '
                  f'den faktor du bygger upp helt själv, och den enda som blir bättre av att '
                  f'ingenting händer — hur den fungerar står under '
                  f'<a href="/bonus-och-skadefria-ar/">bonus och skadefria år</a>. '
                  f'Tillsammans förklarar de tre faktorerna oftare skillnaden mellan två '
                  f'offerter än vilken bil det gäller.</p>')

    if nyckel == 'niva':
        rader = [['Under 3 år', 'Halvförsäkring räcker om vagnskadegarantin gäller',
                  'Garantin täcker vagnskadedelen'],
                 ['3–8 år', 'Helförsäkring', 'Marknadsvärdet motiverar vagnskadedelen'],
                 ['8–12 år', 'Räkna på det', 'Jämför premien mot bilens värde'],
                 ['Över 12 år', 'Ofta halvförsäkring', 'Vagnskadedelen betalar sällan ut '
                  'mer än den kostar']]
        return (f'<h2>{h}</h2><p>{NIVA_ING[(i * 7 + 3) % len(NIVA_ING)]} {mod["niva"]}</p>'
                + _tbl(f'Skyddsnivå för {b} efter ålder',
                       ['Bilens ålder', 'Rimlig nivå', 'Motivering'], rader, swipe=True)
                + f'<p>{GARANTI_ING[(i * 7 + 4) % len(GARANTI_ING)]} Garantin upphör på dagen, och '
                  f'det är värt en påminnelse i kalendern: därefter står bilen utan '
                  f'vagnskadeskydd om ingen gör något. Går bilen på leasing gäller i stället '
                  f'avtalets krav, som i praktiken alltid innebär helförsäkring under hela '
                  f'perioden — se <a href="/leasingbil-forsakring/">försäkring vid '
                  f'leasing</a>.</p>'
                + f'<p>Läs mer om skillnaden mellan '
                  f'<a href="/halvforsakring/">halvförsäkring</a> och '
                  f'<a href="/helforsakring/">helförsäkring</a>, eller om hur '
                  f'<a href="/sjalvrisk/">självrisken</a> påverkar vad som faktiskt '
                  f'betalas ut.</p>')

    if nyckel == 'skada':
        return (f'<h2>{h}</h2><p>{SKADA_ING[(i * 3 + 4) % len(SKADA_ING)]}</p>'
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
        return (f'<h2>{h}</h2><p>{VILLKOR_ING[(i * 5 + 1) % len(VILLKOR_ING)]}</p>'
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
        punkter = BYTA_PUNKTER[(i * 7 + 7) % len(BYTA_PUNKTER)]
        rader = [[t, b_] for t, b_ in punkter]
        return (f'<h2>{h}</h2><p>{BYTA_ING[(i * 7 + 2) % len(BYTA_ING)]}</p>'
                + _tbl('Åtgärder i prioritetsordning', ['Åtgärd', 'Varför'], rader)
                + f'<p>Hela regelverket för när du får byta står under '
                  f'<a href="/byta-bilforsakring/">byta bilförsäkring</a>.</p>')
    return ''


def _syskontabell(m, mod, syskon, i=0):
    rader = []
    for s in syskon:
        if s['slug'] == mod['slug']:
            continue
        k = upp.klass_for(s['slug'], s['namn'], m['grupp'])
        rader.append([f'<a href="/bilmarken/{m["slug"]}/{s["slug"]}/">'
                      f'{m["namn"]} {s["namn"]}</a>',
                      s['typ'].capitalize(), upp.spann(k, 'halv'), upp.spann(k, 'hel')])
    return (_tbl(f'Andra {m["namn"]}-modeller — uppskattat spann',
                 ['Modell', 'Typ', 'Halvförsäkring', 'Helförsäkring'], rader, swipe=True)
            + upp.metodruta(kort=True, i=i))


def sidor():
    ut = []
    # Varje märke får en egen förskjutning i variantpoolerna. Utan den
    # hämtar modell nummer fem hos Cupra samma formuleringar som modell
    # nummer fem hos Volvo, och sidorna börjar likna varandra på tvären.
    for marke_slug, lista in MODELLER.items():
        m = MARKE[marke_slug]
        for i, mod in enumerate(lista):
            b = f'{m["namn"]} {mod["namn"]}'
            mod_extra = EXTRA.get(mod['slug'], {})
            ordning = ORDNING[(i * 5 + 5) % len(ORDNING)]
            kroppar = ''.join(_sektion(k, m, mod, b, i, lista) for k in ordning)

            faq = [
                mod['fraga'],
                (f'Vad kostar bilförsäkring till {b}?', FAQ_PRIS[(i * 5 + 3) % len(FAQ_PRIS)]),
                (f'Behöver jag helförsäkring på min {b}?',
                 mod['niva'] + ' Räkna alltid på bilens marknadsvärde minus självrisken — '
                 'det är den summan vagnskadedelen kan betala ut.'),
                (f'Vilket bolag är billigast för {b}?',
                 'Det varierar med förarprofilen. Ett bolag som är billigast för en '
                 '25-åring i Malmö kan vara dyrast för en 60-åring i Umeå. Jämför alltid '
                 'på ditt eget registreringsnummer.'),
                (f'Vilka skador är vanligast på en {b}?', mod['skada']),
                (f'Vad påverkar premien mest på en {b}?',
                 f'Utöver din egen ålder, bonus och bostadsort är det tre saker: '
                 f'{mod["punkter"][0].lower()}, {mod["punkter"][1].lower()} och hur bilen '
                 f'värderas vid en totalskada. {mod["varde"]}'),
                (f'Hur står sig {b} mot liknande bilar?',
                 (mod_extra.get('jamfor', '').split('. ')[0] + '.') if mod_extra.get('jamfor')
                 else 'Premien styrs av ersättningsvärde, reparationskostnad och '
                      'verkstadsnät — jämför alltid på samma skyddsnivå.'),
                (f'Vad ingår i en helförsäkring till {b}?',
                 'Trafik, stöld, brand, glas, räddning, rättsskydd och maskinskada — plus '
                 'vagnskada, som är det enda momentet helförsäkringen lägger till utöver '
                 'halvförsäkringen. Vagnskadedelen täcker skador på din egen bil vid en '
                 'olycka du själv orsakat, vid skadegörelse och vid parkeringsskada utan '
                 'känd motpart.'),
            ]

            ut.append({
                'slug': f'bilmarken/{m["slug"]}/{mod["slug"]}',
                'key': True,
                'title': _titel(b, i, data.UPPDATERAD[:4]),
                # Metabeskrivning: kapas vid ordgräns så att den aldrig slutar
                # mitt i ett ord, och håller sig under 155 tecken.
                'desc': _desc(b, mod['slug'], mod['kort'], i),
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
                    + f'<h2>{SYSKON_H2[(i * 3 + 2) % len(SYSKON_H2)].replace("{m}", m["namn"])}</h2>'
                    + f'<p>{SYSKON_ING[(i * 3 + 5) % len(SYSKON_ING)]}</p>'
                    + _syskontabell(m, mod, lista, i)
                    + f'<h2>{mod_extra.get("lang", ("", ""))[0]}</h2>'
                    + f'<p class="direkt">{mod_extra.get("lang", ("", ""))[1]}</p>'
                    + (f'<h2>{mod_extra["lang2"][0]}</h2>'
                       f'<p class="direkt">{mod_extra["lang2"][1]}</p>'
                       if mod_extra.get('lang2') else '')
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
