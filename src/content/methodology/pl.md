# Jak naprawdę działa Aperto

Jeśli czytałeś [naszą stronę o procesie](/process), wiesz już, *dlaczego* to robimy. Ta strona mówi o tym, *jak* — opisuje sam mechanizm, łącznie z tym, co wciąż powstaje.

„Tłumaczenie Biblii przez sztuczną inteligencję” to sformułowanie, na którego dźwięk uważny czytelnik powinien przystanąć. Nas też skłania do zatrzymania. Uczciwą odpowiedzią na tę nieufność nie są zapewnienia, że wszystko gra — lecz odsłonięcie szwów. Nic, co opisujemy poniżej, nie jest metaforą: to realne kontrole, realne progi, realne błędy, które wychwyciliśmy i naprawiliśmy. Gdzie coś jest tymczasowe albo dopiero powstaje, mówimy o tym wprost.

## Problem, który rozwiązujemy

W większości rozmów o „tłumaczeniu przez AI” milcząco zakłada się angielski i milcząco zakłada się, że *wystarczająco dobrze* w zupełności wystarczy. Żadne z tych założeń się tu nie broni.

**Poza angielskim jakość modeli wyraźnie spada.** Dzisiejsze modele są najsilniejsze w języku, którego widziały najwięcej. Ten sam model, który po angielsku pisze płynnie, w niemieckim czy polskim — a w mniejszych językach tym bardziej — potrafi tworzyć prozę poprawną gramatycznie, lecz wyraźnie *obcą*: o rytmie przekładu, a nie głosie rodzimego pisarza. Bez nadzoru tłumaczenie dziedziczy dokładnie te słabości.

**Pismo Święte nie znosi „mniej więcej”.** Parafraza trafna w 95% to świetny wynik dla większości produktów opartych na AI. W przypadku Biblii znaczy to mylić się w 5% co do tekstu, na którym ludzie opierają swoje życie — a te 5% objawia się jako zapożyczony kościelny żargon, zmyślone znaczenie, współczesny przedmiot wstawiony w scenę z pierwszego wieku. Poprzeczką nie jest *ogólny sens*; jest nią rodzimy rejestr literacki, wolny od każdej dającej się uniknąć usterki.

Prawdziwy problem brzmi więc tak: jak sprawić, by nierówne, przechylone w stronę angielskiego narzędzie tworzyło naprawdę rodzime, naprawdę wierne słowo Pisma — język po języku — i jak *wiedzieć*, kiedy już się to udało? Naszą odpowiedzią nie jest jeden sprytny model. To system zbudowany po to, by wychwytywać to, co myli każdy pojedynczy model, i by uczciwie mierzyć rezultat. Jeśli sam budujesz rozwiązania oparte na AI, rozpoznasz ten schemat: generować wiele wariantów, oceniać je automatycznymi ewaluatorami, blokować publikację na twardych bramkach, oznaczać wyniki o niskiej pewności, trzymać człowieka w pętli. Każdy z tych elementów nazywamy tam, gdzie do niego dochodzimy.

<!--DIAGRAM:pipeline-->

## Tłumaczymy z greki i hebrajskiego — nie z angielskiego

Każdy fragment zaczyna się od nauki, nie od oprogramowania. Najpierw etap badawczy przegląda najnowszą literaturę naukową poświęconą danemu rozdziałowi — bieżące komentarze, prace z czasopism, opracowania leksykalne, a nie tylko to, co jest na tyle stare, że dostępne za darmo — i zbiera to wszystko w opracowaniu wstępnym. Następnie tłumacz-badacz pracuje nad oryginalną greką lub hebrajskim w świetle tego opracowania: nad zakresem znaczeń każdego ważkiego słowa, echami Starego Testamentu, ciężarem, jaki niesie dany termin, szczegółem kulturowym oczywistym dla słuchacza z pierwszego wieku. Powstaje z tego spisana egzegeza, przed którą odpowiada cały dalszy proces.

Mówiąc wprost: **Aperto jest tłumaczone z tekstów źródłowych, a nie przeredagowane z cudzego przekładu.** AI wychodzi od greki, naszej egzegezy, specyfikacji stylu i glosariusza właściwego dla danego języka — i pisze świeżą literaturę w języku docelowym.

## Źródła i prawa autorskie

Pod tym wszystkim kryją się dwa zasadne pytania: *co* właściwie czytasz oraz *czy tak wolno?*

Nasza egzegeza jest naszą własną pracą — syntezą najlepszej myśli naukowej z różnych tradycji: katolickiej, protestanckiej, prawosławnej, zielonoświątkowej — z myślą o naprawdę ekumenicznym odczytaniu. Sięgamy po nią tak, jak od zawsze robi każdy komentator: czytamy, ważymy, piszemy własną analizę. **Nie publikujemy ponownie całych komentarzy ani Biblii objętych prawami autorskimi, a Pismo, które wydajemy, nie zawiera żadnego cudzego przekładu — jest to nasze własne tłumaczenie z języków źródłowych.** Tam, gdzie nasza egzegeza sięga do konkretnego źródła, robi to tak jak każda Biblia z komentarzem: krótkim, wyraźnie przypisanym cytatem. Wolimy stać na najlepszej współczesnej myśli naukowej, niż ograniczać się do tego, co akurat wygasło spod ochrony prawnej i jest o sto lat przestarzałe.

> *Jak każde narzędzie badawcze: podaj źródło, cytuj krótko i syntetyzuj — bez ponownego udostępniania samych źródeł.*

## Wiele wersji roboczych, nie jedna

Pojedynczy model ma jeden zestaw nawyków. Dlatego dla każdego rozdziału tworzymy równolegle kilka niezależnych wersji roboczych — obecnie do czterech, od różnych dostawców (Anthropic, OpenAI, Google, Mistral) — a każda dostaje identyczne dane wejściowe. Różne rodziny modeli mają różne mocne strony; wybór spośród kandydatów bije zaufanie jednemu. Wersji się nie miesza: każda jest kompletnym tłumaczeniem, a o tym, która wygra, rozstrzyga kolejny etap — próbując ją złamać.

> *Próbkowanie zespołowe (ensemble), by znieść tendencyjność któregokolwiek pojedynczego modelu.*

## Panel, który próbuje złamać tekst

Każdą wersję roboczą czyta panel niezależnych krytyków — osobnych ewaluatorów, z których każdy ma jedno zadanie i polecenie, by trudno było go zadowolić. Tropią: nienaturalne sformułowania; archaizmy i kościelny żargon; kalki (gramatykę języka źródłowego przemyconą do docelowego); zsuwanie się rejestru w kazanie lub w suchość; luki w zrozumiałości; szkodliwe stereotypy; niewierność teologiczną; oraz błędy mechaniczne, wychwytywane przez deterministyczne narzędzia, a nie przez opinię. Każdy zwraca konkretne ustalenia — werset, fragment, na czym zawodzi, jak poważnie — a panel uwidacznia rozbieżności, zamiast je uśredniać.

Wybór to jeden, bezstronny przebieg: każdy kandydat jest oceniany tą samą miarą, a wygrywa wersja z najmniejszą liczbą najmniej poważnych usterek, która następnie wchodzi w opisaną niżej pętlę poprawek. Część krytyków działa już dziś we wszystkich naszych podstawowych językach; inni — spójność międzyjęzykowa, tłumaczenie zwrotne — są zbudowani tylko częściowo i jeszcze nie wszędzie na nich polegamy.

> *Ocena typu LLM-jako-sędzia: wiele wąskich, kontradyktoryjnych kontroli zamiast jednej mglistej oceny.*

## Bramki, przez które tekst musi się przebić

Krytyka ma charakter doradczy; niektóre kontrole — nie. Kilka bramek jest twardych: jeśli fragment ich nie przejdzie, nie rusza dalej.

**Bramka mechaniczna** jest najsurowsza: każdy błąd gramatyczny, ortograficzny, interpunkcyjny czy strukturalny zatrzymuje tekst — sprawdzamy to prawdziwymi narzędziami lingwistycznymi tam, gdzie są one dojrzałe. **Bramka anachronizmów** wychwytuje współczesne przedmioty w scenie z pierwszego wieku — jeśli dwudziestoośmiolatek z Berlina czy Warszawy wyobraziłby sobie samochód, telefon albo monetę euro, a w Judei pierwszego wieku to nie istniało, fragment zostaje odrzucony. Prawdziwy przypadek: w jednej z niemieckich wersji Zachariasz „pojechał do domu” — samochód tam, gdzie tekst mówi o idącym człowieku. Bramka blokuje teraz całą tę klasę błędów.

To jest **podłoga**: nic zepsutego ani widocznie obcego nigdy nie zostaje opublikowane. Jest to też tylko podłoga — tekst zdrowy, lecz jeszcze nieśpiewający.

> *Bramki regresji w CI: automatyczne kontrole, które blokują publikację, a nie tylko ostrzegają.*

<!--DIAGRAM:floorvision-->

## Od podłogi do wizji

Trzymamy dwa standardy — i robimy to świadomie. **Podłoga** to mechaniczna poprawność. **Wizja** to rodzimy rejestr literacki — proza, która czyta się tak, jak pisze współczesny powieściopisarz w danym języku. Większość fragmentów przekracza podłogę szybko; dojście do wizji wymaga iteracji, gdy ustalenia krytyków zasilają pętlę poprawek, która naprawia oznaczone fragmenty i sprawdza je ponownie — kilka rund, aż wynik się ustali.

A teraz część uczciwa: fragment, który przekroczył podłogę, lecz nie sięgnął jeszcze wizji, mimo to zostaje opublikowany — opatrzony **etykietą niskiej pewności**, tak by w pierwszej kolejności trafiał do dopracowania, a nie był przedstawiany jako gotowy. Tekst zepsuty albo widocznie przetłumaczony nie zostaje opublikowany w ogóle. Wolimy pokazać ci tekst zdrowy, choć prosty, który sami oznaczyliśmy, niż zacierać granicę między *poprawnym* a *pięknym*. System jest zbudowany tak, by wiedzieć, czego jeszcze nie wie.

> *Oznaczanie pewności, które kieruje słabsze wyniki do przeglądu, zamiast wydawać je po cichu.*

## Porównanie z innymi przekładami

Ponieważ tłumaczymy ze źródła, zestawiamy też naszą pracę z istniejącymi przekładami — z dwóch ochronnych powodów.

**Oryginalność.** Porównujemy każdą wersję roboczą, werset po wersecie, z uznanymi przekładami w danym języku. Jeśli nasze sformułowanie trzyma się zbyt blisko któregokolwiek z nich, to sygnał ostrzegawczy: zwykle wkradło się zapożyczone brzmienie, a fragment piszemy na nowo, własnym głosem. To czujnik, który wychwytuje przypadkowe echa — potwierdza naszą niezależność, a nie tworzy zależności.

**Jasność.** Zestawiamy się także z najczytelniejszymi współczesnymi przekładami — nie po to, by je naśladować, lecz by mieć pewność, że jesteśmy przynajmniej równie jaśni. Jeśli gładsza wersja czyta się lepiej tam, gdzie nasza jest sztywna, to usterka; jeśli nasza jest trudniejsza, bo zachowuje ostrość, którą gładsza wygładziła, to działanie celowe i odnotowujemy dlaczego.

Teksty te pochodzą z licencjonowanych naukowych interfejsów biblijnych — w tym z YouVersion, z którego wolno nam korzystać do pracy niekomercyjnej, takiej jak nasza — oraz z wydań w domenie publicznej, używanych wyłącznie do kontroli wewnętrznych. Biblia, którą publikujemy, nie zawiera żadnego z tych cudzych tekstów.

> *Porównywanie z punktami odniesienia, plus kontrola skażenia sprawdzająca, czy wynik ich nie powtarza.*

## Najtrudniejsza część: języki inne niż angielski

Tu trafia większość naszej pracy inżynierskiej, bo to tu modele są najsłabsze. Niemiecki potrafi przejąć widmowy rytm Biblii Lutra; polski może zsunąć się w kaznodziejski ton, którego czytelnicy nie znoszą; niektóre języki niemal nie mają tradycji Biblii *jako literatury*. Tłumaczenie może mieć nienaganną gramatykę, a mimo to brzmieć obco.

Nasze środki zaradcze są konkretne. **Krytycy rozumują w języku docelowym** — ich instrukcje są w nim napisane, więc system ocenia tak, jak zrobiłby to rodzimy redaktor, zamiast przepuszczać swój osąd przez angielski (jeden z głównych sposobów, w jaki jakość poza angielskim po cichu się obniża). **Każdy język ma swój profil literacki** — konkretnego czytelnika, autorów wzorcowych, glosariusz teologiczny. A **wdrożenie języka jest bramką**: specyfikacje stylu, opracowane przykłady, glosariusz, narzędzia gramatyczne i zestaw porównawczy muszą być gotowe, zanim język wejdzie na żywo.

Gdzie jesteśmy: **niemiecki i polski są najdalej posunięte, a angielski tuż za nimi; szerszy zestaw języków europejskich jest w trakcie wdrażania.** Wolimy wymienić kilka solidnych języków, niż sugerować wiele ukończonych.

> *Ocena dla każdego języka z osobna, a nie jedna, skrojona pod angielski poprzeczka jakości dla wszystkich.*

## Gdzie wchodzi człowiek

Najważniejsze pytanie, na które odpowiadamy wprost — w tym o to, jak zmienia się to wraz z naszym wzrostem.

**W fazie próbnej, w której teraz jesteśmy, system doprowadza każdy fragment do standardu wizji, a następnie człowiek czyta go, zanim zostanie opublikowany** — przegląd z prawem do zmiany czegokolwiek, dokonywany przez kogoś, kto zna zarówno język źródłowy, jak i docelowy. Tak właśnie uczymy się, gdzie systemowi można zaufać, i dlatego zaczynamy od niewielkiego zestawu rozdziałów, zamiast pospiesznie wypuszczać całą Biblię.

**Na dużą skalę ten przedpublikacyjny przegląd nie może pozostać taki sam — i twierdzimy, że nie powinien.** Sensem Aperto jest dotarcie do wspólnot, które czekały pokoleniami właśnie dlatego, że tłumaczenie wers po wersie ręką człowieka się dla nich nie skaluje. Dlatego system jest zbudowany tak, by *od tego nie zależeć*: ludzie ustalają metodę i standardy oraz kuratorują każdego krytyka; podłoga gwarantuje, że nic zepsutego ani anachronicznego nigdy nie zostanie opublikowane; słabsze fragmenty pojawiają się oznaczone, a nie ukryte.

**Tu przekład cyfrowy ma przewagę, jakiej drukowany nigdy nie miał: może być żywy, a nie ostateczny.** Każdy tłumacz wie, że o tym, czy dane oddanie tekstu działa, ostatecznie nie rozstrzyga jego własny osąd, lecz odbiór czytelników — to, czy słowa trafiają do tych, którzy je czytają — a to jedyna rzecz, której żaden przegląd przedpublikacyjny nie zmierzy w pełni z góry. Drukowana Biblia zamraża swój najlepszy domysł na całe pokolenie; cyfrowa nie musi. Przegląd staje się więc rozmową, która trwa po publikacji: nasze narzędzie pod adresem [translate.aperto.bible](https://translate.aperto.bible) pozwala każdemu przeczytać fragment, zobaczyć rozumowanie stojące za danym oddaniem i powiedzieć nam, gdzie brzmi prawdziwie, a gdzie nie. Ta informacja zwrotna wraca do systemu — powracające nieporozumienie staje się poprawką, drażniący rejestr aktualizuje instrukcję krytyka. Część tej pętli działa już dziś; część jest jeszcze podłączana.

Dlatego „ludzki osąd jest zwielokrotniony, a nie zastąpiony” znaczy tyle: to ludzie decydują, jak wygląda *dobro*, sprawdzają tekst przed publikacją, póki jesteśmy na tyle mali, by móc to robić, oraz — w każdej skali — nieustannie słuchają tych, dla których przekład naprawdę powstaje. Maszyna bierze na siebie objętość. Osąd pozostaje ludzki.

> *Człowiek w pętli z kołem zamachowym informacji zwrotnej — realne poprawki z czasem ulepszają same standardy.*

## Czego jeszcze nie skończyliśmy

Strona, która opisywałaby wyłącznie to, co działa, byłaby marketingiem. Kilka rzeczy jest naprawdę wciąż w toku:

- Część krytyków — spójność międzyjęzykowa, tłumaczenie zwrotne, statystyczna kontrola „czyta się jak rodzima literatura” — jest zbudowana tylko częściowo i jeszcze nie wszędzie na nich polegamy.
- Pełne pokrycie sięga kilku języków, a nie całej mapy.
- Pętla od oznaczenia zgłoszonego przez czytelnika z powrotem do standardów częściowo działa, a częściowo jest jeszcze podłączana.
- Niektóre kroki publikacji między naszym wewnętrznym repozytorium a tą witryną są nadal wykonywane ręcznie.

Nic z tego nie zmienia podłogi: nic zepsutego ani anachronicznego nie zostaje opublikowane. Ta strona opisuje system wciąż budowany — i będziemy ją aktualizować w miarę, jak luki się domykają.
