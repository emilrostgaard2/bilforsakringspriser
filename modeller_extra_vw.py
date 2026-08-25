# -*- coding: utf-8 -*-
"""Textavsnitt för Volkswagen-modellerna.

Fyra löptextavsnitt, två långsvar och en metaklausul per modell. Samma
struktur som övriga extrafiler.
"""

EXTRA_VW = {

'golf': {
 'meta': 'Europas mest sålda bil',
 'direktsvar':
  'Volkswagen Golf ligger lågt i premie för sin storleksklass. Beståndet är enormt, '
  'skadestatistiken sträcker sig decennier bakåt och delarna finns hos varje verkstad i '
  'landet. Räkna med volymklassens spann, 280–400 kr i månaden för halvförsäkring. GTI och R '
  'ligger betydligt högre på grund av effektklassen.',
 'agare':
  'Golf har den bredaste ägarprofilen av alla bilar på svenska vägar. Den är förstabil, '
  'tjänstebil, familjebil och pensionärsbil samtidigt, vilket gör genomsnittssiffror för '
  'modellen nästan meningslösa. Två personer med samma årsmodell kan betala dubbelt så mycket '
  'som varandra. Det som förenar beståndet är att bilen körs mycket i tätort — Golf är i '
  'praktiken Sveriges vanligaste stadsbil, och skadebilden följer därefter med '
  'parkeringsskador i topp.',
 'teknik':
  'Golf bygger på MQB-plattformen, den mest spridda i Europa. Delarna finns nya, begagnade '
  'och i eftermarknad, vilket är ovanligt och pressar reparationskostnaden rejält. Det som '
  'kostar på nyare årsmodeller är elektroniken: kameran bakom vindrutan styr autobroms och '
  'filhållning och kräver kalibrering efter rutbyte, och matrisstrålkastarna på högre '
  'utrustningsnivåer är dyra att ersätta. På en åtta år gammal Golf finns inget av det.',
 'jamfor':
  'Mot Skoda Octavia och Seat Leon, som delar teknik, ligger Golf något högre i premie — '
  'nypriset och därmed ersättningsvärdet är högre. Mot Volvo V40 och Toyota Corolla är '
  'skillnaden liten. Mot en jämnstor SUV som T-Roc ligger Golf lägre, både för att '
  'ägarprofilen är äldre och för att halvkombin drabbas av färre parkeringsskador.',
 'kostnad':
  'Golf är billig i varje post utom en: värdeminskningen på nya exemplar är brantare än på '
  'många konkurrenter, eftersom nypriset är högt i klassen. På begagnade exemplar vänder det '
  'helt — då är Golf en av marknadens mest ekonomiska bilar att äga, och försäkringen blir en '
  'av de större löpande posterna. Det är också där jämförelsen mellan bolag ger mest.',
 'lang': ('Hur mycket dyrare är Golf GTI att försäkra?',
  'Betydligt. Effektklassen är en av de tyngsta faktorerna för kompaktbilar, och flera bolag '
  'kräver dessutom förhöjd självrisk över ett visst effektuttag. Hämta offert på både GTI och '
  'en vanlig Golf innan du bestämmer dig för version.'),
 'lang2': ('Är en gammal Golf billig att försäkra?',
  'Ja, mycket. Lågt marknadsvärde gör vagnskadedelen billig, delarna är billiga och '
  'verkstäderna många. På exemplar över tio år är halvförsäkring nästan alltid det '
  'rationella valet.'),
},

'passat': {
 'meta': 'Sveriges klassiska tjänstebil',
 'direktsvar':
  'Volkswagen Passat kostar mindre att försäkra än nypriset antyder, eftersom premien följer '
  'marknadsvärdet och Passat tappar kraftigt i värde de första fyra åren. En begagnad Passat '
  'hamnar ofta i samma premieläge som en ny bil i en mindre klass.',
 'agare':
  'Passat har levt sitt liv i tjänstebilsflottor, och det präglar hela beståndet. De första '
  'tre åren rullar bilen 3 000 mil om året hos ett företag, därefter köps den av en '
  'privatperson som kör en tredjedel så mycket. Den vanligaste och dyraste missen är att '
  'utgå från bilens historik i annonsen när man fyller i offerten. Den privata ägarprofilen '
  'är däremot gynnsam: medelålder över fyrtio, hög andel villaparkering och lång skadefri '
  'historik.',
 'teknik':
  'Passat delar plattform och delkatalog med Skoda Superb och Audi A4, vilket ger både bra '
  'delstillgång och konkurrens mellan verkstäderna. Adaptiv underredesfjädring finns på en '
  'del exemplar och är värd att kontrollera mot maskinskademomentet — den är dyr att ersätta '
  'och undantas oftare än man tror. Kombiversionens baklucka är en av de dyraste enskilda '
  'delarna, och på GTE-versionen tillkommer ett batteripaket som höjer ersättningsvärdet.',
 'jamfor':
  'Mot Skoda Superb, som är samma bil under plåten, ligger Passat något högre i premie av '
  'ett enda skäl: nypriset. Mot Volvo V60 är skillnaden liten och beror mest på förarprofil. '
  'Mot en Audi A4 Avant ligger Passat tydligt lägre, trots delad teknik — ersättningsvärdet '
  'skiljer sig kraftigt.',
 'kostnad':
  'På en begagnad Passat är värdeminskningen redan tagen av förste ägaren, vilket gör bilen '
  'billig att äga. Bränslet dominerar kalkylen på dieselversionerna, medan försäkringen är '
  'måttlig. Den som fortfarande betalar en premie beräknad på tjänstebilens körsträcka '
  'betalar dock ofta tusenlappar för mycket varje år.',
 'lang': ('Vilken Passat är billigast att försäkra?',
  'Dieselversionerna med lägre effekt, i äldre årsmodeller. Laddhybriden GTE har högre '
  'ersättningsvärde och därmed högre premie. Skillnaden mellan motoralternativen är dock '
  'mindre än skillnaden mellan två försäkringsbolag på samma bil.'),
 'lang2': ('Hur mycket kan jag spara på att rätta körsträckan?',
  'Premien beräknas i intervall, så en justering från 2 000 till 1 200 mil kan flytta dig ett '
  'eller två steg nedåt. Ange aldrig lägre än du faktiskt kör — överskriden sträcka kan ge '
  'nedsatt ersättning vid skada.'),
},

'tiguan': {
 'meta': 'Volkswagens mest sålda SUV',
 'direktsvar':
  'Volkswagen Tiguan ligger något över Golf i premie men i samma volymklass. Bilarna delar '
  'plattform och delkatalog, men Tiguan är större, tyngre och har högre ersättningsvärde. '
  'Räkna med 280–400 kr i månaden för halvförsäkring och 450–650 kr för helförsäkring.',
 'agare':
  'Tiguan är barnfamiljens bil i Sverige, och ägarprofilen är den mest gynnsamma som finns: '
  'medelålder kring fyrtiofem, villa eller radhus, egen uppfart och körsträckor kring 1 500 '
  'mil om året. Bolagen har enorma datamängder på precis den profilen, vilket gör att '
  'spridningen mellan olika bolags offerter är mindre på Tiguan än på ovanligare modeller. '
  'Det betyder inte att jämförelse är onödig — när ingen kan gömma sig bakom osäkerhet '
  'konkurrerar bolagen i stället på pris.',
 'teknik':
  'Tiguan är en MQB-bil rakt igenom, med samma delar som Golf, Skoda Karoq och Seat Ateca. '
  '4Motion-versionerna har fyrhjulsdrift med kardanaxel och bakaxelkoppling, komponenter som '
  'blir kostsamma vid påkörning bakifrån och som helt saknas på framhjulsdrivna exemplar. '
  'Sensorpaketet i fronten är standard på nyare årsmodeller och innebär kalibrering efter '
  'även måttliga stötfångarskador.',
 'jamfor':
  'Mot Skoda Karoq och Seat Ateca, som är samma bil i annan kostym, ligger Tiguan högst i '
  'premie av de tre — nypriset avgör. Mot Volvo XC40 är skillnaden liten. Mot en Audi Q5 '
  'ligger Tiguan tydligt lägre, trots att bilarna delar mycket teknik.',
 'kostnad':
  'Tiguan är dyrare i drift än Golf men billigare än de flesta konkurrenter i sin klass. '
  'Bränsle och däck väger tyngre än premien i kalkylen, särskilt på 4Motion-versionerna där '
  'både förbrukning och däckslitage är högre. Försäkringen är däremot den post där du '
  'enklast kan påverka utfallet utan att ändra något annat.',
 'lang': ('Är 4Motion dyrare att försäkra?',
  'Något, ja. Fyrhjulsdriften innehåller komponenter som saknas på framhjulsdrivna versioner '
  'och som blir dyra vid vissa skadetyper. Skillnaden är liten men konsekvent, och den vägs '
  'delvis upp av att 4Motion håller värdet bättre.'),
 'lang2': ('Vilken skyddsnivå passar en fem år gammal Tiguan?',
  'Helförsäkring. Vid fem år ligger marknadsvärdet vanligen kvar en bra bit över 150 000 kr, '
  'vilket ger vagnskadedelen tillräckligt utrymme för att motivera premien.'),
},

'polo': {
 'meta': 'Volkswagens minsta modell',
 'direktsvar':
  'Volkswagen Polo hör till de billigaste bilarna att försäkra i Sverige. Låg vikt, lågt '
  'ersättningsvärde och delad teknik med Skoda Fabia och Seat Ibiza drar alla åt samma håll. '
  'Det som höjer genomsnittet är förarprofilen — Polo är en av landets vanligaste förstabilar.',
 'agare':
  'Polo delar Fabias problem med statistiken: samma bil körs av 18-åringen, barnfamiljen och '
  'pensionären, och de tre betalar helt olika premier. Publicerade genomsnitt för modellen '
  'dras upp av de yngsta förarna, vilket betyder att du som är över trettio med full bonus '
  'sannolikt får ett pris långt under det du läser om. Bilen används nästan uteslutande i '
  'tätort, med korta körsträckor och hög andel gatuparkering.',
 'teknik':
  'Polo bygger på MQB-A0, samma grund som Fabia och Ibiza. Tekniken är enkel i den meningen '
  'att det finns få dyra komponenter att förstöra, och delarna är billiga och lättillgängliga. '
  'Nyare årsmodeller har sensorpaket som kräver kalibrering efter frontskador, men i mindre '
  'omfattning än på större bilar. Den låga vikten är den mest underskattade fördelen — den '
  'minskar skadan både på egen bil och på motparten.',
 'jamfor':
  'Mot Skoda Fabia och Seat Ibiza ligger Polo något högre i premie, av samma skäl som gäller '
  'hela koncernen: högre nypris. Mot en Toyota Yaris är skillnaden liten. Mot en liten SUV i '
  'samma prisklass ligger Polo tydligt lägre — karossformen kostar mer än man tror i den här '
  'delen av marknaden.',
 'kostnad':
  'Polo är billig i alla poster, vilket gör försäkringen till en stor andel av totalen — för '
  'en ung förare kan premien överstiga bränslekostnaden. Det är också därför valet av '
  'skyddsnivå betyder så mycket: på ett exemplar värt 70 000 kr kostar vagnskadedelen mer '
  'under några år än den någonsin kan betala ut.',
 'lang': ('Är Polo eller Golf billigare att försäkra?',
  'Polo, tydligt. Bilen är mindre, lättare och har lägre ersättningsvärde. Skillnaden är '
  'störst för unga förare, där både vikt och värde påverkar ungdomstillägget.'),
 'lang2': ('Behöver jag helförsäkring på en Polo?',
  'På nyare exemplar ja, på äldre sällan. När marknadsvärdet passerar nedåt förbi omkring '
  '80 000 kr blir vagnskadedelen svår att motivera, om inte bilen står på gatan i en stad '
  'där parkeringsskador och skadegörelse är vanliga.'),
},

'id4': {
 'meta': 'Volkswagens mest sålda elbil',
 'direktsvar':
  'Volkswagen ID.4 hör till de billigare elbilarna att försäkra i sin storleksklass. '
  'MEB-plattformen ger standardiserade delar och ett av marknadens bredaste verkstadsnät med '
  'högvoltsbehörighet. Räkna med elbilsklassens spann, 310–440 kr i månaden för '
  'halvförsäkring.',
 'agare':
  'ID.4 började som tjänstebil och har blivit familjebil. Ägarprofilen liknar i dag Tiguans: '
  'fyrtio plus, villa, hemmaladdning och normala svenska körsträckor. Det är en av '
  'förklaringarna till att premien ligger lågt för att vara en elbil — bolagen har data både '
  'på bilen och på förarna. Har du laddbox på väggen hör den normalt till villa- eller '
  'hemförsäkringen, medan laddkabeln som följer bilen oftast omfattas av bilförsäkringen. '
  'Den gränsdragningen är den vanligaste källan till besvikelse vid en skada.',
 'teknik':
  'MEB-plattformen finns i hundratusentals exemplar i Europa, och det är hela poängen. '
  'Batteriet ligger i golvet som en strukturell del av bilen, vilket gör att hårda kontakter '
  'med farthinder eller trottoarkanter kan utlösa en undersökning av batteripaketet. '
  'Vindrutan är stor och lutande med kameror bakom sig, så kalibrering efter rutbyte är '
  'regel. GTX-versionen har tvåmotorsdrift och hamnar i en högre effektklass.',
 'jamfor':
  'Mot Skoda Enyaq, som är samma bil under plåten, ligger ID.4 något högre i premie tack vare '
  'nypriset. Mot Tesla Model Y har ID.4 en tydlig fördel i verkstadsval — reparationerna är '
  'konventionella. Mot nyare kinesiska elbilsmärken är skillnaden störst: där betalar man för '
  'tunn skadestatistik, här gör man inte det.',
 'kostnad':
  'ID.4 är billig att köra och måttlig att försäkra, vilket gör premien till en stor andel av '
  'driftkostnaden. Med hemmaladdning, minimal service och låg fordonsskatt är försäkringen '
  'ofta den största rörliga posten. Det gör jämförelsen mellan bolag mer lönsam här än på en '
  'bensinbil där bränslet dominerar.',
 'lang': ('Täcks batteriet i en ID.4 av försäkringen?',
  'Batteriet omfattas normalt av samma skydd som resten av bilen vid yttre skada, alltså av '
  'vagnskadedelen i en helförsäkring. Gradvis kapacitetsförlust räknas som slitage och '
  'hanteras av garantin i stället. Läs båda dokumenten.'),
 'lang2': ('Är ID.4 dyrare att försäkra än en Tiguan?',
  'Något, ja. Ersättningsvärdet är högre och antalet verkstäder med högvoltsbehörighet färre. '
  'Skillnaden är dock mindre än mellan två olika försäkringsbolag på samma bil.'),
},

'id3': {
 'meta': 'Volkswagens eldrivna Golf',
 'direktsvar':
  'Volkswagen ID.3 är den billigaste elbilen att försäkra i Volkswagens utbud. Den är mindre '
  'och lättare än ID.4, har lägre ersättningsvärde och delar hela sin teknik med Cupra Born '
  'och Skoda Elroq — vilket ger ett verkstadsnät långt bredare än beståndets storlek antyder.',
 'agare':
  'ID.3 köps av två grupper: yngre hushåll som gör sin första elbilsaffär och äldre som byter '
  'ned från en större bil. Den dubbla profilen gör genomsnittssiffror missvisande åt båda '
  'håll. Bilen används mest i stad och pendling, med korta körsträckor och laddning hemma, '
  'vilket i sig är gynnsamt för premien. Många exemplar går på privatleasing, och då kräver '
  'avtalet helförsäkring under hela perioden oavsett vad som vore rationellt.',
 'teknik':
  'ID.3 var den första MEB-bilen och är i dag den mest spridda i sin klass. Delarna är '
  'standardiserade och verkstäderna med rätt behörighet många. Glasytorna är mindre än på '
  'ID.4, vilket gör glasmomentet lättare — en detalj som betyder mer än man tror, eftersom '
  'glasskador är den vanligaste ersatta skadan på moderna bilar. Batteriet ligger i golvet '
  'och utgör en stor del av bilens värde.',
 'jamfor':
  'Mot Cupra Born, som är samma bil med sportigare avstämning, ligger ID.3 marginellt lägre. '
  'Mot Skoda Elroq är skillnaden liten. Mot en bensindriven Golf är bilden jämn: ID.3 har '
  'högre ersättningsvärde, Golf har fler verkstäder, och i praktiken hamnar de nära varandra.',
 'kostnad':
  'ID.3 är en av få elbilar där hela ägarkalkylen går ihop utan asterisker: låg '
  'energikostnad, låg fordonsskatt, måttlig värdeminskning på begagnade exemplar och en '
  'premie som inte sticker ut. Den enda posten som varit skakig är restvärdet, som föll '
  'kraftigt 2023 och sedan stabiliserats.',
 'lang': ('Vilken är billigast att försäkra av ID.3, Cupra Born och Skoda Elroq?',
  'De ligger mycket nära varandra eftersom de delar plattform, delar och verkstadsnät. '
  'Skillnaden avgörs av ersättningsvärdet, där Elroq oftast ligger lägst. Spridningen mellan '
  'försäkringsbolagen är större än mellan bilarna.'),
 'lang2': ('Behöver jag speciell försäkring för elbil?',
  'Nej, samma tre skyddsnivåer gäller. Det som skiljer är vad du bör kontrollera i villkoren: '
  'att batteriet omfattas av vagnskadedelen, hur laddkabeln behandlas och hur många '
  'hyrbilsdagar som ingår.'),
},

'id7': {
 'meta': 'Volkswagens största elbil',
 'direktsvar':
  'Volkswagen ID.7 ligger i den övre delen av elbilsspannet. Ersättningsvärdet är högst i hela '
  'MEB-familjen och utrustningsnivån hög, medan tekniken är bekant för verkstäderna. Är bilen '
  'en före detta tjänstebil ska du ange din egen körsträcka, inte bilens historik.',
 'agare':
  'ID.7 har tagit över Passats roll som tjänstebilen framför andra, och beståndet ser ut '
  'därefter: höga körsträckor de första tre åren, hög utrustningsnivå och sedan en övergång '
  'till privatägande. Det gör körsträckan till den vanligaste felkällan i offerten på just '
  'den här modellen. Ägarprofilen efter tjänstebilsperioden är gynnsam — medelålder över '
  'fyrtiofem och hög andel villaparkering — vilket ofta ger priser under vad publicerade '
  'modellsiffror antyder.',
 'teknik':
  'ID.7 bygger på MEB men i sitt största utförande, med större batteri och mer omfattande '
  'assistanspaket än övriga familjen. Sensorerna är den tekniska knäckpunkten: radar, kameror '
  'och ultraljud sitter samlade i fronten, och även en måttlig parkeringsskada kan utlösa '
  'kalibrering av hela paketet. Tourer-versionen har dessutom en stor bakruta som gör '
  'glasmomentet tyngre än på sedanen.',
 'jamfor':
  'Mot Tesla Model 3 och Model S ligger ID.7 mitt emellan i premie, med fördelen att '
  'reparationerna är konventionella och verkstadsvalet fritt på riktigt. Mot en bensindriven '
  'Passat ligger ID.7 tydligt högre, vilket följer av ersättningsvärdet. Mot Skoda Superb iV '
  'är avståndet ännu större.',
 'kostnad':
  'Som ny bil domineras kalkylen av värdeminskning, och ID.7 följer tjänstebilsmönstret med '
  'en brant kurva de första åren. Det gör begagnade exemplar prisvärda att köpa och relativt '
  'dyra att försäkra i förhållande till inköpspriset — samma fenomen som drabbar alla före '
  'detta tjänstebilar i premiumsegmentet.',
 'lang': ('Är ID.7 dyrare att försäkra än ID.4?',
  'Ja, tydligt. Ersättningsvärdet är högre, bilen är större och utrustningsnivån mer '
  'omfattande. Räkna med den övre delen av elbilsspannet snarare än mitten.'),
 'lang2': ('Vad ska jag tänka på när jag köper en begagnad ID.7 från en företagsflotta?',
  'Ange din egen körsträcka, inte bilens tidigare. Kontrollera att offerten utgår från rätt '
  'utrustningsnivå, eftersom den styr ersättningsvärdet. Och passa på att jämföra bolag — '
  'vid ägarbyte får du byta utan att vänta på huvudförfallodagen.'),
},

'id-buzz': {
 'meta': 'eldriven minibuss utan direkt konkurrent',
 'direktsvar':
  'Volkswagen ID. Buzz är svår att prissätta eftersom den saknar direkta konkurrenter. Den '
  'avgörande frågan är registreringen: bilen finns som både personbil och lätt lastbil, och '
  'de två ger helt olika villkor och premie. Kontrollera registreringsbeviset innan du begär '
  'offert.',
 'agare':
  'ID. Buzz köps av två helt olika grupper — barnfamiljer som behöver plats och företag som '
  'behöver transportutrymme. Registreringen skiljer dem åt, och det är därför den frågan '
  'kommer först. För privatägda exemplar är profilen gynnsam: bilen används mest på helger '
  'och semestrar, körsträckorna är måttliga och den står nästan alltid på en egen uppfart, '
  'eftersom höjden gör de flesta parkeringsgarage omöjliga. Just höjden är också en risk — '
  'bommar och garageinfarter står för en påfallande andel av skadorna.',
 'teknik':
  'Under plåten är ID. Buzz en MEB-bil, vilket betyder att drivlinan är densamma som i ID.4 '
  'och verkstadsnätet därmed brett. Det modellspecifika ligger i karossen: de elektriska '
  'skjutdörrarna har skenor, motorer och sensorer längs hela sidan, och skador på dem är '
  'både vanliga och dyra. Den stora, plana fronten gör dessutom att en kollision fördelar '
  'kraften över en yta som är dyr att återställa.',
 'jamfor':
  'Det finns knappt något att jämföra med på svenska marknaden. XPeng X9 är det närmaste, och '
  'där har Volkswagen en avgörande fördel i verkstadsnät och etablerad modelldata. Mot en '
  'sjusitsig SUV som Tayron handlar valet mer om format än om ekonomi — men ID. Buzz är den '
  'dyrare bilen att försäkra av de två.',
 'kostnad':
  'ID. Buzz är dyr att köpa och har hittills hållit värdet ovanligt väl, vilket är gynnsamt '
  'för ägaren men höjer premien — vagnskadedelen ska kunna ersätta ett högt marknadsvärde. '
  'Energikostnaden är låg, däcken är stora och dyra, och den post som överraskar flest är '
  'just försäkringen, som ligger högre än formatet antyder.',
 'lang': ('Vad kostar det att försäkra en ID. Buzz?',
  'Mer än en jämnstor SUV, eftersom ersättningsvärdet är högt och skadebilden bred. Exakt '
  'nivå beror på om fordonet är registrerat som personbil eller lätt lastbil — kontrollera '
  'det först, eftersom det avgör vilken produkt du överhuvudtaget ska teckna.'),
 'lang2': ('Kan jag använda ID. Buzz i verksamhet på en privatförsäkring?',
  'Nej. Yrkesmässig användning kräver rätt försäkring, och ersättningen kan sättas ned helt '
  'om användningen inte angetts. Ange den korrekta användningen redan när du tecknar.'),
},

'tayron': {
 'meta': 'sjusitsig SUV som ersatte Tiguan Allspace',
 'direktsvar':
  'Volkswagen Tayron är ny som modellnamn men bygger på beprövad MQB-teknik, vilket betyder '
  'att bolagen har underlag från dag ett och att premien inte innehåller något '
  'osäkerhetspåslag. Nya bilar har vagnskadegaranti i tre år, och under den tiden räcker '
  'halvförsäkring.',
 'agare':
  'Tayron riktar sig till hushåll som behöver sju säten men inte vill gå till en dyrare '
  'premiummodell. Det är samma köpare som tidigare valde Tiguan Allspace: barnfamiljer med '
  'dragkrok, ofta bosatta utanför storstad. Just geografin är gynnsam för premien — bilar '
  'utanför tätort drabbas av färre parkeringsskador och färre stölder. Dragkroken i sig '
  'påverkar inte premien, men om du drar släp behöver släpet egen försäkring för att skador '
  'på det ska ersättas.',
 'teknik':
  'Tayron är en Tiguan i förlängt utförande, med samma plattform, samma motorer och samma '
  'delkatalog. Att modellbeteckningen är ny spelar därför mindre roll än man kan tro. '
  'Fyrhjulsdrift finns på en stor del av beståndet och innebär komponenter som blir dyra vid '
  'påkörning bakifrån. Den extra längden gör backningsskador vanligare än på Tiguan.',
 'jamfor':
  'Mot Skoda Kodiaq, som är samma bil under plåten, ligger Tayron högre i premie — nypriset '
  'avgör. Mot Volvo XC90 ligger den tydligt lägre, eftersom XC90 hamnar i premiumklassen med '
  'krav på stöldskydd i vissa områden. Mot Tiguan är skillnaden måttlig och följer av '
  'storleken.',
 'kostnad':
  'På en ny bil är värdeminskningen den överlägset största kostnaden, och försäkringen en '
  'mindre post. Det gör skyddsnivån viktigare än bolagsvalet de första åren: med '
  'vagnskadegaranti räcker halvförsäkring i tre år, och skillnaden mot helförsäkring under '
  'den perioden är pengar du kan behålla utan att försämra skyddet.',
 'lang': ('Räcker halvförsäkring på en ny Tayron?',
  'Ja, så länge vagnskadegarantin gäller — normalt tre år från första registrering. Den '
  'täcker samma sak som vagnskadedelen i en helförsäkring. Sätt en påminnelse när garantin '
  'går ut, för då står bilen utan vagnskadeskydd om ingen gör något.'),
 'lang2': ('Hittar försäkringsbolaget Tayron i sina system?',
  'Ja, men eftersom modellen är ny och ersatte Tiguan Allspace kan namnet skapa förvirring i '
  'offertformulär. Utgå alltid från registreringsnumret så att offerten hamnar på rätt bil '
  'och rätt utrustningsnivå.'),
},

't-roc': {
 'meta': 'Volkswagens kompakta SUV',
 'direktsvar':
  'Volkswagen T-Roc kostar något mer att försäkra än Golf, trots att bilarna delar teknik. '
  'Skillnaden ligger inte i bilen utan i vem som kör den — T-Roc har en yngre ägarprofil, och '
  'förarens ålder väger tyngre än karossformen i premieberäkningen.',
 'agare':
  'T-Roc är Volkswagens bil för den som köper sin första nya bil, och medelåldern i beståndet '
  'är märkbart lägre än för Golf och Tiguan. Det får två konsekvenser. Genomsnittspremien för '
  'modellen ligger högre än tekniken motiverar, och du som är över trettiofem med full bonus '
  'får därför ofta ett pris under vad publicerade siffror antyder. Bilen används mest i '
  'tätort och pendling, och står oftare på gatan än övriga Volkswagen-modeller.',
 'teknik':
  'T-Roc är en Golf på högre ben. Samma MQB-plattform, samma motorer, samma delkatalog och '
  'samma verkstäder. Det gör bilen billig att laga i förhållande till sitt segment. '
  'R-versionen är undantaget: den har fyrhjulsdrift, betydligt högre effekt och hamnar i en '
  'klass där flera bolag kräver förhöjd självrisk. Skillnaden mellan en T-Roc 1.0 TSI och en '
  'T-Roc R är större i premie än i pris.',
 'jamfor':
  'Mot Skoda Kamiq och Seat Arona ligger T-Roc högre i premie, både på grund av nypriset och '
  'ägarprofilen. Mot Volvo XC40 är skillnaden liten — båda har yngre ägare än sina '
  'märkessyskon. Mot Golf ligger T-Roc något högre, vilket alltså handlar om förarna snarare '
  'än om bilarna.',
 'kostnad':
  'T-Roc är dyrare i drift än Golf i varje post: högre förbrukning, dyrare däck och högre '
  'premie. Skillnaden är måttlig men konsekvent. För en yngre förare är försäkringen ofta den '
  'näst största posten efter värdeminskningen, vilket gör att en korrekt registrerad bonus '
  'och en rätt angiven körsträcka betyder mer här än på en bil med äldre ägarprofil.',
 'lang': ('Hur mycket dyrare är T-Roc R att försäkra?',
  'Betydligt. Fyrhjulsdrift och hög effekt placerar bilen i en klass där flera bolag kräver '
  'förhöjd självrisk. Hämta offert på både R och en vanlig T-Roc innan du väljer version — '
  'skillnaden per år kan överraska.'),
 'lang2': ('Är T-Roc ett bra val för en ung förare?',
  'Det är ett vanligt val, men inte det billigaste. En Polo eller Golf i samma prisklass ger '
  'lägre premie, eftersom både vikt och ersättningsvärde är lägre. Skillnaden är störst under '
  '25 år, då ungdomssjälvrisken dessutom tillkommer.'),
},

'touran': {
 'meta': 'sjusitsig familjebil i ovanligt format',
 'direktsvar':
  'Volkswagen Touran är billigare att försäkra än sjusitsiga SUV:ar i samma storlek. Bilen är '
  'lägre, lättare och har lägre ersättningsvärde, och den är dessutom sällsynt i '
  'stöldstatistiken. Sju säten till en kompaktbils premie är svårt att hitta någon annanstans.',
 'agare':
  'Touran köps av familjer som räknat efter och kommit fram till att en MPV ger mer plats per '
  'krona än en SUV. Det är en prismedveten ägarprofil med måttliga körsträckor och hög andel '
  'villaparkering. Bilen används också en del som taxi och i färdtjänst, vilket drar upp '
  'genomsnittssiffrorna för modellen — men yrkesmässig trafik är en annan riskklass med egna '
  'villkor, så de siffrorna gäller inte dig som privatperson.',
 'teknik':
  'Touran delar plattform och delkatalog med Golf och Passat, vilket ger utmärkt '
  'delstillgång. Den låga höjden är en fördel både i garage och i skadestatistiken — bilen '
  'är enklare att manövrera än en SUV i samma längd. Skjutdörrar saknas, vilket tar bort en '
  'reparationspost som finns på de flesta konkurrenter i formatet.',
 'jamfor':
  'Mot en sjusitsig SUV som Tayron eller Skoda Kodiaq ligger Touran tydligt lägre i premie. '
  'Mot Golf är skillnaden liten trots storleken, eftersom ersättningsvärdet är jämförbart. '
  'Det är en av få bilar där du får betydligt mer utrymme utan att betala för det i '
  'försäkringen.',
 'kostnad':
  'Touran är billig i drift men har en svaghet i kalkylen: andrahandsvärdet sjunker snabbare '
  'än på SUV-alternativen, eftersom efterfrågan på formatet minskar. Det gör bilen prisvärd '
  'att köpa begagnad och flyttar samtidigt gränsen för när helförsäkring slutar löna sig '
  'nedåt i ålder.',
 'lang': ('Är Touran billig att försäkra?',
  'Ja, i förhållande till sitt utrymme. Låg höjd, låg vikt, lågt ersättningsvärde och en '
  'undanskymd plats i stöldstatistiken ger en premie på nivå med en kompaktbil.'),
 'lang2': ('När bör jag gå från hel- till halvförsäkring på en Touran?',
  'När marknadsvärdet närmar sig 100 000 kr. Värdet sjunker snabbare på Touran än på '
  'SUV-alternativen, så räkna om vid varje förnyelse i stället för att förnya automatiskt.'),
},
}
