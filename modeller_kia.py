# -*- coding: utf-8 -*-
"""Modelldata för Kia.

Tio modeller: de sju från brands.py som fortfarande säljs plus EV3,
XCeed och Stonic. Rio har utgått ur det svenska utbudet och ersätts av
modeller som faktiskt går att köpa ny.

SJUÅRSGARANTIN ÄR DEN RÖDA TRÅDEN
Kia lämnar sju års garanti som följer bilen vid ägarbyte. Det påverkar
försäkringen på två sätt som är värda att förstå: garantin täcker
fabrikationsfel som annars kunde bli en maskinskadefråga, och den
håller uppe andrahandsvärdet — vilket är exakt det belopp vagnskadedelen
utgår från vid en totalskada. Det är därför garantin nämns på flera av
modellsidorna, men med olika konsekvens beroende på bilens ålder.
"""

MODELLER_KIA = {
'kia': [
{
 'slug': 'sportage', 'namn': 'Sportage', 'typ': 'mellanstor SUV', 'ar': '2022–',
 'drivlina': 'bensin, mildhybrid, hybrid och laddhybrid',
 'kort': 'Kias mest sålda modell i Sverige och märkets viktigaste familjebil.',
 'vinkel': 'Sportage ligger mitt i volymklassen och prissätts därefter. Beståndet är stort '
           'nog för säker skadestatistik, delarna delas med Hyundai Tucson, och '
           'ägarprofilen är gynnsam. Laddhybriden är undantaget — den har både högre '
           'ersättningsvärde och en drivlina med fler dyra komponenter i samma bil.',
 'punkter': ['Delar plattform och delkatalog med Hyundai Tucson',
             'Laddhybriden har högre ersättningsvärde än mildhybriden',
             'Sjuårsgarantin följer bilen och håller uppe andrahandsvärdet'],
 'skada': 'Parkeringsskador och lättare kollisioner i tätort. Bilen är bred nog att bli '
          'trång i äldre parkeringshus.',
 'varde': 'Stabil värdeminskning med garantin som stöd de första sju åren, vilket gör '
          'begagnade exemplar attraktiva och håller uppe ersättningsvärdet.',
 'niva': 'Helförsäkring till omkring åtta år, därefter räkna på marknadsvärdet.',
 'fraga': ('Vad kostar det att försäkra en Kia Sportage?',
           'Volymklassens spann, alltså omkring 280–400 kr i månaden för halvförsäkring i '
           'uppskattning. Laddhybriden ligger högre eftersom ersättningsvärdet är större.'),
},
{
 'slug': 'niro', 'namn': 'Niro', 'typ': 'kompakt SUV', 'ar': '2022–',
 'drivlina': 'hybrid, laddhybrid och helt eldriven',
 'kort': 'Kias mest mångsidiga modell och den enda som finns med tre elektrifierade drivlinor.',
 'vinkel': 'Niro finns som hybrid, laddhybrid och ren elbil i samma kaross, och skillnaden '
           'mellan ytterligheterna är den största inom en och samma modell i Kias utbud. '
           'e-Niro har högre ersättningsvärde och kräver certifierad verkstad, medan '
           'hybridversionen prissätts som en vanlig bensinbil.',
 'punkter': ['Tre drivlinor i samma kaross ger tre olika premienivåer',
             'e-Niro prissätts som elbil, hybriden som bensinbil',
             'Populär som taxi och tjänstebil — kontrollera användningen i offerten'],
 'skada': 'Parkeringsskador dominerar. Niro används mest i tätort och pendling, med korta '
          'körsträckor och hemmaladdning på de laddbara versionerna.',
 'varde': 'Håller värdet väl tack vare garantin och stark efterfrågan på begagnade hybrider.',
 'niva': 'Helförsäkring till omkring sju år. Elversionen längre, eftersom värdet är högre.',
 'fraga': ('Hur mycket dyrare är e-Niro att försäkra än hybridversionen?',
           'Märkbart. Batteriet utgör en stor del av bilens värde och arbete på '
           'högvoltssystemet kräver certifierad verkstad. Skillnaden är större än mellan två '
           'olika bensinmotorer i samma bil.'),
},
{
 'slug': 'ev6', 'namn': 'EV6', 'typ': 'eldriven crossover', 'ar': '2021–',
 'drivlina': 'helt eldriven',
 'kort': 'Kias första elbil på E-GMP-plattformen och märkets genombrott i elbilsklassen.',
 'vinkel': 'EV6 använder 800-voltsteknik, vilket låter dyrt men i praktiken inte är det: '
           'plattformen E-GMP delas med Hyundai IONIQ 5 och Kia EV9, och den kombinerade '
           'volymen har gjort delarna standardiserade. Verkstadsnätet med rätt behörighet '
           'har vuxit snabbt, och premien har följt med nedåt.',
 'punkter': ['Delar E-GMP-plattform med Hyundai IONIQ 5',
             '800-voltsteknik kräver certifierad verkstad',
             'GT-versionen ligger i en betydligt högre effektklass'],
 'skada': 'Glasskador väger tungt. Den lutande vindrutan är stor och har kameror bakom sig, '
          'vilket innebär kalibrering efter varje byte.',
 'varde': 'Har hållit värdet bättre än de flesta elbilar i klassen, delvis tack vare '
          'garantin som följer bilen.',
 'niva': 'Helförsäkring så länge marknadsvärdet ligger över 150 000 kr.',
 'fraga': ('Är Kia EV6 dyr att försäkra?',
           'Nej, den ligger i mitten av elbilsspannet. Den delade E-GMP-plattformen med '
           'Hyundai ger både delstillgång och ett växande verkstadsnät, vilket håller premien '
           'nere.'),
},
{
 'slug': 'ev9', 'namn': 'EV9', 'typ': 'stor eldriven SUV med sju säten', 'ar': '2023–',
 'drivlina': 'helt eldriven',
 'kort': 'Kias största elbil och ett av få sjusitsiga eldrivna alternativ på marknaden.',
 'vinkel': 'EV9 är Kias dyraste bil att försäkra och den enda som regelbundet hamnar i '
           'premiumklassen. Sju säten, hög vikt och ett högt ersättningsvärde pekar åt samma '
           'håll. Fördelen är att bilen bygger på E-GMP, samma plattform som EV6 och IONIQ 5, '
           'vilket betyder att verkstäderna redan kan tekniken.',
 'punkter': ['Beprövad E-GMP-plattform trots att modellen är stor och ny',
             'Sju säten ger högre exponering för personskador',
             'Kan omfattas av krav på stöldskydd beroende på postnummer'],
 'skada': 'Backningsskador och skador vid trånga parkeringar. Bilen är över fem meter lång '
          'och bred i förhållande till svenska garage.',
 'varde': 'Stark efterfrågan på sjusitsiga elbilar håller uppe värdet, eftersom alternativen '
          'är få.',
 'niva': 'Helförsäkring under hela den period bilen har ett reellt andrahandsvärde.',
 'fraga': ('Vad kostar det att försäkra en Kia EV9?',
           'Den övre delen av elbilsspannet. Storlek, vikt och ersättningsvärde driver '
           'premien, men den beprövade plattformen gör att bolagen slipper lägga på ett '
           'osäkerhetspåslag för tekniken.'),
},
{
 'slug': 'ev3', 'namn': 'EV3', 'typ': 'kompakt eldriven SUV', 'ar': '2025–',
 'drivlina': 'helt eldriven',
 'kort': 'Kias minsta elbil och märkets försök att göra eldrift till volymprodukt.',
 'vinkel': 'EV3 är byggd för att vara billig, och det märks även i försäkringen. Lägre '
           'ersättningsvärde och lägre vikt än EV6 drar båda premien nedåt. Bilen använder '
           'dessutom 400-voltsteknik i stället för 800, vilket gör att fler verkstäder kan '
           'utföra arbete på högvoltssystemet.',
 'punkter': ['400-voltsteknik ger bredare verkstadsnät än 800-voltsmodellerna',
             'Lägst ersättningsvärde bland Kias elbilar',
             'Ny modell — jämför brett medan bolagen kalibrerar sina priser'],
 'skada': 'Parkeringsskador och skador mot kantsten, typiskt för en kompakt bil som mest '
          'används i tätort.',
 'varde': 'Ingen etablerad andrahandsmarknad ännu, men det låga nypriset begränsar nedsidan.',
 'niva': 'Halvförsäkring så länge vagnskadegarantin gäller, därefter en räknesak.',
 'fraga': ('Är Kia EV3 billigare att försäkra än EV6?',
           'Ja, tydligt. Lägre ersättningsvärde, lägre vikt och 400-voltsteknik som fler '
           'verkstäder kan hantera drar alla tre premien nedåt.'),
},
{
 'slug': 'ceed', 'namn': 'Ceed', 'typ': 'halvkombi och kombi', 'ar': '2018–',
 'drivlina': 'bensin, mildhybrid och laddhybrid',
 'kort': 'Kias kompaktbil och märkets svar på Golf och Octavia.',
 'vinkel': 'Ceed är den Kia där kombiversionen dominerar på svenska vägar, och det är '
           'gynnsamt: Sportswagon har lägre skadefrekvens än halvkombin och en äldre '
           'ägarprofil. Delarna är billiga och verkstadsnätet tätt, vilket gör en typisk '
           'reparation överkomlig.',
 'punkter': ['Sportswagon har lägre skadefrekvens än halvkombin',
             'Laddhybriden finns bara som kombi i Sverige',
             'GT-versionen hamnar i en högre effektklass'],
 'skada': 'Glasskador och parkeringsskador. Ceed används mycket i pendling, och '
          'motorvägsmilen avgör hur ofta rutan tar skada.',
 'varde': 'Måttlig värdeminskning med garantin som stöd, men lägre efterfrågan än Golf på '
          'begagnatmarknaden.',
 'niva': 'Helförsäkring till omkring sju år, därefter avgör marknadsvärdet.',
 'fraga': ('Är Kia Ceed billigare att försäkra än VW Golf?',
           'Ofta ja, framför allt för att ersättningsvärdet är lägre. Delstillgången är god '
           'och verkstadsnätet tätt, även om beståndet är mindre än Golfs.'),
},
{
 'slug': 'xceed', 'namn': 'XCeed', 'typ': 'crossover', 'ar': '2019–',
 'drivlina': 'bensin, mildhybrid och laddhybrid',
 'kort': 'Kias crossover mellan Ceed och Sportage, med högre markfrigång än halvkombin.',
 'vinkel': 'XCeed sitter i ett mellanformat som få konkurrenter har, och det gör att bolagen '
           'klassar bilen olika — vissa som halvkombi, andra som SUV. Skillnaden är några '
           'tior i månaden men den finns, och den gör att spridningen mellan offerter är '
           'större än på Ceed.',
 'punkter': ['Klassas olika av olika bolag — halvkombi eller SUV',
             'Delar teknik och delkatalog med Ceed',
             'Laddhybriden har högre ersättningsvärde'],
 'skada': 'Parkeringsskador och skador mot kantsten. Den högre markfrigången minskar risken '
          'för underredesskador jämfört med Ceed.',
 'varde': 'Starkare andrahandsvärde än Ceed, eftersom crossoverformatet efterfrågas mer.',
 'niva': 'Helförsäkring de första sex till sju åren.',
 'fraga': ('Hur klassar försäkringsbolagen Kia XCeed?',
           'Olika, och det är poängen. Formatet ligger mellan halvkombi och SUV, och bolagen '
           'placerar bilen olika. Begär offert hos flera — spridningen är större här än på '
           'Ceed.'),
},
{
 'slug': 'stonic', 'namn': 'Stonic', 'typ': 'liten SUV', 'ar': '2017–',
 'drivlina': 'bensin och mildhybrid',
 'kort': 'Kias minsta SUV och ett vanligt val som andrabil.',
 'vinkel': 'Stonic är en Rio på högre ben, och den delar allt av betydelse med Hyundai Bayon '
           'inom koncernen. Lågt ersättningsvärde och låg vikt gör den till en av de '
           'billigare bilarna att försäkra i Sverige. SUV-klassningen ger ett litet påslag '
           'jämfört med en halvkombi i samma storlek.',
 'punkter': ['Lågt ersättningsvärde gör vagnskadedelen billig',
             'Delar teknik med Hyundai Bayon inom koncernen',
             'Populär som andrabil, vilket ger låga körsträckor'],
 'skada': 'Parkeringsskador och skador mot trottoarkanter, typiskt för en liten bil som mest '
          'används i stad.',
 'varde': 'Låga men stabila värden, med sjuårsgarantin som stöd de första åren.',
 'niva': 'Halvförsäkring på exemplar över fem år. Helförsäkring på nyare bilar.',
 'fraga': ('Är Kia Stonic billig att försäkra?',
           'Ja, den ligger bland de billigare i Sverige. Låg vikt och lågt ersättningsvärde '
           'gör vagnskadedelen billig, och koncerndelarna finns hos många verkstäder.'),
},
{
 'slug': 'picanto', 'namn': 'Picanto', 'typ': 'minibil', 'ar': '2017–',
 'drivlina': 'bensin',
 'kort': 'Kias minsta bil och en av de sista kvarvarande minibilarna på svenska marknaden.',
 'vinkel': 'Picanto är sannolikt bland de billigaste bilarna att försäkra som säljs ny i '
           'Sverige. Lägst ersättningsvärde i Kias utbud, låg vikt och skador på motparten '
           'som begränsas av ren fysik. För en ung förare är det den kombination som betyder '
           'mest — mer än vilket märke det står på.',
 'punkter': ['Lägst ersättningsvärde av alla Kia-modeller',
             'Låg vikt begränsar skadan på både egen bil och motpart',
             'Segmentet krymper, vilket håller uppe andrahandsvärdet'],
 'skada': 'Parkeringsskador dominerar helt. Bilen används nästan uteslutande i tätort.',
 'varde': 'Håller värdet förvånansvärt väl eftersom utbudet av nya minibilar minskar.',
 'niva': 'Halvförsäkring på de flesta exemplar. Trafikförsäkring om bilen är värd mindre än '
         'självrisken plus några tusenlappar.',
 'fraga': ('Vilken Kia är billigast att försäkra?',
           'Picanto, med marginal. Lägst ersättningsvärde och lägst vikt i utbudet ger den '
           'lägsta premien, särskilt för unga förare där båda faktorerna väger tungt.'),
},
{
 'slug': 'sorento', 'namn': 'Sorento', 'typ': 'stor SUV med sju säten', 'ar': '2020–',
 'drivlina': 'diesel, hybrid och laddhybrid',
 'kort': 'Kias största SUV med förbränningsmotor och en klassisk dragbil för husvagn.',
 'vinkel': 'Sorento är den Kia som oftast används med släp, och det formar både skadebilden '
           'och vad du bör kontrollera. Bilens trafikförsäkring täcker skador släpet orsakar '
           'på annan egendom, men inte skador på själva släpet — det kräver egen försäkring. '
           'Sju säten ger dessutom högre exponering för personskador.',
 'punkter': ['Hög dragvikt gör den vanlig som husvagnsdragare',
             'Släpet behöver egen försäkring för att skador på det ska ersättas',
             'Laddhybriden har högst ersättningsvärde i utbudet'],
 'skada': 'Backningsskador och skador vid trånga parkeringar. Bilen är nära fem meter lång, '
          'och med släp blir manövreringen ytterligare en riskfaktor.',
 'varde': 'Stark efterfrågan på sjusitsiga dragbilar håller uppe andrahandsvärdet.',
 'niva': 'Helförsäkring så länge bilen är värd över 150 000 kr.',
 'fraga': ('Behöver släpet egen försäkring när jag drar med Sorento?',
           'Ja, om du vill ha skador på själva släpet ersatta. Bilens trafikförsäkring täcker '
           'bara skador släpet orsakar på annan egendom.'),
},
],
}
