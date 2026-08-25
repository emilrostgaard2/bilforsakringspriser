# -*- coding: utf-8 -*-
"""Modelldata för Tesla, XPeng och Cupra.

Samma fältstruktur som modeller.py. Läggs ihop med den filen i
modellsidor.py, så att generatorn ser en enda katalog.

URVAL
Vi listar de modeller som faktiskt säljs i Sverige i dag. Att fylla ut
med modeller som aldrig kommit hit ger sidor utan sökvolym och utan
läsare — tio sidor för sakens skull är sämre än fyra som stämmer.
"""

MODELLER_2 = {

# ═══ TESLA ═════════════════════════════════════════════════════════
'tesla': [
{
 'slug': 'model-3', 'namn': 'Model 3', 'typ': 'eldriven sedan', 'ar': '2019–',
 'drivlina': 'helt eldriven, bakhjuls- eller fyrhjulsdrift',
 'kort': 'Sveriges vanligaste eldrivna sedan och den bil som gjorde elbilen till '
         'tjänstebilsstandard.',
 'vinkel': 'Model 3 är den elbil svenska försäkringsbolag har mest data på, vilket i sig '
           'håller nere premien. Det som drar åt andra hållet är reparationskostnaden: Tesla '
           'använder gjutna karossektioner där en skada som på en vanlig bil hade betytt ett '
           'plåtjobb i stället kan kräva att en hel sektion byts.',
 'punkter': ['Störst dataunderlag av alla elbilar i Sverige',
             'Gjuten kaross gör vissa plåtskador oproportionerligt dyra',
             'Fritt verkstadsval är värt mindre — Tesla styr reparationerna'],
 'skada': 'Skador på bakre stötfångarpartiet är överrepresenterade, ofta från backning i '
          'trånga lägen. Kameran och sensorerna sitter så att även lätta smällar utlöser '
          'kalibrering.',
 'varde': 'Restvärdet har varit rörligare än på någon annan modell i klassen, efter '
          'upprepade prissänkningar på nya bilar.',
 'niva': 'Helförsäkring. Bilens värde och reparationskostnaderna gör vagnskadedelen '
         'motiverad även på äldre exemplar.',
 'fraga': ('Är Tesla Model 3 dyr att försäkra?',
           'Premien ligger över en jämnstor bensinbil, framför allt på grund av '
           'reparationskostnaderna och det smala verkstadsnätet. Samtidigt har bolagen mer '
           'skadedata på Model 3 än på någon annan elbil, vilket drar åt andra hållet.'),
},
{
 'slug': 'model-y', 'namn': 'Model Y', 'typ': 'eldriven SUV', 'ar': '2021–',
 'drivlina': 'helt eldriven, bakhjuls- eller fyrhjulsdrift',
 'kort': 'Världens mest sålda bil under flera år och Sveriges vanligaste elbil.',
 'vinkel': 'Model Y delar teknik med Model 3 men väger mer, sitter högre och används oftare '
           'som familjens enda bil. Det ger fler körda mil per år och en högre exponering, '
           'vilket syns i premien. Bakluckan är dessutom en av de dyraste enskilda delarna '
           'på bilen — en skada där blir sällan billig.',
 'punkter': ['Högre årlig körsträcka än Model 3 i statistiken',
             'Panoramataket i glas är dyrt att ersätta',
             'Kontrollera hyrbilsdagar — väntetid på delar förekommer'],
 'skada': 'Glasskador väger tungt. Både vindrutan och det stora glastaket är stora ytor, och '
          'vindrutan kräver kalibrering av kamerorna efter byte.',
 'varde': 'Håller värdet något bättre än Model 3, eftersom efterfrågan på begagnade '
          'el-SUV:ar är stabilare.',
 'niva': 'Helförsäkring under hela bilens livslängd så länge marknadsvärdet ligger över '
         '150 000 kr.',
 'fraga': ('Vad kostar det att försäkra en Tesla Model Y?',
           'Något mer än Model 3, eftersom bilen är tyngre, körs längre och har dyrare glas. '
           'Skillnaden mellan bolagen är stor — hämta offert på registreringsnumret hos '
           'minst tre.'),
},
{
 'slug': 'model-s', 'namn': 'Model S', 'typ': 'stor eldriven sedan', 'ar': '2013–',
 'drivlina': 'helt eldriven, fyrhjulsdrift',
 'kort': 'Teslas flaggskepp och den modell som byggde märkets rykte i Sverige.',
 'vinkel': 'Model S är den dyraste Teslan att försäkra, och skälen staplar sig: högt '
           'ersättningsvärde, hög effekt och ett litet bestånd som ger tunn skadestatistik. '
           'Äldre exemplar är samtidigt billiga att köpa, vilket skapar ett gap — bilen kan '
           'kosta 250 000 kr att köpa och ändå ligga i en premieklass som speglar en betydligt '
           'dyrare bil.',
 'punkter': ['Effektklassen väger tungt, särskilt på Plaid-versionen',
             'Litet bestånd ger stor spridning mellan bolagens priser',
             'Luftfjädringen är dyr och täcks inte av alla maskinskadevillkor'],
 'skada': 'Skador på underrede och batterihölje är den dyraste kategorin. Ett hårt möte med '
          'en trottoarkant kan i värsta fall innebära att batteripaketet måste undersökas.',
 'varde': 'Kraftig värdeminskning på äldre exemplar, men golvet har visat sig stabilt de '
          'senaste åren.',
 'niva': 'Helförsäkring på nyare exemplar. På en tio år gammal Model S bör du räkna på '
         'marknadsvärdet innan du förnyar.',
 'fraga': ('Varför är Tesla Model S så dyr att försäkra?',
           'Tre saker: högt ersättningsvärde, hög motoreffekt och ett litet bestånd som gör '
           'skadestatistiken osäker. Bolagen prissätter osäkerheten, vilket gör att '
           'skillnaden mellan billigaste och dyraste offert blir ovanligt stor.'),
},
{
 'slug': 'model-x', 'namn': 'Model X', 'typ': 'stor eldriven SUV', 'ar': '2016–',
 'drivlina': 'helt eldriven, fyrhjulsdrift',
 'kort': 'Teslas största SUV, känd för falcon wing-dörrarna och sju säten.',
 'vinkel': 'Model X är den svåraste bilen i Teslas utbud att få ett bra pris på. '
           'Falcon wing-dörrarna innehåller sensorer och en mekanism som få verkstäder rör, '
           'bilen är tung, effektstark och dyr att ersätta. Flera bolag ställer dessutom krav '
           'på stöldskydd i storstadsområdena.',
 'punkter': ['Falcon wing-dörrarna är en egen reparationsrisk',
             'Sju säten och hög vikt ger hög exponering',
             'Kan omfattas av krav på spårsändare beroende på postnummer'],
 'skada': 'Dörrmekanismen står för en oproportionerlig andel av ärendena. Skador uppstår '
          'ofta i garage med lågt tak eller trånga parkeringar.',
 'varde': 'Höga ersättningsvärden även på äldre bilar, vilket håller vagnskadedelen '
          'motiverad länge.',
 'niva': 'Helförsäkring, och kontrollera uttryckligen att dörrmekanismen omfattas.',
 'fraga': ('Täcks Model X falcon wing-dörrar av försäkringen?',
           'Skador från yttre händelser omfattas av vagnskadedelen i en helförsäkring. '
           'Mekaniska fel i själva dörrmekanismen är däremot en maskinskadefråga, och där '
           'skiljer sig villkoren rejält mellan bolagen. Läs det momentet innan du tecknar.'),
},
],

# ═══ XPENG ═════════════════════════════════════════════════════════
'xpeng': [
{
 'slug': 'g6', 'namn': 'G6', 'typ': 'eldriven SUV', 'ar': '2024–',
 'drivlina': 'helt eldriven',
 'kort': 'XPengs mest sålda modell i Sverige och märkets konkurrent till Tesla Model Y.',
 'vinkel': 'G6 är den XPeng-modell som svenska bolag har mest data på, vilket inte säger så '
           'mycket — beståndet är ändå litet. Det gör att spridningen mellan bolagens '
           'offerter är stor, och att det verkligen lönar sig att hämta fler än tre. '
           'Bilen använder 800-voltsteknik, vilket kräver certifierad verkstad vid arbete på '
           'högvoltssystemet.',
 'punkter': ['Litet bestånd ger stor spridning mellan bolagens priser',
             '800-voltsteknik kräver verkstad med rätt behörighet',
             'Kontrollera antalet hyrbilsdagar — delvägar är fortfarande under uppbyggnad'],
 'skada': 'Skador på fronten är dyra. Radar, kameror och lidar sitter samlade där, och även '
          'en låg parkeringssmäll kan utlösa kalibrering av hela assistanspaketet.',
 'varde': 'Kort marknadshistorik gör restvärdet svårbedömt, vilket några bolag prissätter '
          'som en osäkerhet.',
 'niva': 'Helförsäkring. Bilen är för ny för något annat, och vagnskadegarantin täcker de '
         'första åren.',
 'fraga': ('Är XPeng G6 dyr att försäkra i Sverige?',
           'Premien ligger normalt något över en jämnstor etablerad elbil, eftersom '
           'skadeunderlaget är tunt och verkstadsnätet under uppbyggnad. Skillnaden mellan '
           'bolagen är samtidigt ovanligt stor — jämför brett.'),
},
{
 'slug': 'g9', 'namn': 'G9', 'typ': 'stor eldriven SUV', 'ar': '2023–',
 'drivlina': 'helt eldriven',
 'kort': 'XPengs största SUV, positionerad mot Audi Q8 e-tron och Tesla Model X.',
 'vinkel': 'G9 är stor, tung och välutrustad, och kombinationen ger både högt '
           'ersättningsvärde och hög exponering. Det som avgör din premie mer än något annat '
           'är dock hur bolaget hanterar märket över huvud taget — vissa bolag har ännu inte '
           'byggt in kinesiska premiummärken i sina modeller och lägger på ett generellt '
           'osäkerhetspåslag.',
 'punkter': ['Högt ersättningsvärde i en klass där få jämförelseobjekt finns',
             'Luftfjädring på flera versioner — kontrollera maskinskademomentet',
             'Fråga uttryckligen om bolaget har egen prissättning för märket'],
 'skada': 'Sensorpaketet gör även små frontskador dyra, och bilens bredd gör den utsatt i '
          'äldre parkeringshus.',
 'varde': 'Snabb värdeminskning de första åren, som på de flesta nya premiumelbilar.',
 'niva': 'Helförsäkring under hela den period bilen har ett reellt andrahandsvärde.',
 'fraga': ('Vilka bolag försäkrar XPeng G9?',
           'De flesta större bolag tecknar märket, men alla har inte egen prissättning för '
           'det. Ett bolag som saknar modelldata lägger ofta på ett generellt påslag. Fråga '
           'uttryckligen, och jämför brett — spridningen är stor.'),
},
{
 'slug': 'p7', 'namn': 'P7', 'typ': 'eldriven sedan', 'ar': '2024–',
 'drivlina': 'helt eldriven',
 'kort': 'XPengs sportiga sedan och märkets svar på Tesla Model 3.',
 'vinkel': 'P7 är låg, lång och byggd med fokus på aerodynamik, vilket ger två '
           'försäkringsrelevanta konsekvenser: markfrigången är låg och underredet utsatt, '
           'och karossen har stora sammanhängande partier som blir dyra att laga. Lägg till '
           'ett litet svenskt bestånd, så förklarar det varför premien kan ligga högre än '
           'bilens pris antyder.',
 'punkter': ['Låg markfrigång gör underredet utsatt vid farthinder',
             'Stora karossektioner ger dyra plåtskador',
             'Litet bestånd — hämta fler offerter än vanligt'],
 'skada': 'Underredesskador och skador på frontspoilern är vanligare än på en SUV i samma '
          'prisklass, av rent geometriska skäl.',
 'varde': 'Restvärdet är ännu oprövat på den svenska marknaden.',
 'niva': 'Helförsäkring, med särskild kontroll av att batteriet omfattas av vagnskadedelen.',
 'fraga': ('Vad kostar försäkring till XPeng P7?',
           'Vi har inte hittat publicerade prisexempel för modellen. Räkna med att den '
           'hamnar i samma spann som andra eldrivna sedaner i klassen, men med större '
           'spridning mellan bolagen eftersom underlaget är tunt.'),
},
{
 'slug': 'x9', 'namn': 'X9', 'typ': 'eldriven MPV', 'ar': '2025–',
 'drivlina': 'helt eldriven',
 'kort': 'En eldriven sjusitsig MPV i ett segment där svenska alternativ nästan saknas.',
 'vinkel': 'X9 är ovanlig på flera sätt: det är en stor MPV i en marknad som övergett '
           'formatet, den är eldriven, och beståndet i Sverige är mycket litet. Det gör '
           'prissättningen svårförutsägbar. Flera bolag saknar helt enkelt en modellprofil '
           'och prissätter bilen som "övrig stor personbil", vilket kan slå åt båda hållen.',
 'punkter': ['Segmentet saknar jämförelseobjekt — prissättningen varierar kraftigt',
             'Sju säten ger hög exponering för personskador',
             'De elektriska skjutdörrarna är en egen reparationspost'],
 'skada': 'Skjutdörrarnas mekanism och skenor är den mest modellspecifika skaderisken, '
          'särskilt vid användning i trånga stadsmiljöer.',
 'varde': 'Marknadsvärdet är svårbedömt eftersom andrahandsmarknaden knappt existerar ännu.',
 'niva': 'Helförsäkring, och begär skriftligt besked om hur bolaget klassar bilen.',
 'fraga': ('Hur försäkrar man en XPeng X9?',
           'Som vilken personbil som helst, men eftersom modellen är ny och ovanlig i Sverige '
           'saknar flera bolag egen modelldata. Begär skriftligt besked om vilken klass bilen '
           'placeras i, och jämför fler bolag än du annars skulle.'),
},
],

# ═══ CUPRA ═════════════════════════════════════════════════════════
'cupra': [
{
 'slug': 'formentor', 'namn': 'Formentor', 'typ': 'kompakt SUV-coupé', 'ar': '2020–',
 'drivlina': 'bensin, mildhybrid och laddhybrid',
 'kort': 'Cupras mest sålda modell och den enda som byggts som Cupra från början.',
 'vinkel': 'Formentor delar plattform och delkatalog med VW Tiguan och Seat Ateca, vilket är '
           'goda nyheter för reparationskostnaden. Det som drar upp premien är i stället '
           'effektuttaget: VZ-versionerna ligger i en helt annan effektklass än basmodellen, '
           'och bolagen prissätter dem därefter. Skillnaden mellan en Formentor 1.5 TSI och '
           'en VZ5 är större i premie än i pris.',
 'punkter': ['Delar delkatalog med VW och Seat — bra delstillgång',
             'VZ-versionerna hamnar i en betydligt högre effektklass',
             'Stora fälgar är dyra att ersätta och tar ofta skada mot trottoarkanter'],
 'skada': 'Fälg- och däckskador är överrepresenterade. Sportfjädringen och de stora fälgarna '
          'gör bilen känslig mot kantstenar och farthinder.',
 'varde': 'Håller värdet väl i den kompakta SUV-klassen, delvis tack vare stark efterfrågan '
          'på privatleasingmarknaden.',
 'niva': 'Helförsäkring till omkring åtta år. Många exemplar går på leasing, och då krävs '
         'helförsäkring enligt avtalet.',
 'fraga': ('Är Cupra Formentor dyr att försäkra?',
           'Basversionerna ligger i nivå med andra kompakta SUV:ar tack vare den delade '
           'VW-tekniken. VZ-versionerna är en annan sak — effektklassen gör att premien kan '
           'bli avsevärt högre för samma kaross.'),
},
{
 'slug': 'born', 'namn': 'Born', 'typ': 'eldriven halvkombi', 'ar': '2022–',
 'drivlina': 'helt eldriven',
 'kort': 'Cupras första elbil, byggd på samma plattform som Volkswagen ID.3.',
 'vinkel': 'Born är i grunden en ID.3 med annan kaross och sportigare avstämning, och det är '
           'goda nyheter för premien: MEB-plattformen är en av de vanligaste i Europa, vilket '
           'ger både delstillgång och en skadestatistik bolagen känner. Det gör Born till en '
           'av de billigare elbilarna att försäkra i sin klass.',
 'punkter': ['Delar MEB-plattform med VW ID.3 — utmärkt delstillgång',
             'Fler verkstäder med rätt behörighet än för nyare elbilsmärken',
             'Kontrollera att batteriet omfattas av vagnskadedelen'],
 'skada': 'Parkeringsskador dominerar, som på de flesta kompakta stadsbilar. Skador på '
          'fronten utlöser kalibrering av assistanssystemen.',
 'varde': 'Följer elbilsmarknaden i stort, med ett golv som stabiliserats de senaste åren.',
 'niva': 'Helförsäkring så länge bilen är värd över 150 000 kr, därefter en räknesak.',
 'fraga': ('Är Cupra Born billigare att försäkra än andra elbilar?',
           'Ofta ja, i sin storleksklass. Den delade VW-plattformen ger både bra '
           'delstillgång och ett stort verkstadsnät, vilket är precis de två faktorer som '
           'annars driver upp premien på elbilar.'),
},
{
 'slug': 'leon', 'namn': 'Leon', 'typ': 'halvkombi och kombi', 'ar': '2020–',
 'drivlina': 'bensin, mildhybrid och laddhybrid',
 'kort': 'Prestandaversionen av Seat Leon, med både halvkombi och Sportstourer.',
 'vinkel': 'Cupra Leon är en Seat Leon med mer effekt, och det är den skillnaden bolagen '
           'prissätter. Karossen, delarna och verkstäderna är desamma, men effektklassen '
           'ligger högre — och effekt är en av de faktorer som väger tyngst på just den här '
           'typen av bil, eftersom skadestatistiken för starka kompaktbilar är tydlig.',
 'punkter': ['Samma kaross och delar som Seat Leon, högre effektklass',
             'Sportstourer-versionen har lägre skadefrekvens än halvkombin',
             'Kontrollera om bolaget kräver förhöjd självrisk på de starkaste versionerna'],
 'skada': 'Kollisionsskador i trafik väger tyngre här än på jämförbara bilar, vilket är '
          'typiskt för prestandaversioner av vanliga modeller.',
 'varde': 'Följer Seat Leon nedåt i värde men från en högre startpunkt.',
 'niva': 'Helförsäkring till omkring sju år, sedan en fråga om marknadsvärdet.',
 'fraga': ('Kostar Cupra Leon mer att försäkra än Seat Leon?',
           'Ja, normalt. Bilarna delar kaross och delar, men Cupra-versionerna har högre '
           'effekt, och effektklassen är en av de tyngsta faktorerna i premieberäkningen för '
           'kompaktbilar.'),
},
{
 'slug': 'tavascan', 'namn': 'Tavascan', 'typ': 'eldriven SUV-coupé', 'ar': '2024–',
 'drivlina': 'helt eldriven',
 'kort': 'Cupras eldrivna SUV-coupé, byggd på MEB-plattformen.',
 'vinkel': 'Tavascan bygger på samma MEB-teknik som Born och VW ID.5, men tillverkas i Kina, '
           'vilket har påverkat delvägarna under de första åren. Tekniken är alltså bekant '
           'för verkstäderna medan logistiken inte alltid varit det — och det är väntetid på '
           'delar, inte reparationens svårighetsgrad, som drabbar dig via hyrbilsmomentet.',
 'punkter': ['Känd MEB-teknik men importerad från Kina',
             'Kontrollera hyrbilsdagar noga',
             'VZ-versionen har tvåmotorsdrift och högre effektklass'],
 'skada': 'Den sluttande taklinjen gör bakrutan stor och dyr, och glasskador blir därför en '
          'tyngre post än på en vanlig SUV.',
 'varde': 'Ännu oprövat restvärde på den svenska marknaden.',
 'niva': 'Helförsäkring. Vagnskadegarantin täcker de första åren.',
 'fraga': ('Vad skiljer försäkringen på Cupra Tavascan från Born?',
           'Tekniskt lite, eftersom båda bygger på MEB-plattformen. Tavascan är däremot '
           'större, dyrare och nyare på marknaden, vilket ger högre ersättningsvärde och '
           'därmed högre premie — särskilt på vagnskadedelen.'),
},
{
 'slug': 'terramar', 'namn': 'Terramar', 'typ': 'mellanstor SUV', 'ar': '2025–',
 'drivlina': 'mildhybrid och laddhybrid',
 'kort': 'Cupras största SUV med förbränningsmotor, placerad över Formentor.',
 'vinkel': 'Terramar är ny på marknaden och delar teknik med Audi Q3, vilket ger bra '
           'delstillgång från start. Eftersom modellen är ny saknar flera bolag egen '
           'skadestatistik och lutar sig mot koncernens övriga modeller. Det är i regel bra '
           'för dig: en ny modell på en beprövad plattform prissätts sällan med '
           'osäkerhetspåslag.',
 'punkter': ['Delar teknik med Audi Q3 — beprövad plattform',
             'Laddhybriden har högre ersättningsvärde än mildhybriden',
             'Ny modell, så jämför brett medan bolagen kalibrerar sina priser'],
 'skada': 'För ny för egen skadestatistik. Räkna med samma mönster som Formentor, men med '
          'något fler backningsskador eftersom bilen är större.',
 'varde': 'Ingen etablerad andrahandsmarknad ännu.',
 'niva': 'Halvförsäkring så länge vagnskadegarantin gäller, därefter helförsäkring.',
 'fraga': ('Behöver jag helförsäkring på en ny Cupra Terramar?',
           'Inte nödvändigtvis de första åren. Nya bilar har normalt vagnskadegaranti i tre '
           'år, och under den tiden räcker halvförsäkring. Kontrollera garantins längd på '
           'just ditt exemplar innan du väljer.'),
},
{
 'slug': 'ateca', 'namn': 'Ateca', 'typ': 'kompakt SUV', 'ar': '2018–2024',
 'drivlina': 'bensin, fyrhjulsdrift',
 'kort': 'Prestandaversionen av Seat Ateca, numera utgången ur nyproduktionen.',
 'vinkel': 'Cupra Ateca är den modell i utbudet som går att köpa begagnad till ett rimligt '
           'pris, och det gör premien mer överkomlig än på övriga Cupra. Bilen har '
           'fyrhjulsdrift och stark motor, vilket håller uppe effektklassen, men '
           'marknadsvärdet har sjunkit tillräckligt för att skyddsnivån ska vara värd att '
           'räkna på.',
 'punkter': ['Utgången modell — begagnatpriserna har fallit',
             'Fyrhjulsdriften innehåller komponenter som blir dyra vid påkörning bakifrån',
             'Delar delkatalog med Seat och VW'],
 'skada': 'Skador på drivlinan bakåt är den dyraste kategorin. Bakaxeldifferentialen på '
          'fyrhjulsdrivna versioner är en kostsam post.',
 'varde': 'Faller stadigt nu när modellen utgått, vilket flyttar gränsen för helförsäkring '
          'nedåt i ålder.',
 'niva': 'Helförsäkring så länge bilen är värd över 150 000 kr. Därefter räkna på '
         'halvförsäkring.',
 'fraga': ('Går det att försäkra en Cupra Ateca trots att modellen utgått?',
           'Ja, utan problem. Att en modell inte längre säljs ny påverkar varken '
           'möjligheten att teckna eller villkoren. Delstillgången är dessutom god eftersom '
           'bilen delar teknik med Seat och Volkswagen.'),
},
],
}
