# -*- coding: utf-8 -*-
"""Modelldata för Toyota.

Tio modeller: de åtta från brands.py plus Camry och Land Cruiser.

HYBRIDEN ÄR DEN RÖDA TRÅDEN
Nästan hela Toyotas svenska utbud är självladdande hybrid, och det får
en konsekvens som få tänker på: hybriddrivlinan är varken en ren
bensinbil eller en laddbar bil, och några bolag prissätter den fel.
Kontrollera att offerten inte klassar en självladdande hybrid som
laddhybrid — skillnaden i ersättningsvärde är betydande, och den går åt
fel håll för dig.
"""

MODELLER_TOYOTA = {
'toyota': [
{
 'slug': 'yaris', 'namn': 'Yaris', 'typ': 'liten halvkombi', 'ar': '2020–',
 'drivlina': 'bensin och hybrid',
 'kort': 'Toyotas småbil och en av Sveriges vanligaste hybrider.',
 'vinkel': 'Yaris är en av de billigaste bilarna att försäkra i Sverige. Låg vikt, lågt '
           'ersättningsvärde och Toyotas låga skadefrekvens drar alla åt samma håll. '
           'Hybridversionen dominerar beståndet, och den prissätts som en bensinbil — inte '
           'som en laddbar bil, vilket är viktigt att kontrollera i offerten.',
 'punkter': ['Låg vikt begränsar skadan på både egen bil och motpart',
             'Självladdande hybrid ska inte prissättas som laddhybrid',
             'GR Yaris ligger i en helt annan effektklass'],
 'skada': 'Parkeringsskador och skador mot trottoarkanter dominerar. Bilen används nästan '
          'uteslutande i tätort.',
 'varde': 'Låga men mycket stabila värden. Toyotas rykte om driftsäkerhet håller uppe '
          'begagnatpriserna på ett sätt få konkurrenter matchar.',
 'niva': 'Halvförsäkring på exemplar över fem år. Helförsäkring på nyare bilar eller om '
         'bilen står på gatan i en stad.',
 'fraga': ('Är Toyota Yaris billig att försäkra?',
           'Ja, den ligger bland de billigaste i Sverige. Låg vikt, lågt ersättningsvärde och '
           'en av marknadens lägsta skadefrekvenser gör att både trafikdelen och '
           'vagnskadedelen blir billiga.'),
},
{
 'slug': 'yaris-cross', 'namn': 'Yaris Cross', 'typ': 'liten SUV', 'ar': '2021–',
 'drivlina': 'hybrid',
 'kort': 'Yaris på högre ben och Toyotas mest sålda modell i Sverige de senaste åren.',
 'vinkel': 'Yaris Cross delar allt av betydelse med Yaris men klassas som SUV, vilket ger ett '
           'litet påslag. Skillnaden är några tior i månaden och bygger på skadestatistik för '
           'karossformen, inte på tekniska skillnader. Den högre markfrigången är samtidigt '
           'en fördel: färre underredesskador vid farthinder.',
 'punkter': ['Tekniskt nära identisk med Yaris',
             'SUV-klassningen ger något högre premie än halvkombin',
             'Fyrhjulsdrift finns men är ovanlig i det svenska beståndet'],
 'skada': 'Parkeringsskador och skador mot kantsten. Bilen används mest i tätort men har '
          'högre andel landsvägskörning än Yaris.',
 'varde': 'Starkare andrahandsvärde än Yaris, eftersom SUV-formatet efterfrågas mer.',
 'niva': 'Helförsäkring de första sex åren, därefter räkna på marknadsvärdet.',
 'fraga': ('Vad skiljer försäkringen på Yaris och Yaris Cross?',
           'Mycket lite tekniskt. Bilarna delar plattform och delar, så skillnaden ligger i '
           'klassningen och i ett något högre ersättningsvärde för Yaris Cross.'),
},
{
 'slug': 'corolla', 'namn': 'Corolla', 'typ': 'halvkombi och kombi', 'ar': '2019–',
 'drivlina': 'hybrid',
 'kort': 'Världens mest sålda bil genom tiderna och en klassisk svensk taxibil.',
 'vinkel': 'Corolla har den lägsta skadefrekvensen i Toyotas utbud och en ägarprofil som '
           'bolagen älskar. Det som drar upp genomsnittspremien är att modellen är vanlig som '
           'taxi och tjänstebil — yrkesmässig trafik är en annan riskklass, och de siffrorna '
           'gäller inte dig som privatperson.',
 'punkter': ['Lägst skadefrekvens i Toyotas utbud',
             'Vanlig som taxi — kontrollera att användningen är rätt angiven',
             'Touring Sports har lägre skadefrekvens än halvkombin'],
 'skada': 'Glasskador dominerar. Corolla används mycket i pendling och yrkestrafik, och '
          'motorvägsmilen avgör hur ofta rutan tar skada.',
 'varde': 'Bland de stabilaste andrahandsvärdena på marknaden, vilket håller uppe det belopp '
          'vagnskadedelen kan betala ut.',
 'niva': 'Helförsäkring till omkring åtta år. Därefter är halvförsäkring ofta rimligare.',
 'fraga': ('Är Toyota Corolla billig att försäkra?',
           'Ja, för sin storlek. Låg skadefrekvens och stabilt andrahandsvärde ger en av de '
           'lägre premierna i kompaktklassen. Kontrollera bara att offerten avser privat bruk '
           'och inte yrkestrafik.'),
},
{
 'slug': 'corolla-cross', 'namn': 'Corolla Cross', 'typ': 'kompakt SUV', 'ar': '2022–',
 'drivlina': 'hybrid',
 'kort': 'SUV-versionen av Corolla och Toyotas svar på Sportage och Tucson.',
 'vinkel': 'Corolla Cross ärver Corollas låga skadefrekvens men i ett format som väger mer '
           'och kostar mer att ersätta. Nettoeffekten är en premie som ligger något över '
           'Corolla men under de flesta konkurrenterna i klassen, eftersom skadestatistiken '
           'väger tungt i bolagens modeller.',
 'punkter': ['Ärver Corollas låga skadefrekvens',
             'AWD-i-versionen har elektrisk bakaxel — kontrollera villkoren',
             'Nyare modell med mindre bestånd än Corolla'],
 'skada': 'Parkeringsskador och lättare kollisioner i tätort. Bilen är bredare än Corolla och '
          'därmed mer utsatt i äldre parkeringshus.',
 'varde': 'Håller värdet väl tack vare Toyotas rykte och stark efterfrågan på hybrid-SUV:ar.',
 'niva': 'Helförsäkring till omkring åtta år så länge marknadsvärdet motiverar det.',
 'fraga': ('Är Corolla Cross dyrare att försäkra än Corolla?',
           'Något, ja. SUV-formatet ger fler parkeringsskador och ett högre ersättningsvärde. '
           'Skillnaden är dock mindre än mellan två märken i samma klass.'),
},
{
 'slug': 'rav4', 'namn': 'RAV4', 'typ': 'mellanstor SUV', 'ar': '2019–',
 'drivlina': 'hybrid och laddhybrid',
 'kort': 'Toyotas mest sålda SUV och en av Sveriges vanligaste familjebilar.',
 'vinkel': 'RAV4 finns som självladdande hybrid och som laddhybrid, och skillnaden i premie '
           'mellan dem är större än man kan tro. Laddhybriden har både högre '
           'ersättningsvärde och ett betydligt större batteri. Kontrollera att offerten avser '
           'rätt version — de säljs under samma modellnamn.',
 'punkter': ['Två hybridtyper med olika premie under samma modellnamn',
             'Laddhybriden har högst ersättningsvärde i Toyotas volymutbud',
             'Populär som dragbil — släpet behöver egen försäkring'],
 'skada': 'Parkeringsskador och viltolyckor. RAV4 används både i tätort och på landsväg, '
          'vilket ger en bredare skadebild än Toyotas mindre modeller.',
 'varde': 'Ett av marknadens starkaste andrahandsvärden, vilket håller vagnskadedelen '
          'motiverad längre än på de flesta konkurrenter.',
 'niva': 'Helförsäkring till omkring tio år, tack vare det höga marknadsvärdet.',
 'fraga': ('Är RAV4 laddhybrid dyrare att försäkra?',
           'Ja, märkbart. Den har både högre nypris och ett betydligt större batteri än den '
           'självladdande hybriden. Båda säljs som RAV4, så kontrollera att offerten avser '
           'rätt version.'),
},
{
 'slug': 'c-hr', 'namn': 'C-HR', 'typ': 'kompakt SUV-coupé', 'ar': '2023–',
 'drivlina': 'hybrid och laddhybrid',
 'kort': 'Toyotas designdrivna crossover och märkets mest särpräglade modell.',
 'vinkel': 'C-HR har en sluttande taklinje och en liten bakruta, vilket ger sämre sikt bakåt '
           'än i en konventionell SUV. Det syns i skadebilden: backningsskador är '
           'överrepresenterade jämfört med Corolla Cross i samma storlek. Sensorerna '
           'kompenserar, men de är också det som gör skadan dyr att åtgärda.',
 'punkter': ['Sluttande taklinje ger sämre sikt och fler backningsskador',
             'Sensorpaketet gör även måttliga skador dyra att åtgärda',
             'Laddhybriden har högre ersättningsvärde'],
 'skada': 'Backningsskador och skador på bakre stötfångaren. Den lilla bakrutan är '
          'huvudorsaken, och det är också därför parkeringssensorerna är standard.',
 'varde': 'Starkt andrahandsvärde, men designen gör efterfrågan mer smaksberoende än på '
          'Corolla Cross.',
 'niva': 'Helförsäkring till omkring åtta år.',
 'fraga': ('Varför är backningsskador vanliga på Toyota C-HR?',
           'Den sluttande taklinjen ger en liten bakruta och sämre sikt bakåt än i en '
           'konventionell SUV. Sensorer och kamera kompenserar, men de är också det som gör '
           'en till synes liten skada dyr att åtgärda.'),
},
{
 'slug': 'aygo-x', 'namn': 'Aygo X', 'typ': 'minibil', 'ar': '2022–',
 'drivlina': 'bensin och hybrid',
 'kort': 'Toyotas minsta bil och en av få kvarvarande minibilarna på marknaden.',
 'vinkel': 'Aygo X är sannolikt bland de billigaste bilarna att försäkra som säljs ny i '
           'Sverige. Lägst ersättningsvärde i Toyotas utbud, låg vikt och skador på motparten '
           'som begränsas av ren fysik. För en ung förare är det den kombination som betyder '
           'mest — mer än vilket märke det står på.',
 'punkter': ['Lägst ersättningsvärde av alla Toyota-modeller',
             'Låg vikt begränsar skadan på både egen bil och motpart',
             'Segmentet krymper, vilket håller uppe andrahandsvärdet'],
 'skada': 'Parkeringsskador dominerar helt. Bilen används nästan uteslutande i tätort.',
 'varde': 'Håller värdet väl eftersom utbudet av nya minibilar minskar och Toyotas '
          'driftsäkerhet efterfrågas.',
 'niva': 'Halvförsäkring på de flesta exemplar. Trafikförsäkring om bilen är värd mindre än '
         'självrisken plus några tusenlappar.',
 'fraga': ('Vilken Toyota är billigast att försäkra?',
           'Aygo X, med marginal. Lägst ersättningsvärde och lägst vikt i utbudet ger den '
           'lägsta premien, särskilt för unga förare där båda faktorerna väger tungt.'),
},
{
 'slug': 'bz4x', 'namn': 'bZ4X', 'typ': 'eldriven SUV', 'ar': '2022–',
 'drivlina': 'helt eldriven',
 'kort': 'Toyotas första riktiga elbil, utvecklad tillsammans med Subaru.',
 'vinkel': 'bZ4X är Toyotas enda rena elbil i volym, och beståndet i Sverige är litet i '
           'förhållande till märkets övriga modeller. Det ger tunnare skadestatistik och '
           'större spridning mellan bolagens offerter än på en Corolla eller RAV4. Tekniken '
           'delas med Subaru Solterra, vilket breddar delunderlaget något.',
 'punkter': ['Delar teknik med Subaru Solterra',
             'Litet svenskt bestånd ger större spridning mellan bolagen',
             'Kontrollera att batteriet omfattas av vagnskadedelen'],
 'skada': 'Glasskador och frontskador med sensorkalibrering. Bilen används mest som familjens '
          'huvudbil med normala svenska körsträckor.',
 'varde': 'Har fallit kraftigt på begagnatmarknaden i takt med att elbilsvärdena rört sig.',
 'niva': 'Helförsäkring så länge marknadsvärdet ligger över 150 000 kr.',
 'fraga': ('Är Toyota bZ4X dyr att försäkra?',
           'Den ligger i elbilsklassen, alltså över Toyotas hybridmodeller. Det lilla '
           'beståndet i Sverige gör dessutom att spridningen mellan bolagens offerter är '
           'större än på märkets volymmodeller.'),
},
{
 'slug': 'camry', 'namn': 'Camry', 'typ': 'stor sedan', 'ar': '2024–',
 'drivlina': 'hybrid',
 'kort': 'Toyotas stora sedan, tillbaka på den svenska marknaden efter flera års frånvaro.',
 'vinkel': 'Camry är en ovanlig bil i Sverige och det påverkar prissättningen. Modellen är '
           'stor, hybriddriven och har lågt ersättningsvärde i förhållande till formatet, men '
           'beståndet är litet nog att flera bolag saknar egen modellprofil. Det ger större '
           'spridning mellan offerter än på Corolla.',
 'punkter': ['Litet svenskt bestånd ger spridning mellan bolagens priser',
             'Lågt ersättningsvärde i förhållande till storleken',
             'Vanlig som taxi i andra länder — kontrollera användningen i offerten'],
 'skada': 'Skador vid backning och i trånga parkeringar. Bilen är nära fem meter lång.',
 'varde': 'Ingen etablerad svensk andrahandsmarknad ännu, vilket gör värdet svårbedömt.',
 'niva': 'Helförsäkring de första sex åren.',
 'fraga': ('Vad kostar det att försäkra en Toyota Camry?',
           'Stor bil-klassens spann, men med större variation mellan bolagen än vanligt '
           'eftersom modellen är ovanlig i Sverige. Hämta fler offerter än du annars skulle.'),
},
{
 'slug': 'land-cruiser', 'namn': 'Land Cruiser', 'typ': 'stor terrängbil', 'ar': '2024–',
 'drivlina': 'diesel',
 'kort': 'Toyotas terrängbil och en av få kvarvarande ramkonstruktionerna på marknaden.',
 'vinkel': 'Land Cruiser är byggd på ram i stället för självbärande kaross, vilket är '
           'ovanligt bland personbilar i dag. Det gör bilen tålig men också dyr att laga vid '
           'större skador, eftersom en skadad ram kräver mätning och riktning på ett sätt en '
           'självbärande kaross inte gör. Lägg till högt ersättningsvärde och stöldrisk.',
 'punkter': ['Ramkonstruktion gör större skador dyra att åtgärda',
             'Hög dragvikt gör den vanlig som häst- och husvagnsdragare',
             'Kan omfattas av krav på stöldskydd beroende på postnummer'],
 'skada': 'Skador vid terrängkörning och släpmanövrering. Bilen är också stöldutsatt, '
          'eftersom Land Cruiser har hög efterfrågan på export.',
 'varde': 'Ett av marknadens starkaste andrahandsvärden, vilket håller vagnskadedelen '
          'motiverad mycket länge.',
 'niva': 'Helförsäkring under hela den period bilen har ett reellt andrahandsvärde, i '
         'praktiken över tio år.',
 'fraga': ('Är Land Cruiser stöldutsatt?',
           'Modellen har hög efterfrågan internationellt, vilket gör den mer stöldutsatt än '
           'genomsnittet. Flera bolag ställer krav på godkänt stöldskydd — kontrollera '
           'villkoren innan du tecknar.'),
},
],
}
