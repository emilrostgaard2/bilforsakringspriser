# -*- coding: utf-8 -*-
"""Modelldata för Skoda.

Tio modeller: de åtta som finns i brands.py plus Elroq och Yeti. Elroq
är märkets nyaste elbil och saknades helt, Yeti finns inte längre att
köpa ny men rullar i tusental på svenska vägar och söks därefter.
"""

MODELLER_SKODA = {
'skoda': [
{
 'slug': 'octavia', 'namn': 'Octavia', 'typ': 'halvkombi och kombi', 'ar': '2020–',
 'drivlina': 'bensin, diesel, mildhybrid och laddhybrid',
 'kort': 'Skodas mest sålda modell och en av Sveriges vanligaste tjänstebilar.',
 'vinkel': 'Octavia är närmast en referenspunkt i försäkringssammanhang. Beståndet är stort, '
           'skadestatistiken välunderbyggd och delarna delas med hela Volkswagen-koncernen. '
           'Det gör att premien sällan innehåller något osäkerhetspåslag alls — bolagen vet '
           'exakt vad bilen kostar dem.',
 'punkter': ['Ett av Sveriges största bilbestånd ger säker skadestatistik',
             'Delar delkatalog med Volkswagen, Seat och Audi',
             'Combi-versionen har lägre skadefrekvens än halvkombin'],
 'skada': 'Glasskador dominerar. Octavia används mycket i pendling och tjänstekörning, och '
          'antalet motorvägsmil är det som avgör hur ofta rutan tar skada.',
 'varde': 'Stabilt andrahandsvärde tack vare stor efterfrågan på begagnatmarknaden, men '
          'brant kurva de första tre åren på grund av tjänstebilsvolymerna.',
 'niva': 'Helförsäkring till omkring åtta år, därefter är halvförsäkring värd att räkna på.',
 'fraga': ('Är Skoda Octavia billig att försäkra?',
           'Ja, i förhållande till sin storlek. Det stora beståndet, den delade '
           'delkatalogen med VW-koncernen och en ägarprofil med låg skadefrekvens drar alla '
           'åt samma håll.'),
},
{
 'slug': 'superb', 'namn': 'Superb', 'typ': 'stor kombi och sedan', 'ar': '2015–',
 'drivlina': 'bensin, diesel och laddhybrid',
 'kort': 'Skodas flaggskepp och en av marknadens rymligaste kombibilar.',
 'vinkel': 'Superb erbjuder utrymme i klass med en premiumbil till ett betydligt lägre '
           'nypris, och det är exakt den kombinationen som gör den billig att försäkra. '
           'Ersättningsvärdet ligger under vad storleken antyder, medan delarna kommer från '
           'samma katalog som Passat och Octavia.',
 'punkter': ['Premiumutrymme till volymprisklassens ersättningsvärde',
             'Laddhybriden iV har högre ersättningsvärde än dieselversionerna',
             'Stor andel tidigare tjänstebilar med hög körsträcka'],
 'skada': 'Skador vid backning och parkering är vanliga. Superb Combi är nära fem meter '
          'lång, och det märks i äldre parkeringshus och på trånga infarter.',
 'varde': 'Faller snabbt de första fyra åren och planar sedan ut, vilket gör begagnade '
          'exemplar prisvärda och helförsäkring mindre motiverad med åren.',
 'niva': 'Helförsäkring på exemplar under sju år. På en tio år gammal Superb är '
         'halvförsäkring nästan alltid rätt.',
 'fraga': ('Vad kostar det att försäkra en Skoda Superb?',
           'Mindre än storleken antyder. Premien följer ersättningsvärdet, och Superb ligger '
           'i volymklassen trots att utrymmet motsvarar en premiumbil.'),
},
{
 'slug': 'kodiaq', 'namn': 'Kodiaq', 'typ': 'stor SUV med sju säten', 'ar': '2017–',
 'drivlina': 'bensin, diesel och laddhybrid',
 'kort': 'Skodas största SUV och ett av få sjusitsiga alternativ i mellanprisklassen.',
 'vinkel': 'Kodiaq är den Skoda som oftast används som familjens enda bil, ofta med '
           'dragkrok och släp. Det ger höga körsträckor och en bredare exponering än '
           'märkets övriga modeller. Samtidigt är ersättningsvärdet lägre än hos de tyska '
           'konkurrenterna i samma storlek, vilket håller premien nere.',
 'punkter': ['Sju säten ger högre exponering för personskador',
             'Ofta utrustad med dragkrok — släpet behöver egen försäkring',
             'Fyrhjulsdriften innehåller komponenter som blir dyra vid påkörning bakifrån'],
 'skada': 'Viltolyckor väger tungt. Kodiaq används mycket på landsväg och i glesbygd, och '
          'djurkollisioner är den skada som oftast leder till ett större belopp.',
 'varde': 'Håller värdet väl i sin klass, delvis eftersom sjusitsiga alternativ är få.',
 'niva': 'Helförsäkring så länge bilen är värd över 150 000 kr, i praktiken upp till tio år.',
 'fraga': ('Behöver jag extra försäkring för släpet på min Kodiaq?',
           'Bilens trafikförsäkring täcker skador släpet orsakar på annan egendom, men inte '
           'skador på släpet självt. Vill du ha släpet ersatt behöver det egen försäkring.'),
},
{
 'slug': 'karoq', 'namn': 'Karoq', 'typ': 'kompakt SUV', 'ar': '2018–',
 'drivlina': 'bensin, diesel och mildhybrid',
 'kort': 'Skodas mellanstora SUV och märkets vanligaste val bland barnfamiljer.',
 'vinkel': 'Karoq sitter i den prisklass där svensk bilförsäkring är som billigast: '
           'tillräckligt stor för att vara praktisk, tillräckligt billig för att '
           'ersättningsvärdet ska vara måttligt, och byggd på en plattform som varenda '
           'verkstad känner. Få bilar ger så lite anledning till osäkerhetspåslag.',
 'punkter': ['MQB-plattformen delas med hela VW-koncernen',
             'Måttligt ersättningsvärde håller vagnskadedelen billig',
             'Fyrhjulsdrift finns men är ovanlig i beståndet'],
 'skada': 'Parkeringsskador och lättare kollisioner i stadstrafik dominerar. Bilen används '
          'mest i tätort och pendling.',
 'varde': 'Jämn och förutsägbar värdeminskning utan de branta fall som drabbar större '
          'modeller.',
 'niva': 'Helförsäkring till omkring åtta år. Står bilen i garage kan halvförsäkring bli '
         'aktuell tidigare.',
 'fraga': ('Är Skoda Karoq dyrare att försäkra än Octavia?',
           'Något, ja. SUV-formatet ger fler parkeringsskador och ett högre ersättningsvärde '
           'än en jämngammal Octavia med samma motor.'),
},
{
 'slug': 'fabia', 'namn': 'Fabia', 'typ': 'liten halvkombi', 'ar': '2015–',
 'drivlina': 'bensin',
 'kort': 'Skodas minsta bil och ett vanligt val som förstabil och andrabil.',
 'vinkel': 'Fabia är en av de billigaste bilarna att försäkra på den svenska marknaden. '
           'Låg vikt betyder mindre skada vid kollision, både på egen bil och på motparten, '
           'och det låga ersättningsvärdet gör vagnskadedelen billig. Det som kan dra upp '
           'premien är förarprofilen — en stor del av beståndet körs av unga utan bonus.',
 'punkter': ['Låg vikt ger mindre skador vid kollision',
             'Lågt ersättningsvärde gör vagnskadedelen billig',
             'Vanlig förstabil — förarens ålder påverkar mer än bilen'],
 'skada': 'Parkeringsskador och skador mot trottoarkanter är de vanligaste ärendena, '
          'typiskt för en liten bil som mest används i stad.',
 'varde': 'Låga men stabila värden. Skillnaden mellan ett välskött och ett slitet exemplar '
          'är större än mellan årsmodellerna.',
 'niva': 'Halvförsäkring på de flesta exemplar över fem år. Helförsäkring på nyare bilar '
         'eller om bilen står på gatan i en stad.',
 'fraga': ('Vad kostar försäkring till en Skoda Fabia för en ung förare?',
           'Betydligt mer än för en äldre förare, men mindre än på nästan någon annan bil. '
           'Fabia är ett av de vanligaste valen just därför — låg vikt och lågt '
           'ersättningsvärde mildrar ungdomstillägget.'),
},
{
 'slug': 'scala', 'namn': 'Scala', 'typ': 'halvkombi', 'ar': '2019–',
 'drivlina': 'bensin',
 'kort': 'Skodas halvkombi mellan Fabia och Octavia, byggd på samma plattform som Kamiq.',
 'vinkel': 'Scala är en av de mest förbisedda bilarna i klassen, och det märks i '
           'försäkringen på ett gynnsamt sätt: beståndet är litet nog att bilen sällan '
           'figurerar i stöldstatistiken, men tekniken är delad med hela VW-koncernen så '
           'delarna finns överallt. Kombinationen ger låg premie utan osäkerhetspåslag.',
 'punkter': ['Delar plattform och delkatalog med Kamiq och VW Polo',
             'Litet bestånd men ingen exotisk teknik',
             'Stor baklucka för klassen — glasmomentet väger något tyngre'],
 'skada': 'Glas- och parkeringsskador dominerar. Bilen används mest i pendling och tätort.',
 'varde': 'Måttlig värdeminskning, men lägre efterfrågan än Octavia på begagnatmarknaden.',
 'niva': 'Helförsäkring de första sex åren, därefter räkna på marknadsvärdet.',
 'fraga': ('Är Skoda Scala billigare att försäkra än Octavia?',
           'Oftast ja. Scala är mindre, lättare och har lägre ersättningsvärde, och alla tre '
           'faktorerna drar premien nedåt.'),
},
{
 'slug': 'kamiq', 'namn': 'Kamiq', 'typ': 'liten SUV', 'ar': '2019–',
 'drivlina': 'bensin',
 'kort': 'Skodas minsta SUV, i praktiken en Scala med högre markfrigång.',
 'vinkel': 'Kamiq visar tydligt hur karossformen påverkar premien. Den delar plattform, '
           'motorer och delkatalog med Scala, men klassas som SUV och får därmed en något '
           'högre premie — trots att bilarna är närmast identiska under plåten. Skillnaden '
           'är liten men den finns, och den beror på skadestatistik snarare än på teknik.',
 'punkter': ['Tekniskt nära identisk med Scala',
             'SUV-klassningen ger något högre premie än halvkombin',
             'Populär som andrabil, vilket ger låga körsträckor'],
 'skada': 'Skador mot trottoarkanter och i parkeringssituationer är vanligast. Den högre '
          'markfrigången minskar risken för underredesskador jämfört med Scala.',
 'varde': 'Starkare andrahandsvärde än Scala, eftersom SUV-formatet efterfrågas mer.',
 'niva': 'Helförsäkring de första sex till sju åren.',
 'fraga': ('Vad skiljer försäkringen på Kamiq och Scala?',
           'Mycket lite. Bilarna delar teknik och delar, så skillnaden ligger i klassningen '
           'och i ett något högre ersättningsvärde för Kamiq. I praktiken handlar det om '
           'några tior i månaden.'),
},
{
 'slug': 'enyaq', 'namn': 'Enyaq', 'typ': 'eldriven SUV', 'ar': '2021–',
 'drivlina': 'helt eldriven',
 'kort': 'Skodas första riktiga elbil och en av Sveriges mest sålda eldrivna SUV:ar.',
 'vinkel': 'Enyaq bygger på Volkswagens MEB-plattform, vilket gör den till en av de '
           'billigare elbilarna att försäkra i sin storleksklass. Delarna är '
           'standardiserade, verkstäderna med högvoltsbehörighet är många och '
           'skadestatistiken börjar bli riktigt bra. Det är kombinationen som gör skillnad — '
           'inte att bilen är eldriven.',
 'punkter': ['MEB-plattformen ger stort verkstadsnät och god delstillgång',
             'Coupé-versionen har större bakruta och dyrare glasmoment',
             'Kontrollera att batteriet omfattas av vagnskadedelen'],
 'skada': 'Glasskador väger tungt, särskilt på coupé-versionen. Kamerorna bakom vindrutan '
          'kräver kalibrering efter varje byte.',
 'varde': 'Följer elbilsmarknaden men med stabilare golv än nyare märken, tack vare stort '
          'bestånd.',
 'niva': 'Helförsäkring så länge marknadsvärdet ligger över 150 000 kr.',
 'fraga': ('Är Skoda Enyaq dyr att försäkra jämfört med andra elbilar?',
           'Nej, tvärtom. Den delade VW-plattformen ger både delstillgång och ett brett '
           'verkstadsnät, vilket är precis de två faktorer som annars driver upp '
           'elbilspremier.'),
},
{
 'slug': 'elroq', 'namn': 'Elroq', 'typ': 'kompakt eldriven SUV', 'ar': '2025–',
 'drivlina': 'helt eldriven',
 'kort': 'Skodas nyaste elbil och märkets mindre alternativ till Enyaq.',
 'vinkel': 'Elroq är ny på marknaden men bygger på samma MEB-teknik som Enyaq och VW ID.4, '
           'vilket betyder att bolagen inte behöver gissa. En ny modell på en beprövad '
           'plattform prissätts sällan med osäkerhetspåslag, och det är den viktigaste '
           'skillnaden mot nya elbilar från märken utan historik i Sverige.',
 'punkter': ['Beprövad MEB-plattform trots att modellen är ny',
             'Vagnskadegarantin täcker de första tre åren',
             'Mindre och lättare än Enyaq, vilket sänker premien'],
 'skada': 'För ny för egen skadestatistik. Räkna med samma mönster som Enyaq, med tyngdpunkt '
          'på glas- och parkeringsskador i tätort.',
 'varde': 'Ingen etablerad andrahandsmarknad ännu, men plattformens spridning talar för ett '
          'stabilare restvärde än hos nya märken.',
 'niva': 'Halvförsäkring så länge vagnskadegarantin gäller, därefter helförsäkring.',
 'fraga': ('Räcker halvförsäkring på en ny Skoda Elroq?',
           'Ja, så länge vagnskadegarantin gäller — normalt tre år från första '
           'registrering. Den täcker samma sak som vagnskadedelen. Sätt en påminnelse när '
           'garantin går ut.'),
},
{
 'slug': 'yeti', 'namn': 'Yeti', 'typ': 'kompakt SUV', 'ar': '2009–2017',
 'drivlina': 'bensin och diesel',
 'kort': 'Skodas första SUV, utgången ur nyproduktionen men fortfarande vanlig på vägarna.',
 'vinkel': 'Yeti är den Skoda där valet av skyddsnivå betyder mest. Marknadsvärdet ligger '
           'på nivåer där vagnskadedelen ofta kostar mer i premie under några år än den '
           'någonsin kan betala ut, samtidigt som delarna är billiga och verkstäderna många. '
           'Det gör halvförsäkring till rätt val på de flesta exemplar.',
 'punkter': ['Marknadsvärdet gör halvförsäkring rätt för de flesta exemplar',
             'Utmärkt delstillgång via VW-koncernen',
             'Maskinskademomentet har oftast upphört på grund av ålder'],
 'skada': 'Slitagerelaterade fel dominerar verkstadsbesöken, men de ersätts inte av någon '
          'nivå — förslitning är inte skada. Av försäkringsskadorna är parkeringsskador '
          'vanligast.',
 'varde': 'Låga och stabila värden. Fyrhjulsdrivna exemplar håller värdet bäst.',
 'niva': 'Halvförsäkring på i princip alla exemplar. Trafikförsäkring om bilen är värd '
         'mindre än självrisken plus några tusenlappar.',
 'fraga': ('Lönar sig helförsäkring på en Skoda Yeti?',
           'Sällan. Vagnskadedelen ersätter marknadsvärdet minus självrisken, och på en Yeti '
           'är det utrymmet litet. Halvförsäkring behåller stöld, brand, glas och räddning '
           'till en betydligt lägre premie.'),
},
],
}
