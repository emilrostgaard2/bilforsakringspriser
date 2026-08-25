# -*- coding: utf-8 -*-
"""Modelldata för Volkswagen.

Elva modeller: de åtta som redan låg i brands.py plus ID.7, ID. Buzz och
Tayron. Tayron ersatte Tiguan Allspace i utbudet 2025 och saknades helt,
ID.7 är märkets stora eldrivna kombi och ID. Buzz det enda eldrivna
alternativet i sitt format på svenska marknaden.
"""

MODELLER_VW = {
'volkswagen': [
{
 'slug': 'golf', 'namn': 'Golf', 'typ': 'halvkombi', 'ar': '2020–',
 'drivlina': 'bensin, diesel, mildhybrid och laddhybrid',
 'kort': 'Europas mest sålda bil genom tiderna och referenspunkten i kompaktklassen.',
 'vinkel': 'Golf är den bil svenska försäkringsbolag har allra mest data på. Beståndet är '
           'enormt, skadestatistiken finns i decennier bakåt och varenda verkstad i landet '
           'kan bilen. Det gör att premien innehåller noll osäkerhetspåslag — men också att '
           'GTI- och R-versionerna prissätts hårt, eftersom statistiken för starka '
           'kompaktbilar är lika välbelagd.',
 'punkter': ['Marknadens mest väldokumenterade skadestatistik',
             'GTI och R hamnar i en betydligt högre effektklass',
             'Reservdelar finns nya, begagnade och i eftermarknad'],
 'skada': 'Parkeringsskador och lättare kollisioner i tätort dominerar. Golf används mer i '
          'stadstrafik än de flesta bilar i sin storlek.',
 'varde': 'Bland de stabilaste andrahandsvärdena i klassen, vilket gör att vagnskadedelen '
          'behåller sitt värde längre än på konkurrenterna.',
 'niva': 'Helförsäkring till omkring åtta år. På äldre exemplar är halvförsäkring värd att '
         'räkna på, särskilt om bilen står i garage.',
 'fraga': ('Är Volkswagen Golf dyr att försäkra?',
           'Nej, basversionerna ligger lågt tack vare det enorma beståndet och den goda '
           'delstillgången. GTI och R är en annan sak — effektklassen gör att premien kan '
           'bli avsevärt högre för samma kaross.'),
},
{
 'slug': 'passat', 'namn': 'Passat', 'typ': 'stor kombi', 'ar': '2015–',
 'drivlina': 'bensin, diesel och laddhybrid',
 'kort': 'Sveriges klassiska tjänstebil och en av de vanligaste kombibilarna på vägarna.',
 'vinkel': 'Passat har i decennier varit tjänstebilen framför andra, och det präglar '
           'beståndet: höga körsträckor de första tre åren, sedan en övergång till '
           'privatägande där bilen körs en tredjedel så mycket. Att ange sin egen körsträcka '
           'i stället för bilens historik är därför den enskilt största besparingen en '
           'begagnad Passat-ägare kan göra.',
 'punkter': ['Stor andel tidigare tjänstebilar med hög körsträcka',
             'Laddhybriden GTE har högre ersättningsvärde än dieselversionerna',
             'Delar delkatalog med Skoda Superb och Audi A4'],
 'skada': 'Viltolyckor och skador vid backning väger tyngst. Passat körs mycket på landsväg '
          'och är lång nog att bli otymplig i äldre parkeringsgarage.',
 'varde': 'Brant värdeminskning de första fyra åren, därefter platå. Det gör begagnade '
          'exemplar prisvärda men flyttar gränsen för helförsäkring nedåt i ålder.',
 'niva': 'Helförsäkring på exemplar under sju år. På en tio år gammal Passat är '
         'halvförsäkring nästan alltid rätt.',
 'fraga': ('Vad kostar det att försäkra en begagnad Passat?',
           'Mindre än nypriset antyder. Premien följer marknadsvärdet, och Passat tappar '
           'kraftigt i värde de första åren. En sex år gammal Passat kostar ofta mindre att '
           'försäkra än en ny bil i en mindre klass.'),
},
{
 'slug': 'tiguan', 'namn': 'Tiguan', 'typ': 'mellanstor SUV', 'ar': '2016–',
 'drivlina': 'bensin, diesel, mildhybrid och laddhybrid',
 'kort': 'Volkswagens mest sålda SUV och en av Europas vanligaste familjebilar.',
 'vinkel': 'Tiguan är SUV-versionen av allt som gör Golf billig att försäkra: samma '
           'plattform, samma delkatalog, samma verkstadsnät. Skillnaden ligger i formatet — '
           'högre, bredare och tyngre ger fler parkeringsskador och ett högre '
           'ersättningsvärde. Fyrhjulsdriften 4Motion lägger till komponenter som blir dyra '
           'vid vissa skadetyper.',
 'punkter': ['MQB-plattformen delas med Golf, Skoda Karoq och Seat Ateca',
             '4Motion innehåller delar som blir dyra vid påkörning bakifrån',
             'Laddhybriden eHybrid har högre ersättningsvärde'],
 'skada': 'Parkeringsskador dominerar. Tiguan är bred nog att bli trång i garage byggda för '
          'en annan tid, och de flesta ärenden gäller repor och stötfångarskador.',
 'varde': 'Håller värdet väl tack vare stark efterfrågan på begagnatmarknaden.',
 'niva': 'Helförsäkring till omkring åtta år, därefter räkna på marknadsvärdet.',
 'fraga': ('Är Tiguan dyrare att försäkra än Golf?',
           'Ja, något. Bilarna delar teknik men Tiguan är större, tyngre och har högre '
           'ersättningsvärde. SUV-formatet ger dessutom fler parkeringsskador i statistiken.'),
},
{
 'slug': 'polo', 'namn': 'Polo', 'typ': 'liten halvkombi', 'ar': '2018–',
 'drivlina': 'bensin',
 'kort': 'Volkswagens minsta modell och ett av de vanligaste valen som förstabil.',
 'vinkel': 'Polo hör till de billigaste bilarna att försäkra i Sverige. Låg vikt betyder '
           'mindre skada både på egen bil och på motparten, ersättningsvärdet är lågt och '
           'delarna delas med Skoda Fabia och Seat Ibiza. Det som drar upp genomsnittet är '
           'förarprofilen — en stor del av beståndet körs av unga utan uppbyggd bonus.',
 'punkter': ['Låg vikt ger mindre skador vid kollision',
             'Delar plattform med Skoda Fabia och Seat Ibiza',
             'GTI-versionen hamnar i en helt annan effektklass'],
 'skada': 'Skador mot trottoarkanter och i parkeringssituationer är vanligast, typiskt för '
          'en liten bil som mest används i stad.',
 'varde': 'Låga men mycket stabila värden — Polo är en av få småbilar som behåller ett '
          'reellt andrahandsvärde långt upp i ålder.',
 'niva': 'Halvförsäkring på de flesta exemplar över fem år. Helförsäkring om bilen är nyare '
         'eller står på gatan i en stad.',
 'fraga': ('Vad kostar försäkring till en Polo för en ung förare?',
           'Mer än för en äldre förare, men mindre än på nästan någon annan bil. Låg vikt '
           'och lågt ersättningsvärde mildrar ungdomstillägget, vilket är skälet till att '
           'Polo är ett så vanligt val som förstabil.'),
},
{
 'slug': 'id4', 'namn': 'ID.4', 'typ': 'eldriven SUV', 'ar': '2021–',
 'drivlina': 'helt eldriven',
 'kort': 'Volkswagens mest sålda elbil och grunden för hela MEB-familjen.',
 'vinkel': 'ID.4 är den elbil som gjorde MEB-plattformen till standard i Europa, och det är '
           'precis därför den är billig att försäkra. Delarna är standardiserade, '
           'verkstäderna med högvoltsbehörighet är många och skadestatistiken börjar bli '
           'riktigt bra. Elbil betyder inte automatiskt dyr premie — det beror på hur många '
           'som kan laga bilen.',
 'punkter': ['MEB-plattformen ger ett av marknadens bredaste elbilsverkstadsnät',
             'GTX-versionen har tvåmotorsdrift och högre effektklass',
             'Kontrollera att batteriet omfattas av vagnskadedelen'],
 'skada': 'Glasskador väger tungt. Vindrutan är stor och lutande med kameror bakom sig, '
          'vilket innebär kalibrering efter varje byte.',
 'varde': 'Stabilare restvärde än de flesta elbilar tack vare beståndets storlek.',
 'niva': 'Helförsäkring så länge marknadsvärdet ligger över 150 000 kr.',
 'fraga': ('Är Volkswagen ID.4 dyr att försäkra?',
           'Nej, jämfört med andra elbilar i samma storlek ligger den lågt. Den delade '
           'MEB-plattformen ger både delstillgång och ett brett verkstadsnät, vilket är de '
           'två faktorer som annars driver upp elbilspremier.'),
},
{
 'slug': 'id3', 'namn': 'ID.3', 'typ': 'eldriven halvkombi', 'ar': '2020–',
 'drivlina': 'helt eldriven',
 'kort': 'Volkswagens eldrivna svar på Golf och märkets första MEB-modell.',
 'vinkel': 'ID.3 är den billigaste elbilen att försäkra i Volkswagens utbud, och en av de '
           'billigare på marknaden överhuvudtaget. Den är mindre och lättare än ID.4, har '
           'lägre ersättningsvärde och delar hela sin teknik med Cupra Born och Skoda Elroq. '
           'Verkstadsnätet är därmed betydligt bredare än beståndets storlek antyder.',
 'punkter': ['Lägst ersättningsvärde av Volkswagens elbilar',
             'Delar teknik med Cupra Born och Skoda Elroq',
             'Mindre glasytor än ID.4 gör glasmomentet lättare'],
 'skada': 'Parkeringsskador dominerar. ID.3 används mest som stadsbil och pendlare, med '
          'korta körsträckor och hemmaladdning.',
 'varde': 'Har haft en skakig värdekurva men stabiliserats de senaste åren i takt med att '
          'begagnatmarknaden mognat.',
 'niva': 'Helförsäkring så länge bilen är värd över 150 000 kr, därefter en räknesak.',
 'fraga': ('Är ID.3 billigare att försäkra än Golf?',
           'Inte nödvändigtvis. ID.3 har högre ersättningsvärde än en jämngammal Golf, medan '
           'Golf har fler verkstäder. I praktiken ligger de nära varandra, och skillnaden '
           'mellan bolagen är större än skillnaden mellan bilarna.'),
},
{
 'slug': 'id7', 'namn': 'ID.7', 'typ': 'stor eldriven kombi och sedan', 'ar': '2024–',
 'drivlina': 'helt eldriven',
 'kort': 'Volkswagens största elbil och den eldrivna efterträdaren till Passat.',
 'vinkel': 'ID.7 har tagit över Passats roll som tjänstebil, och det formar hela '
           'försäkringsbilden. Höga körsträckor de första åren, hög utrustningsnivå och ett '
           'ersättningsvärde som ligger över allt annat i MEB-familjen. Samtidigt är '
           'tekniken bekant för verkstäderna, vilket gör att premien inte innehåller det '
           'osäkerhetspåslag som drabbar nya elbilar från nya märken.',
 'punkter': ['Högst ersättningsvärde bland Volkswagens elbilar',
             'Tourer-versionen har stor bakruta och tyngre glasmoment',
             'Stor andel tjänstebilar med höga körsträckor'],
 'skada': 'Glas- och sensorrelaterade ärenden dominerar. Bilen har ett omfattande '
          'assistanspaket som kräver kalibrering efter även måttliga frontskador.',
 'varde': 'Snabb värdeminskning de första åren, som på de flesta stora tjänstebilar.',
 'niva': 'Helförsäkring. Bilen är för ny och för värdefull för att något annat ska vara '
         'aktuellt.',
 'fraga': ('Vad kostar det att försäkra en Volkswagen ID.7?',
           'Mer än ID.4 och ID.3, eftersom ersättningsvärdet är högre. Räkna med den övre '
           'delen av elbilsspannet. Är bilen en före detta tjänstebil ska du ange din egen '
           'körsträcka, inte bilens historik.'),
},
{
 'slug': 'id-buzz', 'namn': 'ID. Buzz', 'typ': 'eldriven minibuss', 'ar': '2023–',
 'drivlina': 'helt eldriven',
 'kort': 'Den eldrivna efterföljaren till Transporter och märkets mest särpräglade modell.',
 'vinkel': 'ID. Buzz är svår att jämföra med något annat, och det märks i premien. Bilen är '
           'hög, bred och tung, den kan registreras som både personbil och lätt lastbil, och '
           'de två registreringarna ger helt olika villkor. Kontrollera vilken din bil har '
           'innan du begär offert — en personbilsförsäkring på ett fordon registrerat som '
           'lätt lastbil är fel produkt.',
 'punkter': ['Kan vara registrerad som personbil eller lätt lastbil',
             'Höjden gör den utesluten från många parkeringsgarage',
             'De elektriska skjutdörrarna är en egen reparationspost'],
 'skada': 'Skador på skjutdörrarnas mekanik och på taket är modellspecifika. Höjden gör att '
          'bommar och garageinfarter blir en verklig risk.',
 'varde': 'Starkt restvärde hittills, delvis eftersom modellen saknar direkta konkurrenter.',
 'niva': 'Helförsäkring. Bilen är dyr att ersätta och skadebilden bred.',
 'fraga': ('Ska ID. Buzz försäkras som personbil eller lätt lastbil?',
           'Det avgörs av hur fordonet är registrerat hos Transportstyrelsen, inte av hur du '
           'använder det. Kontrollera registreringsbeviset innan du tecknar — fel produkt kan '
           'innebära att ersättningen sätts ned.'),
},
{
 'slug': 'tayron', 'namn': 'Tayron', 'typ': 'stor SUV med sju säten', 'ar': '2025–',
 'drivlina': 'bensin, mildhybrid och laddhybrid',
 'kort': 'Volkswagens sjusitsiga SUV som ersatte Tiguan Allspace i utbudet.',
 'vinkel': 'Tayron är ny som namn men inte som bil — den bygger på samma MQB-teknik som '
           'Tiguan och delar delkatalog med hela koncernen. Det betyder att bolagen har '
           'underlag från dag ett, och att en ny modellbeteckning inte kostar dig något i '
           'osäkerhetspåslag. Namnbytet kan däremot skapa förvirring i offertformulär, så '
           'utgå från registreringsnumret.',
 'punkter': ['Ersatte Tiguan Allspace — kan förekomma under båda namnen',
             'Sju säten ger högre exponering för personskador',
             'Beprövad MQB-teknik trots ny modellbeteckning'],
 'skada': 'För ny för egen statistik. Räkna med Tiguans mönster men med fler '
          'backningsskador, eftersom bilen är längre.',
 'varde': 'Ingen etablerad andrahandsmarknad ännu.',
 'niva': 'Halvförsäkring så länge vagnskadegarantin gäller, därefter helförsäkring.',
 'fraga': ('Är Tayron samma bil som Tiguan Allspace?',
           'I praktiken ja — Tayron ersatte Tiguan Allspace och bygger på samma plattform i '
           'sjusitsigt utförande. Vid tecknandet är det säkrast att utgå från '
           'registreringsnumret så att offerten hamnar rätt.'),
},
{
 'slug': 't-roc', 'namn': 'T-Roc', 'typ': 'kompakt SUV', 'ar': '2018–',
 'drivlina': 'bensin, diesel och mildhybrid',
 'kort': 'Volkswagens kompakta SUV och märkets vanligaste val bland yngre köpare.',
 'vinkel': 'T-Roc har en yngre ägarprofil än Volkswagens övriga modeller, och det är den '
           'faktorn som styr premien mer än bilen själv. Tekniskt är den en Golf på högre '
           'ben, med samma delar och samma verkstäder. R-versionen är undantaget: den ligger '
           'i en effektklass där flera bolag kräver förhöjd självrisk.',
 'punkter': ['Yngre ägarprofil än övriga Volkswagen-modeller',
             'Delar teknik och delkatalog med Golf',
             'R-versionen hamnar i en betydligt högre effektklass'],
 'skada': 'Parkeringsskador och skador mot trottoarkanter dominerar. Bilen används mest i '
          'tätort.',
 'varde': 'Stark efterfrågan på begagnatmarknaden ger stabilt värde.',
 'niva': 'Helförsäkring de första sju åren, därefter räkna på marknadsvärdet.',
 'fraga': ('Varför är T-Roc dyrare att försäkra än Golf?',
           'Främst för att ägarprofilen är yngre. Bilarna delar teknik, men förarens ålder '
           'väger tyngre i premieberäkningen än skillnaden mellan halvkombi och kompakt SUV.'),
},
{
 'slug': 'touran', 'namn': 'Touran', 'typ': 'sjusitsig familjebuss', 'ar': '2015–',
 'drivlina': 'bensin och diesel',
 'kort': 'Volkswagens praktiska sjusitsiga familjebil i ett format som blivit ovanligt.',
 'vinkel': 'Touran tillhör en utdöende kategori — MPV:n har förlorat mot SUV:en — och det '
           'är faktiskt en fördel för premien. Bilen är låg, lätt och undanskymd i '
           'stöldstatistiken, samtidigt som delarna delas med Golf och Passat. Sju säten till '
           'en kompaktbils försäkringskostnad är svårt att hitta någon annanstans.',
 'punkter': ['Låg och lätt jämfört med sjusitsiga SUV:ar',
             'Sällsynt i stöldstatistiken',
             'Delar delkatalog med Golf och Passat'],
 'skada': 'Parkeringsskador och lättare kollisioner. Bilens låga höjd gör den lättare att '
          'manövrera än en SUV i samma längd.',
 'varde': 'Sjunkande värden i takt med att efterfrågan på formatet minskar, vilket flyttar '
          'gränsen för helförsäkring nedåt i ålder.',
 'niva': 'Helförsäkring till omkring sex år, därefter är halvförsäkring ofta rimligare.',
 'fraga': ('Är Touran billigare att försäkra än en sjusitsig SUV?',
           'Oftast ja. Touran är lägre, lättare och har lägre ersättningsvärde än en Tayron '
           'eller Kodiaq, och alla tre faktorerna drar premien nedåt.'),
},
],
}
