# -*- coding: utf-8 -*-
"""Modelldata för Polestar, Zeekr och Hyundai.

URVAL
Polestar och Zeekr säljer tre modeller var i Sverige — vi listar dem och
inget mer. Hyundai får tio: de åtta som redan låg i brands.py plus
INSTER och IONIQ 9, som båda kom till marknaden 2025 och saknades helt.
"""

MODELLER_3 = {

# ═══ POLESTAR ══════════════════════════════════════════════════════
'polestar': [
{
 'slug': 'polestar-2', 'namn': 'Polestar 2', 'typ': 'eldriven halvkombi', 'ar': '2020–',
 'drivlina': 'helt eldriven, bak- eller fyrhjulsdrift',
 'kort': 'Polestars mest sålda modell och märkets genombrott på den svenska marknaden.',
 'vinkel': 'Polestar 2 delar verkstadsnät med Volvo, och det är den enskilt viktigaste '
           'faktorn bakom premien. Där andra elbilsmärken kämpar med få certifierade '
           'verkstäder har Polestar tillgång till ett av Sveriges tätaste servicenät från '
           'start. Det som väger åt andra hållet är vikten — bilen är tyngre än formatet '
           'antyder, och vikt driver skadekostnad.',
 'punkter': ['Delar verkstadsnät och delkatalog med Volvo',
             'Tyngre än en jämnstor bensinbil, vilket ökar skadekostnaden',
             'Performance-paketet ger högre effektklass och större fälgar'],
 'skada': 'Skador på fronten är dyra. Sensorpaketet sitter samlat bakom stötfångaren, och '
          'även en låg parkeringssmäll kan utlösa kalibrering av hela assistanspaketet.',
 'varde': 'Restvärdet föll kraftigt 2023 och har sedan stabiliserats, vilket gör begagnade '
          'exemplar prisvärda och flyttar gränsen för helförsäkring nedåt.',
 'niva': 'Helförsäkring så länge marknadsvärdet ligger över 150 000 kr.',
 'fraga': ('Är Polestar 2 dyr att försäkra?',
           'Nej, jämfört med andra elbilar i samma klass ligger den lågt. Det delade '
           'verkstadsnätet med Volvo är avgörande — antalet verkstäder som får laga bilen är '
           'större än för nästan något annat elbilsmärke.'),
},
{
 'slug': 'polestar-3', 'namn': 'Polestar 3', 'typ': 'stor eldriven SUV', 'ar': '2024–',
 'drivlina': 'helt eldriven, fyrhjulsdrift',
 'kort': 'Polestars stora SUV, byggd på samma plattform som Volvo EX90.',
 'vinkel': 'Polestar 3 är märkets dyraste modell och den enda som regelbundet omfattas av '
           'krav på stöldskydd. Stora eldrivna premium-SUV:ar är eftertraktade, och flera '
           'bolag kräver godkänt larm eller spårsändare i vissa postnummerområden. Kravet '
           'står i villkoren och är en förutsättning för ersättning — inte ett råd.',
 'punkter': ['Kan omfattas av krav på spårsändare beroende på var du bor',
             'Delar plattform med Volvo EX90 — bra delstillgång',
             'Luftfjädring på flera versioner, kontrollera maskinskademomentet'],
 'skada': 'Stöldförsök och inbrott väger tyngre här än på Polestar 2. Bilens värde och '
          'utrustningsnivå gör den intressant, särskilt i storstadsområdena.',
 'varde': 'Högt ersättningsvärde även på begagnade exemplar, vilket håller vagnskadedelen '
          'motiverad länge.',
 'niva': 'Helförsäkring under hela den period bilen har ett reellt andrahandsvärde.',
 'fraga': ('Krävs spårsändare på Polestar 3?',
           'Flera bolag ställer krav på godkänt stöldskydd för stora eldrivna SUV:ar, ofta '
           'kopplat till postnummer. Kontrollera villkoren innan du tecknar — uppfylls kravet '
           'inte kan ersättningen sättas ned vid stöld.'),
},
{
 'slug': 'polestar-4', 'namn': 'Polestar 4', 'typ': 'eldriven SUV-coupé', 'ar': '2024–',
 'drivlina': 'helt eldriven',
 'kort': 'Polestars SUV-coupé, känd för att sakna bakruta helt.',
 'vinkel': 'Polestar 4 har en konstruktionsdetalj som faktiskt påverkar försäkringen: den '
           'saknar bakruta och använder i stället en kamera med skärm som backspegel. Det '
           'tar bort en av de vanligaste glasskadorna helt, men lägger till en '
           'elektronikkomponent som är dyr att ersätta och som bilen är beroende av för att '
           'vara körbar.',
 'punkter': ['Ingen bakruta — en vanlig glasskada försvinner helt',
             'Kamerabaserad backspegel är dyr elektronik att ersätta',
             'Tillverkas i Kina, vilket påverkat delvägarna'],
 'skada': 'Frontskador med sensorkalibrering dominerar. Den sluttande taklinjen gör '
          'dessutom att skador på bakpartiet blir plåtjobb snarare än glasjobb.',
 'varde': 'Kort marknadshistorik gör restvärdet svårbedömt.',
 'niva': 'Helförsäkring. Bilen är för ny och för dyr för att något annat ska vara aktuellt.',
 'fraga': ('Påverkar den saknade bakrutan försäkringen på Polestar 4?',
           'Ja, på två sätt. Risken för krossad bakruta försvinner, vilket gör glasmomentet '
           'lättare. Samtidigt är kamerasystemet som ersätter rutan dyrt att laga och '
           'nödvändigt för att bilen ska vara körbar.'),
},
],

# ═══ ZEEKR ═════════════════════════════════════════════════════════
'zeekr': [
{
 'slug': 'x', 'namn': 'X', 'typ': 'kompakt eldriven SUV', 'ar': '2024–',
 'drivlina': 'helt eldriven',
 'kort': 'Zeekrs minsta modell och märkets vanligaste bil på svenska vägar.',
 'vinkel': 'Zeekr X bygger på samma SEA-plattform som Volvo EX30 och Smart #1, vilket gör '
           'tekniken mindre främmande för svenska verkstäder än märkesnamnet antyder. Det '
           'som ändå håller premien uppe är beståndets storlek: skadestatistiken är tunn, '
           'och flera bolag prissätter osäkerheten snarare än bilen.',
 'punkter': ['Delar SEA-plattform med Volvo EX30 och Smart #1',
             'Litet svenskt bestånd ger stor spridning mellan bolagen',
             'Kontrollera antalet hyrbilsdagar — delvägarna är unga'],
 'skada': 'Frontskador med sensorkalibrering är den dyraste kategorin. Bilen är kompakt och '
          'används mest i stad, där parkeringsskador är vanligast.',
 'varde': 'Ingen etablerad andrahandsmarknad i Sverige ännu, vilket några bolag prissätter '
          'som en risk.',
 'niva': 'Helförsäkring. Vagnskadegarantin täcker de första åren.',
 'fraga': ('Vilka bolag försäkrar Zeekr X i Sverige?',
           'De flesta större bolag tecknar märket, men alla har inte egen prissättning för '
           'det. Ett bolag utan modelldata lägger ofta på ett generellt påslag. Fråga '
           'uttryckligen hur bilen klassas och jämför brett.'),
},
{
 'slug': '001', 'namn': '001', 'typ': 'stor eldriven kombi', 'ar': '2024–',
 'drivlina': 'helt eldriven, fyrhjulsdrift',
 'kort': 'Zeekrs stora kombi och märkets flaggskepp på den svenska marknaden.',
 'vinkel': 'Zeekr 001 är stor, tung och effektstark, en kombination som prissätts hårt '
           'oavsett märke. Lägg till ett litet bestånd och ett verkstadsnät under uppbyggnad, '
           'så förklarar det varför spridningen mellan bolagens offerter är ovanligt stor på '
           'just den här bilen. Det är också därför det lönar sig extra att jämföra brett.',
 'punkter': ['Hög effekt och hög vikt driver premien',
             'Luftfjädring på flera versioner — kontrollera maskinskademomentet',
             'Utvecklad delvis i Göteborg, men tillverkad i Kina'],
 'skada': 'Skador på underrede och batterihölje är den dyraste kategorin, eftersom '
          'batteripaketet utgör bilens strukturella botten.',
 'varde': 'Svårbedömt restvärde utan etablerad andrahandsmarknad.',
 'niva': 'Helförsäkring, med särskild kontroll av att batteriet omfattas av vagnskadedelen.',
 'fraga': ('Är Zeekr 001 dyr att försäkra?',
           'Den ligger i den övre delen av elbilsspannet. Storlek, vikt och effekt driver '
           'premien, och det tunna skadeunderlaget gör att bolagen prissätter med marginal.'),
},
{
 'slug': '7x', 'namn': '7X', 'typ': 'mellanstor eldriven SUV', 'ar': '2025–',
 'drivlina': 'helt eldriven',
 'kort': 'Zeekrs nyaste SUV, positionerad mot Tesla Model Y och Volvo EX40.',
 'vinkel': 'Zeekr 7X är för ny för att ha egen skadestatistik i Sverige, och det märks i '
           'offerterna. Flera bolag saknar modellprofil och klassar bilen som övrig stor '
           'personbil, vilket kan slå åt båda hållen. Begär skriftligt besked om klassningen '
           'innan du tecknar — den avgör både premie och hur bilen värderas vid totalskada.',
 'punkter': ['För ny för egen skadestatistik i Sverige',
             '800-voltsteknik kräver verkstad med rätt behörighet',
             'Begär skriftligt besked om hur bolaget klassar bilen'],
 'skada': 'Sensorpaketet i fronten gör även måttliga skador dyra. I övrigt väntas samma '
          'mönster som för andra mellanstora el-SUV:ar.',
 'varde': 'Helt oprövat på den svenska marknaden.',
 'niva': 'Helförsäkring. Vagnskadegarantin täcker de första åren.',
 'fraga': ('Hur klassar försäkringsbolagen en Zeekr 7X?',
           'Som personbil, men vilken modellprofil som används varierar. Saknas egen data '
           'klassas bilen ofta schablonmässigt. Begär skriftligt besked, eftersom '
           'klassningen påverkar både premie och värdering vid totalskada.'),
},
],

# ═══ HYUNDAI ═══════════════════════════════════════════════════════
'hyundai': [
{
 'slug': 'kona', 'namn': 'Kona', 'typ': 'kompakt SUV', 'ar': '2023–',
 'drivlina': 'bensin, hybrid och helt eldriven',
 'kort': 'Hyundais mest sålda modell i Sverige och en av få som finns med tre olika drivlinor.',
 'vinkel': 'Kona är den modell där drivlinevalet påverkar premien mest i hela Hyundais '
           'utbud. Samma kaross finns som bensin, hybrid och elbil, och skillnaden mellan '
           'ytterligheterna är betydande — inte för att elbilen är sämre, utan för att '
           'batteriet utgör en stor del av ersättningsvärdet och kräver certifierad verkstad.',
 'punkter': ['Samma kaross finns som bensin, hybrid och elbil',
             'Elversionen har högre ersättningsvärde än bensinversionen',
             'Femårsgarantin utan milbegränsning håller uppe andrahandsvärdet'],
 'skada': 'Parkeringsskador dominerar. Kona används mest i tätort och pendling, och är '
          'kompakt nog att slippa de trängselproblem större SUV:ar har.',
 'varde': 'Håller värdet väl tack vare garantin, som följer bilen och inte ägaren.',
 'niva': 'Helförsäkring till omkring sju år. Elversionen längre, eftersom värdet är högre.',
 'fraga': ('Är Kona Electric dyrare att försäkra än bensinversionen?',
           'Ja, märkbart. Batteriet utgör en stor del av bilens värde och arbete på '
           'högvoltssystemet kräver certifierad verkstad. Skillnaden är större än mellan två '
           'bensinmotorer i samma bil.'),
},
{
 'slug': 'tucson', 'namn': 'Tucson', 'typ': 'mellanstor SUV', 'ar': '2021–',
 'drivlina': 'bensin, mildhybrid, hybrid och laddhybrid',
 'kort': 'Hyundais storsäljare i SUV-klassen och märkets vanligaste familjebil.',
 'vinkel': 'Tucson ligger i volymklassen och prissätts därefter. Beståndet är stort nog för '
           'säker skadestatistik, delarna finns hos alla Hyundai-verkstäder och '
           'ägarprofilen är gynnsam. Laddhybriden är undantaget: den har både högre '
           'ersättningsvärde och en drivlina med fler dyra komponenter.',
 'punkter': ['Stort bestånd ger välunderbyggd skadestatistik',
             'Laddhybriden har högre ersättningsvärde än mildhybriden',
             'Fyrhjulsdrift finns men är ovanlig i det svenska beståndet'],
 'skada': 'Parkeringsskador och lättare kollisioner i tätort. Bilen är bred nog att bli '
          'trång i äldre parkeringshus.',
 'varde': 'Stabil värdeminskning utan de branta fall som drabbar större premiummodeller.',
 'niva': 'Helförsäkring till omkring åtta år, därefter räkna på marknadsvärdet.',
 'fraga': ('Vad kostar det att försäkra en Hyundai Tucson?',
           'Volymklassens spann, alltså omkring 280–400 kr i månaden för halvförsäkring. '
           'Laddhybriden ligger högre eftersom ersättningsvärdet är större.'),
},
{
 'slug': 'ioniq-5', 'namn': 'IONIQ 5', 'typ': 'eldriven SUV', 'ar': '2021–',
 'drivlina': 'helt eldriven',
 'kort': 'Hyundais mest sålda elbil och den modell som etablerade märket i elbilsklassen.',
 'vinkel': 'IONIQ 5 använder 800-voltsteknik, vilket låter dyrt men i praktiken inte är '
           'det: plattformen E-GMP delas med Kia EV6 och EV9, och den kombinerade volymen '
           'har gjort delarna standardiserade. Verkstadsnätet med rätt behörighet har vuxit '
           'snabbt, och premien har följt med nedåt.',
 'punkter': ['Delar E-GMP-plattform med Kia EV6 och EV9',
             '800-voltsteknik kräver certifierad verkstad',
             'Den stora bakrutan gör glasmomentet tyngre än på en vanlig SUV'],
 'skada': 'Glasskador väger tungt, och de kvadratiska hjulhusskydden i plast tar ofta skada '
          'först vid kontakt med kantsten.',
 'varde': 'Har hållit värdet bättre än de flesta elbilar i klassen tack vare stark '
          'efterfrågan på begagnatmarknaden.',
 'niva': 'Helförsäkring så länge marknadsvärdet ligger över 150 000 kr.',
 'fraga': ('Är IONIQ 5 dyr att försäkra?',
           'Nej, den ligger i mitten av elbilsspannet. Den delade E-GMP-plattformen med Kia '
           'ger både delstillgång och ett växande verkstadsnät, vilket håller premien nere.'),
},
{
 'slug': 'ioniq-6', 'namn': 'IONIQ 6', 'typ': 'eldriven sedan', 'ar': '2023–',
 'drivlina': 'helt eldriven',
 'kort': 'Hyundais eldrivna sedan, byggd med aerodynamiken som utgångspunkt.',
 'vinkel': 'IONIQ 6 delar teknik med IONIQ 5 men har en helt annan kaross, och det är '
           'karossen som skiljer i försäkringen. Den låga, droppformade linjen ger stora '
           'sammanhängande ytor som blir dyra att laga, och markfrigången är låg nog att '
           'göra underredet utsatt vid farthinder.',
 'punkter': ['Delar drivlina med IONIQ 5 men har egen kaross',
             'Låg markfrigång gör underredet utsatt',
             'Stora karossektioner ger dyra plåtskador'],
 'skada': 'Underredesskador och skador på frontspoilern är vanligare än på IONIQ 5, av rent '
          'geometriska skäl.',
 'varde': 'Lägre efterfrågan än IONIQ 5 på begagnatmarknaden, vilket ger brantare '
          'värdeminskning.',
 'niva': 'Helförsäkring så länge bilen är värd över 150 000 kr.',
 'fraga': ('Är IONIQ 6 billigare att försäkra än IONIQ 5?',
           'Ofta något, eftersom sedanen är lättare och har lägre ersättningsvärde. '
           'Skillnaden är dock mindre än mellan två försäkringsbolag på samma bil.'),
},
{
 'slug': 'inster', 'namn': 'INSTER', 'typ': 'liten eldriven stadsbil', 'ar': '2025–',
 'drivlina': 'helt eldriven',
 'kort': 'Hyundais minsta elbil och ett av marknadens billigaste eldrivna alternativ.',
 'vinkel': 'INSTER är intressant ur försäkringssynpunkt just för att den är billig. Lågt '
           'ersättningsvärde gör vagnskadedelen billig, och låg vikt minskar skadan både på '
           'egen bil och på motparten. Det är den kombination som gör små bilar billiga att '
           'försäkra — och den gäller även när bilen är eldriven.',
 'punkter': ['Lägst ersättningsvärde bland elbilar på svenska marknaden',
             'Låg vikt ger mindre skador vid kollision',
             'Ny modell, så jämför brett medan bolagen kalibrerar sina priser'],
 'skada': 'Parkeringsskador och skador mot trottoarkanter, typiskt för en liten stadsbil.',
 'varde': 'Ingen etablerad andrahandsmarknad ännu, men det låga nypriset begränsar '
          'nedsidan.',
 'niva': 'Halvförsäkring så länge vagnskadegarantin gäller, därefter en räknesak.',
 'fraga': ('Är Hyundai INSTER billig att försäkra?',
           'Ja, för att vara elbil. Det låga ersättningsvärdet och den låga vikten drar båda '
           'premien nedåt, och det uppväger en del av det som annars gör elbilar dyrare.'),
},
{
 'slug': 'santa-fe', 'namn': 'Santa Fe', 'typ': 'stor SUV med sju säten', 'ar': '2024–',
 'drivlina': 'hybrid och laddhybrid',
 'kort': 'Hyundais största SUV och ett av få sjusitsiga alternativ i mellanprisklassen.',
 'vinkel': 'Santa Fe är Hyundais dyraste modell att försäkra, och det följer av storleken. '
           'Sju säten ger högre exponering för personskador, bilen används ofta med släp och '
           'ersättningsvärdet är högt. Det som håller emot är att modellen ligger under de '
           'tyska premiumalternativen i pris, vilket märks i vagnskadedelen.',
 'punkter': ['Sju säten ger högre exponering för personskador',
             'Ofta utrustad med dragkrok — släpet behöver egen försäkring',
             'Laddhybriden har högst ersättningsvärde i utbudet'],
 'skada': 'Backningsskador och skador vid trånga parkeringar dominerar. Bilen är nära fem '
          'meter lång.',
 'varde': 'Stark efterfrågan på sjusitsiga bilar håller uppe andrahandsvärdet.',
 'niva': 'Helförsäkring så länge bilen är värd över 150 000 kr.',
 'fraga': ('Behöver släpet egen försäkring när jag drar med Santa Fe?',
           'Ja, om du vill ha skador på själva släpet ersatta. Bilens trafikförsäkring '
           'täcker bara skador släpet orsakar på annan egendom.'),
},
{
 'slug': 'bayon', 'namn': 'Bayon', 'typ': 'liten SUV', 'ar': '2021–',
 'drivlina': 'bensin och mildhybrid',
 'kort': 'Hyundais minsta SUV, byggd på samma grund som i20.',
 'vinkel': 'Bayon visar samma mönster som Skoda Kamiq mot Scala: den delar allt av betydelse '
           'med i20 men klassas som SUV och får därför en något högre premie. Skillnaden '
           'bygger på skadestatistik för karossformen, inte på tekniska skillnader mellan '
           'bilarna.',
 'punkter': ['Delar plattform och delkatalog med i20',
             'SUV-klassningen ger något högre premie än halvkombin',
             'Populär som andrabil, vilket ger låga körsträckor'],
 'skada': 'Parkeringsskador och skador mot kantsten. Den högre markfrigången minskar risken '
          'för underredesskador jämfört med i20.',
 'varde': 'Bättre andrahandsvärde än i20, eftersom SUV-formatet efterfrågas mer.',
 'niva': 'Helförsäkring de första sex åren, därefter räkna på marknadsvärdet.',
 'fraga': ('Vad skiljer försäkringen på Bayon och i20?',
           'Mycket lite. Bilarna delar teknik och delar, så skillnaden ligger i klassningen '
           'och i ett något högre ersättningsvärde för Bayon.'),
},
{
 'slug': 'i20', 'namn': 'i20', 'typ': 'liten halvkombi', 'ar': '2020–',
 'drivlina': 'bensin och mildhybrid',
 'kort': 'Hyundais småbil och ett vanligt val som förstabil och andrabil.',
 'vinkel': 'i20 är en av de billigaste bilarna att försäkra i Sverige. Låg vikt, lågt '
           'ersättningsvärde och en femårsgaranti som följer bilen gör den attraktiv både '
           'som förstabil och som andrabil. Det som drar upp genomsnittspremien är '
           'förarprofilen — en stor del av beståndet körs av unga utan uppbyggd bonus.',
 'punkter': ['Låg vikt ger mindre skador vid kollision',
             'Femårsgaranti utan milbegränsning följer bilen vid ägarbyte',
             'N-versionen hamnar i en betydligt högre effektklass'],
 'skada': 'Parkeringsskador och skador mot trottoarkanter, typiskt för en liten stadsbil.',
 'varde': 'Låga men stabila värden, med garantin som stöd de första fem åren.',
 'niva': 'Halvförsäkring på de flesta exemplar över fem år. Helförsäkring på nyare bilar.',
 'fraga': ('Är Hyundai i20 ett bra val för en ung förare?',
           'Ja, det är ett av de vanligare valen. Låg vikt och lågt ersättningsvärde mildrar '
           'ungdomstillägget. N-versionen är däremot en helt annan sak — den hamnar i en '
           'effektklass som prissätts hårt.'),
},
{
 'slug': 'i10', 'namn': 'i10', 'typ': 'minibil', 'ar': '2020–',
 'drivlina': 'bensin',
 'kort': 'Hyundais minsta bil och en av de sista kvarvarande minibilarna på marknaden.',
 'vinkel': 'i10 är sannolikt den billigaste bilen att försäkra som säljs ny i Sverige. '
           'Ersättningsvärdet är lägst i utbudet, vikten är låg och skadorna bilen orsakar på '
           'motparten är begränsade av ren fysik. För en ung förare är det den kombination '
           'som betyder mest.',
 'punkter': ['Lägst ersättningsvärde av alla Hyundai-modeller',
             'Låg vikt begränsar skadan på både egen bil och motpart',
             'Segmentet krymper, vilket håller uppe andrahandsvärdet'],
 'skada': 'Parkeringsskador dominerar helt. Bilen används nästan uteslutande i tätort.',
 'varde': 'Håller värdet förvånansvärt väl eftersom utbudet av nya minibilar minskar.',
 'niva': 'Halvförsäkring på de flesta exemplar. Trafikförsäkring om bilen är värd mindre än '
         'självrisken plus några tusenlappar.',
 'fraga': ('Vilken är billigast att försäkra av Hyundais modeller?',
           'i10, med marginal. Lägst ersättningsvärde och lägst vikt i utbudet ger den lägsta '
           'premien, särskilt för unga förare.'),
},
{
 'slug': 'ioniq-9', 'namn': 'IONIQ 9', 'typ': 'stor eldriven SUV med sju säten', 'ar': '2025–',
 'drivlina': 'helt eldriven',
 'kort': 'Hyundais största elbil och märkets sjusitsiga flaggskepp.',
 'vinkel': 'IONIQ 9 är Hyundais dyraste bil att försäkra och den enda som regelbundet '
           'hamnar i premiumklassen. Sju säten, hög vikt och ett högt ersättningsvärde pekar '
           'åt samma håll. Fördelen är att bilen bygger på E-GMP, samma plattform som IONIQ 5 '
           'och Kia EV9, vilket betyder att verkstäderna redan kan tekniken.',
 'punkter': ['Beprövad E-GMP-plattform trots att modellen är ny',
             'Sju säten och hög vikt ger hög exponering',
             'Kan omfattas av krav på stöldskydd beroende på postnummer'],
 'skada': 'För ny för egen statistik. Räkna med IONIQ 5:s mönster men med fler '
          'backningsskador, eftersom bilen är betydligt längre.',
 'varde': 'Ingen etablerad andrahandsmarknad ännu.',
 'niva': 'Helförsäkring. Bilen är för ny och för värdefull för något annat.',
 'fraga': ('Vad kostar det att försäkra en Hyundai IONIQ 9?',
           'Den övre delen av elbilsspannet. Storlek, vikt och ersättningsvärde driver '
           'premien, men den beprövade plattformen gör att bolagen slipper lägga på ett '
           'osäkerhetspåslag för tekniken.'),
},
],
}
