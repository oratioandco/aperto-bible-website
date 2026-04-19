#!/usr/bin/env python3
"""Update home.accessible, home.accessibleDesc, and home.getInvolved.description
in all i18n language files (except DE and EN which are already updated)."""

import json
import os

I18N_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')

UPDATES = {
    'ar': {
        'accessible': 'سياق مُدمَج في النص',
        'accessibleDesc': 'السياق الثقافي والتاريخي الأساسي مُدمَج مباشرةً في النص — محدَّد بصريًا، لتعرف دائمًا ما هو النص المقدس وما هو الإثراء. تفتح الحواشي طبقات أعمق لمن يريد التعمق.',
        'getInvolved_description': 'أبيرتو مشروع مفتوح — يتنامى بفضل الناس الذين يريدون المشاركة فيه. سواء أكان ذلك ترجمةً أم إنتاجًا صوتيًا أم ملاحظات أم شيئًا آخر تمامًا: كل شكل من أشكال المشاركة مرحَّب به.',
    },
    'bg': {
        'accessible': 'Контекст, вграден в текста',
        'accessibleDesc': 'Ключовият културен и исторически контекст е вграден директно в текста — визуално маркиран, за да знаеш винаги кое е Писание и кое е обогатяване. Бележките под линия разкриват още по-дълбоки пластове за желаещите.',
        'getInvolved_description': 'Aperto е отворен проект — расте чрез хората, които искат да бъдат част от него. Независимо дали става дума за превод, аудиопроизводство, обратна връзка или нещо съвсем различно: всяка форма на участие е добре дошла.',
    },
    'ca': {
        'accessible': 'Context integrat',
        'accessibleDesc': 'El context cultural i històric clau és teixit directament en el text — marcat visualment, perquè sempre sàpigues el que és l\'Escriptura i el que és enriquiment. Les notes obren capes encara més profundes per als qui les volen.',
        'getInvolved_description': 'Aperto és un projecte obert — i creix gràcies a les persones que volen formar-ne part. Tant si és traducció, producció d\'àudio, comentaris o qualsevol altra cosa: tota forma d\'implicació és benvinguda.',
    },
    'cs': {
        'accessible': 'Kontext přímo v textu',
        'accessibleDesc': 'Klíčový kulturní a historický kontext je přímo vetkaný do textu — vizuálně označený, abyste vždy věděli, co je Písmo a co je obohacení. Poznámky pod čarou otevírají ještě hlubší vrstvy pro ty, kdo je hledají.',
        'getInvolved_description': 'Aperto je otevřený projekt — a roste skrze lidi, kteří chtějí být jeho součástí. Ať už jde o překlad, audioproducci, zpětnou vazbu nebo něco úplně jiného: každá forma zapojení je vítána.',
    },
    'da': {
        'accessible': 'Kontekst indvævet',
        'accessibleDesc': 'Kulturel og historisk kontekst er indvævet direkte i teksten — visuelt markeret, så du altid ved, hvad der er Skrift, og hvad der er berigelse. Fodnoter åbner dybere lag for dem, der ønsker det.',
        'getInvolved_description': 'Aperto er et åbent projekt — og det vokser gennem mennesker, der vil være en del af det. Hvad enten det er oversættelse, audioproduktion, feedback eller noget helt andet: enhver form for deltagelse er velkommen.',
    },
    'el': {
        'accessible': 'Ενσωματωμένο πλαίσιο',
        'accessibleDesc': 'Το βασικό πολιτιστικό και ιστορικό πλαίσιο είναι υφασμένο απευθείας στο κείμενο — οπτικά σημειωμένο, ώστε να γνωρίζεις πάντα τι είναι Γραφή και τι είναι εμπλουτισμός. Τα υποσημειώματα ανοίγουν βαθύτερα επίπεδα για όσους τα θέλουν.',
        'getInvolved_description': 'Το Aperto είναι ένα ανοιχτό έργο — και μεγαλώνει μέσα από ανθρώπους που θέλουν να αποτελούν μέρος του. Είτε πρόκειται για μετάφραση, ηχητική παραγωγή, σχόλια ή κάτι εντελώς διαφορετικό: κάθε μορφή συμμετοχής είναι ευπρόσδεκτη.',
    },
    'es': {
        'accessible': 'Contexto integrado',
        'accessibleDesc': 'El contexto cultural e histórico clave está tejido directamente en el texto — marcado visualmente, para que siempre sepas qué es Escritura y qué es enriquecimiento. Las notas al pie abren capas aún más profundas para quienes las quieran.',
        'getInvolved_description': 'Aperto es un proyecto abierto — y crece gracias a las personas que quieren formar parte de él. Ya sea traducción, producción de audio, comentarios o cualquier otra cosa: toda forma de participación es bienvenida.',
    },
    'et': {
        'accessible': 'Kontekst tekstis sees',
        'accessibleDesc': 'Peamine kultuuriline ja ajalooline kontekst on põimitud otse teksti — visuaalselt tähistatud, nii et tead alati, mis on Pühakiri ja mis on rikastamine. Allmärkused avavad veel sügavamaid kihte neile, kes seda soovivad.',
        'getInvolved_description': 'Aperto on avatud projekt — ja see kasvab läbi inimeste, kes tahavad sellest osa saada. Olgu see tõlkimine, helitootmine, tagasiside või midagi muud: iga osalemisvorm on teretulnud.',
    },
    'fi': {
        'accessible': 'Konteksti sisällä',
        'accessibleDesc': 'Keskeinen kulttuurinen ja historiallinen konteksti on kudottu suoraan tekstiin — visuaalisesti merkittynä, jotta tiedät aina, mikä on Raamattua ja mikä on rikastusta. Alaviitteet avaavat vielä syvempiä kerroksia halukkaille.',
        'getInvolved_description': 'Aperto on avoin projekti — ja se kasvaa ihmisten kautta, jotka haluavat olla osa sitä. Olipa se käännöstyötä, äänentuotantoa, palautetta tai jotain muuta: jokainen osallistumisen muoto on tervetullut.',
    },
    'fr': {
        'accessible': 'Contexte intégré',
        'accessibleDesc': 'Le contexte culturel et historique essentiel est tissé directement dans le texte — visuellement marqué, pour que vous sachiez toujours ce qui est Écriture et ce qui est enrichissement. Les notes de bas de page ouvrent des couches encore plus profondes pour ceux qui les cherchent.',
        'getInvolved_description': 'Aperto est un projet ouvert — et il grandit grâce aux personnes qui veulent en faire partie. Que ce soit la traduction, la production audio, les retours ou autre chose : toute forme d\'implication est la bienvenue.',
    },
    'ga': {
        'accessible': 'Comhthéacs fite isteach',
        'accessibleDesc': 'Tá an príomhchomhthéacs cultúrtha agus stairiúil fite go díreach isteach sa téacs — marcáilte go físiúil, ionas go mbeidh a fhios agat i gcónaí cad é an Scrioptúr agus cad é an saibhriú. Osclaíonn na nótaí bun-leathanaigh sraitheanna níos doimhne dóibh siúd a bhfuil suim acu.',
        'getInvolved_description': 'Is tionscadal oscailte é Aperto — agus fásann sé tríd na daoine ar mhian leo a bheith páirteach ann. Cibé an aistriúchán, táirgeadh fuaime, aiseolas nó rud éigin eile ar fad é: tá gach cineál rannpháirtíochta fáiltithe.',
    },
    'hr': {
        'accessible': 'Kontekst utkán u tekst',
        'accessibleDesc': 'Ključni kulturni i povijesni kontekst utkan je izravno u tekst — vizualno označen, da uvijek znaš što je Pismo, a što obogaćenje. Bilješke otvaraju još dublje slojeve za one koji to žele.',
        'getInvolved_description': 'Aperto je otvoreni projekt — i raste kroz ljude koji žele biti dio njega. Bilo da se radi o prevođenju, audioprodukciji, povratnim informacijama ili nečem sasvim drugom: svaki oblik sudjelovanja je dobrodošao.',
    },
    'hu': {
        'accessible': 'Beépített kontextus',
        'accessibleDesc': 'A legfontosabb kulturális és történeti kontextus közvetlenül a szövegbe van szőve — vizuálisan jelölve, hogy mindig tudd, mi az Írás és mi a gazdagítás. A lábjegyzetek még mélyebb rétegeket tárnak fel azok számára, akik szeretnék.',
        'getInvolved_description': 'Az Aperto egy nyitott projekt — és azok az emberek által növekszik, akik részt akarnak venni benne. Legyen az fordítás, hanganyag-gyártás, visszajelzés vagy valami egészen más: minden részvételi forma üdvözlendő.',
    },
    'it': {
        'accessible': 'Contesto integrato',
        'accessibleDesc': 'Il contesto culturale e storico fondamentale è tessuto direttamente nel testo — marcato visivamente, così sai sempre cosa è Scrittura e cosa è arricchimento. Le note a piè di pagina aprono strati ancora più profondi per chi li vuole.',
        'getInvolved_description': 'Aperto è un progetto aperto — e cresce grazie alle persone che vogliono farne parte. Che si tratti di traduzione, produzione audio, feedback o qualcos\'altro: ogni forma di coinvolgimento è benvenuta.',
    },
    'lt': {
        'accessible': 'Kontekstas įaustas',
        'accessibleDesc': 'Pagrindinis kultūrinis ir istorinis kontekstas yra įaustas tiesiai į tekstą — vizualiai pažymėtas, kad visada žinotumėte, kas yra Raštas ir kas yra praturtinimas. Išnašos atskleidžia dar gilesnius sluoksnius tiems, kurie to nori.',
        'getInvolved_description': 'Aperto yra atviras projektas — ir auga per žmones, kurie nori būti jo dalimi. Nesvarbu, ar tai vertimas, garso gamyba, atsiliepimai ar kažkas visai kita: kiekviena dalyvavimo forma yra laukiama.',
    },
    'lv': {
        'accessible': 'Konteksts ieausts',
        'accessibleDesc': 'Galvenais kultūras un vēsturiskais konteksts ir ieausts tieši tekstā — vizuāli iezīmēts, lai vienmēr zinātu, kas ir Raksti un kas ir papildinājums. Zemsvītras piezīmes atver vēl dziļākus slāņus tiem, kas to vēlas.',
        'getInvolved_description': 'Aperto ir atvērts projekts — un tas aug caur cilvēkiem, kuri vēlas būt tā daļa. Vai tas ir tulkošana, audio produkcija, atsauksmes vai kaut kas cits: katra iesaistīšanās forma ir laipni gaidīta.',
    },
    'mt': {
        'accessible': 'Kuntest integrat',
        'accessibleDesc': 'Il-kuntest kulturali u storiku ewlieni huwa minsuġ direttament fit-test — immarkat viżwalment, ħalli dejjem tkun taf x\'inhu l-Iskrittura u x\'inhu l-arrikkiment. In-noti tal-qiegħ tal-paġna jiftħu saffi aktar fondi għal min irid.',
        'getInvolved_description': 'Aperto huwa proġett miftuħ — u jikber permezz tal-persuni li jridu jkunu parti minnu. Kemm jekk huwa traduzzjoni, produzzjoni tal-awdjo, feedback jew xi ħaġa oħra: kull forma ta\' involviment hija milqugħa.',
    },
    'nb': {
        'accessible': 'Kontekst vevd inn',
        'accessibleDesc': 'Viktig kulturell og historisk kontekst er vevd direkte inn i teksten — visuelt markert, slik at du alltid vet hva som er Skrift og hva som er berikelse. Fotnoter åpner enda dypere lag for dem som ønsker det.',
        'getInvolved_description': 'Aperto er et åpent prosjekt — og det vokser gjennom mennesker som vil være en del av det. Enten det er oversettelse, lydproduksjon, tilbakemeldinger eller noe helt annet: enhver form for deltakelse er velkommen.',
    },
    'nl': {
        'accessible': 'Context ingeweven',
        'accessibleDesc': 'De belangrijkste culturele en historische context is direct in de tekst geweven — visueel gemarkeerd, zodat je altijd weet wat Schrift is en wat verrijking. Voetnoten openen nog diepere lagen voor wie dat wil.',
        'getInvolved_description': 'Aperto is een open project — en het groeit door mensen die er deel van willen uitmaken. Of het nu gaat om vertalen, audioproductie, feedback of iets anders: elke vorm van betrokkenheid is welkom.',
    },
    'pl': {
        'accessible': 'Kontekst wpleciony',
        'accessibleDesc': 'Kluczowy kontekst kulturowy i historyczny jest wpleciony bezpośrednio w tekst — oznaczony wizualnie, abyś zawsze wiedział, co jest Pismem, a co wzbogaceniem. Przypisy otwierają jeszcze głębsze warstwy dla tych, którzy chcą.',
        'getInvolved_description': 'Aperto to otwarty projekt — i rośnie dzięki ludziom, którzy chcą być jego częścią. Czy to tłumaczenie, produkcja audio, opinie czy coś zupełnie innego: każda forma zaangażowania jest mile widziana.',
    },
    'pt': {
        'accessible': 'Contexto integrado',
        'accessibleDesc': 'O contexto cultural e histórico fundamental está tecido diretamente no texto — visualmente marcado, para que saiba sempre o que é Escritura e o que é enriquecimento. As notas de rodapé abrem camadas ainda mais profundas para quem as quiser.',
        'getInvolved_description': 'Aperto é um projeto aberto — e cresce através das pessoas que querem fazer parte dele. Seja tradução, produção de áudio, comentários ou outra coisa qualquer: toda forma de envolvimento é bem-vinda.',
    },
    'ro': {
        'accessible': 'Context integrat',
        'accessibleDesc': 'Contextul cultural și istoric esențial este țesut direct în text — marcat vizual, pentru ca să știi mereu ce este Scriptură și ce este îmbogățire. Notele de subsol deschid straturi și mai adânci pentru cei care le doresc.',
        'getInvolved_description': 'Aperto este un proiect deschis — și crește prin oamenii care vor să facă parte din el. Fie că este vorba de traducere, producție audio, feedback sau altceva cu totul: orice formă de implicare este binevenită.',
    },
    'ru': {
        'accessible': 'Контекст вплетён',
        'accessibleDesc': 'Ключевой культурный и исторический контекст вплетён прямо в текст — визуально выделен, чтобы вы всегда знали, где Писание, а где пояснение. Сноски открывают ещё более глубокие пласты для тех, кто хочет.',
        'getInvolved_description': 'Aperto — открытый проект, который растёт благодаря людям, желающим быть его частью. Будь то перевод, звуковое производство, обратная связь или что-то совсем иное: любая форма участия приветствуется.',
    },
    'sk': {
        'accessible': 'Kontext vpletený',
        'accessibleDesc': 'Kľúčový kultúrny a historický kontext je vpletený priamo do textu — vizuálne označený, aby ste vždy vedeli, čo je Písmo a čo je obohatenie. Poznámky pod čiarou otvárajú ešte hlbšie vrstvy pre tých, ktorí o ne majú záujem.',
        'getInvolved_description': 'Aperto je otvorený projekt — a rastie prostredníctvom ľudí, ktorí chcú byť jeho súčasťou. Či už ide o preklad, audioproukciu, spätnú väzbu alebo niečo iné: každá forma zapojenia je vítaná.',
    },
    'sl': {
        'accessible': 'Kontekst vpleten',
        'accessibleDesc': 'Ključni kulturni in zgodovinski kontekst je vpleten neposredno v besedilo — vizualno označen, da vedno veš, kaj je Pismo in kaj obogatitev. Opombe odpirajo še globlje plasti za tiste, ki jih želijo.',
        'getInvolved_description': 'Aperto je odprt projekt — in raste prek ljudi, ki želijo biti njegov del. Bodisi prevajanje, zvočna produkcija, povratne informacije ali kaj povsem drugega: vsaka oblika sodelovanja je dobrodošla.',
    },
    'sq': {
        'accessible': 'Kontekst i ndërtuar brenda',
        'accessibleDesc': 'Konteksti kryesor kulturor dhe historik është ndërtuar drejtpërdrejt në tekst — i shënuar vizualisht, që të dish gjithmonë çfarë është Shkrimi dhe çfarë është pasurimi. Shënimet e fundit hapin shtresa edhe më të thella për ata që i duan.',
        'getInvolved_description': 'Aperto është një projekt i hapur — dhe rritet nëpërmjet njerëzve që duan të jenë pjesë e tij. Qoftë përkthim, prodhim audio, reagime apo diçka tjetër: çdo formë pjesëmarrjeje është e mirëpritur.',
    },
    'sv': {
        'accessible': 'Kontext invävd',
        'accessibleDesc': 'Det viktigaste kulturella och historiska sammanhanget är invävt direkt i texten — visuellt markerat, så att du alltid vet vad som är Skrift och vad som är berikning. Fotnoter öppnar ännu djupare lager för dem som vill.',
        'getInvolved_description': 'Aperto är ett öppet projekt — och det växer genom människor som vill vara en del av det. Oavsett om det handlar om översättning, audioproduktion, återkoppling eller något helt annat: alla former av engagemang är välkomna.',
    },
    'tr': {
        'accessible': 'Bağlam metne işlenmiş',
        'accessibleDesc': 'Temel kültürel ve tarihsel bağlam, metne doğrudan işlenmiştir — görsel olarak işaretlenmiş, böylece neyin Kutsal Yazı, neyin zenginleştirme olduğunu her zaman bilirsiniz. Dipnotlar, isteyenler için daha da derin katmanlar açar.',
        'getInvolved_description': 'Aperto açık bir projedir — ve parçası olmak isteyen insanlar aracılığıyla büyür. İster çeviri, ister ses prodüksiyonu, ister geri bildirim, ister başka bir şey olsun: her türlü katılım memnuniyetle karşılanır.',
    },
    'uk': {
        'accessible': 'Контекст вплетений',
        'accessibleDesc': 'Ключовий культурний і історичний контекст вплетений безпосередньо в текст — візуально позначений, щоб ви завжди знали, що є Писанням, а що — поясненням. Виноски відкривають ще глибші шари для тих, хто цього бажає.',
        'getInvolved_description': 'Aperto — відкритий проект, який зростає завдяки людям, що хочуть бути його частиною. Будь то переклад, аудіовиробництво, зворотний зв\'язок чи щось інше: кожна форма участі є вітаною.',
    },
}

for lang, updates in UPDATES.items():
    path = os.path.join(I18N_DIR, f'{lang}.json')
    if not os.path.exists(path):
        print(f'SKIP {lang} — file not found')
        continue

    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    home = data.setdefault('home', {})
    home['accessible'] = updates['accessible']
    home['accessibleDesc'] = updates['accessibleDesc']
    gi = home.setdefault('getInvolved', {})
    gi['description'] = updates['getInvolved_description']

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')

    print(f'✓ {lang}')

print('\nDone.')
