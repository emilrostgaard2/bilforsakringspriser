# -*- coding: utf-8 -*-
"""Bilmärken på den svenska marknaden.

'karakteristik' är det som gör varje sida unik — en faktisk egenskap hos märket
som påverkar försäkringspremien. Ingen sida får återanvända en annan sidas text.

Priserna är PLATSHÅLLARE tills egen insamling gjorts. Se README.
"""

MARKEN = [
{'slug':'volvo','namn':'Volvo','grupp':'premium','ursprung':'Sverige',
 'karakteristik':'Volvo är Sveriges mest sålda bilmärke och därmed också det mest försäkrade. '
   'Det stora beståndet betyder gott om reservdelar, en väldokumenterad skadestatistik och ett '
   'tätt verkstadsnät i hela landet — tre faktorer som håller premien nere trots att bilarna '
   'ofta ligger högt i inköpspris. Märket har dessutom en egen försäkring, Volvia, som drivs av If.',
 'modeller':['XC60','XC40','V60','V90','XC90','S60','EX30','EX40'],
 'punkter':['Störst bestånd i Sverige — bred tillgång på delar och verkstäder',
            'Egen märkesförsäkring via Volvia',
            'Höga säkerhetsbetyg påverkar personskaderisken positivt']},

{'slug':'volkswagen','namn':'Volkswagen','grupp':'volym','ursprung':'Tyskland',
 'karakteristik':'Volkswagen delar plattform, motorer och reservdelskatalog med Skoda, Seat, '
   'Cupra och Audi. Den enorma volymen inom VAG-koncernen gör delar billiga och tillgängliga '
   'hos i stort sett varje fristående verkstad — vilket är den viktigaste enskilda förklaringen '
   'till att en Golf kostar mindre att försäkra än en jämnstor bil från ett smalare märke.',
 'modeller':['Golf','Passat','Tiguan','Polo','ID.4','ID.3','ID.7','ID. Buzz',
             'Tayron','T-Roc','Touran'],
 'punkter':['Delar teknik med Skoda, Seat, Cupra och Audi',
            'Reservdelar kan skaffas av nästan alla verkstäder',
            'Fritt verkstadsval är därför mer värt här än på smalare märken']},

{'slug':'toyota','namn':'Toyota','grupp':'volym','ursprung':'Japan',
 'karakteristik':'Toyota har i decennier legat i topp i europeiska tillförlitlighetsmätningar. '
   'För ett försäkringsbolag betyder färre driftstopp färre bärgningar och färre följdskador, '
   'och det syns i premien. Hybridtekniken är dessutom välbeprövad — batteriet är ett litet '
   'buffertbatteri, inte ett stort drivbatteri, vilket gör att Toyotas hybrider prissätts '
   'nära bensinbilar och inte nära elbilar.',
 'modeller':['Yaris','Yaris Cross','Corolla','Corolla Cross','RAV4','C-HR',
             'Aygo X','bZ4X','Camry','Land Cruiser'],
 'punkter':['Låg skadefrekvens ger lägre premie',
            'Hybridbatteriet är litet och billigt jämfört med elbil',
            'Hybridgarantin kan förlängas med årlig kontroll']},

{'slug':'kia','namn':'Kia','grupp':'volym','ursprung':'Sydkorea',
 'karakteristik':'Kias sjuåriga nybilsgaranti följer bilen och inte ägaren, vilket håller '
   'andrahandsvärdet uppe längre än hos många konkurrenter. Det påverkar dig direkt vid '
   'totalskada, eftersom ersättningen räknas på marknadsvärdet. Elbilarna delar E-GMP-plattform '
   'med Hyundai, vilket ger volym i reservdelskatalogen.',
 'modeller':['Sportage','Niro','EV6','EV9','EV3','Ceed','XCeed','Stonic',
             'Picanto','Sorento'],
 'punkter':['Sju års garanti som följer bilen håller uppe restvärdet',
            'E-GMP-plattformen delas med Hyundai',
            'Elbilar kräver uttryckligt batteriskydd i villkoren']},

{'slug':'bmw','namn':'BMW','grupp':'premium','ursprung':'Tyskland',
 'karakteristik':'BMW ligger konsekvent över snittet i premie, och orsaken är sällan den man '
   'tror. Det handlar mindre om effekt och mer om reservdelspriser och den förarassistans som '
   'sitter bakom vindrutan: en rutbyte med kalibrering kostar mångdubbelt mot en enklare bil. '
   'M-modellerna hamnar i en egen riskklass där flera bolag kräver förhöjd självrisk.',
 'modeller':['3-serie','5-serie','X1','X3','X5','iX1','iX3','i4','i5','iX'],
 'punkter':['Dyra reservdelar driver kaskopremien',
            'ADAS bakom vindrutan gör rutbyten kostsamma',
            'M-modeller placeras i högsta effektgruppen']},

{'slug':'audi','namn':'Audi','grupp':'premium','ursprung':'Tyskland',
 'karakteristik':'Audi bygger på VAG-plattformar, vilket gör grundtekniken välkänd och '
   'delarna tillgängliga. Ändå ligger premien över Volkswagen med motsvarande motor, och '
   'skillnaden ligger i nypriset: kaskopremien räknas på vad bilen kostar att ersätta. '
   'Quattro-modellerna har fler komponenter som kan ta skada vid en påkörning.',
 'modeller':['A4','A6','A3','Q3','Q5','Q7','Q4 e-tron','Q6 e-tron',
             'A6 e-tron','e-tron GT'],
 'punkter':['Samma plattform som VW men högre nypris ger högre premie',
            'Quattro innebär fler skadekänsliga komponenter',
            'Stora fälgar är dyra att ersätta och täcks bara av helförsäkring']},

{'slug':'mercedes','namn':'Mercedes-Benz','grupp':'premium','ursprung':'Tyskland',
 'karakteristik':'Mercedes ligger i den dyrare änden på både halv- och helförsäkring. '
   'Reservdelar är kostsamma, servicenätet är smalare än hos volymmärkena, och modellerna är '
   'överrepresenterade i stöldstatistiken i storstadsområden. Bopostnumret väger därför tyngre '
   'här än på ett genomsnittligt märke.',
 'modeller':['C-Klass','E-Klass','A-Klass','CLA','GLA','GLB','GLC','GLE',
             'EQA','V-Klass'],
 'punkter':['Höga reservdelspriser slår igenom på kaskopremien',
            'Stöldrisken påverkar premien mer i storstad',
            'Smalare verkstadsnät än volymmärkena']},

{'slug':'skoda','namn':'Skoda','grupp':'volym','ursprung':'Tjeckien',
 'karakteristik':'Skoda är den billigaste vägen in i VAG-tekniken. Samma plattformar, samma '
   'motorer och samma reservdelskatalog som Volkswagen — men ett lägre nypris. Eftersom '
   'kaskopremien beräknas på ersättningsvärdet innebär det en märkbart lägre premie för i '
   'praktiken samma bil.',
 'modeller':['Octavia','Superb','Kodiaq','Karoq','Fabia','Enyaq','Elroq',
             'Kamiq','Scala','Yeti'],
 'punkter':['Samma teknik som VW till lägre nypris',
            'Lägre ersättningsvärde ger lägre kaskopremie',
            'Reservdelar finns hos alla VAG-kunniga verkstäder']},

{'slug':'tesla','namn':'Tesla','grupp':'elbil','ursprung':'USA',
 'karakteristik':'Tesla är bland de dyraste att helförsäkra i Sverige. Tre skäl: batteriet '
   'utgör en stor del av bilens värde, karossen är delvis gjuten i stora sektioner som är '
   'kostsamma att reparera, och verkstadsnätet är smalare än hos etablerade märken. Fritt '
   'verkstadsval är därför mindre värt här — det finns färre ställen att välja mellan.',
 'modeller':['Model 3','Model Y','Model S','Model X'],
 'punkter':['Batteriet är en tredjedel av bilens värde',
            'Gjutna karosssektioner fördyrar reparationer',
            'Smalt verkstadsnät begränsar valfriheten']},

{'slug':'ford','namn':'Ford','grupp':'volym','ursprung':'USA',
 'karakteristik':'Ford har ett stort bestånd av äldre bilar i Sverige, vilket ger god '
   'tillgång på begagnade delar och lägre reparationskostnader. För de äldsta modellerna är '
   'det ofta halvförsäkring snarare än helförsäkring som är det rationella valet, eftersom '
   'vagnskadans ersättning ändå begränsas av marknadsvärdet.',
 'modeller':['Focus','Kuga','Fiesta','Puma','Mondeo','Transit','Mustang Mach-E','Ranger'],
 'punkter':['Stort bestånd av äldre bilar ger billiga delar',
            'På äldre modeller räcker ofta halvförsäkring',
            'Mustang Mach-E prissätts som elbil, inte som Ford']},

{'slug':'peugeot','namn':'Peugeot','grupp':'volym','ursprung':'Frankrike',
 'karakteristik':'Peugeot ingår i Stellantis tillsammans med Citroën, Opel, Fiat och Jeep. '
   'Koncerntillhörigheten har breddat reservdelstillgången de senaste åren och pressat '
   'reparationskostnaderna. Elbilsvarianterna delar teknik med Opel, vilket ger volymfördelar '
   'som mindre elbilsmärken saknar.',
 'modeller':['208','e-208','2008','308','408','3008','5008','508',
             'Rifter','Traveller'],
 'punkter':['Stellantis-tillhörigheten ger bredare delstillgång',
            'Elbilar delar teknik med Opel',
            'Dieselmodeller är dyrare att kaskoförsäkra än bensin']},

{'slug':'renault','namn':'Renault','grupp':'volym','ursprung':'Frankrike',
 'karakteristik':'Renault delar teknik med Dacia och Nissan genom alliansen. E-Tech-hybriden '
   'är tekniskt ovanlig med en kopplingslös växellåda som få fristående verkstäder har vana '
   'vid, vilket oftare leder till märkesverkstad — och det prissätter bolagen in.',
 'modeller':['Clio','Captur','Megane','Zoe','Arkana','Austral','Kangoo','Scenic'],
 'punkter':['Delar teknik med Dacia och Nissan',
            'E-Tech-växellådan hänvisas oftare till märkesverkstad',
            'Zoe var tidigt ute — batterileasing förekommer på begagnade']},

{'slug':'hyundai','namn':'Hyundai','grupp':'volym','ursprung':'Sydkorea',
 'karakteristik':'Hyundai delar E-GMP-plattform med Kia, och den kombinerade volymen inom '
   'koncernen håller reservdelspriserna nere även på elbilarna. IONIQ-modellernas '
   '800-voltsteknik uppfattas ofta som dyr att försäkra, men i praktiken prissätts de närmare '
   'en Volkswagen ID.4 än en Tesla.',
 'modeller':['Kona','Tucson','IONIQ 5','IONIQ 6','INSTER','Santa Fe','Bayon',
             'i20','i10','IONIQ 9'],
 'punkter':['E-GMP-plattformen delas med Kia',
            '800-voltstekniken är inte dyrare att försäkra än den uppfattas',
            'Fem års garanti utan milbegränsning']},

{'slug':'nissan','namn':'Nissan','grupp':'volym','ursprung':'Japan',
 'karakteristik':'Nissans e-POWER förvirrar både ägare och bolag. Bilen har en elmotor som '
   'driver hjulen, men förbränningsmotorn fungerar bara som generator — den laddas aldrig från '
   'ett uttag. Tekniskt är det en seriehybrid, och den ska inte prissättas som elbil. Får du '
   'en offert på elbilsnivå är det värt att fråga hur bolaget klassificerat bilen.',
 'modeller':['Qashqai','Juke','Leaf','X-Trail','Ariya','Micra','Townstar'],
 'punkter':['e-POWER är en seriehybrid, inte en laddhybrid',
            'Kontrollera att bolaget inte klassat bilen som elbil',
            'Leaf har ett äldre batterikoncept utan aktiv kylning']},

{'slug':'opel','namn':'Opel','grupp':'volym','ursprung':'Tyskland',
 'karakteristik':'Opel bytte ägare från General Motors till PSA och ingår idag i Stellantis. '
   'Nyare modeller delar därför plattform med Peugeot och Citroën, medan äldre bygger på '
   'GM-teknik. Det betyder att reservdelsbilden skiljer sig markant mellan årsmodeller — '
   'kontrollera vilken generation din bil tillhör.',
 'modeller':['Corsa','Astra','Mokka','Grandland','Crossland','Combo','Zafira'],
 'punkter':['Nyare modeller delar teknik med Peugeot och Citroën',
            'Äldre modeller bygger på GM-teknik med annan delsbild',
            'Elvarianterna är tekniskt identiska med Peugeots']},

{'slug':'seat','namn':'Seat','grupp':'volym','ursprung':'Spanien',
 'karakteristik':'Seat bygger på MQB-plattformen och delar reservdelskatalog med Volkswagen '
   'Polo och Skoda Fabia. FR-utrustningen är i grunden kosmetisk, men de större fälgarna är '
   'dyrare att ersätta och tar oftare skada vid trottoarkanter — vilket bolagen prissätter in '
   'även när effekten är oförändrad.',
 'modeller':['Ibiza','Leon','Arona','Ateca','Tarraco'],
 'punkter':['MQB-plattformen delas med Polo och Fabia',
            'FR-paketets stora fälgar höjer premien',
            'Fälgskador täcks bara av helförsäkring']},

{'slug':'cupra','namn':'Cupra','grupp':'premium','ursprung':'Spanien',
 'karakteristik':'Cupra är inte en uppgraderad Seat utan ett eget märke med egen prissättning. '
   'Tekniken under är densamma, men nypriset ligger betydligt högre — och prestandaprofilen ger '
   'en dokumenterat högre skadefrekvens. VZ-varianterna hamnar i högsta effektgruppen där flera '
   'bolag kräver förhöjd självrisk.',
 'modeller':['Formentor','Leon','Born','Ateca','Tavascan'],
 'punkter':['Samma plattform som Seat men markant högre nypris',
            'Prestandaprofil ger högre skadefrekvens',
            'VZ-modeller kan kräva förhöjd självrisk']},

{'slug':'mazda','namn':'Mazda','grupp':'volym','ursprung':'Japan',
 'karakteristik':'Mazda ligger stabilt i mittfältet. Bolaget har hållit fast vid '
   'förbränningsmotorer längre än många konkurrenter, vilket innebär färre av de dyra '
   'högvoltskomponenter som driver upp premien på elektrifierade bilar. Skadestatistiken är '
   'välkänd och utan ytterligheter.',
 'modeller':['CX-5','CX-30','Mazda2','Mazda3','CX-60','MX-5','CX-80'],
 'punkter':['Få högvoltskomponenter i beståndet',
            'Välkänd skadestatistik utan ytterligheter',
            'MX-5 prissätts som sportbil, inte som Mazda']},

{'slug':'mitsubishi','namn':'Mitsubishi','grupp':'volym','ursprung':'Japan',
 'karakteristik':'Mitsubishi var tidigt ute med laddhybrider i Sverige, och Outlander PHEV '
   'finns i stort antal på begagnatmarknaden. Vid köp av en begagnad laddhybrid är '
   'batteriets kondition avgörande — begär ett kapacitetsintyg, eftersom försäkringen inte '
   'ersätter normalt åldrande.',
 'modeller':['Outlander','ASX','Space Star','Eclipse Cross','Colt'],
 'punkter':['Stort bestånd begagnade laddhybrider',
            'Batterikondition bör kontrolleras vid köp',
            'Försäkringen ersätter inte normalt kapacitetstapp']},

{'slug':'dacia','namn':'Dacia','grupp':'budget','ursprung':'Rumänien',
 'karakteristik':'Dacia är bland de billigaste bilarna att försäkra i Sverige, och '
   'förklaringen är enkel: kaskopremien beräknas på vad bilen kostar att ersätta, och Dacias '
   'nypris är marknadens lägsta i sina klasser. Den avskalade utrustningen betyder dessutom '
   'färre sensorer och därmed billigare vindrutor och stötfångare.',
 'modeller':['Sandero','Duster','Jogger','Spring','Bigster'],
 'punkter':['Lägsta nypris i klassen ger lägsta kaskopremie',
            'Färre sensorer gör rutor och stötfångare billigare',
            'Överväg om helförsäkring alls behövs']},

{'slug':'citroen','namn':'Citroën','grupp':'volym','ursprung':'Frankrike',
 'karakteristik':'Citroën ingår i Stellantis och delar teknik med Peugeot och Opel. Märket '
   'har profilerat sig på komfort snarare än prestanda, vilket ger en förarprofil med lägre '
   'genomsnittlig skadefrekvens än hos sportigare märken i samma prisklass.',
 'modeller':['C3','C4','C5 Aircross','Berlingo','ë-C4','C3 Aircross'],
 'punkter':['Delar teknik med Peugeot och Opel',
            'Komfortprofil ger lägre skadefrekvens',
            'Berlingo används ofta i tjänst — kontrollera användningsområdet']},

{'slug':'mini','namn':'MINI','grupp':'premium','ursprung':'Storbritannien',
 'karakteristik':'MINI ägs av BMW och delar teknik med 1-serien, men prissätts som ett eget '
   'märke. Bilarna används i hög grad i storstad, där parkeringsskador och skadegörelse är '
   'vanligare — vilket gör bopostnumret till en tyngre faktor än på ett genomsnittligt märke.',
 'modeller':['Cooper','Countryman','Clubman','Cooper SE'],
 'punkter':['Delar teknik med BMW 1-serie',
            'Storstadsanvändning höjer risken för parkeringsskador',
            'John Cooper Works placeras i högre effektgrupp']},

{'slug':'suzuki','namn':'Suzuki','grupp':'volym','ursprung':'Japan',
 'karakteristik':'Suzuki bygger små, lätta bilar med enkel teknik. Låg vikt betyder mindre '
   'skada vid kollision — både på den egna bilen och på motparten — och det syns i premien. '
   'Bolaget har få elektrifierade modeller, vilket innebär färre dyra komponenter.',
 'modeller':['Swift','Vitara','S-Cross','Ignis','Across','Jimny'],
 'punkter':['Låg vikt ger mindre skada vid kollision',
            'Enkel teknik håller reparationskostnaden nere',
            'Jimny är en terrängbil och prissätts därefter']},

{'slug':'honda','namn':'Honda','grupp':'volym','ursprung':'Japan',
 'karakteristik':'Honda har ett mindre bestånd i Sverige än de japanska konkurrenterna, '
   'vilket ger ett smalare verkstadsnät. Tillförlitligheten är hög, men vid en skada kan '
   'väntetiden bli längre än på ett volymmärke — kontrollera villkoren för hyrbil.',
 'modeller':['Jazz','CR-V','HR-V','Civic','ZR-V','e:Ny1'],
 'punkter':['Mindre bestånd ger smalare verkstadsnät',
            'Hög tillförlitlighet men längre väntetid vid skada',
            'Hyrbilsmomentet är mer värt här än på volymmärken']},

{'slug':'polestar','namn':'Polestar','grupp':'elbil','ursprung':'Sverige',
 'karakteristik':'Polestar delar teknik och verkstadsnät med Volvo, vilket är en fördel '
   'jämfört med fristående elbilsmärken. Bilarna är tunga, och vikten är en underskattad '
   'premiefaktor: en tyngre bil orsakar större skada vid kollision, både på sig själv och på '
   'motparten.',
 'modeller':['Polestar 2','Polestar 3','Polestar 4'],
 'punkter':['Delar verkstadsnät med Volvo',
            'Hög vikt är en underskattad premiefaktor',
            'Batteriskydd måste framgå uttryckligen av villkoren']},

{'slug':'mg','namn':'MG','grupp':'elbil','ursprung':'Kina',
 'karakteristik':'MG ägs av kinesiska SAIC och har vuxit snabbt i Sverige på låga priser. '
   'Reservdelskedjan är kortare än hos etablerade märken, vilket kan ge längre väntetid vid '
   'skada. Kontrollera hyrbilsmomentet och hur många dagar det täcker innan du tecknar.',
 'modeller':['MG4','ZS','MG5','Marvel R','MG3'],
 'punkter':['Låga nypriser ger låg kaskopremie',
            'Kortare reservdelskedja kan ge väntetid',
            'Hyrbilsmomentet är särskilt relevant']},

{'slug':'byd','namn':'BYD','grupp':'elbil','ursprung':'Kina',
 'karakteristik':'BYD tillverkar sina egna batterier, vilket är ovanligt och ger bolaget '
   'kontroll över den dyraste komponenten. På den svenska marknaden är märket nytt, och '
   'skadestatistiken därmed tunn — vilket gör att bolagen prissätter med en viss försiktighet '
   'tills underlaget blivit större.',
 'modeller':['Atto 3','Dolphin','Seal','Sealion 7','Tang'],
 'punkter':['Egen batteritillverkning',
            'Tunn skadestatistik gör prissättningen försiktig',
            'Verkstadsnätet byggs fortfarande ut']},

{'slug':'jeep','namn':'Jeep','grupp':'suv','ursprung':'USA',
 'karakteristik':'Jeep ingår i Stellantis. Terrängprofilen betyder att bilarna används i '
   'miljöer där skador är vanligare, och fyrhjulsdriften innehåller komponenter som är dyra '
   'att reparera efter en påkörning bakifrån. Nyare modeller delar teknik med Peugeot.',
 'modeller':['Compass','Renegade','Avenger','Wrangler','Grand Cherokee'],
 'punkter':['Terränganvändning ökar skaderisken',
            'Fyrhjulsdriftens komponenter är dyra att reparera',
            'Nyare modeller delar teknik med Peugeot']},

{'slug':'porsche','namn':'Porsche','grupp':'premium','ursprung':'Tyskland',
 'karakteristik':'Porsche placeras i högsta effektgruppen hos i stort sett samtliga bolag. '
   'Flera kräver förhöjd självrisk, och ett par försäkrar inte förare under trettio. Premien '
   'styrs mer av effekt och nypris än av hur du faktiskt kör — hämta offert innan du köper '
   'bilen, inte efter.',
 'modeller':['911','Macan','Cayenne','Taycan','718'],
 'punkter':['Högsta effektgruppen hos i stort sett alla bolag',
            'Flera bolag kräver förhöjd självrisk',
            'Hämta offert före köpet, inte efter']},

{'slug':'fiat','namn':'Fiat','grupp':'budget','ursprung':'Italien',
 'karakteristik':'Fiat ingår i Stellantis och tillverkar små stadsbilar med lågt nypris — '
   'vilket ger låg kaskopremie. Bilarna används mest i tätort, där parkeringsskador utgör en '
   'stor andel av skadorna. Kontrollera hur bolaget hanterar skador utan känd motpart.',
 'modeller':['500','Panda','500e','Tipo','Ducato'],
 'punkter':['Lågt nypris ger låg kaskopremie',
            'Stadsanvändning ger många parkeringsskador',
            'Ducato används i tjänst — kontrollera användningsområdet']},

{'slug':'subaru','namn':'Subaru','grupp':'suv','ursprung':'Japan',
 'karakteristik':'Subaru har permanent fyrhjulsdrift som standard, vilket är ovanligt. Det '
   'ger goda vinteregenskaper men innebär också fler komponenter som kan ta skada. Beståndet '
   'i Sverige är litet, vilket ger ett smalare verkstadsnät än volymmärkena.',
 'modeller':['Forester','Outback','XV','Solterra','Impreza'],
 'punkter':['Permanent fyrhjulsdrift innehåller fler skadekänsliga delar',
            'Litet bestånd ger smalare verkstadsnät',
            'Starkt i vinterförhållanden — men det sänker inte premien']},

{'slug':'lexus','namn':'Lexus','grupp':'premium','ursprung':'Japan',
 'karakteristik':'Lexus är Toyotas premiummärke och ärver koncernens låga skadefrekvens. '
   'Nypriset är dock betydligt högre, och eftersom kaskopremien räknas på ersättningsvärdet '
   'landar den över Toyota med motsvarande storlek. Hybridtekniken är densamma och lika '
   'välbeprövad.',
 'modeller':['UX','NX','RX','ES','LBX'],
 'punkter':['Ärver Toyotas låga skadefrekvens',
            'Högre nypris ger högre kaskopremie',
            'Samma välbeprövade hybridteknik som Toyota']},

{'slug':'land-rover','namn':'Land Rover','grupp':'suv','ursprung':'Storbritannien',
 'karakteristik':'Land Rover ligger högt i både premie och stöldstatistik. Modellerna har '
   'varit överrepresenterade i stöldligornas målbild i flera europeiska länder, och flera '
   'bolag ställer krav på spårsändare eller extra stöldskydd för att teckna helförsäkring.',
 'modeller':['Range Rover Evoque','Discovery Sport','Defender','Range Rover Sport'],
 'punkter':['Överrepresenterad i stöldstatistiken',
            'Flera bolag kräver spårsändare',
            'Höga reservdelspriser och smalt verkstadsnät']},

{'slug':'alfa-romeo','namn':'Alfa Romeo','grupp':'premium','ursprung':'Italien',
 'karakteristik':'Alfa Romeo ingår i Stellantis men har ett litet bestånd i Sverige. '
   'Kombinationen av sportig profil, begränsad reservdelstillgång och få specialiserade '
   'verkstäder gör att premien ligger högre än vad nypriset ensamt skulle motivera.',
 'modeller':['Giulia','Stelvio','Tonale','Junior'],
 'punkter':['Litet bestånd ger begränsad reservdelstillgång',
            'Sportig profil höjer skadefrekvensen',
            'Fritt verkstadsval är extra värdefullt här']},

{'slug':'xpeng','namn':'XPeng','grupp':'elbil','ursprung':'Kina',
 'karakteristik':'XPeng är ny på den svenska marknaden och saknar ännu bred skadestatistik. '
   'Bilarna är välutrustade med förarassistans, vilket gör vindrutorna dyra att byta eftersom '
   'sensorerna måste kalibreras. Glasmomentet med låg självrisk är därför mer värt här än på '
   'en enklare bil.',
 'modeller':['G9','G6','P7'],
 'punkter':['Ny på marknaden — tunn skadestatistik',
            'Omfattande förarassistans fördyrar rutbyten',
            'Verkstadsnätet är fortfarande begränsat']},

{'slug':'jaguar','namn':'Jaguar','grupp':'premium','ursprung':'Storbritannien',
 'karakteristik':'Jaguar delar koncern och verkstadsnät med Land Rover och har ett litet '
   'bestånd i Sverige. Karosserna är i stor utsträckning byggda i aluminium, vilket kräver '
   'certifierad utrustning för att repareras korrekt — antalet verkstäder som får göra jobbet '
   'är därför begränsat och timpriset högt. Det, snarare än effekten, är det som lyfter '
   'kaskopremien mest.',
 'modeller':['F-Pace','E-Pace','I-Pace','XE','XF','F-Type'],
 'punkter':['Aluminiumkarosser kräver certifierad verkstad',
            'Litet bestånd ger längre väntan på delar',
            'Kontrollera att bolaget accepterar märkesverkstad i villkoren']},

{'slug':'zeekr','namn':'Zeekr','grupp':'elbil','ursprung':'Kina',
 'karakteristik':'Zeekr ingår i Geely-koncernen, samma ägare som Volvo och Polestar, och delar '
   'delar av utvecklingsarbetet med de svenska systermärkena. Det gör tekniken mindre främmande '
   'för verkstäderna än hos flera andra nya kinesiska märken. Beståndet i Sverige är ändå litet '
   'och skadestatistiken tunn, och den osäkerheten prissätter bolagen in tills siffrorna finns.',
 'modeller':['X','001','7X'],
 'punkter':['Geely-koncernen — samma ägare som Volvo och Polestar',
            'Litet bestånd ger tunn skadestatistik och försiktig prissättning',
            'Fråga hur reservdelar hanteras innan du tecknar']},
]

# ═══ BILDTEXTER ═════════════════════════════════════════════════════
# Per märke: 'alt' beskriver bilden (tillgänglighet + bildsök),
# 'cap' är den synliga bildtexten och ska säga något eget om just det
# märkets premie — aldrig samma formulering på två sidor.
# Märken som saknar nyckel här faller tillbaka på en generisk text i
# generators.py. Filnamnet måste vara bilder/<slug>.webp.

BILD = {
'volkswagen': {
  'alt': 'Silverfärgad Volkswagen ID.4 på en kustväg',
  'cap': 'Volkswagen ID.4. Den delade VAG-tekniken gör att nästan varje verkstad kan '
         'skaffa delarna — den enskilt viktigaste orsaken till att premien håller sig nere.'},
'toyota': {
  'alt': 'Silverfärgad Toyota Corolla parkerad längs en våt gata',
  'cap': 'Toyota Corolla. Låg skadefrekvens ger färre bärgningar och färre följdskador, '
         'och det syns direkt i premien.'},
'bmw': {
  'alt': 'Silverfärgad BMW M4 Competition på en kustväg i kvällsljus',
  'cap': 'BMW M4. Det är reservdelspriserna och kalibreringen av förarassistansen som '
         'driver kaskopremien — inte hästkrafterna i sig.'},
'audi': {
  'alt': 'Silverfärgad Audi e-tron GT på en bergsväg i skymning',
  'cap': 'Audi e-tron GT. Kaskopremien räknas på vad bilen kostar att ersätta, vilket '
         'förklarar avståndet till en Volkswagen med samma grundteknik.'},
'skoda': {
  'alt': 'Silverfärgad Skoda Octavia Combi på en kustväg vid en småbåtshamn',
  'cap': 'Skoda Octavia Combi. Samma delkatalog som Volkswagen, men lägre nypris — '
         'kombinationen ger ofta den lägsta premien i klassen.'},
'ford': {
  'alt': 'Silverfärgad Ford Focus parkerad på en butiksgata',
  'cap': 'Ford Focus. Ett stort begagnatbestånd betyder gott om delar och verklig '
         'konkurrens mellan verkstäderna vid en skada.'},
'alfa-romeo': {
  'alt': 'Röd Alfa Romeo Giulia GTA på en kullerstensgata',
  'cap': 'Alfa Romeo Giulia. Litet bestånd och få specialiserade verkstäder lyfter premien '
         'mer än nypriset ensamt skulle motivera.'},
'kia': {
  'alt': 'Silverfärgad Kia EV6 parkerad på en uppfart framför ett villagarage',
  'cap': 'Kia EV6. Sjuårsgarantin följer bilen och håller uppe marknadsvärdet — och det är '
         'marknadsvärdet du får ersättning för vid totalskada.'},
'tesla': {
  'alt': 'Mörkblå Tesla Model 3 på en parkeringsplats',
  'cap': 'Tesla Model 3. Gjutna karossektioner och ett smalt verkstadsnät gör reparationerna '
         'dyra, vilket slår igenom på helförsäkringen.'},
'peugeot': {
  'alt': 'Grå Peugeot 308 parkerad på en gata i en stadskärna',
  'cap': 'Peugeot 308. Stellantis-tillhörigheten har breddat delstillgången och pressat '
         'reparationskostnaderna de senaste åren.'},
'renault': {
  'alt': 'Blå Renault Clio i rörelse på en kustväg',
  'cap': 'Renault Clio. E-Tech-hybridens ovanliga växellåda leder oftare till märkesverkstad, '
         'och det prissätter bolagen in.'},
'hyundai': {
  'alt': 'Blå Hyundai IONIQ 5 i rörelse på en kustväg',
  'cap': 'Hyundai IONIQ 5. 800-voltstekniken låter dyr, men den delade E-GMP-volymen med Kia '
         'håller delpriserna nere.'},
'nissan': {
  'alt': 'Grå Nissan Ariya parkerad på en kullerstensgata i en gammal bykärna',
  'cap': 'Nissan Ariya. Kontrollera att offerten inte prissätter e-POWER som elbil — det är '
         'en seriehybrid och ska inte behandlas som en laddbar bil.'},
'opel': {
  'alt': 'Röd Opel Astra Sports Tourer parkerad på en uppfart vid ett äldre hus',
  'cap': 'Opel Astra. Reservdelsbilden skiljer sig markant mellan GM-eran och Stellantis-eran '
         '— årsmodellen avgör mer här än hos de flesta märken.'},
'seat': {
  'alt': 'Grå Seat Leon Sportstourer parkerad på en uppfart i ett villaområde',
  'cap': 'Seat Leon. FR-utrustningen är i grunden kosmetisk, men de större fälgarna är dyrare '
         'att ersätta och tar oftare skada mot trottoarkanter.'},
'citroen': {
  'alt': 'Röd Citroën C4 i rörelse på en kustväg',
  'cap': 'Citroën C4. Komfortprofilen ger en förarprofil med lägre genomsnittlig skadefrekvens '
         'än sportigare märken i samma prisklass.'},
'cupra': {
  'alt': 'Kopparfärgad Cupra Formentor parkerad vid en kust med kritklippor',
  'cap': 'Cupra Formentor. Samma teknik som Seat under plåten, men högre nypris och en '
         'prestandaprofil som bolagen prissätter i en egen klass.'},
'polestar': {
  'alt': 'Blå Polestar 2 i rörelse på en kustväg',
  'cap': 'Polestar 2. Delat verkstadsnät med Volvo är en fördel — men vikten är den '
         'underskattade faktorn bakom premien.'},
'byd': {
  'alt': 'Blå BYD-elbil parkerad på en kullerstensgata i en gammal fiskeby',
  'cap': 'BYD. Egen batteritillverkning ger kontroll över bilens dyraste komponent, men det '
         'tunna svenska skadeunderlaget gör bolagen försiktiga i prissättningen.'},
'xpeng': {
  'alt': 'Silverfärgad XPeng-sedan parkerad framför en modern byggnad vid en hamnkaj',
  'cap': 'XPeng. Sensorerna bakom vindrutan måste kalibreras vid ett rutbyte — därför är '
         'glasmomentet med låg självrisk värt mer här än på en enklare bil.'},
'zeekr': {
  'alt': 'Blå Zeekr-elbil parkerad på en kullerstensplats i en gammal hamnby',
  'cap': 'Zeekr. Geely-släktskapet med Volvo och Polestar gör tekniken mindre främmande för '
         'verkstäderna än beståndets storlek antyder.'},
'mercedes': {
  'alt': 'Silverfärgad Mercedes-Benz EQS parkerad på en kaj framför en glasbyggnad',
  'cap': 'Mercedes-Benz EQS. Stöldstatistiken i storstadsområdena gör bopostnumret till en '
         'tyngre premiefaktor här än på ett genomsnittligt märke.'},
'mitsubishi': {
  'alt': 'Röd Mitsubishi Eclipse Cross parkerad vid en hamnpromenad',
  'cap': 'Mitsubishi Eclipse Cross. På begagnade laddhybrider är batteriets kondition '
         'avgörande — begär kapacitetsintyg innan du tecknar.'},
'dacia': {
  'alt': 'Grå Dacia Duster parkerad på en grusparkering i ett hedlandskap',
  'cap': 'Dacia Duster. Marknadens lägsta nypris i klassen ger också den lägsta '
         'kaskopremien — det är ersättningsvärdet som räknas.'},
'suzuki': {
  'alt': 'Blå Suzuki Swift parkerad på en kullerstensgata i en gammal stadskärna',
  'cap': 'Suzuki Swift. Låg vikt betyder mindre skada vid kollision, både på egen bil och '
         'på motparten, och det syns i premien.'},
'mini': {
  'alt': 'Mörkgrön MINI Cooper med vitt tak parkerad på en villauppfart',
  'cap': 'MINI Cooper. BMW-teknik under plåten, men storstadsanvändningen gör '
         'parkeringsskador till den vanligaste skadetypen.'},
'lexus': {
  'alt': 'Silverfärgad Lexus NX parkerad längs en villagata',
  'cap': 'Lexus NX. Toyotas låga skadefrekvens ärvs, men det högre ersättningsvärdet lyfter '
         'kaskopremien över en jämnstor Toyota.'},
'land-rover': {
  'alt': 'Silverfärgad Land Rover Defender på en lerig grusväg i ett kustlandskap',
  'cap': 'Land Rover Defender. Flera bolag kräver spårsändare eller extra stöldskydd — '
         'kontrollera kravet innan du tecknar, inte efter.'},
'jaguar': {
  'alt': 'Mörkgrön Jaguar F-Type parkerad på en kullerstensplats i en gammal stadskärna',
  'cap': 'Jaguar F-Type. Aluminiumkarossen kräver certifierad verkstad, vilket begränsar '
         'valet av reparatör mer än på de flesta premiummärken.'},
'porsche': {
  'alt': 'Röd Porsche 911 parkerad på en uppfart i ett villaområde',
  'cap': 'Porsche 911. Effektgrupp och nypris styr premien mer än körstilen — flera bolag '
         'kräver förhöjd självrisk.'},
'volvo': {
  'alt': 'Silverfärgad Volvo V60 Cross Country parkerad längs en villagata',
  'cap': 'Volvo V60 Cross Country. Landets största bestånd ger både gott om delar och den '
         'mest väldokumenterade skadestatistiken — det håller premien nere.'},
'mazda': {
  'alt': 'Röd Mazda CX-5 parkerad på en kullerstensgata i en gammal stadskärna',
  'cap': 'Mazda CX-5. Färre högvoltskomponenter än hos elektrifierade konkurrenter, och en '
         'skadebild bolagen känner väl.'},
'honda': {
  'alt': 'Silverfärgad Honda CR-V parkerad på en uppfart i ett villaområde',
  'cap': 'Honda CR-V. Tillförlitligheten är hög, men det smalare verkstadsnätet kan förlänga '
         'väntetiden — läs hyrbilsmomentet noga.'},
'mg': {
  'alt': 'Grå MG ZS parkerad längs en gata i ett villaområde',
  'cap': 'MG ZS. Den kortare reservdelskedjan är den verkliga risken — kontrollera hur många '
         'dagar hyrbilen täcker innan du tecknar.'},
'jeep': {
  'alt': 'Grön Jeep Wrangler parkerad på en parkeringsplats',
  'cap': 'Jeep Wrangler. Fyrhjulsdriften innehåller komponenter som blir dyra att laga efter '
         'en påkörning bakifrån.'},
'fiat': {
  'alt': 'Blå Fiat 500 parkerad på en uppfart framför ett garage',
  'cap': 'Fiat 500. Lågt nypris ger låg kaskopremie, men parkeringsskador utan känd motpart '
         'är den vanligaste skadan — kolla hur bolaget hanterar dem.'},
'subaru': {
  'alt': 'Blå Subaru Outback i rörelse på en kustväg',
  'cap': 'Subaru Outback. Permanent fyrhjulsdrift ger goda vinteregenskaper men fler '
         'komponenter som kan ta skada.'},
}
