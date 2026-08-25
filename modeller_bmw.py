# -*- coding: utf-8 -*-
"""Modelldata för BMW.

Tio modeller: de sju från brands.py som fortfarande säljs i volym plus
i5, iX och iX3. 1-serie har utgått ur listan till förmån för modeller
med större bestånd på svenska vägar — BMW säljer i dag betydligt fler
X1 och iX1 än 1-serie i Sverige.

EFFEKTKLASSEN ÄR DEN RÖDA TRÅDEN
BMW är märket där skillnaden mellan basversion och M-version slår
hårdast i premien. Samma kaross, samma verkstad, samma delkatalog — och
en premie som kan ligga i en helt annan klass. Det står utskrivet på
varje modellsida där det är relevant.
"""

MODELLER_BMW = {
'bmw': [
{
 'slug': '3-serie', 'namn': '3-serie', 'typ': 'sedan och kombi', 'ar': '2019–',
 'drivlina': 'bensin, diesel, mildhybrid och laddhybrid',
 'kort': 'BMW:s mest sålda modell genom tiderna och en klassisk svensk tjänstebil.',
 'vinkel': '3-serie är den BMW som bolagen har mest skadedata på, och det håller nere '
           'osäkerhetspåslaget. Det som drar upp premien är effektklassen: samma kaross '
           'säljs som 318i och som M340i, och skillnaden i premie mellan dem är större än '
           'skillnaden i pris. Touring-versionen har dessutom lägre skadefrekvens än sedanen.',
 'punkter': ['Störst skadeunderlag av alla BMW-modeller i Sverige',
             'M-versionerna hamnar i en betydligt högre effektklass',
             'Touring har lägre skadefrekvens än sedanen'],
 'skada': 'Glasskador dominerar. 3-serie har gått som tjänstebil i decennier, och '
          'motorvägsmilen avgör hur ofta rutan tar skada.',
 'varde': 'Brant värdeminskning de första fyra åren, sedan platå — typiskt för en '
          'tjänstebil i premiumsegmentet.',
 'niva': 'Helförsäkring på exemplar under sju år. På en tio år gammal 3-serie är '
         'halvförsäkring nästan alltid rätt.',
 'fraga': ('Är BMW 3-serie dyr att försäkra?',
           'Basversionerna ligger rimligt för premiumsegmentet tack vare det stora beståndet. '
           'M-versionerna är en annan sak — effektklassen gör att premien kan bli avsevärt '
           'högre för exakt samma kaross.'),
},
{
 'slug': '5-serie', 'namn': '5-serie', 'typ': 'stor sedan och kombi', 'ar': '2023–',
 'drivlina': 'bensin, diesel, mildhybrid och laddhybrid',
 'kort': 'BMW:s stora representationsbil och ett vanligt val som chefsbil i Sverige.',
 'vinkel': '5-serie har högt ersättningsvärde och en utrustningsnivå som varierar kraftigt '
           'mellan exemplaren. Två bilar med samma årsmodell kan skilja sexsiffrigt i värde '
           'beroende på om de har luftfjädring, Laserlight och förarstödspaket eller inte. '
           'Eftersom vagnskadedelen ersätter marknadsvärdet måste offerten utgå från '
           'registreringsnumret.',
 'punkter': ['Utrustningsnivån varierar kraftigt och styr ersättningsvärdet',
             'Luftfjädring på många exemplar — kontrollera maskinskademomentet',
             'Adaptiva strålkastare är dyra att ersätta vid frontskada'],
 'skada': 'Skador vid backning och i trånga parkeringar. Bilen är nära fem meter lång och '
          'bred nog att bli otymplig i äldre garage.',
 'varde': 'Kraftig värdeminskning de första åren, vilket gör begagnade exemplar prisvärda '
          'och flyttar gränsen för helförsäkring nedåt i ålder.',
 'niva': 'Helförsäkring på exemplar under sex år. Därefter avgör marknadsvärdet.',
 'fraga': ('Vad kostar det att försäkra en begagnad BMW 5-serie?',
           'Mindre än nypriset antyder, eftersom premien följer marknadsvärdet och 5-serie '
           'tappar snabbt i värde. Kontrollera att offerten utgår från rätt utrustningsnivå — '
           'den styr ersättningsvärdet.'),
},
{
 'slug': 'x1', 'namn': 'X1', 'typ': 'kompakt SUV', 'ar': '2022–',
 'drivlina': 'bensin, mildhybrid och laddhybrid',
 'kort': 'BMW:s minsta SUV och märkets mest sålda modell i Sverige de senaste åren.',
 'vinkel': 'X1 är den billigaste vägen in i BMW:s SUV-utbud och därmed den modell där '
           'ägarprofilen är yngst. Det påverkar premien mer än bilen gör. Tekniskt är X1 '
           'framhjulsdriven i grunden, till skillnad från märkets större modeller, vilket '
           'också gör en typisk reparation billigare.',
 'punkter': ['Framhjulsdriven grund, till skillnad från BMW:s större modeller',
             'Yngre ägarprofil än 3-serie och X3',
             'M Sport-paketets större fälgar är dyra att ersätta'],
 'skada': 'Parkeringsskador och fälgskador mot trottoarkanter. Bilen används mest i tätort.',
 'varde': 'Stark efterfrågan på kompakta premium-SUV:ar håller uppe andrahandsvärdet.',
 'niva': 'Helförsäkring till omkring åtta år så länge marknadsvärdet motiverar det.',
 'fraga': ('Är BMW X1 dyrare att försäkra än 3-serie?',
           'Ofta något, trots att X1 är den mindre bilen. Ägarprofilen är yngre, och '
           'SUV-formatet ger fler parkeringsskador i statistiken. Skillnaden är dock liten.'),
},
{
 'slug': 'x3', 'namn': 'X3', 'typ': 'mellanstor SUV', 'ar': '2024–',
 'drivlina': 'bensin, diesel, mildhybrid och laddhybrid',
 'kort': 'BMW:s mest sålda SUV globalt och en klassisk familjebil i premiumsegmentet.',
 'vinkel': 'X3 ligger i den storleksklass där både ersättningsvärde och skadefrekvens börjar '
           'bli kännbara. Bilen är tung, bred och nästan alltid utrustad med xDrive — '
           'fyrhjulsdrift som innehåller kardanaxel och bakaxeldifferential, komponenter som '
           'blir dyra vid en påkörning bakifrån.',
 'punkter': ['xDrive innehåller delar som blir dyra vid påkörning bakifrån',
             'Stort bestånd ger välunderbyggd skadestatistik',
             'M50-versionen hamnar i en betydligt högre effektklass'],
 'skada': 'Parkeringsskador och backningsskador. Bilen är bred, och de flesta ärenden gäller '
          'stötfångare och fälgar snarare än större kollisioner.',
 'varde': 'Håller värdet bättre än BMW:s sedanmodeller, eftersom efterfrågan på SUV:ar är '
          'stabilare.',
 'niva': 'Helförsäkring så länge bilen är värd över 150 000 kr, i praktiken upp till tio år.',
 'fraga': ('Är xDrive dyrare att försäkra?',
           'Något, ja. Fyrhjulsdriften innehåller komponenter som saknas på bakhjulsdrivna '
           'versioner och som blir kostsamma vid vissa skadetyper. Skillnaden vägs delvis upp '
           'av att xDrive håller värdet bättre i Sverige.'),
},
{
 'slug': 'x5', 'namn': 'X5', 'typ': 'stor SUV', 'ar': '2018–',
 'drivlina': 'bensin, diesel, mildhybrid och laddhybrid',
 'kort': 'BMW:s stora SUV och en av de mest stöldutsatta bilarna i svenska storstäder.',
 'vinkel': 'X5 är den BMW som oftast omfattas av särskilda stöldkrav. Stora premium-SUV:ar '
           'är eftertraktade, och flera bolag kräver godkänt stöldskydd eller spårsändare i '
           'vissa postnummerområden. Kravet står i villkoren och är en förutsättning för '
           'ersättning — inte ett råd. Kontrollera det innan du tecknar, inte efter.',
 'punkter': ['Kan omfattas av krav på spårsändare beroende på postnummer',
             'Luftfjädring är standard och dyr att ersätta',
             'M60i och M-versionerna ligger i en helt annan effektklass'],
 'skada': 'Stöldförsök och inbrott väger tyngre här än på BMW:s mindre modeller. Bilens '
          'värde och utrustningsnivå gör den intressant, särskilt i storstadsområdena.',
 'varde': 'Höga ersättningsvärden även på äldre exemplar, vilket håller vagnskadedelen '
          'motiverad länge.',
 'niva': 'Helförsäkring under hela den period bilen har ett reellt andrahandsvärde.',
 'fraga': ('Krävs spårsändare på BMW X5?',
           'Flera bolag ställer krav på godkänt stöldskydd för stora premium-SUV:ar, ofta '
           'kopplat till postnummer. Uppfylls kravet inte den natt bilen försvinner kan '
           'ersättningen sättas ned eller nekas helt.'),
},
{
 'slug': 'ix1', 'namn': 'iX1', 'typ': 'kompakt eldriven SUV', 'ar': '2023–',
 'drivlina': 'helt eldriven',
 'kort': 'Den eldrivna X1 och BMW:s mest sålda elbil i Sverige.',
 'vinkel': 'iX1 delar kaross och delkatalog med bensindrivna X1, vilket gör plåtskador lika '
           'billiga att laga. Skillnaden ligger i drivlinan: batteriet utgör en stor del av '
           'ersättningsvärdet och arbete på högvoltssystemet kräver certifierad verkstad. '
           'BMW:s verkstadsnät i Sverige är dock tätt, vilket gör skillnaden mindre än på '
           'nyetablerade elbilsmärken.',
 'punkter': ['Samma kaross och plåtdelar som bensindrivna X1',
             'BMW:s täta verkstadsnät begränsar elbilspåslaget',
             'Kontrollera att batteriet omfattas av vagnskadedelen'],
 'skada': 'Samma skadebild som X1, med den skillnaden att arbete nära högvoltssystemet '
          'kräver certifierad verkstad och därmed ibland längre transport.',
 'varde': 'Följer elbilsmarknaden men med stabilare golv än nyare märken, tack vare BMW:s '
          'varumärke och verkstadsnät.',
 'niva': 'Helförsäkring så länge marknadsvärdet ligger över 150 000 kr.',
 'fraga': ('Är iX1 dyrare att försäkra än X1?',
           'Ja, trots att karossen är densamma. Batteriets värde och kravet på certifierad '
           'verkstad förklarar hela skillnaden — plåtskadorna kostar detsamma på båda.'),
},
{
 'slug': 'i4', 'namn': 'i4', 'typ': 'eldriven fastback', 'ar': '2021–',
 'drivlina': 'helt eldriven',
 'kort': 'Den eldrivna 4-serie Gran Coupé och BMW:s svar på Tesla Model 3.',
 'vinkel': 'i4 bygger på samma grund som 3- och 4-serie, vilket betyder att en stor del av '
           'delkatalogen delas med BMW:s volymmodeller. Det är en tydlig fördel jämfört med '
           'elbilar på egna plattformar. M50-versionen är undantaget: den ligger i en '
           'effektklass där flera bolag kräver förhöjd självrisk.',
 'punkter': ['Delar grund och delkatalog med 3- och 4-serie',
             'M50 hamnar i en effektklass med krav på förhöjd självrisk',
             'Batteriet i golvet gör underredet utsatt vid farthinder'],
 'skada': 'Glasskador och sensorrelaterade ärenden. Den stora bakluckan i glas är en dyr '
          'komponent att ersätta.',
 'varde': 'Har fallit kraftigt på begagnatmarknaden i takt med att elbilsvärdena rört sig.',
 'niva': 'Helförsäkring så länge marknadsvärdet ligger över 150 000 kr.',
 'fraga': ('Är BMW i4 M50 mycket dyrare att försäkra?',
           'Ja, betydligt. Effektklassen är en av de tyngsta faktorerna i premieberäkningen, '
           'och flera bolag kräver dessutom förhöjd självrisk över ett visst effektuttag. '
           'Hämta offert på både M50 och eDrive40 innan du väljer version.'),
},
{
 'slug': 'i5', 'namn': 'i5', 'typ': 'stor eldriven sedan och kombi', 'ar': '2023–',
 'drivlina': 'helt eldriven',
 'kort': 'Den eldrivna 5-serie och BMW:s stora tjänstebil i eldrivet utförande.',
 'vinkel': 'i5 har tagit över 5-seriens roll som tjänstebil, och beståndet präglas av det: '
           'höga körsträckor de första åren och hög utrustningsnivå. Touring-versionen är '
           'populär i Sverige och har större glasytor än sedanen, vilket gör glasmomentet '
           'tyngre. Köper du begagnat: ange din egen körsträcka, inte bilens historik.',
 'punkter': ['Delar kaross och delkatalog med bensindrivna 5-serie',
             'Touring har större glasytor och tyngre glasmoment',
             'Stor andel tjänstebilar med höga körsträckor'],
 'skada': 'Glas- och sensorrelaterade ärenden dominerar. Assistanspaketet är omfattande och '
          'kräver kalibrering efter även måttliga frontskador.',
 'varde': 'Snabb värdeminskning de första åren, som på alla stora tjänstebilar.',
 'niva': 'Helförsäkring under hela den period bilen har ett reellt andrahandsvärde.',
 'fraga': ('Vad kostar det att försäkra en BMW i5?',
           'Den övre delen av elbilsspannet. Högt ersättningsvärde och stor kaross driver '
           'premien, medan den delade delkatalogen med 5-serie håller nere '
           'reparationskostnaden.'),
},
{
 'slug': 'ix', 'namn': 'iX', 'typ': 'stor eldriven SUV', 'ar': '2021–',
 'drivlina': 'helt eldriven',
 'kort': 'BMW:s eldrivna flaggskepp och märkets mest teknikintensiva modell.',
 'vinkel': 'iX är byggd med kolfiberförstärkt kaross i delar av strukturen, vilket är '
           'ovanligt och får konsekvenser vid en skada: reparationer kräver särskild '
           'kompetens och antalet verkstäder som får utföra dem är begränsat även inom BMW:s '
           'nät. Lägg till högt ersättningsvärde och stöldbegärlighet, så förklarar det '
           'premieläget.',
 'punkter': ['Kolfiberförstärkt kaross kräver särskild reparationskompetens',
             'Kan omfattas av krav på spårsändare beroende på postnummer',
             'Luftfjädring är standard och dyr att ersätta'],
 'skada': 'Karosskador blir oproportionerligt dyra på grund av materialvalet. Stöldförsök '
          'väger dessutom tungt i storstadsområdena.',
 'varde': 'Har fallit kraftigt från en mycket hög startpunkt, men behåller ett högt '
          'absolutvärde.',
 'niva': 'Helförsäkring. Bilens värde och reparationskostnad gör allt annat orimligt.',
 'fraga': ('Varför är BMW iX dyr att försäkra?',
           'Tre saker samtidigt: högt ersättningsvärde, en kolfiberförstärkt kaross som kräver '
           'särskild reparationskompetens, och stöldbegärlighet i storstadsområdena. Flera '
           'bolag ställer dessutom krav på stöldskydd.'),
},
{
 'slug': 'ix3', 'namn': 'iX3', 'typ': 'mellanstor eldriven SUV', 'ar': '2026–',
 'drivlina': 'helt eldriven',
 'kort': 'BMW:s första modell på Neue Klasse-plattformen med 800-voltsteknik.',
 'vinkel': 'iX3 är den första BMW på Neue Klasse-plattformen, vilket betyder helt ny teknik '
           'med 800-voltssystem och en ny generation batterier. Ny teknik betyder färre '
           'verkstäder med rätt behörighet i början, och det är den skillnaden du betalar '
           'för snarare än bilens storlek. Jämför brett medan bolagen kalibrerar sina priser.',
 'punkter': ['Första modellen på Neue Klasse-plattformen',
             '800-voltsteknik kräver verkstad med särskild behörighet',
             'Ny modell — spridningen mellan bolagens offerter är stor'],
 'skada': 'För ny för egen skadestatistik. Sensorpaketet är omfattande, vilket gör även '
          'måttliga frontskador dyra på grund av kalibreringen.',
 'varde': 'Ingen etablerad andrahandsmarknad ännu.',
 'niva': 'Helförsäkring. Vagnskadegarantin täcker de första åren.',
 'fraga': ('Är nya iX3 dyr att försäkra?',
           'Den ligger i elbilsklassen men med större spridning mellan bolagen än etablerade '
           'modeller, eftersom Neue Klasse-plattformen är ny och skadeunderlaget saknas. '
           'Begär offert hos fler bolag än du annars skulle.'),
},
],
}
