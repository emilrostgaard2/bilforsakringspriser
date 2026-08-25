# -*- coding: utf-8 -*-
"""Modelldata för Peugeot.

Tio modeller: de sju personbilar som redan låg i brands.py plus 408,
Rifter och Traveller. Partner är i första hand ett lätt lastfordon och
har flyttats till förmån för Rifter, som är personbilsversionen av
samma grund — skillnaden spelar roll försäkringsmässigt, eftersom
registreringen avgör vilken produkt som ska tecknas.

e-208 har egen sida trots att karossen delas med 208. Det är inte
dubblering: söktrycket ligger på båda namnen, och försäkringsfrågorna
skiljer sig genuint — batteriets värde, verkstadskravet och
laddkabelns status finns inte alls på bensinversionen.
"""

MODELLER_PEUGEOT = {
'peugeot': [
{
 'slug': '208', 'namn': '208', 'typ': 'liten halvkombi', 'ar': '2019–',
 'drivlina': 'bensin och mildhybrid',
 'kort': 'Peugeots mest sålda modell och en av Europas vanligaste småbilar.',
 'vinkel': 'Peugeot 208 hör till de billigaste bilarna att försäkra i Sverige. Låg vikt, '
           'lågt ersättningsvärde och en delkatalog som delas med hela Stellantis-koncernen '
           'drar alla åt samma håll. Det som höjer genomsnittspremien är förarprofilen — 208 '
           'är en vanlig förstabil, och beståndet innehåller många unga utan uppbyggd bonus.',
 'punkter': ['Delar CMP-plattform med Opel Corsa och Citroën C3',
             'Låg vikt begränsar skadan på både egen bil och motpart',
             'GT-utrustningen ger större fälgar som är dyrare att ersätta'],
 'skada': 'Skador mot trottoarkanter och i parkeringssituationer dominerar. Bilen används '
          'nästan uteslutande i tätort.',
 'varde': 'Låga men stabila värden. i-Cockpit-interiören och utrustningsnivån påverkar '
          'andrahandspriset mer än årsmodellen.',
 'niva': 'Halvförsäkring på de flesta exemplar över fem år. Helförsäkring på nyare bilar '
         'eller om bilen står på gatan i en stad.',
 'fraga': ('Är Peugeot 208 billig att försäkra?',
           'Ja, den ligger bland de billigare i Sverige. Låg vikt och lågt ersättningsvärde '
           'gör vagnskadedelen billig, och Stellantis-delarna finns hos de flesta '
           'verkstäder.'),
},
{
 'slug': 'e-208', 'namn': 'e-208', 'typ': 'liten eldriven halvkombi', 'ar': '2020–',
 'drivlina': 'helt eldriven',
 'kort': 'Den eldrivna 208 och en av de billigaste elbilarna på svenska begagnatmarknaden.',
 'vinkel': 'e-208 delar kaross och delkatalog med bensinversionen, vilket gör plåtskador '
           'lika billiga att laga. Skillnaden ligger i drivlinan: batteriet utgör en stor del '
           'av ersättningsvärdet, och arbete på högvoltssystemet kräver certifierad verkstad. '
           'Det är den skillnaden du betalar för, inte bilens storlek.',
 'punkter': ['Samma kaross och plåtdelar som bensindrivna 208',
             'Batteriet utgör en betydande del av ersättningsvärdet',
             'Kontrollera hur laddkabeln behandlas i villkoren'],
 'skada': 'Samma skadebild som 208 i övrigt, med den skillnaden att arbete nära '
          'högvoltssystemet kräver certifierad verkstad och därmed längre transport.',
 'varde': 'Har fallit kraftigt på begagnatmarknaden, vilket gör exemplaren prisvärda att '
          'köpa och flyttar gränsen för helförsäkring nedåt i ålder.',
 'niva': 'Helförsäkring så länge marknadsvärdet ligger över 100 000 kr, därefter en '
         'räknesak.',
 'fraga': ('Är e-208 dyrare att försäkra än vanliga 208?',
           'Ja, trots att karossen är densamma. Batteriets värde och kravet på certifierad '
           'verkstad förklarar hela skillnaden — plåtskadorna kostar detsamma på båda.'),
},
{
 'slug': '2008', 'namn': '2008', 'typ': 'liten SUV', 'ar': '2020–',
 'drivlina': 'bensin, mildhybrid och helt eldriven',
 'kort': 'Peugeots kompakta SUV och märkets vanligaste val bland barnfamiljer.',
 'vinkel': '2008 är 208 på högre ben, och skillnaden i premie följer samma mönster som hos '
           'alla märken: SUV-klassningen ger ett påslag trots att tekniken är identisk. '
           'Skillnaden är liten men konsekvent, och den bygger på skadestatistik för '
           'karossformen snarare än på reparationskostnad.',
 'punkter': ['Tekniskt nära identisk med 208',
             'SUV-klassningen ger något högre premie än halvkombin',
             'e-2008 finns som eldriven variant med annan premiebild'],
 'skada': 'Parkeringsskador och skador mot kantsten. Den högre markfrigången minskar risken '
          'för underredesskador jämfört med 208.',
 'varde': 'Starkare andrahandsvärde än 208, eftersom SUV-formatet efterfrågas mer.',
 'niva': 'Helförsäkring de första sex åren, därefter räkna på marknadsvärdet.',
 'fraga': ('Vad skiljer försäkringen på 208 och 2008?',
           'Mycket lite tekniskt. Bilarna delar plattform och delar, så skillnaden ligger i '
           'klassningen och i ett något högre ersättningsvärde för 2008.'),
},
{
 'slug': '308', 'namn': '308', 'typ': 'halvkombi och kombi', 'ar': '2021–',
 'drivlina': 'bensin, diesel, mildhybrid och laddhybrid',
 'kort': 'Peugeots kompaktbil och märkets svar på Golf och Octavia.',
 'vinkel': '308 ligger mitt i volymklassen och prissätts därefter. Beståndet är stort nog '
           'för säker skadestatistik, och delarna delas med Opel Astra och DS 4 inom '
           'Stellantis. Laddhybriden är undantaget — den har både högre ersättningsvärde och '
           'en drivlina med fler dyra komponenter i samma bil.',
 'punkter': ['Delar EMP2-plattform med Opel Astra och DS 4',
             'SW-versionen har lägre skadefrekvens än halvkombin',
             'Laddhybriden har högre ersättningsvärde än mildhybriden'],
 'skada': 'Glasskador väger tungt. 308 används mycket i pendling, och motorvägsmilen är det '
          'som avgör hur ofta rutan tar skada.',
 'varde': 'Måttlig värdeminskning men lägre efterfrågan än Golf på begagnatmarknaden.',
 'niva': 'Helförsäkring till omkring sju år, därefter avgör marknadsvärdet.',
 'fraga': ('Är Peugeot 308 billigare att försäkra än VW Golf?',
           'Ofta ja, framför allt för att ersättningsvärdet är lägre. Delstillgången är god '
           'genom Stellantis, även om Golfs bestånd är större.'),
},
{
 'slug': '408', 'namn': '408', 'typ': 'crossover-fastback', 'ar': '2023–',
 'drivlina': 'bensin, mildhybrid och laddhybrid',
 'kort': 'Peugeots crossover mellan 308 och 3008, med sluttande taklinje.',
 'vinkel': '408 sitter i ett format som knappt existerar hos konkurrenterna, och det märks i '
           'prissättningen: flera bolag saknar en självklar modellprofil och klassar bilen '
           'någonstans mellan halvkombi och SUV. Det gör spridningen mellan offerter större '
           'än på 308, och det lönar sig att hämta fler än tre.',
 'punkter': ['Ovanligt format ger större spridning mellan bolagens priser',
             'Den sluttande taklinjen ger en stor bakruta',
             'Delar teknik med 308 och Opel Astra'],
 'skada': 'Glasmomentet väger tyngre än på 308 på grund av den stora bakrutan. I övrigt '
          'samma mönster som märkets kompaktbilar.',
 'varde': 'Litet bestånd och oklar segmentstillhörighet gör andrahandsvärdet svårare att '
          'förutsäga.',
 'niva': 'Helförsäkring de första sex åren.',
 'fraga': ('Hur klassas Peugeot 408 av försäkringsbolagen?',
           'Olika, och det är poängen. Formatet ligger mellan halvkombi och SUV, och bolagen '
           'placerar bilen olika. Begär offert hos flera — spridningen är större här än på '
           'mer konventionella modeller.'),
},
{
 'slug': '3008', 'namn': '3008', 'typ': 'mellanstor SUV', 'ar': '2016–',
 'drivlina': 'bensin, diesel, laddhybrid och helt eldriven',
 'kort': 'Peugeots mest sålda SUV och en av märkets viktigaste modeller i Sverige.',
 'vinkel': '3008 finns i två generationer med helt olika förutsättningar. Den äldre är en '
           'konventionell SUV på EMP2-plattformen med stort bestånd och låg premie. Den nya '
           'från 2024 bygger på STLA Medium och finns även som e-3008, vilket flyttar bilen '
           'till en annan premieklass. Kontrollera vilken generation offerten avser.',
 'punkter': ['Två generationer med olika plattform och premiebild',
             'e-3008 är eldriven och prissätts som elbil',
             'Laddhybriden har högre ersättningsvärde än bensinversionen'],
 'skada': 'Parkeringsskador dominerar. Bilen är bred nog att bli trång i äldre '
          'parkeringshus, och de flesta ärenden gäller stötfångare och fälgar.',
 'varde': 'Den äldre generationen har fallit stadigt, den nya har ännu ingen etablerad '
          'värdekurva.',
 'niva': 'Helförsäkring till omkring åtta år på den äldre generationen. Helförsäkring rakt '
         'av på den nya.',
 'fraga': ('Är e-3008 dyrare att försäkra än vanliga 3008?',
           'Ja. Batteriets värde och kravet på certifierad verkstad höjer premien, precis som '
           'på alla elbilar. Skillnaden är större än mellan två bensinmotorer i samma bil.'),
},
{
 'slug': '5008', 'namn': '5008', 'typ': 'stor SUV med sju säten', 'ar': '2017–',
 'drivlina': 'bensin, diesel, laddhybrid och helt eldriven',
 'kort': 'Peugeots sjusitsiga SUV och ett av de prisvärdare alternativen i formatet.',
 'vinkel': '5008 ger sju säten till en premie som ligger under de tyska och japanska '
           'alternativen, vilket är modellens starkaste argument. Sju passagerare betyder '
           'högre exponering för personskador, men ersättningsvärdet är måttligt och delarna '
           'kommer från Stellantis volymproduktion.',
 'punkter': ['Sju säten till volymklassens ersättningsvärde',
             'Ofta utrustad med dragkrok — släpet behöver egen försäkring',
             'e-5008 finns som eldriven variant i den nya generationen'],
 'skada': 'Backningsskador och skador vid trånga parkeringar. Bilen är nära fyra och en halv '
          'meter lång.',
 'varde': 'Stabil efterfrågan på sjusitsiga bilar håller uppe värdet bättre än på märkets '
          'mindre modeller.',
 'niva': 'Helförsäkring så länge bilen är värd över 120 000 kr.',
 'fraga': ('Behöver släpet egen försäkring när jag drar med 5008?',
           'Ja, om du vill ha skador på själva släpet ersatta. Bilens trafikförsäkring täcker '
           'bara skador släpet orsakar på annan egendom.'),
},
{
 'slug': '508', 'namn': '508', 'typ': 'stor sedan och kombi', 'ar': '2018–',
 'drivlina': 'bensin, diesel och laddhybrid',
 'kort': 'Peugeots flaggskepp och märkets alternativ till Passat och A4.',
 'vinkel': '508 är den Peugeot som tappar mest i värde, och det är faktiskt en fördel för '
           'premien på begagnade exemplar. En fyra år gammal 508 kostar ofta mindre att '
           'försäkra än en ny bil i en betydligt mindre klass, eftersom vagnskadedelen '
           'beräknas på marknadsvärdet och inte på vad bilen en gång kostade.',
 'punkter': ['Kraftig värdeminskning gör begagnade exemplar billiga att försäkra',
             'PSE-versionen hamnar i en betydligt högre effektklass',
             'SW-versionen har större bakruta och tyngre glasmoment'],
 'skada': 'Skador vid backning och i trånga utrymmen. Bilen är låg och lång, vilket gör '
          'frontspoilern utsatt vid branta infarter.',
 'varde': 'Den brantaste värdekurvan i Peugeots utbud, vilket flyttar gränsen för '
          'helförsäkring nedåt i ålder.',
 'niva': 'Helförsäkring på exemplar under fem år. Därefter blir halvförsäkring snabbt '
         'rimligare.',
 'fraga': ('Vad kostar det att försäkra en begagnad Peugeot 508?',
           'Mindre än nypriset antyder. Premien följer marknadsvärdet, och 508 tappar '
           'kraftigt i värde de första åren. Det gör begagnade exemplar ovanligt prisvärda '
           'att både köpa och försäkra.'),
},
{
 'slug': 'rifter', 'namn': 'Rifter', 'typ': 'personbilsregistrerad skåpbil', 'ar': '2018–',
 'drivlina': 'bensin, diesel och helt eldriven',
 'kort': 'Peugeots högtaksbil för familjer som behöver utrymme utan att köpa en SUV.',
 'vinkel': 'Rifter är personbilsversionen av Partner, och den skillnaden är avgörande '
           'försäkringsmässigt. Registreringen avgör vilken produkt du ska teckna: Rifter är '
           'personbil, Partner är lätt lastbil, och en personbilsförsäkring på ett fordon '
           'registrerat som lätt lastbil är fel produkt. Kontrollera registreringsbeviset '
           'först.',
 'punkter': ['Personbil, till skillnad från Partner som är lätt lastbil',
             'Skjutdörrarna är en egen reparationspost',
             'Höjden gör bilen utesluten från många parkeringsgarage'],
 'skada': 'Skador på skjutdörrarnas skenor och på taket är modellspecifika. Höjden gör '
          'bommar och garageinfarter till en verklig risk.',
 'varde': 'Låga värden och stabil efterfrågan från hantverkare och stora familjer.',
 'niva': 'Halvförsäkring på äldre exemplar, helförsäkring så länge värdet motiverar det.',
 'fraga': ('Ska Rifter försäkras som personbil eller lätt lastbil?',
           'Det avgörs av hur fordonet är registrerat hos Transportstyrelsen, inte av hur du '
           'använder det. Rifter är normalt personbil och Partner lätt lastbil, men '
           'kontrollera alltid registreringsbeviset innan du tecknar.'),
},
{
 'slug': 'traveller', 'namn': 'Traveller', 'typ': 'stor personbilsregistrerad buss', 'ar': '2016–',
 'drivlina': 'diesel och helt eldriven',
 'kort': 'Peugeots största personbil, med plats för upp till nio personer.',
 'vinkel': 'Traveller är stor nog att hamna i en egen kategori hos flera bolag, och det är '
           'den viktigaste frågan att reda ut innan du tecknar. Nio sittplatser innebär hög '
           'exponering för personskador, och används bilen yrkesmässigt gäller andra villkor '
           'helt. Ange användningen korrekt från början — yrkesmässig persontransport på en '
           'privatförsäkring kan ge nedsatt ersättning.',
 'punkter': ['Upp till nio sittplatser ger hög exponering för personskador',
             'Yrkesmässig persontransport kräver annan försäkring',
             'e-Traveller finns som eldriven variant'],
 'skada': 'Skjutdörrar, tak och bakre stötfångare. Bilens storlek gör den utsatt i trånga '
          'stadsmiljöer och i parkeringsgarage.',
 'varde': 'Stabil efterfrågan från taxi, färdtjänst och stora familjer håller uppe värdet.',
 'niva': 'Helförsäkring så länge värdet motiverar det, med kontroll av att användningen är '
         'korrekt angiven.',
 'fraga': ('Kan jag använda Traveller i verksamhet på en privatförsäkring?',
           'Nej. Yrkesmässig persontransport kräver rätt försäkring, och ersättningen kan '
           'sättas ned helt om användningen inte angetts. Ange den korrekta användningen '
           'redan när du tecknar.'),
},
],
}
