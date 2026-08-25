# -*- coding: utf-8 -*-
"""Textavsnitt för Tesla-, XPeng- och Cupra-modellerna.

Fyra löptextavsnitt och två långsvar per modell. Det är de fälten som
lyfter en modellsida från tabellsamling till något som faktiskt går att
läsa — och det är dem AI-översikter och utvalda utdrag hämtar ifrån.

FÄLTEN
  direktsvar  Fyrtio till sextio ord som besvarar prisfrågan helt.
  agare       Vem som kör bilen och hur det påverkar premien.
  teknik      Vad under plåten som styr reparationskostnaden.
  jamfor      Modellen mot sina konkurrenter.
  kostnad     Försäkringen i den totala ägarkostnaden.
  lang, lang2 Två långsvarsfrågor med svaret först.
  meta        Kort klausul till metabeskrivningen, max 60 tecken.
"""

EXTRA_2 = {

# ═══ TESLA ═════════════════════════════════════════════════════════
'model-3': {
 'meta': 'Sveriges vanligaste eldrivna sedan',
 'direktsvar':
  'Tesla Model 3 kostar mer att försäkra än en jämnstor bensinbil, men mindre än de flesta '
  'andra elbilar i klassen. Bolagen har mer skadedata på Model 3 än på någon annan elbil i '
  'Sverige, vilket sänker osäkerhetspåslaget. Räkna med att skillnaden mellan billigaste och '
  'dyraste offert är stor, och hämta minst tre.',
 'agare':
  'Model 3 kom till Sverige som tjänstebil och har blivit privatbil. Det betyder att en stor '
  'del av beståndet i dag ägs av personer som köpt bilen begagnad efter tre år i en '
  'företagsflotta, med körsträckor på 3 000 mil om året bakom sig. Din egen körsträcka är '
  'sannolikt en helt annan, och det är den som ska stå i offerten. Ägarprofilen har också '
  'blivit bredare med åren: från tidiga entusiaster till barnfamiljer som valt bilen för '
  'driftskostnaden. Bolagen har hunnit med i den utvecklingen, och Model 3 prissätts i dag '
  'som den vanliga bil den blivit — inte som den exotiska den var 2019.',
 'teknik':
  'Det som gör Model 3 dyr att laga är inte elmotorn utan karossen. Tesla använder stora '
  'gjutna aluminiumsektioner i stället för många sammanfogade plåtdelar. Det gör bilen styv '
  'och billig att bygga, men vid en skada finns ingen mellanväg: där en traditionell kaross '
  'hade kunnat riktas eller få en delsektion utbytt kan Teslas konstruktion kräva att en hel '
  'gjuten sektion ersätts. Lägg till att Tesla i praktiken styr reparationerna till sitt eget '
  'nät, och du får en bil där fritt verkstadsval i villkoren är värt mindre än på nästan '
  'någon annan modell. Fråga bolaget vad som gäller i praktiken, inte bara vad som står.',
 'jamfor':
  'Mot Polestar 2 ligger Model 3 ofta något lägre i premie, trots liknande prestanda — '
  'skillnaden är dataunderlaget. Mot en BMW i4 eller Mercedes EQE är Model 3 tydligt '
  'billigare, framför allt för att ersättningsvärdet är lägre efter Teslas prissänkningar. '
  'Mot en bensindriven Volvo S60 i samma storleksklass ligger Model 3 däremot högre, och där '
  'går den verkliga skiljelinjen: det är drivlinan och reparationsmetoden, inte segmentet, '
  'som avgör.',
 'kostnad':
  'Försäkringen utgör en större andel av den totala ägarkostnaden på en Model 3 än på en '
  'bensinbil, av det enkla skälet att de övriga posterna är låga. Ingen fordonsskatt värd '
  'namnet, låg energikostnad och minimal service gör att premien plötsligt är den största '
  'rörliga utgiften. Det är också därför det lönar sig mer att jämföra bolag här än på en bil '
  'där bränslet dominerar kalkylen — några hundralappar i månaden på premien är en betydligt '
  'större andel av totalen.',
 'lang': ('Vilket bolag är billigast för Tesla Model 3?',
  'Det varierar med förarprofilen, och inget bolag är billigast för alla. Det som är '
  'specifikt för Model 3 är att spridningen mellan bolagen är större än på en '
  'genomsnittsbil, eftersom de värderar reparationsrisken olika. Hämta offert på '
  'registreringsnumret hos minst tre bolag.'),
 'lang2': ('Täcks batteriet i en Tesla Model 3 av försäkringen?',
  'Batteriet omfattas normalt av samma skydd som resten av bilen vid yttre skada, alltså av '
  'vagnskadedelen i en helförsäkring. Gradvis kapacitetsförlust räknas däremot som slitage '
  'och hanteras av Teslas garanti, inte av försäkringen. Läs båda dokumenten — de täcker '
  'olika saker.'),
},

'model-y': {
 'meta': 'Sveriges vanligaste elbil',
 'direktsvar':
  'Tesla Model Y ligger något över Model 3 i premie. Bilen väger mer, körs längre per år och '
  'har två stora glasytor som är dyra att ersätta. Samtidigt är beståndet stort, vilket ger '
  'bolagen gott skadeunderlag och håller nere osäkerhetspåslaget jämfört med nyare '
  'elbilsmärken.',
 'agare':
  'Model Y är för många hushåll den enda bilen, inte den andra. Det märks i statistiken: '
  'körsträckorna är högre än för Model 3, bilen används för semesterresor och '
  'hämtning-lämning, och den står oftare parkerad på gatan i en stad. Alla tre faktorerna '
  'drar premien uppåt. Å andra sidan är förarprofilen gynnsam — medelåldern ligger högre än '
  'för elbilsköpare i allmänhet, och andelen med lång skadefri historik är stor. För dig som '
  'är över fyrtio med full bonus betyder det att de publicerade genomsnittspriserna '
  'sannolikt ligger över vad du själv får betala.',
 'teknik':
  'Två saker sticker ut. Panoramataket i glas sträcker sig över hela kupén och är en enda '
  'stor komponent — det finns inget litet parti att byta. Vindrutan är kraftigt lutande och '
  'stor, och bakom den sitter kamerorna som styr assistanssystemen, vilket innebär '
  'kalibrering efter varje byte. I praktiken betyder det att glasmomentet och dess självrisk '
  'är den villkorspost som spelar störst roll på just den här bilen. Ett bolag med låg '
  'glassjälvrisk vid byte kan vara billigare i verkligheten än ett med lägre årspremie.',
 'jamfor':
  'Mot Volvo EX40 och Hyundai IONIQ 5 ligger Model Y i mitten. Volvo har fler verkstäder, '
  'Hyundai delar plattform med Kia och har därmed god delstillgång, medan Tesla har det '
  'största dataunderlaget. Mot en bensindriven XC60 i samma storlek ligger Model Y högre, '
  'trots att XC60 är dyrare att köpa — ett tydligt exempel på att inköpspriset och '
  'försäkringspremien inte följs åt.',
 'kostnad':
  'Model Y hamnar i den ovanliga situationen att försäkringen kan vara den enskilt största '
  'rörliga kostnaden. Med hemmaladdning ligger energikostnaden lågt, servicebehovet är '
  'begränsat och fordonsskatten är minimal. Det gör att en premieskillnad på trehundra kronor '
  'i månaden mellan två bolag motsvarar en betydande del av vad bilen kostar att köra. Räkna '
  'på hela ägarkostnaden, inte bara på premien — men inse också att premien är den post där '
  'du enklast kan påverka utfallet.',
 'lang': ('Är Tesla Model Y dyrare att försäkra än Model 3?',
  'Normalt ja, med samma förare. Model Y är tyngre, har större glasytor och används i '
  'genomsnitt mer per år. Skillnaden är dock mindre än mellan två olika märken i samma '
  'storlek, eftersom bilarna delar drivlina och reparationsmetod.'),
 'lang2': ('Vad kostar det att laga glastaket på en Tesla Model Y?',
  'Glastaket är en enda stor komponent utan mindre delar att byta, vilket gör en skada dyr. '
  'Exakt belopp varierar, men det är skälet till att glassjälvrisken är den villkorspost du '
  'bör jämföra först på den här modellen — skillnaden mellan bolagen är stor.'),
},

'model-s': {
 'meta': 'Teslas flaggskepp med hög effektklass',
 'direktsvar':
  'Tesla Model S är den dyraste Teslan att försäkra. Högt ersättningsvärde, hög motoreffekt '
  'och ett litet svenskt bestånd gör att bolagen prissätter med marginal. Spridningen mellan '
  'offerter är ovanligt stor på just den här modellen, vilket gör det extra lönsamt att '
  'jämföra brett.',
 'agare':
  'Model S köps i dag i huvudsak begagnad. Nybilsförsäljningen i Sverige är minimal, medan '
  'andrahandsmarknaden rymmer allt från tio år gamla exemplar till nästan nya Plaid. Det '
  'skapar en märklig situation för försäkringen: två bilar med samma modellbeteckning kan '
  'skilja en miljon kronor i ersättningsvärde. Ägarprofilen är också bred, från entusiaster '
  'som köpt en tidig 85D som andrabil till företagare som kör en Plaid. Utgå aldrig från '
  'generella prisuppgifter för modellen — de blandar ihop två helt olika bilar.',
 'teknik':
  'Luftfjädringen är den post som oftast överraskar. Den sitter på de flesta exemplar, den '
  'slits, och den är dyr att ersätta — och den täcks inte av alla maskinskadevillkor, '
  'särskilt inte när bilen passerat åldersgränsen. Batteripaketet ligger dessutom i golvet '
  'och utgör bilens strukturella botten, vilket gör att ett hårt möte med en trottoarkant '
  'eller ett farthinder i värsta fall utlöser en undersökning av hela paketet. Det är den '
  'typen av ärende där skillnaden mellan bolagens villkor blir verkligt dyr.',
 'jamfor':
  'Mot Mercedes EQS och BMW i7 ligger Model S lägre i premie, men skillnaden är mindre än '
  'prisskillnaden på begagnatmarknaden antyder. Mot Model 3 är avståndet stort, och det beror '
  'inte bara på värdet utan på effektklassen — Plaid-versionen ligger i ett effektspann där '
  'flera bolag kräver förhöjd självrisk. Jämför du en äldre Model S mot en ny Model 3 kan den '
  'äldre, billigare bilen mycket väl vara dyrast att försäkra.',
 'kostnad':
  'På en begagnad Model S kan försäkringen bli den dominerande ägarkostnaden. Bilen kostar '
  'lite att köpa, lite att ladda och lite i skatt, medan premien speglar ett '
  'ersättningsvärde och en effektklass som hör till en betydligt dyrare bil. Räkna igenom '
  'helheten innan du köper: det är inte ovanligt att försäkringen kostar mer per år än vad '
  'värdeminskningen gör på ett tio år gammalt exemplar.',
 'lang': ('Varför är premien så hög på en gammal Tesla Model S?',
  'För att premien speglar effektklassen och reparationskostnaden, inte inköpspriset. En tio '
  'år gammal Model S har fortfarande över 400 hästkrafter, luftfjädring och ett batteripaket '
  'som är dyrt att ersätta. Bolagen prissätter risken, inte vad du betalade.'),
 'lang2': ('Ska jag ha helförsäkring på en äldre Tesla Model S?',
  'Räkna på det. Vagnskadedelen ersätter marknadsvärdet minus självrisken, och på ett '
  'exemplar värt 200 000 kr är utrymmet fortfarande stort nog att motivera helförsäkring. '
  'Ligger värdet under 100 000 kr blir kalkylen betydligt tveksammare.'),
},

'model-x': {
 'meta': 'stor eldriven SUV med falcon wing-dörrar',
 'direktsvar':
  'Tesla Model X är den svåraste modellen i Teslas utbud att få ett lågt pris på. '
  'Falcon wing-dörrarna, den höga vikten, effektklassen och stöldbegärligheten pekar alla åt '
  'samma håll. Flera bolag ställer dessutom krav på godkänt stöldskydd i storstadsområdena — '
  'ett krav som är en förutsättning för ersättning.',
 'agare':
  'Model X köps av hushåll som behöver sju säten och av företagare som vill ha en dragbil '
  'med el. Båda användningarna påverkar försäkringen. Sju passagerare betyder högre '
  'exponering för personskador, vilket trafikdelen täcker utan beloppstak. Dragkrok betyder '
  'att du bör kontrollera hur släpet är försäkrat — bilens trafikförsäkring täcker skador '
  'släpet orsakar på annan, men inte skador på släpet självt. Bilen står ofta i garage, '
  'vilket är den enda faktorn i sammanhanget som drar premien nedåt, och den är värd att '
  'ange.',
 'teknik':
  'Falcon wing-dörrarna är modellens signatur och dess dyraste reparationspost. Mekanismen '
  'innehåller sensorer som känner av hinder, gångjärn med egen elektronik och en '
  'tätningslösning som är känslig för snedbelastning. Skador uppstår oftast i garage med lågt '
  'tak eller vid parkering nära en vägg — situationer där dörren öppnas mot något den inte '
  'hinner registrera. Yttre skador omfattas av vagnskadedelen, men rena mekaniska fel är en '
  'maskinskadefråga, och där skiljer sig villkoren rejält. Läs det momentet ordentligt.',
 'jamfor':
  'Mot BMW iX och Mercedes EQS SUV ligger Model X i samma premieklass, med skillnaden att de '
  'tyska märkena har fler verkstäder. Mot Volvo EX90 har Model X en nackdel i verkstadsnätet '
  'och en fördel i dataunderlaget. Den avgörande skillnaden mot alla tre är dörrarna: ingen '
  'av konkurrenterna har en lika modellspecifik reparationsrisk, och det är den som gör '
  'spridningen mellan bolagens offerter så stor.',
 'kostnad':
  'Model X är dyr i alla poster utom energi. Däcken är stora och slits fort på grund av '
  'vikten, försäkringen ligger högt och värdeminskningen har varit betydande. Den enda '
  'kostnaden som är låg är laddningen. Det gör att försäkringen inte dominerar totalen på '
  'samma sätt som på en Model 3 — men det gör också att en premieskillnad mellan bolagen är '
  'lättare att missa i en kalkyl där allt annat är stort.',
 'lang': ('Kräver försäkringsbolagen spårsändare på Tesla Model X?',
  'Flera bolag ställer krav på godkänt stöldskydd eller spårsändare för stora, dyra SUV:ar, '
  'och kravet är ofta kopplat till postnummer. Det står i villkoren, inte i offerten. '
  'Uppfylls kravet inte den natt bilen försvinner kan ersättningen sättas ned eller nekas.'),
 'lang2': ('Går det att dra släp med Model X och påverkar det försäkringen?',
  'Ja, bilen är godkänd för släp, och det påverkar inte bilens premie i sig. Släpet behöver '
  'däremot egen försäkring om du vill ha skador på släpet ersatta — bilens trafikförsäkring '
  'täcker bara skador släpet orsakar på annan egendom.'),
},

# ═══ XPENG ═════════════════════════════════════════════════════════
'g6': {
 'meta': 'XPengs mest sålda modell i Sverige',
 'direktsvar':
  'XPeng G6 kostar normalt något mer att försäkra än en jämnstor etablerad elbil. Skälet är '
  'inte bilen utan underlaget: beståndet i Sverige är litet, skadestatistiken tunn och '
  'verkstadsnätet under uppbyggnad. Spridningen mellan bolagens offerter är ovanligt stor, '
  'vilket gör det extra lönsamt att jämföra brett.',
 'agare':
  'G6 köps av personer som medvetet valt bort de etablerade märkena, ofta med räckvidd och '
  'utrustning per krona som argument. Det är en förarprofil bolagen ännu inte har mycket '
  'statistik på, vilket är en del av förklaringen till prisspridningen. Många exemplar går '
  'på privatleasing, och då gäller avtalets krav på skyddsnivå — i praktiken alltid '
  'helförsäkring. Bilen används mest som familjens huvudbil, med normala svenska '
  'körsträckor kring 1 500 mil om året och laddning hemma.',
 'teknik':
  'G6 använder 800-voltsteknik, samma principiella lösning som Porsche Taycan och Hyundai '
  'IONIQ 5. Det ger snabb laddning men innebär också att arbete på högvoltssystemet kräver '
  'särskild behörighet — antalet verkstäder som får röra bilen är alltså mindre än antalet '
  'verkstäder som kan laga en plåtskada. Fronten är den andra tekniska knäckpunkten: radar, '
  'kameror och lidar sitter samlade bakom stötfångaren, och en parkeringssmäll i låg fart '
  'kan därför utlösa kalibrering av hela assistanspaketet.',
 'jamfor':
  'Mot Tesla Model Y, som är den direkta konkurrenten, ligger G6 högre i premie trots ett '
  'lägre pris. Skillnaden är dataunderlaget, inte bilen. Mot Volvo EX40 är avståndet större, '
  'eftersom Volvo har både verkstadsnät och skadehistorik. Bilden lär förändras — samma sak '
  'gällde för koreanska märken för femton år sedan — men i dag betalar du för att vara tidig.',
 'kostnad':
  'G6 är billig att köpa och billig att köra, vilket gör försäkringen till en stor andel av '
  'totalen. Det finns också en post som är lätt att glömma: väntetid vid skada. Står bilen på '
  'verkstad i sex veckor i väntan på en del är det hyrbilsmomentet som avgör om det kostar '
  'dig något. Ett bolag med tjugo hyrbilsdagar och ett med fem kan ha samma premie och helt '
  'olika utfall.',
 'lang': ('Vilka försäkringsbolag tecknar XPeng i Sverige?',
  'De flesta större bolag gör det, men alla har inte egen prissättning för märket. Ett bolag '
  'utan modelldata lägger ofta på ett generellt osäkerhetspåslag. Fråga uttryckligen hur '
  'bilen klassas, och hämta fler offerter än du annars skulle.'),
 'lang2': ('Hur lång tid tar det att få reservdelar till en XPeng?',
  'Det varierar, och det är den verkliga risken med ett nyetablerat märke. Därför är antalet '
  'hyrbilsdagar den viktigaste villkorsposten på en XPeng — viktigare än självrisken, '
  'eftersom väntetid är sannolikare än totalskada.'),
},

'g9': {
 'meta': 'XPengs största SUV',
 'direktsvar':
  'XPeng G9 hamnar i en premieklass som speglar bilens storlek och utrustning snarare än dess '
  'pris. Flera bolag saknar egen modelldata för märket och prissätter med ett generellt '
  'påslag, vilket gör att skillnaden mellan billigaste och dyraste offert kan bli mycket '
  'stor. Begär skriftligt besked om hur bilen klassas.',
 'agare':
  'G9 är en stor familjebil för hushåll som prioriterar utrymme och utrustning. '
  'Ägarprofilen liknar den för en Audi Q8 e-tron eller Model X, men med en avgörande '
  'skillnad: de flesta har medvetet valt ett märke utan etablerad historik i Sverige, och en '
  'del av dem har gjort det just för att prisbilden på bilen är låg i förhållande till '
  'utrustningen. Det gör att gapet mellan vad bilen kostar och vad den kostar att försäkra '
  'blir mer märkbart här än på de flesta andra modeller.',
 'teknik':
  'G9 finns med luftfjädring på flera versioner, och det är en post värd att kontrollera mot '
  'maskinskademomentet — luftfjädring är dyr att laga och undantas oftare än många tror. '
  'Bilen har också ett omfattande sensorpaket och stora karossektioner, vilket innebär att '
  'även måttliga skador snabbt blir kostsamma. Precis som på G6 gäller att '
  'högvoltsbehörighet krävs för arbete på drivlinan, vilket begränsar verkstadsvalet mer än '
  'villkorstexten antyder.',
 'jamfor':
  'Mot Tesla Model X och Audi Q8 e-tron ligger G9 lägre i inköpspris men inte nödvändigtvis i '
  'premie. Mot systermodellen G6 är skillnaden tydlig och förväntad: större bil, högre '
  'ersättningsvärde, högre premie. Det verkligt intressanta i jämförelsen är spridningen — '
  'på en Model X är bolagen relativt eniga om risken, på en G9 är de inte det, och det är där '
  'du kan tjäna mest på att jämföra.',
 'kostnad':
  'G9 är billig att köpa i förhållande till vad den är, och det påverkar hela kalkylen. '
  'Värdeminskningen i kronor kan bli hög i procent men måttlig i belopp, medan försäkringen '
  'är den post som ligger mest oförutsägbart. Räkna med att premien kan skilja med flera '
  'tusen kronor om året mellan två bolag, och att det är den enda posten du kan förhandla om '
  'i efterhand.',
 'lang': ('Är XPeng G9 dyr att försäkra jämfört med tyska premium-SUV:ar?',
  'Inte nödvändigtvis dyrare, men mer oförutsägbar. Tyska premiummärken har etablerade '
  'modellprofiler hos alla bolag, medan XPeng saknar det hos flera. Det gör att du kan få '
  'både lägre och betydligt högre offerter på samma bil.'),
 'lang2': ('Täcks luftfjädringen på en XPeng G9 av maskinskadeförsäkringen?',
  'Det beror på bolaget. Luftfjädring undantas eller begränsas i flera villkor, och '
  'maskinskademomentet upphör dessutom vid en viss ålder och körsträcka. Läs just det '
  'momentet innan du tecknar — det är en av de dyraste komponenterna på bilen.'),
},

'p7': {
 'meta': 'XPengs sportiga eldrivna sedan',
 'direktsvar':
  'Vi har inte hittat publicerade prisexempel för XPeng P7 på den svenska marknaden. Räkna '
  'med att modellen hamnar i samma spann som andra eldrivna sedaner i klassen, men med större '
  'spridning mellan bolagen eftersom skadeunderlaget är tunt. Hämta fler offerter än du '
  'annars skulle.',
 'agare':
  'P7 vänder sig till förare som vill ha en eldriven sedan med prestandaprofil till ett pris '
  'under de etablerade alternativen. Beståndet i Sverige är litet, och den typiska ägaren är '
  'därmed också en tidig adoptör — en grupp som statistiskt kör mer och oftare i storstad än '
  'genomsnittet. Båda faktorerna påverkar premien uppåt, och ingen av dem har med bilen att '
  'göra. Är du inte den typiske ägaren bör du därför inte utgå från generella prisuppgifter '
  'utan hämta egen offert.',
 'teknik':
  'P7 är byggd med aerodynamiken som utgångspunkt: låg nos, låg markfrigång och stora '
  'sammanhängande karossytor. Det ger tre konsekvenser för försäkringen. Underredet och '
  'frontspoilern är utsatta vid farthinder och branta infarter. Stora ytor betyder att en '
  'skada sällan kan lagas som ett litet parti. Och de infällda dörrhandtagen, som är en '
  'signatur på modellen, innehåller elektronik som gör en till synes trivial skada dyrare än '
  'väntat.',
 'jamfor':
  'Mot Tesla Model 3, som är den uppenbara jämförelsen, har P7 en nackdel i verkstadsnät och '
  'dataunderlag men ingen nackdel i själva konstruktionen. Mot BMW i4 är prisskillnaden på '
  'bilen stor och premieskillnaden mindre — vilket är samma mönster vi ser hos alla nya '
  'märken: du betalar mindre för bilen och relativt mer för att försäkra den.',
 'kostnad':
  'Som på alla elbilar utgör försäkringen en stor andel av driftkostnaden, och på P7 '
  'förstärks det av att bilen är billig att köpa. Den post som är lätt att underskatta är '
  'däck: låg profil och hög vridmoment sliter fort, och stora fälgar är dyra att ersätta om '
  'de skadas mot en kantsten. Just fälgskador faller ofta utanför försäkringen helt, eftersom '
  'de räknas som ensidiga skador utan yttre händelse.',
 'lang': ('Vad bör jag kontrollera i villkoren innan jag försäkrar en XPeng P7?',
  'Tre saker: antalet hyrbilsdagar, om batteriet omfattas av vagnskadedelen och hur bolaget '
  'hanterar kalibrering av assistanssystem efter en skada. På ett nyetablerat märke är '
  'väntetid och kalibrering de kostnader som oftast överraskar.'),
 'lang2': ('Är eldrivna sedaner billigare att försäkra än el-SUV:ar?',
  'Ofta något billigare, ja. Sedanen är lättare, har mindre glasytor och drabbas av färre '
  'parkeringsskador än en högre och bredare SUV. Skillnaden är dock mindre än mellan två '
  'märken med olika verkstadsnät.'),
},

'x9': {
 'meta': 'eldriven sjusitsig MPV',
 'direktsvar':
  'XPeng X9 är svår att prissätta eftersom segmentet nästan saknar jämförelseobjekt i '
  'Sverige. Flera bolag har ingen modellprofil och klassar bilen som övrig stor personbil, '
  'vilket kan slå åt båda hållen. Begär skriftligt besked om hur bilen klassas innan du '
  'tecknar, och jämför brett.',
 'agare':
  'X9 köps av stora hushåll och av företag som kör persontransport. Det är två användningar '
  'med helt olika riskprofil, och bolagen skiljer på dem: används bilen yrkesmässigt gäller '
  'andra villkor och ofta en annan premie. Ange användningen korrekt från början — '
  'yrkesmässig persontransport på en privatförsäkring är en av de situationer där '
  'ersättningen kan sättas ned helt. För privat bruk gäller att sju säten innebär hög '
  'exponering för personskador, vilket trafikdelen täcker utan beloppstak.',
 'teknik':
  'De elektriska skjutdörrarna är modellens mest särskilda reparationspost. Skenor, motorer '
  'och sensorer sitter längs hela sidan, och skador uppstår typiskt i trånga stadsmiljöer '
  'eller när dörren möter ett hinder den inte hinner registrera. Bilen är dessutom både lång '
  'och hög, vilket gör den utsatt i parkeringsgarage byggda för en annan tid. Kombinationen '
  'gör att vagnskadedelen är mer aktiv på den här modellen än på en vanlig SUV.',
 'jamfor':
  'Det finns knappt något att jämföra med. Volkswagen ID.Buzz är det närmaste alternativet i '
  'Sverige, och där har VW en avgörande fördel i verkstadsnät och etablerad modelldata. Mot '
  'en stor SUV som Model X handlar valet mer om utrymme än om ekonomi — men försäkringsmässigt '
  'är X9 den svårare bilen, just för att bolagen inte har någon etablerad bild av den.',
 'kostnad':
  'X9 är en stor bil, och alla kostnader följer med storleken: däck, värdeminskning och '
  'premie. Det som är billigt är energin. Den viktigaste ekonomiska frågan på den här bilen '
  'är dock inte den löpande kostnaden utan andrahandsvärdet, som är helt oprövat i Sverige. '
  'Eftersom vagnskadedelen ersätter marknadsvärdet betyder det också att du bör begära '
  'besked om hur bolaget värderar bilen vid totalskada. Till det kommer en praktisk fråga: bilens längd och höjd gör att den inte får plats i alla parkeringsgarage, vilket i sin tur betyder gatuparkering i vissa lägen. Var bilen står nattetid är en uppgift bolagen frågar om och prissätter, och för X9 är det en fråga som avgörs av geometri snarare än av vad du föredrar.',
 'lang': ('Hur klassas en XPeng X9 av försäkringsbolagen?',
  'Som personbil, men vilken modellprofil bolaget använder varierar. Saknas egen data klassas '
  'bilen ofta som övrig stor personbil, vilket ger en schablonpremie. Begär skriftligt besked '
  '— klassningen avgör både premie och hur bilen värderas vid totalskada.'),
 'lang2': ('Behöver jag särskild försäkring om jag kör persontransport med X9?',
  'Ja. Yrkesmässig persontransport omfattas inte av en vanlig privatförsäkring, och '
  'ersättningen kan sättas ned helt om användningen inte angetts. Ange den korrekta '
  'användningen redan när du tecknar.'),
},

# ═══ CUPRA ═════════════════════════════════════════════════════════
'formentor': {
 'meta': 'Cupras mest sålda modell',
 'direktsvar':
  'Cupra Formentor i basutförande ligger i nivå med andra kompakta SUV:ar tack vare den '
  'delade VW-tekniken och den goda delstillgången. VZ-versionerna är en annan sak: '
  'effektklassen gör att premien kan bli avsevärt högre för exakt samma kaross. Ange alltid '
  'registreringsnumret så att offerten hamnar på rätt version.',
 'agare':
  'Formentor har lyckats med något få märken gör: den lockar både den som vill ha en praktisk '
  'kompakt SUV och den som vill ha en snabb bil. Det syns i beståndet, där en 1.5 TSI och en '
  'VZ5 med femcylindrig motor står under samma modellnamn. Ägarprofilen skiljer sig lika '
  'mycket, och det är därför generella prisuppgifter för modellen är nästan värdelösa. En '
  'stor andel går på privatleasing, vilket innebär att helförsäkring krävs enligt avtalet '
  'och att självrisknivån ofta är låst.',
 'teknik':
  'Under plåten är Formentor en Volkswagen, och det är den enskilt viktigaste '
  'försäkringsfaktorn. MQB-plattformen delas med Tiguan, Ateca och en rad andra modeller, '
  'vilket betyder att i princip varje verkstad kan skaffa delarna och att konkurrensen '
  'pressar timpriset. Det som inte delas är fjädringen och fälgarna. Sportfjädringen är '
  'styvare och fälgarna större än på syskonmodellerna, och kombinationen gör bilen känslig '
  'mot kantstenar och farthinder — fälgskador är den vanligaste enskilda kostnaden.',
 'jamfor':
  'Mot VW Tiguan och Seat Ateca ligger Formentor högre i premie, trots delad teknik. '
  'Skillnaden är effekten och ägarprofilen, inte reparationskostnaden. Mot en BMW X2 eller '
  'Audi Q3 är Formentor billigare att försäkra, framför allt på grund av delstillgången. '
  'Vill du ha samma kaross till lägst möjliga premie är basmotorn svaret — steget till VZ '
  'kostar mer i försäkring per år än många räknar med.',
 'kostnad':
  'Formentor är en bil där försäkringen är en måttlig del av totalen. Bränsle, '
  'värdeminskning och däck väger tyngre, särskilt på VZ-versionerna där både förbrukning och '
  'däckslitage är höga. Det gör inte premien oviktig, men det betyder att den som jagar lägst '
  'total ägarkostnad bör titta på motorvalet först — det påverkar samtliga poster samtidigt, '
  'medan bolagsvalet bara påverkar en.',
 'lang': ('Hur mycket dyrare är Cupra Formentor VZ att försäkra?',
  'Skillnaden kan vara betydande, eftersom effektklassen är en av de tyngsta faktorerna för '
  'kompaktbilar. Vissa bolag kräver dessutom förhöjd självrisk över ett visst effektuttag. '
  'Hämta offert på båda versionerna innan du bestämmer dig för motor.'),
 'lang2': ('Är Cupra Formentor billigare att försäkra än en Audi Q3?',
  'Oftast ja, i jämförbara motoralternativ. Bilarna delar koncern men Cupra har lägre '
  'nypris och därmed lägre ersättningsvärde, vilket väger tyngre än märkets prestandaprofil '
  'i premieberäkningen.'),
},

'born': {
 'meta': 'Cupras elbil på VW:s MEB-plattform',
 'direktsvar':
  'Cupra Born hör till de billigare elbilarna att försäkra i sin klass. Den bygger på '
  'Volkswagens MEB-plattform, som är en av Europas vanligaste, vilket ger både god '
  'delstillgång och ett brett verkstadsnät med rätt högvoltsbehörighet. Det är precis de två '
  'faktorer som annars driver upp elbilspremier.',
 'agare':
  'Born köps som förstabil av yngre hushåll och som andrabil av äldre. Den dubbla '
  'ägarprofilen gör att genomsnittssiffror för modellen sällan stämmer på någon enskild '
  'förare. Bilen används mest i stad och pendling, med korta körsträckor och hemmaladdning. '
  'Har du laddbox på väggen är det värt att veta att den normalt hör till villa- eller '
  'hemförsäkringen, medan laddkabeln som följer bilen oftast omfattas av bilförsäkringen — '
  'en gränsdragning som är den vanligaste källan till besvikelse vid en skada.',
 'teknik':
  'Born är en Volkswagen ID.3 med annan kaross och sportigare avstämning, och det är goda '
  'nyheter för allt som rör reparation. MEB-plattformen finns i hundratusentals exemplar i '
  'Europa, delarna är standardiserade och antalet verkstäder med högvoltsbehörighet växer '
  'stadigt. Det som skiljer mot ID.3 är fjädringen och fälgarna, som på alla Cupra-modeller '
  'är sportigare respektive större — vilket gör fälgskador vanligare och dyrare.',
 'jamfor':
  'Mot VW ID.3 ligger Born marginellt högre, av samma skäl som Cupra Leon ligger över Seat '
  'Leon: prestandaprofilen. Mot en Tesla Model 3 är Born billigare att försäkra trots att '
  'bilarna är olika stora, eftersom reparationsmetoden är konventionell och verkstadsvalet '
  'fritt på riktigt. Mot en MG4 eller BYD Dolphin har Born en tydlig fördel i delstillgång.',
 'kostnad':
  'Born är en av få elbilar där hela ägarkalkylen går ihop utan asterisker: låg '
  'energikostnad, låg fordonsskatt, måttlig värdeminskning och en försäkringspremie som inte '
  'sticker ut. Det gör den till en bil där jämförelsen mellan bolag ger mindre i kronor än på '
  'en dyrare elbil — men också till en bil där du sällan behöver oroa dig för att en enskild '
  'skada ska bli oproportionerligt dyr.',
 'lang': ('Är Cupra Born dyrare att försäkra än en VW ID.3?',
  'Marginellt, ja. Bilarna delar plattform, delar och verkstadsnät, men Cupra har högre '
  'effektuttag och en något yngre ägarprofil. Skillnaden är liten jämfört med spridningen '
  'mellan olika försäkringsbolag på samma bil.'),
 'lang2': ('Hör laddboxen till bilförsäkringen på en Cupra Born?',
  'Nej. En fast monterad laddbox sitter på fastigheten och hör därför normalt till villa- '
  'eller hemförsäkringen. Laddkabeln som följer med bilen omfattas däremot oftast av '
  'bilförsäkringen. Kontrollera båda villkoren.'),
},

'leon': {
 'meta': 'prestandaversionen av Seat Leon',
 'direktsvar':
  'Cupra Leon kostar mer att försäkra än en Seat Leon med samma kaross. Skillnaden är '
  'effekten: motorstyrkan är en av de tyngsta faktorerna i premieberäkningen för '
  'kompaktbilar, medan delarna och verkstäderna är identiska. Sportstourer-versionen ligger '
  'något lägre än halvkombin.',
 'agare':
  'Cupra Leon köps av förare som vill ha prestanda i ett format som inte drar '
  'uppmärksamhet till sig. Ägarprofilen är yngre än för en Seat Leon men äldre än för en '
  'typisk sportbil, och skadestatistiken ligger däremellan. Sportstourer-versionen bryter '
  'mönstret: den köps oftare av familjer som vill ha lastutrymme, och den har en märkbart '
  'lugnare skadebild än halvkombin. Väljer du mellan de två av rent ekonomiska skäl är '
  'kombin det billigare valet, både i premie och i praktiken.',
 'teknik':
  'Allt som kostar pengar vid en reparation är delat med Seat och Volkswagen: kaross, '
  'elektronik, drivlina i grunden och hela delkatalogen. Det gör Cupra Leon billig att laga '
  'i förhållande till sin prestanda. Det som är eget är avstämningen — styvare fjädring, '
  'större bromsar och bredare däck. Bromsarna är värda en tanke: de är dyrare att byta än på '
  'en vanlig Leon, och slitage täcks inte av någon försäkringsnivå.',
 'jamfor':
  'Mot VW Golf GTI är Cupra Leon i praktiken samma bil med annan kaross, och premierna ligger '
  'nära varandra. Mot en BMW 128ti eller Audi S3 är Cupra billigare att försäkra, framför '
  'allt på grund av lägre ersättningsvärde. Mot en vanlig Seat Leon är skillnaden tydlig och '
  'helt driven av effektklassen — samma bil, samma verkstad, annan premie.',
 'kostnad':
  'På en prestandaversion av en vanlig bil är det sällan försäkringen som dominerar '
  'ägarkostnaden. Bränsleförbrukningen, däcken och bromsarna gör det. Försäkringen är '
  'däremot den post där skillnaden mellan två bolag kan bli störst i procent, eftersom de '
  'värderar effektklassen olika. Det gör jämförelsen mer lönsam här än på en basmotor, även '
  'om beloppet i kronor inte är det största i kalkylen.',
 'lang': ('Kräver försäkringsbolagen förhöjd självrisk på Cupra Leon?',
  'Vissa bolag gör det över ett visst effektuttag, och gränsen varierar. Det är en av de '
  'poster som inte syns i årspremien utan först vid skadan. Fråga uttryckligen innan du '
  'tecknar, särskilt på de starkaste versionerna.'),
 'lang2': ('Är Cupra Leon Sportstourer billigare att försäkra än halvkombin?',
  'Ofta något, ja. Kombiversionen har en lugnare ägarprofil och lägre skadefrekvens, vilket '
  'väger tyngre än den marginella skillnaden i vikt och värde.'),
},

'tavascan': {
 'meta': 'Cupras eldrivna SUV-coupé',
 'direktsvar':
  'Cupra Tavascan bygger på samma MEB-teknik som Born och VW ID.5, vilket gör tekniken bekant '
  'för svenska verkstäder. Premien ligger högre än på Born, eftersom bilen är större och '
  'dyrare. Den villkorspost som spelar störst roll är antalet hyrbilsdagar, eftersom bilen '
  'tillverkas i Kina och delvägarna varit ojämna.',
 'agare':
  'Tavascan köps av hushåll som vill ha en elbil med utrustning och design i fokus, ofta som '
  'familjens huvudbil. Många exemplar går på privatleasing, vilket innebär att '
  'helförsäkring krävs enligt avtalet under hela avtalstiden — det är alltså ingen valfrihet '
  'i skyddsnivån. Körsträckorna ligger på normala svenska nivåer, kring 1 500 mil om året, '
  'och laddning sker i huvudsak hemma. Ägarprofilen är i genomsnitt äldre än Borns, vilket '
  'drar premien nedåt.',
 'teknik':
  'MEB-plattformen är välkänd, delarna är standardiserade och antalet verkstäder med rätt '
  'behörighet är stort. Det som skiljer Tavascan är karossen: den sluttande taklinjen ger en '
  'stor bakruta och en stor bakre karossektion, och båda är dyra att ersätta. Glasmomentet '
  'väger därför tyngre på den här modellen än på en vanlig SUV. Att bilen tillverkas i Kina '
  'påverkar inte reparationens svårighetsgrad men däremot leveranstiden på delar, vilket är '
  'en helt annan sorts kostnad.',
 'jamfor':
  'Mot VW ID.5, som är den närmaste tekniska släktingen, ligger Tavascan i samma härad. Mot '
  'Tesla Model Y har Tavascan en fördel i verkstadsval och en nackdel i dataunderlag. Mot en '
  'Volvo EX40 är skillnaden liten i premie men tydlig i verkstadsnät, där Volvo fortfarande '
  'har flest servicepunkter i Sverige.',
 'kostnad':
  'Tavascan är dyrare att köpa än Born och kostar mer i både premie och värdeminskning. Den '
  'post som kan bli oväntat stor är däck: stora fälgar och en tung bil sliter fort, och '
  'ersättningsdäck i den dimensionen är dyra. Försäkringsmässigt är det värt att komma ihåg '
  'att fälgskador mot kantsten ofta faller utanför försäkringen helt, eftersom de saknar '
  'yttre händelse i villkorens mening. Ett råd som gäller särskilt den här modellen: begär offert både med och utan de största fälgarna om du står inför ett utrustningsval. Fälgstorleken påverkar både däckkostnaden och risken för skador mot kantsten, och på en bil som redan har en stor bakruta att ta hänsyn till kan det bli en märkbar skillnad över tid.',
 'lang': ('Hur många hyrbilsdagar bör jag ha på en Cupra Tavascan?',
  'Så många som möjligt. Bilen tillverkas i Kina och delvägarna har varit ojämna, vilket gör '
  'väntetid vid skada till den mest sannolika kostnaden. Jämför hyrbilsmomentet före '
  'självrisken på den här modellen.'),
 'lang2': ('Är Cupra Tavascan samma bil som VW ID.5?',
  'Inte samma bil, men samma grund. Båda bygger på MEB-plattformen och delar en stor del av '
  'tekniken. Karossen, avstämningen och utrustningen skiljer sig, och Tavascan tillverkas i '
  'Kina medan ID.5 byggs i Tyskland.'),
},

'terramar': {
 'meta': 'Cupras största SUV med förbränningsmotor',
 'direktsvar':
  'Cupra Terramar är ny på marknaden och delar teknik med Audi Q3, vilket ger god '
  'delstillgång från start. Nya bilar har normalt vagnskadegaranti i tre år, och under den '
  'tiden räcker halvförsäkring. Jämför brett medan bolagen fortfarande kalibrerar sina '
  'priser för modellen.',
 'agare':
  'Terramar riktar sig till hushåll som vill ha en större SUV än Formentor men inte vill gå '
  'över till el. Det är en grupp som blivit mindre men långt ifrån försvunnit, särskilt '
  'utanför storstäderna där laddmöjligheterna är sämre och körsträckorna längre. Just den '
  'geografin påverkar premien positivt: bilar utanför storstad drabbas av färre '
  'parkeringsskador och färre stölder. Laddhybridversionen har högre ersättningsvärde än '
  'mildhybriden och kostar därmed mer att försäkra.',
 'teknik':
  'Terramar bygger på samma grund som Audi Q3, vilket betyder beprövad teknik och en '
  'delkatalog som redan finns hos verkstäderna. Det är en underskattad fördel för en ny '
  'modell — normalt betalar du ett osäkerhetspåslag på en bil ingen har statistik på, men när '
  'plattformen är känd blir påslaget litet. Laddhybriddrivlinan är den enda komponent som '
  'kräver särskild kompetens, och den finns i en rad koncernmodeller sedan flera år.',
 'jamfor':
  'Mot Audi Q3 ligger Terramar lägre i premie, eftersom nypriset och därmed '
  'ersättningsvärdet är lägre. Mot Formentor är den dyrare, vilket följer av storleken. Mot '
  'en VW Tiguan är skillnaden liten i teknik och något större i premie, av samma skäl som '
  'gäller alla Cupra: prestandaprofilen och den yngre ägarprofilen väger in.',
 'kostnad':
  'På en ny bil är värdeminskningen den överlägset största kostnaden de första åren, och '
  'försäkringen en mindre post i sammanhanget. Det är också därför skyddsnivån är viktigare '
  'än premien här: har bilen vagnskadegaranti räcker halvförsäkring i tre år, och '
  'skillnaden mot helförsäkring under den perioden är pengar du kan behålla utan att '
  'försämra skyddet.',
 'lang': ('Räcker halvförsäkring på en ny Cupra Terramar?',
  'Ja, så länge vagnskadegarantin gäller. Den följer normalt med nya bilar i tre år från '
  'första registrering och täcker samma sak som vagnskadedelen i en helförsäkring. '
  'Kontrollera garantins längd på just ditt exemplar och sätt en påminnelse när den går ut.'),
 'lang2': ('Delar Cupra Terramar teknik med Audi Q3?',
  'Ja, bilarna bygger på samma koncernplattform och delar en stor del av tekniken och '
  'delkatalogen. Det är en fördel för dig, eftersom en ny modell på en beprövad plattform '
  'sällan prissätts med osäkerhetspåslag.'),
},

'ateca': {
 'meta': 'utgången prestandaversion av Seat Ateca',
 'direktsvar':
  'Cupra Ateca har utgått ur nyproduktionen, vilket har fått begagnatpriserna att falla. '
  'Premien följer marknadsvärdet nedåt, men effektklassen och fyrhjulsdriften håller emot. '
  'Det gör att skyddsnivån är värd att räkna om varje år på den här modellen.',
 'agare':
  'Cupra Ateca köps i dag begagnad, ofta av förare som vill ha fyrhjulsdrift och prestanda '
  'till ett pris som inte längre motsvarar bilens ursprungliga position. Det skapar samma '
  'situation som på en äldre Tesla Model S, fast i mindre skala: bilen är billig att köpa och '
  'relativt dyr att försäkra, eftersom premien speglar effekt och reparationskostnad snarare '
  'än inköpspris. Är du medveten om det från början är det inget problem — det är när man '
  'räknar på inköpspriset ensamt som kalkylen spricker.',
 'teknik':
  'Fyrhjulsdriften är den tekniska post som betyder mest. Systemet innehåller en '
  'bakaxelkoppling och en kardanaxel, komponenter som blir dyra vid en påkörning bakifrån och '
  'som inte finns på framhjulsdrivna syskonmodeller. I övrigt är bilen en Seat Ateca under '
  'plåten, med samma delkatalog som VW Tiguan — vilket betyder att den vanligaste sortens '
  'skada, plåtskador fram och bak, är förhållandevis billig att åtgärda.',
 'jamfor':
  'Mot en jämngammal VW Tiguan ligger Cupra Ateca högre i premie trots delad teknik, av samma '
  'skäl som gäller hela Cupra-utbudet. Mot en Audi SQ2 eller BMW X2 M35i är den billigare, '
  'både att köpa och att försäkra. Det verkligt intressanta är jämförelsen mot sig själv över '
  'tid: premien faller långsammare än marknadsvärdet, vilket är precis varför skyddsnivån bör '
  'omprövas årligen.',
 'kostnad':
  'På en utgången modell är värdeminskningen låg i kronor, medan bränsle, däck och '
  'försäkring är oförändrade. Det gör att försäkringen med tiden blir en allt större andel av '
  'vad bilen kostar att äga. När marknadsvärdet passerar omkring 150 000 kr bör du räkna på '
  'om vagnskadedelen fortfarande är värd sin premie — det är den beräkningen som avgör mer '
  'än valet av bolag.',
 'lang': ('Går det att teckna ny försäkring på en Cupra Ateca?',
  'Ja, utan problem. Att en modell utgått ur nyproduktionen påverkar varken möjligheten att '
  'teckna eller villkoren. Delstillgången är dessutom god eftersom bilen delar teknik med '
  'Seat och Volkswagen.'),
 'lang2': ('När bör jag gå från hel- till halvförsäkring på en Cupra Ateca?',
  'När marknadsvärdet närmar sig 150 000 kr är det dags att räkna. Vagnskadedelen ersätter '
  'värdet minus självrisken, och när den summan blir liten i förhållande till premien har '
  'halvförsäkring blivit det rationella valet.'),
},
}
