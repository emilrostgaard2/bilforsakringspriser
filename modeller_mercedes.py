# -*- coding: utf-8 -*-
"""Modelldata för Mercedes-Benz.

Tio modeller: sex från brands.py plus CLA, GLB, GLE och V-Klass. EQC
har utgått ur produktionen och B-Klass säljs inte längre i Sverige, så
båda har ersatts av modeller som faktiskt går att köpa.

STÖLDRISKEN ÄR DEN RÖDA TRÅDEN
Mercedes är det märke som oftast omfattas av särskilda stöldkrav i
svenska försäkringsvillkor, och kraven är kopplade till postnummer.
Det står utskrivet på de modeller där det är relevant — och det är
värt att läsa innan man tecknar, inte efter en stöld.
"""

MODELLER_MERCEDES = {
'mercedes': [
{
 'slug': 'c-klass', 'namn': 'C-Klass', 'typ': 'sedan och kombi', 'ar': '2021–',
 'drivlina': 'bensin, diesel, mildhybrid och laddhybrid',
 'kort': 'Mercedes mest sålda modell i Sverige och en klassisk tjänstebil.',
 'vinkel': 'C-Klass är den Mercedes bolagen har mest skadedata på, vilket håller nere '
           'osäkerhetspåslaget. Det som drar upp premien är ersättningsvärdet och '
           'utrustningsvariationen: två C-Klass med samma årsmodell kan skilja sexsiffrigt i '
           'värde beroende på utrustning. Offerten måste utgå från registreringsnumret.',
 'punkter': ['Störst skadeunderlag av Mercedes modeller i Sverige',
             'Utrustningsnivån varierar kraftigt och styr ersättningsvärdet',
             'AMG-versionerna hamnar i en betydligt högre effektklass'],
 'skada': 'Glasskador dominerar. C-Klass har gått som tjänstebil i decennier, och '
          'motorvägsmilen avgör hur ofta rutan tar skada.',
 'varde': 'Brant värdeminskning de första fyra åren och sedan platå, typiskt för en '
          'tjänstebil i premiumsegmentet.',
 'niva': 'Helförsäkring på exemplar under sju år. På en tio år gammal C-Klass är '
         'halvförsäkring nästan alltid rätt.',
 'fraga': ('Är Mercedes C-Klass dyr att försäkra?',
           'Basversionerna ligger rimligt för premiumsegmentet tack vare det stora beståndet. '
           'AMG-versionerna är en annan sak — effektklassen gör att premien kan bli avsevärt '
           'högre för exakt samma kaross.'),
},
{
 'slug': 'e-klass', 'namn': 'E-Klass', 'typ': 'stor sedan och kombi', 'ar': '2023–',
 'drivlina': 'bensin, diesel, mildhybrid och laddhybrid',
 'kort': 'Mercedes stora representationsbil och en av Sveriges vanligaste taxibilar.',
 'vinkel': 'E-Klass har två helt olika liv: som chefsbil i företagsflottor och som taxi. De '
           'två användningarna har olika riskprofil och olika villkor, och det är den '
           'viktigaste uppgiften att få rätt i offerten. Yrkesmässig persontransport på en '
           'privatförsäkring kan ge nedsatt ersättning.',
 'punkter': ['Vanlig som taxi — yrkestrafik kräver annan försäkring',
             'Luftfjädring på många exemplar, kontrollera maskinskademomentet',
             'Kan omfattas av krav på stöldskydd beroende på postnummer'],
 'skada': 'Skador vid backning och i trånga parkeringar. Bilen är nära fem meter lång och '
          'bred nog att bli otymplig i äldre garage.',
 'varde': 'Kraftig värdeminskning de första åren, vilket gör begagnade exemplar prisvärda '
          'och flyttar gränsen för helförsäkring nedåt i ålder.',
 'niva': 'Helförsäkring på exemplar under sex år. Därefter avgör marknadsvärdet.',
 'fraga': ('Kan jag köra taxi med E-Klass på privatförsäkring?',
           'Nej. Yrkesmässig persontransport är en annan riskklass med egna villkor, och '
           'ersättningen kan sättas ned helt om användningen inte angetts. Ange den korrekta '
           'användningen redan när du tecknar.'),
},
{
 'slug': 'a-klass', 'namn': 'A-Klass', 'typ': 'halvkombi och sedan', 'ar': '2018–',
 'drivlina': 'bensin, diesel och laddhybrid',
 'kort': 'Mercedes instegsmodell och märkets vanligaste val bland yngre köpare.',
 'vinkel': 'A-Klass är den Mercedes där ägarprofilen påverkar premien mest. Modellen är för '
           'många den första premiumbilen, ofta köpt begagnad i tjugofemårsåldern, och '
           'medelåldern i beståndet är den lägsta i märkets utbud. Det väger tyngre än att '
           'bilen är den minsta och billigaste.',
 'punkter': ['Yngst ägarprofil i Mercedes utbud',
             'Framhjulsdriven grund till skillnad från märkets större modeller',
             'AMG A 35 och A 45 ligger i en helt annan effektklass'],
 'skada': 'Parkeringsskador och lättare kollisioner i tätort. Bilen används mest i stad och '
          'pendling.',
 'varde': 'Håller värdet väl tack vare varumärket, men sämre än C-Klass i absoluta tal.',
 'niva': 'Helförsäkring till omkring sju år, därefter räkna på marknadsvärdet.',
 'fraga': ('Är A-Klass billigare att försäkra än C-Klass?',
           'Inte alltid. A-Klass har lägre ersättningsvärde men betydligt yngre ägarprofil, '
           'och förarens ålder väger tungt. För en förare över fyrtio är A-Klass billigare, '
           'för en under trettio är skillnaden ofta liten.'),
},
{
 'slug': 'cla', 'namn': 'CLA', 'typ': 'coupéformad sedan och kombi', 'ar': '2025–',
 'drivlina': 'helt eldriven och mildhybrid',
 'kort': 'Mercedes nya CLA, byggd på märkets första dedikerade elbilsplattform för kompaktbilar.',
 'vinkel': 'Nya CLA bygger på MMA-plattformen med 800-voltsteknik, vilket är ny teknik även '
           'inom Mercedes. Ny plattform betyder färre verkstäder med rätt behörighet i '
           'början, och det är den skillnaden du betalar för snarare än bilens storlek. '
           'Jämför brett medan bolagen kalibrerar sina priser.',
 'punkter': ['MMA-plattform med 800-voltsteknik — ny även inom Mercedes',
             'Den sluttande taklinjen ger en stor bakruta',
             'Ny modell, så spridningen mellan bolagens offerter är stor'],
 'skada': 'För ny för egen skadestatistik. Sensorpaketet är omfattande, vilket gör även '
          'måttliga frontskador dyra på grund av kalibreringen.',
 'varde': 'Ingen etablerad andrahandsmarknad ännu.',
 'niva': 'Helförsäkring. Vagnskadegarantin täcker de första åren.',
 'fraga': ('Är nya Mercedes CLA dyr att försäkra?',
           'Den ligger i elbilsklassen men med större spridning mellan bolagen än etablerade '
           'modeller, eftersom MMA-plattformen är ny och skadeunderlaget saknas. Begär offert '
           'hos fler bolag än du annars skulle.'),
},
{
 'slug': 'gla', 'namn': 'GLA', 'typ': 'kompakt SUV', 'ar': '2020–',
 'drivlina': 'bensin, diesel och laddhybrid',
 'kort': 'Mercedes minsta SUV och märkets vanligaste val som första premium-SUV.',
 'vinkel': 'GLA är A-Klass på högre ben och delar allt av betydelse med den. Det gör en '
           'typisk reparation billigare än på en bakhjulsdriven Mercedes, eftersom drivlinan '
           'är enklare. Det som drar upp premien är ägarprofilen, som är yngre än för GLC och '
           'GLE.',
 'punkter': ['Delar plattform och delkatalog med A-Klass',
             'Framhjulsdriven grund gör reparationen enklare',
             'AMG Line-paketets större fälgar är dyra att ersätta'],
 'skada': 'Parkeringsskador och fälgskador mot trottoarkanter. Bilen används mest i tätort.',
 'varde': 'Stark efterfrågan på kompakta premium-SUV:ar håller uppe andrahandsvärdet.',
 'niva': 'Helförsäkring till omkring åtta år så länge marknadsvärdet motiverar det.',
 'fraga': ('Är Mercedes GLA dyrare att försäkra än A-Klass?',
           'Något, ja. Bilarna delar teknik men GLA är tyngre och har högre ersättningsvärde. '
           'SUV-formatet ger dessutom fler parkeringsskador i statistiken.'),
},
{
 'slug': 'glb', 'namn': 'GLB', 'typ': 'kompakt SUV med sju säten', 'ar': '2019–',
 'drivlina': 'bensin, diesel och helt eldriven',
 'kort': 'Mercedes kompakta sjusitsiga SUV och ett ovanligt format i premiumsegmentet.',
 'vinkel': 'GLB är den minsta bilen på svenska marknaden som erbjuder sju säten i '
           'premiumsegmentet, och det gör den svår att jämföra rakt av. Sju sittplatser ger '
           'högre exponering för personskador än formatet antyder, medan ersättningsvärdet '
           'ligger i kompaktklassen. Nettoeffekten är en premie som ofta överraskar positivt.',
 'punkter': ['Sju säten i ett kompakt format — ovanlig kombination',
             'Delar plattform med GLA och A-Klass',
             'EQB är den eldrivna versionen med annan premiebild'],
 'skada': 'Backningsskador och parkeringsskador. Den kantiga karossen ger god sikt men bilen '
          'är längre än GLA.',
 'varde': 'Håller värdet väl eftersom sjusitsiga kompaktbilar är få.',
 'niva': 'Helförsäkring till omkring åtta år.',
 'fraga': ('Är GLB dyr att försäkra för att vara sjusitsig?',
           'Nej, tvärtom. Ersättningsvärdet ligger i kompaktklassen medan utrymmet motsvarar '
           'betydligt större bilar. Sju sittplatser höjer exponeringen något, men effekten är '
           'mindre än storleksskillnaden mot en GLE.'),
},
{
 'slug': 'glc', 'namn': 'GLC', 'typ': 'mellanstor SUV', 'ar': '2022–',
 'drivlina': 'bensin, diesel, mildhybrid och laddhybrid',
 'kort': 'Mercedes mest sålda SUV och en klassisk familjebil i premiumsegmentet.',
 'vinkel': 'GLC ligger i den storleksklass där både ersättningsvärde och stöldrisk börjar bli '
           'kännbara. Bilen är tung, bred och nästan alltid utrustad med 4Matic. '
           'Laddhybriden har dessutom ett stort batteri och det högsta ersättningsvärdet i '
           'modellfamiljen.',
 'punkter': ['4Matic innehåller delar som blir dyra vid påkörning bakifrån',
             'Laddhybriden har högst ersättningsvärde i modellfamiljen',
             'Kan omfattas av krav på stöldskydd beroende på postnummer'],
 'skada': 'Parkeringsskador och backningsskador. Bilen är bred, och de flesta ärenden gäller '
          'stötfångare och fälgar snarare än större kollisioner.',
 'varde': 'Håller värdet bättre än Mercedes sedanmodeller, eftersom efterfrågan på SUV:ar är '
          'stabilare.',
 'niva': 'Helförsäkring så länge bilen är värd över 150 000 kr, i praktiken upp till tio år.',
 'fraga': ('Vad kostar det att försäkra en Mercedes GLC?',
           'Premiumklassen, alltså över volymbilarna men under de största SUV:arna. '
           'Laddhybriden ligger högst, och krav på stöldskydd kan tillkomma beroende på var '
           'du bor.'),
},
{
 'slug': 'gle', 'namn': 'GLE', 'typ': 'stor SUV', 'ar': '2019–',
 'drivlina': 'bensin, diesel, mildhybrid och laddhybrid',
 'kort': 'Mercedes stora SUV och en av de mest stöldutsatta bilarna i svenska storstäder.',
 'vinkel': 'GLE är den Mercedes som oftast omfattas av särskilda stöldkrav. Stora '
           'premium-SUV:ar är eftertraktade, och flera bolag kräver godkänt stöldskydd eller '
           'spårsändare i vissa postnummerområden. Kravet står i villkoren och är en '
           'förutsättning för ersättning — inte ett råd.',
 'punkter': ['Kan omfattas av krav på spårsändare beroende på postnummer',
             'Luftfjädring är standard och dyr att ersätta',
             'AMG-versionerna ligger i en helt annan effektklass'],
 'skada': 'Stöldförsök och inbrott väger tyngre här än på Mercedes mindre modeller. Bilens '
          'värde och utrustningsnivå gör den intressant, särskilt i storstadsområdena.',
 'varde': 'Höga ersättningsvärden även på äldre exemplar, vilket håller vagnskadedelen '
          'motiverad länge.',
 'niva': 'Helförsäkring under hela den period bilen har ett reellt andrahandsvärde.',
 'fraga': ('Krävs spårsändare på Mercedes GLE?',
           'Flera bolag ställer krav på godkänt stöldskydd för stora premium-SUV:ar, ofta '
           'kopplat till postnummer. Uppfylls kravet inte den natt bilen försvinner kan '
           'ersättningen sättas ned eller nekas helt.'),
},
{
 'slug': 'eqa', 'namn': 'EQA', 'typ': 'kompakt eldriven SUV', 'ar': '2021–',
 'drivlina': 'helt eldriven',
 'kort': 'Den eldrivna GLA och Mercedes mest sålda elbil i Sverige.',
 'vinkel': 'EQA delar kaross och delkatalog med GLA, vilket gör plåtskador lika billiga att '
           'laga. Skillnaden ligger i drivlinan: batteriet utgör en stor del av '
           'ersättningsvärdet och arbete på högvoltssystemet kräver certifierad verkstad. '
           'Mercedes verkstadsnät i Sverige är dock tätt, vilket begränsar påslaget.',
 'punkter': ['Samma kaross och plåtdelar som GLA',
             'Mercedes täta verkstadsnät begränsar elbilspåslaget',
             'Kontrollera att batteriet omfattas av vagnskadedelen'],
 'skada': 'Samma skadebild som GLA, med den skillnaden att arbete nära högvoltssystemet '
          'kräver certifierad verkstad och därmed ibland längre transport.',
 'varde': 'Har fallit kraftigt på begagnatmarknaden i takt med att elbilsvärdena rört sig.',
 'niva': 'Helförsäkring så länge marknadsvärdet ligger över 150 000 kr.',
 'fraga': ('Är EQA dyrare att försäkra än GLA?',
           'Ja, trots att karossen är densamma. Batteriets värde och kravet på certifierad '
           'verkstad förklarar hela skillnaden — plåtskadorna kostar detsamma på båda.'),
},
{
 'slug': 'v-klass', 'namn': 'V-Klass', 'typ': 'stor personbilsregistrerad buss', 'ar': '2014–',
 'drivlina': 'diesel och helt eldriven',
 'kort': 'Mercedes största personbil, vanlig i taxitrafik och hos stora familjer.',
 'vinkel': 'V-Klass används i hög grad yrkesmässigt, och det är den viktigaste frågan att '
           'reda ut innan du tecknar. Åtta sittplatser ger hög exponering för personskador, '
           'och yrkesmässig persontransport kräver annan försäkring än privat bruk. Ange '
           'användningen korrekt från början.',
 'punkter': ['Upp till åtta sittplatser ger hög exponering för personskador',
             'Yrkesmässig persontransport kräver annan försäkring',
             'De elektriska skjutdörrarna är en egen reparationspost'],
 'skada': 'Skjutdörrar, tak och bakre stötfångare. Bilens storlek gör den utsatt i trånga '
          'stadsmiljöer och i parkeringsgarage med låg takhöjd.',
 'varde': 'Stabil efterfrågan från taxi och stora familjer håller uppe värdet.',
 'niva': 'Helförsäkring så länge värdet motiverar det, med kontroll av att användningen är '
         'korrekt angiven.',
 'fraga': ('Kan jag använda V-Klass i taxiverksamhet på privatförsäkring?',
           'Nej. Yrkesmässig persontransport är en annan riskklass med egna villkor, och '
           'ersättningen kan sättas ned helt om användningen inte angetts. Ange den korrekta '
           'användningen redan när du tecknar.'),
},
],
}
