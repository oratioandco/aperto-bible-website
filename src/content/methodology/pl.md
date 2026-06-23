# Jak Aperto działa naprawdę

Jeśli czytałeś [naszą stronę o procesie](/process), wiesz już, *dlaczego* się tego podjęliśmy. Ta strona pokazuje, *jak* — sam mechanizm, łącznie z tym, co wciąż powstaje.

„Tłumaczenie Biblii przez sztuczną inteligencję” to słowa, przy których uważny czytelnik powinien się zatrzymać. My też się przy nich zatrzymujemy. Uczciwą odpowiedzią na tę nieufność nie są zapewnienia, że wszystko gra — lecz pokazanie tego, co dzieje się od podszewki. Nic z tego, co opisujemy poniżej, nie jest przenośnią: to prawdziwe kontrole, prawdziwe progi i prawdziwe błędy, które wyłapaliśmy i naprawiliśmy. Gdy coś jest tymczasowe albo dopiero powstaje, mówimy o tym wprost.

## Problem, który rozwiązujemy

Gdy mowa o „tłumaczeniu przez AI”, w tle milcząco zakłada się angielszczyznę — i to, że *wystarczająco dobrze* w zupełności wystarczy. Tutaj żadne z tych założeń się nie sprawdza.

**Poza angielskim jakość modeli wyraźnie spada.** Dzisiejsze modele najlepiej radzą sobie w języku, którego widziały najwięcej. Ten sam model, który po angielsku pisze gładko, w niemieckim czy polskim — a w językach mniejszych tym bardziej — potrafi tworzyć prozę nienaganną gramatycznie, lecz wyraźnie *cudzą*: o rytmie przekładu, nie o głosie rodzimego pisarza. Bez nadzoru tłumaczenie przejmuje dokładnie te słabości.

**Pismo Święte nie znosi tłumaczenia „na oko”.** Parafraza trafna w 95 procentach to znakomity wynik dla większości produktów opartych na AI. W przypadku Biblii oznacza to pomyłkę co do 5 procent tekstu, na którym ludzie budują swoje życie — a te 5 procent daje o sobie znać jako zapożyczony kościelny żargon, zmyślone znaczenie albo współczesny przedmiot wstawiony w scenę sprzed dwóch tysięcy lat. Poprzeczką nie jest *ogólny sens*; jest nim rodzimy rejestr literacki, bez jednej usterki, której dało się uniknąć.

Prawdziwy problem brzmi więc tak: jak skłonić nierówne, faworyzujące angielski narzędzie, by tworzyło naprawdę rodzime, naprawdę wierne Pismo — język po języku — i jak *poznać*, że już się udało? Naszą odpowiedzią nie jest jeden przemyślny model. To system pomyślany tak, by wyłapywać to, w czym myli się każdy pojedynczy model, i by uczciwie zmierzyć rezultat. Jeśli sam tworzysz rozwiązania oparte na AI, rozpoznasz ten schemat: generujemy wiele wariantów, oceniamy je automatycznymi ewaluatorami, blokujemy publikację na twardych kontrolach, oznaczamy wyniki o niskiej pewności i nie wypuszczamy człowieka z obiegu. Każdy z tych elementów nazywamy po imieniu, gdy do niego dochodzimy.

<!--DIAGRAM:pipeline-->

## Tłumaczymy z greki i hebrajskiego — nie z angielskiego

Każdy fragment rodzi się z nauki, nie z oprogramowania. Najpierw etap badawczy przegląda najnowszą literaturę naukową poświęconą danemu rozdziałowi — bieżące komentarze, artykuły naukowe, opracowania leksykalne, a nie tylko to, co jest na tyle stare, że dostępne za darmo — i zbiera ją w jedno opracowanie wstępne. Pracujemy na standardowych wydaniach krytycznych tekstu źródłowego — greckim Nowym Testamencie Nestle-Aland / UBS oraz Biblia Hebraica Stuttgartensia dla tekstu hebrajskiego. Następnie tłumacz-uczony bierze na warsztat oryginalną grekę lub hebrajski w świetle tego opracowania: zakres znaczeń każdego ważkiego słowa, echa Starego Testamentu, ciężar, jaki niesie dany termin, szczegół kulturowy oczywisty dla ówczesnego słuchacza. Powstaje z tego spisana egzegeza, przed którą odpowiada cały dalszy proces.

Mówiąc wprost: **Aperto powstaje w tłumaczeniu z tekstów źródłowych, a nie z przeróbki cudzego przekładu.** AI wychodzi od greki, naszej egzegezy, specyfikacji stylu i glosariusza właściwego dla danego języka — i pisze w języku docelowym nową literaturę.

## Źródła i prawa autorskie

Pod tym wszystkim kryją się dwa zasadne pytania: *co* właściwie czytasz oraz *czy tak wolno?*

Nasza egzegeza to nasza własna praca — synteza najlepszej myśli naukowej różnych tradycji: katolickiej, protestanckiej, prawosławnej i zielonoświątkowej — z myślą o naprawdę ekumenicznym odczytaniu. Korzystamy z niej tak, jak od zawsze postępuje każdy komentator: czytamy, ważymy, piszemy własną analizę. **Nie wydajemy ponownie całych komentarzy ani Biblii objętych prawami autorskimi, a Pismo, które publikujemy, nie zawiera ani jednego cudzego przekładu — to nasze własne tłumaczenie z języków źródłowych.** Tam, gdzie nasza egzegeza sięga do konkretnego źródła, robi to jak każda Biblia z komentarzem: krótkim, wyraźnie przypisanym cytatem. Wolimy oprzeć się na najlepszej współczesnej myśli naukowej, niż zamknąć się w tym, co akurat wygasło spod ochrony prawnej i jest o sto lat przestarzałe.

> *Jak każde narzędzie badawcze: podaj źródło, cytuj krótko i syntetyzuj — bez powielania samych źródeł.*

## Wiele wersji roboczych, nie jedna

Pojedynczy model ma jeden zestaw przyzwyczajeń. Dlatego dla każdego rozdziału tworzymy równolegle kilka niezależnych wersji roboczych — obecnie do czterech, od różnych dostawców (Anthropic, OpenAI, Google, Mistral) — a każda dostaje te same dane wejściowe. Różne rodziny modeli mają różne mocne strony; wybór spośród kandydatów daje więcej niż zaufanie jednemu. Wersji nie zlewamy w jedno: każda jest pełnym tłumaczeniem, a o tym, która zwycięży, rozstrzyga kolejny etap — próbując ją złamać.

> *Próbkowanie zespołowe (ensemble), by zneutralizować skłonności któregokolwiek pojedynczego modelu.*

## Panel, który próbuje złamać tekst

Każdą wersję roboczą czyta panel niezależnych krytyków — osobnych ewaluatorów, z których każdy ma jedno zadanie i polecenie, by stawiać wysokie wymagania. Tropią: nienaturalne sformułowania; archaizmy i kościelny żargon; kalki (gramatykę języka źródłowego przemyconą do docelowego); osuwanie się rejestru w kazanie albo w oschłość; luki w zrozumiałości; krzywdzące stereotypy; niewierność teologiczną; oraz błędy mechaniczne, wychwytywane przez narzędzia deterministyczne, a nie przez czyjąś opinię. Każdy zwraca konkretne ustalenia — werset, fragment, na czym zawodzi, jak poważnie — a panel uwypukla rozbieżności, zamiast je uśredniać.

Wybór to jeden, bezstronny przebieg: każdego kandydata oceniamy tą samą miarą, a zwycięża wersja z najmniejszą liczbą najmniej poważnych usterek, która następnie trafia w opisaną niżej pętlę poprawek. Część krytyków działa już dziś we wszystkich naszych podstawowych językach; inni — spójność międzyjęzykowa, tłumaczenie zwrotne — są gotowi tylko częściowo i nie wszędzie jeszcze na nich polegamy.

> *Ocena typu LLM-jako-sędzia: wiele wąskich, kontradyktoryjnych kontroli zamiast jednej mglistej noty.*

## Kontrole, które tekst musi przejść

Krytyka ma charakter doradczy; niektóre kontrole — nie. Kilka z nich jest twardych: jeśli fragment ich nie przejdzie, nie rusza dalej.

**Kontrola mechaniczna** jest najsurowsza: każdy błąd gramatyczny, ortograficzny, interpunkcyjny czy strukturalny zatrzymuje tekst — sprawdzamy to prawdziwymi narzędziami lingwistycznymi tam, gdzie zdążyły dojrzeć. **Kontrola anachronizmów** wyłapuje współczesne przedmioty w scenie sprzed dwóch tysięcy lat — jeśli dwudziestoośmiolatkowi z Berlina czy Warszawy stanąłby przed oczami samochód, telefon albo moneta euro, a w ówczesnej Judei to nie istniało, fragment zostaje odrzucony. Prawdziwy przykład: w jednej z niemieckich wersji Zachariasz „pojechał do domu” — samochód tam, gdzie tekst mówi o człowieku idącym pieszo. Kontrola blokuje teraz całą tę klasę błędów.

To jest **próg**: nic zepsutego ani rażąco obcego nigdy nie zostaje opublikowane. I to wyłącznie próg — tekst zdrowy, lecz jeszcze nieśpiewający.

> *Kontrole regresji w CI: automatyczne sprawdzenia, które blokują publikację, a nie tylko ostrzegają.*

<!--DIAGRAM:floorvision-->

## Od progu do wizji

Trzymamy dwa standardy — i robimy to świadomie. **Próg** to mechaniczna poprawność. **Wizja** to rodzimy rejestr literacki — proza, która czyta się tak, jak pisze współczesny powieściopisarz w danym języku. Większość fragmentów przekracza próg szybko; dojście do wizji wymaga iteracji: ustalenia krytyków zasilają pętlę poprawek, która naprawia oznaczone fragmenty i sprawdza je na nowo — kilka rund, aż wynik się ustabilizuje.

Teraz część uczciwa: fragment, który przekroczył próg, lecz nie sięgnął jeszcze wizji, mimo to zostaje opublikowany — opatrzony **etykietą niskiej pewności**, tak by w pierwszej kolejności trafiał do dopracowania, a nie był podawany jako gotowy. Tekst zepsuty albo rażąco przetłumaczony nie zostaje opublikowany w ogóle. Wolimy pokazać ci tekst zdrowy, choć skromny, który sami oznaczyliśmy, niż zacierać granicę między *poprawnym* a *pięknym*. System jest pomyślany tak, by wiedział, czego jeszcze nie wie.

> *Oznaczanie pewności, które kieruje słabsze wyniki do przeglądu, zamiast wydawać je po cichu.*

## Porównanie z innymi przekładami

Ponieważ tłumaczymy ze źródła, zestawiamy też naszą pracę z istniejącymi przekładami — z dwóch zabezpieczających powodów.

**Oryginalność.** Porównujemy każdą wersję roboczą, werset po wersecie, z uznanymi przekładami w danym języku. Jeśli nasze sformułowanie trzyma się któregoś z nich zbyt blisko, to sygnał ostrzegawczy: zwykle wkradło się zapożyczone brzmienie, więc fragment piszemy od nowa, własnym głosem. To czujnik, który wyłapuje przypadkowe echa — potwierdza naszą niezależność, a nie tworzy zależności.

**Jasność.** Mierzymy się także z najprzejrzystszymi współczesnymi przekładami — nie po to, by je naśladować, lecz by mieć pewność, że jesteśmy przynajmniej równie jaśni. Jeśli gładsza wersja czyta się lepiej tam, gdzie nasza jest sztywna, to usterka; jeśli nasza jest trudniejsza, bo zachowuje ostrość, którą tamta wygładziła, to zabieg celowy i wyjaśniamy dlaczego.

Teksty te pochodzą z licencjonowanych naukowych serwisów biblijnych — w tym z YouVersion, z którego wolno nam korzystać do pracy niekomercyjnej, takiej jak nasza — oraz z wydań w domenie publicznej, używanych wyłącznie do kontroli wewnętrznych. Biblia, którą publikujemy, nie zawiera ani jednego z tych cudzych tekstów.

> *Porównywanie z punktami odniesienia oraz kontrola skażenia sprawdzająca, że wynik ich nie powtarza.*

## Najtrudniejsza część: języki inne niż angielski

Tu trafia większość naszej pracy inżynierskiej, bo to tu modele są najsłabsze. Niemiecki potrafi przejąć widmowy rytm Biblii Lutra; polski bywa, że osuwa się w kaznodziejski ton, którego czytelnicy nie znoszą; niektóre języki niemal nie mają tradycji Biblii *jako literatury*. Tłumaczenie może mieć nienaganną gramatykę, a mimo to brzmieć obco.

Nasze środki zaradcze są konkretne. **Krytycy myślą w języku docelowym** — ich instrukcje są w nim napisane, więc system ocenia tak, jak zrobiłby to rodzimy redaktor, zamiast przepuszczać swój osąd przez angielski (a to jeden z głównych sposobów, w jaki jakość poza angielskim po cichu się obniża). **Każdy język ma swój profil literacki** — konkretnego czytelnika, autorów wzorcowych, glosariusz teologiczny. A **wdrożenie języka samo jest kontrolą**: specyfikacje stylu, opracowane przykłady, glosariusz, narzędzia gramatyczne i zestaw porównawczy muszą być gotowe, zanim język ruszy.

Gdzie jesteśmy: **niemiecki i polski są najdalej, a angielski tuż za nimi; szerszy zestaw języków europejskich jest właśnie wdrażany.** Wolimy wymienić kilka solidnych języków, niż sugerować wiele ukończonych.

> *Ocena osobna dla każdego języka, a nie jedna, skrojona pod angielski poprzeczka jakości dla wszystkich.*

## Gdzie wchodzi człowiek

Najważniejsze pytanie, na które odpowiadamy wprost — w tym o to, jak zmienia się ono w miarę, jak rośniemy.

**W fazie próbnej, w której jesteśmy teraz, system doprowadza każdy fragment do standardu wizji, a potem człowiek czyta go, zanim zostanie opublikowany** — przegląd z prawem zmiany czegokolwiek, prowadzony przez kogoś, kto zna zarówno język źródłowy, jak i docelowy. Tak właśnie uczymy się, gdzie systemowi można zaufać, i dlatego zaczynamy od garstki rozdziałów, zamiast pospiesznie wypuszczać całą Biblię.

**Na dużą skalę ten przedpublikacyjny przegląd nie może pozostać taki sam — i twierdzimy, że nie powinien.** Sensem Aperto jest dotrzeć do wspólnot, które czekały pokoleniami właśnie dlatego, że tłumaczenie wers po wersie ludzką ręką do nich się nie skaluje. Dlatego system jest tak pomyślany, by *od tego nie zależeć*: ludzie ustalają metodę i standardy oraz czuwają nad każdym krytykiem; próg gwarantuje, że nic zepsutego ani anachronicznego nigdy nie ujrzy światła dziennego; słabsze fragmenty pojawiają się oznaczone, a nie ukryte.

**Tu przekład cyfrowy ma przewagę, jakiej drukowany nigdy nie miał: może być żywy, a nie ostateczny.** Każdy tłumacz wie, że o tym, czy dane oddanie tekstu trafia, ostatecznie nie rozstrzyga jego własny osąd, lecz odbiór czytelników — to, czy słowa docierają do tych, którzy je czytają — a tego jednego żaden przegląd przed publikacją nie zmierzy z góry do końca. Drukowana Biblia zamraża swój najlepszy domysł na całe pokolenie; cyfrowa nie musi. Przegląd staje się więc rozmową, która trwa po publikacji: nasze narzędzie pod adresem [translate.aperto.bible](https://translate.aperto.bible) pozwala każdemu przeczytać fragment, prześledzić rozumowanie stojące za danym oddaniem i powiedzieć nam, gdzie brzmi prawdziwie, a gdzie nie. Ta informacja zwrotna wraca do systemu — powracające nieporozumienie staje się poprawką, drażniący rejestr zmienia instrukcję dla krytyka. Część tej pętli działa już dziś; część jest jeszcze podłączana.

Dlatego „ludzki osąd jest zwielokrotniony, a nie zastąpiony” znaczy tyle: to ludzie decydują, jak wygląda *dobro*, czytają tekst przed publikacją, póki jesteśmy na tyle mali, by móc to robić, i — w każdej skali — nieustannie słuchają tych, dla których przekład naprawdę powstaje. Maszyna bierze na siebie ilość. Osąd pozostaje ludzki.

> *Człowiek w obiegu, napędzany kołem zamachowym informacji zwrotnej — prawdziwe poprawki z czasem ulepszają same standardy.*

## Czego jeszcze nie skończyliśmy

Strona, która opisywałaby wyłącznie to, co działa, byłaby reklamą. Kilka rzeczy jest naprawdę wciąż w toku:

- Część krytyków — spójność międzyjęzykowa, tłumaczenie zwrotne, statystyczna kontrola „czyta się jak rodzima literatura” — jest gotowa tylko częściowo i nie wszędzie jeszcze na nich polegamy.
- Pełne pokrycie sięga kilku języków, a nie całej mapy.
- Pętla wiodąca od zgłoszenia czytelnika z powrotem do standardów częściowo działa, a częściowo jest jeszcze podłączana.
- Niektóre kroki publikacji między naszym wewnętrznym repozytorium a tą witryną nadal wykonujemy ręcznie.

Nic z tego nie rusza progu: nic zepsutego ani anachronicznego nie zostaje opublikowane. Ta strona opisuje system wciąż budowany — i będziemy ją uaktualniać w miarę, jak luki się domykają.
