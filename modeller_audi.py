# -*- coding: utf-8 -*-
"""Modelldata för Audi.

Tio modeller: de sex från brands.py som fortfarande är relevanta plus
Q6 e-tron, A6 e-tron, e-tron GT och Q7. A1 utgick ur det svenska
utbudet och ersätts här av modeller som faktiskt säljs — en sida på en
modell ingen köper ger varken trafik eller nytta.

NAMNBYTET 2025
Audi lade om sin modellbenämning så att jämna siffror används på
eldrivna modeller och udda på förbränningsmotorer. A4 blev därmed A5 i
nyproduktionen. Vi behåller A4 som egen sida eftersom beståndet är
enormt och söktrycket ligger där — och förklarar bytet på sidan.
"""

MODELLER_AUDI = {
'audi': [
{
 'slug': 'a4', 'namn': 'A4', 'typ': 'sedan och kombi', 'ar': '2015–2024',
 'drivlina': 'bensin, diesel, mildhybrid och laddhybrid',
 'kort': 'Audis mest sålda modell genom tiderna och en av Sveriges vanligaste tjänstebilar.',
 'vinkel': 'A4 är den Audi som är billigast att försäkra i förhållande till märkets '
           'prestige. Beståndet är stort, delarna delas med VW Passat och Skoda Superb, och '
           'skadestatistiken är väldokumenterad. Det som drar upp premien är '
           'ersättningsvärdet — en Audi kostar mer att ersätta än en Passat med samma motor '
           'och årsmodell.',
 'punkter': ['Delar plattform och delkatalog med VW Passat',
             'Avant-versionen har lägre skadefrekvens än sedanen',
             'S4 och RS4 hamnar i en helt annan effektklass'],
 'skada': 'Glasskador dominerar. A4 har gått som tjänstebil i decennier, och '
          'motorvägsmilen är det som avgör hur ofta rutan tar skada.',
 'varde': 'Brant värdeminskning de första fyra åren och sedan platå, typiskt för en '
          'tjänstebil i premiumsegmentet.',
 'niva': 'Helförsäkring på exemplar under sju år. På en tio år gammal A4 är '
         'halvförsäkring nästan alltid rätt.',
 'fraga': ('Heter Audi A4 fortfarande A4?',
           'I nyproduktionen ersattes A4 av A5 under 2025, när Audi lade om sin '
           'modellbenämning så att udda siffror används på förbränningsmotorer. Begagnade '
           'exemplar heter fortfarande A4, och det är dem beståndet består av.'),
},
{
 'slug': 'a6', 'namn': 'A6', 'typ': 'stor sedan och kombi', 'ar': '2018–',
 'drivlina': 'bensin, diesel, mildhybrid och laddhybrid',
 'kort': 'Audis stora representationsbil och ett vanligt val som chefsbil i Sverige.',
 'vinkel': 'A6 har det högsta ersättningsvärdet av Audis förbränningsmodeller under Q7, och '
           'utrustningsnivån varierar mer här än på någon annan modell i utbudet. Skillnaden '
           'mellan en enkelt utrustad A6 och en fullt utrustad kan vara sexsiffrig i värde, '
           'vilket gör att offerten måste utgå från registreringsnumret snarare än från en '
           'rullista.',
 'punkter': ['Utrustningsnivån varierar kraftigt och styr ersättningsvärdet',
             'Luftfjädring på många exemplar — kontrollera maskinskademomentet',
             'Avant efterfrågas mer än sedanen på den svenska begagnatmarknaden'],
 'skada': 'Skador vid backning och i trånga parkeringar. A6 Avant är nära fem meter lång och '
          'bred nog att bli otymplig i äldre garage.',
 'varde': 'Kraftig värdeminskning de första åren, vilket gör begagnade exemplar prisvärda '
          'och flyttar gränsen för helförsäkring nedåt i ålder.',
 'niva': 'Helförsäkring på exemplar under sex år. Därefter avgör marknadsvärdet.',
 'fraga': ('Är Audi A6 dyr att försäkra?',
           'Dyrare än A4 men mindre än nypriset antyder, eftersom premien följer '
           'marknadsvärdet och A6 tappar snabbt i värde. En sex år gammal A6 kan kosta mindre '
           'att försäkra än en ny bil i en mindre klass.'),
},
{
 'slug': 'a3', 'namn': 'A3', 'typ': 'halvkombi och sedan', 'ar': '2020–',
 'drivlina': 'bensin, mildhybrid och laddhybrid',
 'kort': 'Audis instegsmodell och märkets vanligaste val bland yngre köpare.',
 'vinkel': 'A3 är en Golf i annan kostym — samma MQB-plattform, samma motorer, samma '
           'delkatalog. Det gör den billig att laga för att vara en premiumbil. Det som '
           'drar upp premien är ägarprofilen: A3 har den yngsta köpargruppen i Audis utbud, '
           'och förarens ålder väger tyngre än bilens teknik.',
 'punkter': ['Delar plattform och delkatalog med VW Golf',
             'Yngst ägarprofil i Audis utbud',
             'S3 och RS3 hamnar i en betydligt högre effektklass'],
 'skada': 'Parkeringsskador och lättare kollisioner i tätort. Bilen används mest i stad och '
          'pendling.',
 'varde': 'Håller värdet väl tack vare stark efterfrågan på begagnatmarknaden och Audis '
          'varumärke.',
 'niva': 'Helförsäkring till omkring sju år, därefter räkna på marknadsvärdet.',
 'fraga': ('Är Audi A3 dyrare att försäkra än VW Golf?',
           'Ja, något. Bilarna delar teknik och delar, men A3 har högre nypris och därmed '
           'högre ersättningsvärde. Ägarprofilen är dessutom yngre, vilket väger tungt.'),
},
{
 'slug': 'q3', 'namn': 'Q3', 'typ': 'kompakt SUV', 'ar': '2019–',
 'drivlina': 'bensin, mildhybrid och laddhybrid',
 'kort': 'Audis minsta SUV och märkets mest sålda modell i Sverige de senaste åren.',
 'vinkel': 'Q3 är SUV-versionen av A3 och delar allt av betydelse med VW Tiguan och Skoda '
           'Karoq. Det gör reparationerna överkomliga. Det som skiljer är fälgarna och '
           'utrustningsnivån — S line-paketet ger större fälgar som är dyrare att ersätta och '
           'som oftare tar skada mot trottoarkanter.',
 'punkter': ['Delar MQB-plattform med VW Tiguan och Skoda Karoq',
             'S line-paketets större fälgar är dyra att ersätta',
             'Sportback-versionen har lägre taklinje och större bakruta'],
 'skada': 'Fälg- och parkeringsskador dominerar. Bilen används mest i tätort och är bred '
          'nog att bli trång i äldre parkeringshus.',
 'varde': 'Stark efterfrågan på kompakta premium-SUV:ar håller uppe andrahandsvärdet.',
 'niva': 'Helförsäkring till omkring åtta år så länge marknadsvärdet motiverar det.',
 'fraga': ('Vad kostar det att försäkra en Audi Q3?',
           'Premiumklassens nedre del. Den delade tekniken med VW och Skoda håller nere '
           'reparationskostnaden, medan Audis högre nypris drar premien uppåt.'),
},
{
 'slug': 'q5', 'namn': 'Q5', 'typ': 'mellanstor SUV', 'ar': '2017–',
 'drivlina': 'bensin, diesel, mildhybrid och laddhybrid',
 'kort': 'Audis mest sålda SUV globalt och en klassisk familjebil i premiumsegmentet.',
 'vinkel': 'Q5 ligger i den storleksklass där både ersättningsvärde och skadefrekvens börjar '
           'bli kännbara. Bilen är tung, bred och ofta utrustad med luftfjädring och '
           'quattro — komponenter som var för sig driver reparationskostnad. Samtidigt är '
           'beståndet stort nog för säker skadestatistik, vilket håller osäkerhetspåslaget '
           'nere.',
 'punkter': ['Quattro innehåller delar som blir dyra vid påkörning bakifrån',
             'Luftfjädring på många exemplar — kontrollera maskinskademomentet',
             'Laddhybriden TFSI e har högst ersättningsvärde i utbudet'],
 'skada': 'Parkeringsskador och backningsskador. Q5 är bred, och de flesta ärenden gäller '
          'stötfångare och fälgar snarare än större kollisioner.',
 'varde': 'Håller värdet bättre än A6 och andra sedanmodeller, eftersom efterfrågan på '
          'SUV:ar är stabilare.',
 'niva': 'Helförsäkring så länge bilen är värd över 150 000 kr, i praktiken upp till tio år.',
 'fraga': ('Är Audi Q5 dyr att försäkra?',
           'Den ligger i premiumklassen, alltså över volymbilarna men under de största '
           'SUV:arna. Quattro och luftfjädring är de två faktorer som oftast förklarar '
           'skillnaden mellan två Q5 med samma årsmodell.'),
},
{
 'slug': 'q7', 'namn': 'Q7', 'typ': 'stor SUV med sju säten', 'ar': '2015–',
 'drivlina': 'bensin, diesel och laddhybrid',
 'kort': 'Audis största SUV med förbränningsmotor och ett av få sjusitsiga premiumalternativ.',
 'vinkel': 'Q7 är den Audi som oftast omfattas av särskilda stöldkrav. Stora premium-SUV:ar '
           'är eftertraktade, och flera bolag kräver godkänt stöldskydd eller spårsändare i '
           'vissa postnummerområden. Kravet står i villkoren och är en förutsättning för '
           'ersättning — inte ett råd. Kontrollera det innan du tecknar, inte efter.',
 'punkter': ['Kan omfattas av krav på spårsändare beroende på postnummer',
             'Sju säten ger högre exponering för personskador',
             'Luftfjädring är standard och dyr att ersätta'],
 'skada': 'Stöldförsök och inbrott väger tyngre här än på Audis mindre modeller. Bilens '
          'värde och utrustningsnivå gör den intressant, särskilt i storstadsområdena.',
 'varde': 'Höga ersättningsvärden även på äldre exemplar, vilket håller vagnskadedelen '
          'motiverad länge.',
 'niva': 'Helförsäkring under hela den period bilen har ett reellt andrahandsvärde.',
 'fraga': ('Krävs spårsändare på Audi Q7?',
           'Flera bolag ställer krav på godkänt stöldskydd för stora premium-SUV:ar, ofta '
           'kopplat till postnummer. Uppfylls kravet inte den natt bilen försvinner kan '
           'ersättningen sättas ned eller nekas helt.'),
},
{
 'slug': 'q4-e-tron', 'namn': 'Q4 e-tron', 'typ': 'eldriven SUV', 'ar': '2021–',
 'drivlina': 'helt eldriven',
 'kort': 'Audis mest sålda elbil och märkets volymmodell i eldrivet segment.',
 'vinkel': 'Q4 e-tron bygger på Volkswagens MEB-plattform, samma som ID.4 och Skoda Enyaq. '
           'Det är avgörande för premien: delarna är standardiserade och verkstäderna med '
           'högvoltsbehörighet många. Q4 e-tron är därför en av de billigare premiumelbilarna '
           'att försäkra, trots Audi-märket.',
 'punkter': ['MEB-plattformen ger brett verkstadsnät och god delstillgång',
             'Sportback-versionen har större bakruta och tyngre glasmoment',
             'Kontrollera att batteriet omfattas av vagnskadedelen'],
 'skada': 'Glasskador väger tungt, särskilt på Sportback. Kamerorna bakom vindrutan kräver '
          'kalibrering efter varje byte.',
 'varde': 'Stabilare restvärde än många elbilar tack vare plattformens spridning.',
 'niva': 'Helförsäkring så länge marknadsvärdet ligger över 150 000 kr.',
 'fraga': ('Är Audi Q4 e-tron dyr att försäkra?',
           'Mindre än märket antyder. Den delade MEB-plattformen med VW och Skoda ger både '
           'delstillgång och ett brett verkstadsnät, vilket är precis de två faktorer som '
           'annars driver upp elbilspremier.'),
},
{
 'slug': 'q6-e-tron', 'namn': 'Q6 e-tron', 'typ': 'mellanstor eldriven SUV', 'ar': '2025–',
 'drivlina': 'helt eldriven',
 'kort': 'Audis nyaste el-SUV, byggd på den nya PPE-plattformen med 800-voltsteknik.',
 'vinkel': 'Q6 e-tron är den första Audi på PPE-plattformen, som märket utvecklat tillsammans '
           'med Porsche. Tekniken är alltså ny och delas ännu med få modeller, vilket betyder '
           'att antalet verkstäder med rätt behörighet är mindre än för Q4 e-tron. Det är den '
           'skillnaden du betalar för, inte bilens storlek.',
 'punkter': ['PPE-plattformen delas med Porsche Macan Electric',
             '800-voltsteknik kräver verkstad med särskild behörighet',
             'Ny modell — jämför brett medan bolagen kalibrerar sina priser'],
 'skada': 'Sensorpaketet i fronten gör även måttliga skador dyra, eftersom kalibrering '
          'tillkommer efter reparationen.',
 'varde': 'Ingen etablerad andrahandsmarknad ännu, vilket några bolag prissätter som en '
          'osäkerhet.',
 'niva': 'Helförsäkring. Bilen är för ny och för värdefull för något annat.',
 'fraga': ('Är Q6 e-tron dyrare att försäkra än Q4 e-tron?',
           'Ja, av två skäl. Ersättningsvärdet är högre, och PPE-plattformen är nyare med '
           'färre certifierade verkstäder än MEB. Skillnaden handlar mer om verkstadsnätet än '
           'om bilarnas storlek.'),
},
{
 'slug': 'a6-e-tron', 'namn': 'A6 e-tron', 'typ': 'stor eldriven kombi och sedan', 'ar': '2025–',
 'drivlina': 'helt eldriven',
 'kort': 'Den eldrivna A6 och Audis svar på BMW i5 och Mercedes EQE.',
 'vinkel': 'A6 e-tron har tagit över A6:s roll som tjänstebil, och beståndet kommer att '
           'präglas av det: höga körsträckor de första åren och hög utrustningsnivå. '
           'Avant-versionen har dessutom en stor bakruta som gör glasmomentet tyngre än på '
           'sedanen. Ange din egen körsträcka om du köper begagnat — inte bilens historik.',
 'punkter': ['PPE-plattform med 800-voltsteknik, som Q6 e-tron',
             'Avant har större glasytor och tyngre glasmoment',
             'Stor andel tjänstebilar med höga körsträckor'],
 'skada': 'Glas- och sensorrelaterade ärenden dominerar. Assistanspaketet är omfattande och '
          'kräver kalibrering efter även måttliga frontskador.',
 'varde': 'Snabb värdeminskning de första åren, som på alla stora tjänstebilar.',
 'niva': 'Helförsäkring under hela den period bilen har ett reellt andrahandsvärde.',
 'fraga': ('Vad kostar det att försäkra en Audi A6 e-tron?',
           'Den övre delen av elbilsspannet. Ersättningsvärdet är högt och plattformen ny, '
           'vilket ger färre certifierade verkstäder än på MEB-baserade modeller.'),
},
{
 'slug': 'e-tron-gt', 'namn': 'e-tron GT', 'typ': 'eldriven sportsedan', 'ar': '2021–',
 'drivlina': 'helt eldriven, fyrhjulsdrift',
 'kort': 'Audis eldrivna flaggskepp, tekniskt nära besläktad med Porsche Taycan.',
 'vinkel': 'e-tron GT är Audis dyraste bil att försäkra, och skälen staplar sig: högt '
           'ersättningsvärde, mycket hög effekt, låg markfrigång och ett litet bestånd som '
           'ger tunn skadestatistik. Flera bolag kräver förhöjd självrisk i den här '
           'effektklassen, och det syns inte i årspremien utan först vid skadan.',
 'punkter': ['Delar teknik med Porsche Taycan',
             'Effektklassen kan utlösa krav på förhöjd självrisk',
             'Låg markfrigång gör underredet och batterihöljet utsatta'],
 'skada': 'Skador på underrede och frontspoiler är den dyraste kategorin, eftersom '
          'batteripaketet utgör bilens strukturella botten.',
 'varde': 'Kraftig värdeminskning de första åren från en mycket hög startpunkt.',
 'niva': 'Helförsäkring. Bilens värde och reparationskostnad gör allt annat orimligt.',
 'fraga': ('Kräver försäkringsbolagen förhöjd självrisk på Audi e-tron GT?',
           'Vissa gör det över ett visst effektuttag, och e-tron GT ligger klart över de '
           'gränser som förekommer. Det är en post som inte syns i årspremien utan först vid '
           'skadan — fråga uttryckligen innan du tecknar.'),
},
],
}
