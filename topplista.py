# -*- coding: utf-8 -*-
"""Topplistan — /basta-bilforsakringen/

RANKNINGEN RÄKNAS FRAM I KOD, INTE FÖR HAND
Poängen bygger på fyra kriterier med fasta vikter. Saknas underlag för
ett kriterium hos ett bolag räknas poängen om på de kriterier som
faktiskt finns, och sidan skriver ut hur många kriterier som ligger
bakom varje placering. Ett bolag utan något underlag alls hamnar inte
på listan — det redovisas separat.

Det är skillnaden mot konkurrenterna: de utser en vinnare och förklarar
i efterhand. Här går modellen att granska, och den ändrar sig av sig
själv när data.py fylls i.
"""
from companies import BOLAG
import data, marknad

# Vikter. Summan behöver inte bli 1 — de normaliseras per bolag utifrån
# vilka kriterier som har underlag.
VIKT = {
    'villkor': 0.35,   # Konsumenternas Försäkringsbyrå, 1–5
    'pris':    0.30,   # helförsäkring på jämförelseprofilen
    'ski':     0.20,   # Svenskt Kvalitetsindex, kundnöjdhet
    'trust':   0.15,   # Trustpilot
}

KRITERIUM_NAMN = {'villkor': 'Villkorsbetyg', 'pris': 'Pris',
                  'ski': 'Kundnöjdhet (SKI)', 'trust': 'Trustpilot'}


def _norm(v, lo, hi, inverterad=False):
    if v is None or hi == lo:
        return None
    x = (v - lo) / (hi - lo)
    return 1 - x if inverterad else x


def rankning():
    """Returnerar (rankade, utan_underlag) — bolag sorterade på poäng."""
    kons = [b['kons'] for b in BOLAG if b.get('kons')]
    ski = [b['ski'] for b in BOLAG if b.get('ski')]
    priser = [data.PRIS[b['slug']]['hel'] for b in BOLAG
              if data.PRIS.get(b['slug'], {}).get('hel')]
    trust = [data.TRUSTPILOT[b['slug']]['betyg'] for b in BOLAG
             if data.TRUSTPILOT.get(b['slug'], {}).get('betyg')]

    rankade, utan = [], []
    for b in BOLAG:
        s = b['slug']
        delar = {
            'villkor': _norm(b.get('kons'), min(kons), max(kons)) if kons else None,
            'ski': _norm(b.get('ski'), min(ski), max(ski)) if ski else None,
            'pris': _norm(data.PRIS.get(s, {}).get('hel'),
                          min(priser), max(priser), inverterad=True) if priser else None,
            'trust': _norm(data.TRUSTPILOT.get(s, {}).get('betyg'),
                           min(trust), max(trust)) if trust else None,
        }
        har = {k: v for k, v in delar.items() if v is not None}
        if not har:
            utan.append(b)
            continue
        vikt_summa = sum(VIKT[k] for k in har)
        poang = sum(v * VIKT[k] for k, v in har.items()) / vikt_summa
        rankade.append({'bolag': b, 'poang': round(poang * 5, 2),
                        'kriterier': sorted(har), 'antal': len(har)})
    rankade.sort(key=lambda x: (-x['poang'], x['bolag']['namn']))
    return rankade, utan


def far_rankas():
    """Placeringssiffror publiceras först när underlaget bär dem.

    Ett bolag som toppar en lista på ett enda kriterium är inte en
    rankning utan en slump. Tills pris och omdömen är insamlade visar
    sidan en sammanställning utan placeringssiffror — och byter av sig
    själv till skarp topplista när data.py är ifylld."""
    r, _ = rankning()
    if not r:
        return False
    tillrackligt = [x for x in r if x['antal'] >= 3]
    return len(tillrackligt) >= max(5, len(r) * 0.6)


def _rad(i, r):
    b = r['bolag']
    s = b['slug']
    prefix = f'{i}. ' if far_rankas() else ''
    return (f'<tr><th scope="row">{prefix}<a href="/forsakringsbolag/{s}/">{b["namn"]}</a></th>'
            f'<td>{str(r["poang"]).replace(".", ",")}</td>'
            f'<td>{data.betyg(b.get("kons"))}</td>'
            f'<td>{data.betyg(b.get("ski"))}</td>'
            f'<td>{data.betyg(data.TRUSTPILOT.get(s, {}).get("betyg"))}</td>'
            f'<td>{data.kr(data.PRIS.get(s, {}).get("hel"))}</td>'
            f'<td>{r["antal"]} av 4</td></tr>')


def sidan():
    rankade, utan = rankning()
    rankat = far_rankas()
    topp = rankade[0]['bolag']['namn'] if (rankade and rankat) else None

    rader = ''.join(_rad(i + 1, r) for i, r in enumerate(rankade))
    tabell = (
        '<div class="tbl"><table>'
        f'<caption>{"Rankning" if rankat else "Sammanställning"} {data.UPPDATERAD_TEXT} — '
        f'sorterad på sammanvägd poäng</caption>'
        f'<thead><tr><th scope="col">{"Placering" if rankat else "Bolag"}</th>'
        '<th scope="col">Poäng</th>'
        '<th scope="col">Villkor</th><th scope="col">SKI</th>'
        '<th scope="col">Trustpilot</th><th scope="col">Helförsäkring/år</th>'
        '<th scope="col">Underlag</th></tr></thead>'
        f'<tbody>{rader}</tbody></table></div>'
        '<p class="swipe">&larr; Dra i sidled för att se alla kolumner</p>')

    vikttabell = (
        '<div class="tbl"><table><caption>Så viktas kriterierna</caption>'
        '<thead><tr><th scope="col">Kriterium</th><th scope="col">Vikt</th>'
        '<th scope="col">Källa</th></tr></thead><tbody>'
        '<tr><th scope="row">Villkorens innehåll</th><td>35 %</td>'
        '<td>Konsumenternas Försäkringsbyrå, skala 1–5</td></tr>'
        '<tr><th scope="row">Pris på helförsäkring</th><td>30 %</td>'
        '<td>Egen offertinsamling på jämförelseprofilen</td></tr>'
        '<tr><th scope="row">Kundnöjdhet</th><td>20 %</td>'
        '<td>Svenskt Kvalitetsindex, skala 0–100</td></tr>'
        '<tr><th scope="row">Kundomdömen</th><td>15 %</td>'
        '<td>Trustpilot, skala 1–5</td></tr>'
        '</tbody></table></div>')

    utan_txt = ''
    if utan:
        namn = ', '.join(f'<a href="/forsakringsbolag/{b["slug"]}/">{b["namn"]}</a>'
                         for b in utan)
        utan_txt = (f'<h2>Bolag utan tillräckligt underlag</h2>'
                    f'<p>Följande bolag saknar ännu betyg från både Konsumenternas '
                    f'Försäkringsbyrå och Svenskt Kvalitetsindex, och har därför ingen '
                    f'placering på listan: {namn}. Att de saknas här är inget omdöme om '
                    f'deras försäkringar — de deltar inte i de oberoende mätningarna, '
                    f'vilket ofta beror på att bolaget är litet eller nytt. Läs bolagssidan '
                    f'i stället, och begär offert direkt.</p>')

    saknade = [k for k in ('pris', 'trust')
               if not (data.har_priser() if k == 'pris' else data.har_trustpilot())]
    varning = ''
    if not rankat:
        vilka = ' och '.join(KRITERIUM_NAMN[k].lower() for k in saknade) or 'flera kriterier'
        varning = ('<div class="warn"><strong>Ingen placering publiceras ännu.</strong> '
                   f'Underlag för {vilka} saknas för flera bolag, och ett bolag som toppar '
                   'en lista på ett enda kriterium är ingen rankning — det är en slump. '
                   'Tabellen nedan visar därför vad vi faktiskt vet, sorterat på poäng men '
                   'utan placeringssiffror. Så snart minst tre av fyra kriterier är '
                   'insamlade för merparten av bolagen publiceras listan som rankning.</div>')

    body = f'''
<section class="sec"><div class="wrap narrow">
<div class="note"><p><strong>Kort sagt.</strong> Det finns ingen försäkring som är bäst för
alla. Den här listan rangordnar bolagen på fyra kriterier med öppna vikter, så att du kan se
exakt varför ett bolag hamnar där det hamnar — och räkna om det själv om du värderar pris
högre än villkor.</p></div>

<h2>Så här rankar vi</h2>
<p>De flesta topplistor på marknaden utser en vinnare och motiverar den i efterhand. Vi gör
tvärtom: kriterierna och vikterna bestäms först, poängen räknas fram maskinellt, och
placeringen blir vad den blir. Modellen står nedan i sin helhet.</p>
{vikttabell}
<p>Saknas underlag för ett kriterium hos ett bolag räknas poängen om på de kriterier som
finns. Kolumnen längst till höger visar hur många av de fyra som ligger bakom siffran — ju
färre, desto osäkrare. Vi publicerar ingen placeringssiffra förrän minst tre av fyra
kriterier finns för merparten av bolagen.</p>

<h2>{'Topplistan' if rankat else 'Sammanställning av bolagen'}</h2>
{varning}
{tabell}
{data.profil_ruta()}
{data.kontrollerad()}

<h2>Vad andra källor har publicerat</h2>
<p>Medan vår egen insamling pågår redovisar vi de betyg och priser som publicerats av
oberoende källor och av andra jämförelsesajter. Betygen från Konsumenternas Försäkringsbyrå
är primärkällor och jämförbara rakt av. Prisexemplen är hämtade från andra sajter med varsin
egen profil och redovisas i sin helhet på sidan om
<a href="/billigaste-bilforsakringen/">billigaste bilförsäkringen</a>.</p>
{marknad.betyg_tabell()}

<h2>Vad listan inte kan säga</h2>
<p>Poängen säger något om bolaget. Den säger ingenting om vad just din bil kostar hos det
bolaget, eftersom premien räknas fram ur din bil, din ålder, ditt postnummer och din
körsträcka. Ett bolag långt ned på listan kan mycket väl vara billigast för dig. Använd
listan för att välja vilka tre eller fyra bolag du begär offert från — inte för att välja
åt dig.</p>
<p>Läs vidare om <a href="/billigaste-bilforsakringen/">vad som styr priset</a> och om
<a href="/jamfor-bilforsakring/">hur du jämför offerter på lika villkor</a>.</p>

{utan_txt}

<div class="cta"><h2>Se ditt eget pris</h2>
<p>Ange registreringsnumret så hämtas bilens uppgifter automatiskt.</p>
<div class="cta-inner">{{PLATE}}</div></div>
</div></section>'''

    return {
        'slug': 'basta-bilforsakringen', 'key': True,
        'title': f'Bästa bilförsäkringen {data.UPPDATERAD[:4]} — rankning av {len(BOLAG)} bolag',
        'desc': 'Vilken är bästa bilförsäkringen? Vi rankar bolagen på villkor, pris, '
                'kundnöjdhet och omdömen — med öppna vikter du kan granska.',
        'eyebrow': f'Uppdaterad {data.UPPDATERAD_TEXT}',
        'h1': 'Bästa bilförsäkringen',
        'lead': 'Vi rangordnar de svenska bilförsäkringsbolagen på fyra kriterier: villkorens '
                'innehåll, pris på jämförelseprofilen, kundnöjdhet och kundomdömen. Vikterna '
                'är publicerade, poängen räknas fram maskinellt och underlaget redovisas per '
                'bolag.',
        'checks': ['Öppen modell — du ser vikterna och kan räkna om själv',
                   'Bolag utan verifierat underlag rankas inte, de redovisas separat',
                   'Samma jämförelseprofil för alla priser'],
        'card_t': 'Se vad de bäst rankade kostar för din bil',
        'sticky': 'Jämför de bäst rankade bolagen',
        'body': body,
        'faq_h2': 'Vanliga frågor om bästa bilförsäkringen',
        'faq': [
            ('Vilken är bästa bilförsäkringen?',
             ('Enligt vår sammanvägning ligger ' + topp + ' högst just nu, men placeringen '
              'säger inget om vad försäkringen kostar för din bil. Använd listan för att '
              'välja vilka bolag du begär offert från.') if topp else
             'Rankningen publiceras så snart underlaget är insamlat på samtliga bolag.'),
            ('Hur räknar ni fram poängen?',
             'Fyra kriterier med fasta vikter: villkorens innehåll 35 procent, pris 30 '
             'procent, kundnöjdhet 20 procent och kundomdömen 15 procent. Saknas underlag '
             'för ett kriterium räknas poängen om på de övriga, och antalet kriterier '
             'redovisas i tabellen.'),
            ('Varför saknas vissa bolag på listan?',
             'De deltar inte i de oberoende mätningarna, vilket är vanligt för små och nya '
             'bolag. Vi väljer att redovisa dem separat i stället för att gissa fram en '
             'placering.'),
            ('Är den bäst rankade också billigast?',
             'Nej. Priset är ett av fyra kriterier och väger 30 procent. Ett bolag med starka '
             'villkor kan hamna högt trots ett medelmåttigt pris — och tvärtom.'),
            ('Hur ofta uppdateras listan?',
             f'Underlaget gicks senast igenom i {data.UPPDATERAD_TEXT}. Betygen från '
             'Konsumenternas och SKI uppdateras årligen, priser och omdömen oftare.'),
        ],
        'rel': [('/billigaste-bilforsakringen/', 'Billigaste bilförsäkringen'),
                ('/forsakringsbolag/', 'Alla försäkringsbolag'),
                ('/jamfor-bilforsakring/', 'Så jämför du offerter'),
                ('/redaktionell-metod/', 'Vår redaktionella metod'),
                ('/helforsakring/', 'Helförsäkring — vad ingår?')],
    }
