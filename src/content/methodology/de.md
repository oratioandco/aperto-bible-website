# Wie Aperto wirklich funktioniert

Wer [unsere Prozessseite](/process) gelesen hat, kennt das *Warum*. Hier geht es um das *Wie* — um die eigentliche Maschinerie, samt der Teile, an denen noch gebaut wird.

„KI-Bibelübersetzung": ein Begriff, bei dem man stutzen sollte. Auch uns lässt er stutzen. Und die ehrliche Antwort auf dieses Misstrauen ist keine Beschwichtigung, sondern der offene Blick auf die Nähte. Nichts im Folgenden ist Metapher — es sind echte Prüfungen, echte Grenzwerte, echte Fehler, aufgespürt und behoben. Wo etwas vorläufig ist oder noch nicht gebaut, steht es da.

## Das Problem, das wir lösen

Wer von „KI-Übersetzung" redet, meint meist stillschweigend Englisch — und setzt ebenso stillschweigend voraus, *gut genug* genüge. Beides trifft hier nicht zu.

**Außerhalb des Englischen fällt die Qualität der Modelle ab.** Am stärksten sind die heutigen Modelle in jener Sprache, die sie am häufigsten gesehen haben. Dasselbe Modell, das mühelos flüssiges Englisch schreibt, bringt im Deutschen oder Polnischen — und in kleineren Sprachen erst recht — Prosa hervor, die grammatisch tadellos ist und sich trotzdem unverkennbar *fremd* anhört: der Tonfall einer Übersetzung, nicht die Stimme eines Autors in seiner Muttersprache. Ungezähmt erbt eine Übersetzung genau diese Schwächen.

**Die Bibel verträgt kein „ungefähr".** Eine Paraphrase, die zu 95 Prozent stimmt, ist für die meisten KI-Produkte ein gutes Ergebnis. Bei einer Bibel hieße das, zu 5 Prozent falschzuliegen über einen Text, auf den Menschen ihr Leben gründen — und diese 5 Prozent treten zutage als geliehenes Kirchenvokabular, als untergeschobene Bedeutung, als modernes Ding in einer Szene des ersten Jahrhunderts. Der Maßstab ist nicht *ungefähr*. Er ist muttersprachliches literarisches Niveau, ohne einen einzigen vermeidbaren Makel.

Das eigentliche Problem lautet also: Wie bewegt man ein ungleichmäßiges, aufs Englische verzerrtes Werkzeug dazu, Sprache um Sprache eine wirklich muttersprachliche, wirklich genaue Bibelsprache hervorzubringen — und *zu wissen*, wann das gelungen ist? Die Antwort ist kein einzelnes geniales Modell. Sie ist ein System, gebaut, um aufzufangen, was jedes Modell für sich falsch macht, und um das Ergebnis ehrlich zu vermessen. Wer selbst mit KI baut, erkennt die Grundform wieder: mehrere Fassungen erzeugen, sie von automatischen Prüfern beurteilen lassen, Veröffentlichungen an harten Schranken stoppen, unsichere Ausgaben markieren, den Menschen im Spiel halten. Jeder dieser Schritte wird benannt, sobald er an der Reihe ist.

<!--DIAGRAM:pipeline-->

## Wir übersetzen aus dem Griechischen und Hebräischen — nicht aus dem Englischen

Jede Passage beginnt mit Wissenschaft, nicht mit Software. Am Anfang sichtet ein Rechercheschritt die jüngere Fachliteratur zum Kapitel — aktuelle Kommentare, Forschung aus Fachzeitschriften, lexikalische Arbeiten, nicht bloß das, was alt genug ist, um frei zu sein — und trägt sie in einem Dossier zusammen. Grundlage sind die maßgeblichen wissenschaftlichen Editionen des Urtextes: das griechische Neue Testament von Nestle-Aland/UBS und, fürs Hebräische, die Biblia Hebraica Stuttgartensia. Dann geht ein Übersetzer und Bibelwissenschaftler den griechischen oder hebräischen Originaltext an diesem Dossier durch — die Bedeutungsbreite jedes gewichtigen Wortes, die alttestamentlichen Anklänge, das Gewicht eines Begriffs, das kulturelle Detail, das ein Hörer des ersten Jahrhunderts als selbstverständlich mitdachte. Daraus entsteht eine schriftliche Auslegung, der die gesamte Pipeline verpflichtet bleibt.

Unverblümt gesagt: **Aperto ist aus den Quelltexten übersetzt, nicht aus der Übersetzung eines anderen umformuliert.** Die KI setzt beim Griechischen an, bei unserer Auslegung, bei einer Stilvorgabe und einem Glossar je Sprache — und schreibt frische Literatur in der Zielsprache.

## Quellen und Urheberrecht

Zwei berechtigte Fragen liegen unter all dem: *Was* steht da eigentlich — und *ist das überhaupt erlaubt?*

Unsere Auslegung ist eigene Arbeit, zusammengeführt aus der besten Wissenschaft über alle Traditionen hinweg — katholisch, protestantisch, orthodox, pfingstkirchlich —, um zu einer wahrhaft ökumenischen Lesart zu kommen. Wir ziehen sie zurate, wie es jeder Kommentator seit jeher getan hat: lesen, abwägen, die eigene Analyse schreiben. **Wir geben keine ganzen urheberrechtlich geschützten Kommentare oder Bibeln neu heraus, und der veröffentlichte Bibeltext enthält keine fremde Übersetzung — er ist unsere eigene Wiedergabe aus den Ursprachen.** Wo unsere Auslegung eine bestimmte Quelle aufgreift, tut sie es wie jede Studienbibel: als kurzes, klar ausgewiesenes Zitat. Lieber steht sie auf der besten Wissenschaft der Gegenwart, als sich auf das zu beschränken, was zufällig gemeinfrei und ein Jahrhundert veraltet ist.

> *Wie bei jedem Forschungswerkzeug: belegen, kurz zitieren, zusammenführen — ohne die Quellen selbst erneut bereitzustellen.*

## Viele Entwürfe, nicht einer

Ein einzelnes Modell hat ein einziges Bündel von Gewohnheiten. Also entsteht von jedem Kapitel mehrere unabhängige Entwürfe parallel — derzeit bis zu vier, von verschiedenen Anbietern (Anthropic, OpenAI, Google, Mistral) — jeder mit denselben Eingaben. Verschiedene Modellfamilien haben verschiedene Stärken; zwischen Kandidaten zu wählen, ist besser, als einem einzigen zu vertrauen. Die Entwürfe werden nicht vermischt: Jeder ist eine vollständige Übersetzung, und die nächste Stufe entscheidet, welcher gewinnt — indem sie versucht, ihn auseinanderzunehmen.

> *Ensemble-Sampling, um die Schlagseite eines einzelnen Modells auszugleichen.*

## Das Gremium, das den Text auseinandernimmt

Jeden Entwurf liest ein Gremium unabhängiger Kritiker — getrennte Prüfer, jeder mit einer einzigen Aufgabe und dazu angehalten, sich schwer zufriedenzugeben. Sie fahnden nach: unnatürlicher Formulierung; Archaismen und Kirchenjargon; Calque, also der heimlich in die Zielsprache geschmuggelten Grammatik der Ausgangssprache; einem Tonfall, der ins Predigthafte oder ins Trockene abrutscht; Verständnislücken; schädlichen Stereotypen; theologischer Untreue; und mechanischen Fehlern, die nicht eine Meinung, sondern deterministische Werkzeuge aufspüren. Jeder Kritiker liefert konkrete Befunde — Vers, Textstelle, Grund des Scheiterns, Schweregrad —, und das Gremium legt Uneinigkeit offen, statt sie wegzumitteln.

Die Auswahl ist ein einziger, unparteiischer Durchgang: Jeder Kandidat wird auf dieselbe Weise bewertet, und der Entwurf mit den wenigsten und am wenigsten schweren Makeln gewinnt — und tritt anschließend in die unten beschriebene Überarbeitungsschleife ein. Manche Kritiker laufen heute schon über unsere Kernsprachen; andere — sprachübergreifende Konsistenz, Rückübersetzung — sind erst teilweise gebaut, und noch ist nicht überall auf sie Verlass.

> *LLM-as-judge-Bewertung: viele eng gefasste, gegnerische Prüfungen statt einer einzigen vagen Note.*

## Pflichtprüfungen, die eine Übersetzung erst bestehen muss

Kritik ist beratend; manche Prüfungen sind es nicht. Ein paar Pflichtprüfungen sind hart — wer an ihnen scheitert, kommt mit der Passage keinen Schritt weiter.

Am strengsten ist die **mechanische Prüfung**: Jeder Grammatik-, Rechtschreib-, Zeichensetzungs- oder Strukturfehler hält den Text auf, kontrolliert mit echtem Sprachwerkzeug, wo dieses Werkzeug ausgereift ist. Eine **Anachronismus-Prüfung** fängt moderne Dinge in einer Szene des ersten Jahrhunderts ab — würde sich eine Achtundzwanzigjährige in Berlin oder Warschau ein Auto vorstellen, ein Telefon oder eine Euromünze, und gab es das im Judäa des ersten Jahrhunderts nicht, wird es abgewiesen. Ein echter Fund: In einem deutschen Entwurf „fuhr" Zacharias einmal „nach Hause" — ein Auto, wo der Text einen Mann zu Fuß gehen lässt. Diese ganze Fehlerklasse blockiert die Prüfung inzwischen.

Das ist **die Schwelle**: Nichts Defektes und nichts sichtbar Fremdes wird je veröffentlicht. Und es ist eben auch nur die Schwelle — solide, aber noch ohne Klang.

> *CI-Regressionsschranken: automatische Prüfungen, die eine Veröffentlichung blockieren, nicht bloß warnen.*

<!--DIAGRAM:floorvision-->

## Von der Schwelle zur Vision

Wir halten mit Absicht zwei Maßstäbe. Die **Schwelle** ist mechanische Solidität. Die **Vision** ist muttersprachliches literarisches Niveau — Prosa, die sich liest, wie sie ein heutiger Romancier in dieser Sprache schriebe. Die meisten Passagen überschreiten die Schwelle mühelos; bis zur Vision braucht es Iteration: Die Befunde der Kritiker speisen eine Überarbeitungsschleife, die die markierten Stellen ausbessert und neu prüft — ein paar Runden lang, bis es zusammenläuft.

Der ehrliche Teil: Eine Passage, die die Schwelle überschreitet, die Vision aber noch nicht erreicht hat, wird trotzdem veröffentlicht — sie trägt dann eine **Markierung „geringe Sicherheit"**, damit sie zuerst zum Feinschliff hervorgehoben und nicht als fertig ausgegeben wird. Text, der defekt oder sichtbar übersetzt ist, wird überhaupt nie veröffentlicht. Lieber zeigen wir soliden, aber schlichten Text, markiert als unsicher, als die Grenze zwischen *korrekt* und *schön* zu verwischen. Das System ist darauf gebaut, zu wissen, was es noch nicht weiß.

> *Sicherheitsmarkierung, die schwache Ausgaben in die Prüfung leitet, statt sie stillschweigend auszuliefern.*

## Der Abgleich mit anderen Übersetzungen

Weil wir aus der Quelle übersetzen, prüfen wir die Arbeit auch *an* bestehenden Übersetzungen — aus zwei schützenden Gründen.

**Eigenständigkeit.** Jeder Entwurf wird Vers für Vers mit etablierten Übersetzungen derselben Sprache verglichen. Liegt unsere Formulierung einer von ihnen zu nah, ist das ein Warnsignal: Meist hat sich geliehene Formulierung eingeschlichen, und die Passage wird in ihrer eigenen Stimme neu geschrieben. Es ist ein Stolperdraht, der zufällige Anklänge fängt — er bestätigt unsere Unabhängigkeit, er schafft keine Abhängigkeit.

**Klarheit.** Gemessen wird außerdem an den klarsten modernen Übersetzungen — nicht um sie nachzuahmen, sondern um sicherzugehen, mindestens ebenso klar zu sein. Liest sich eine glattere Fassung dort besser, wo unsere steif klingt, ist das ein Mangel; ist unsere schwerer, weil sie eine Kante bewahrt, die die glattere weggeschliffen hat, geschieht das mit Absicht — und der Grund wird vermerkt.

Diese Texte stammen aus lizenzierten wissenschaftlichen Bibelschnittstellen — darunter die von YouVersion, frei nutzbar für nichtkommerzielle Arbeit wie unsere — und aus gemeinfreien Ausgaben, ausschließlich für interne Prüfungen verwendet. Der veröffentlichte Bibeltext enthält nichts von diesem fremden Text.

> *Abgleich mit Referenzen, dazu eine Kontaminationsprüfung, dass die Ausgabe kein Echo von ihnen trägt.*

## Der schwere Teil: andere Sprachen als Englisch

Hierhin fließt der Großteil der Entwicklungsarbeit, denn hier sind die Modelle am schwächsten. Das Deutsche kann den geisterhaften Tonfall der Lutherbibel aufnehmen; das Polnische kann in eine Kanzelstimme abgleiten, die Leser ihm verübeln; manche Sprachen kennen kaum eine Tradition der Bibel *als Literatur*. Eine Übersetzung kann grammatisch makellos sein und sich trotzdem fremd anfühlen.

Die Gegenmaßnahmen sind konkret. **Die Kritiker denken in der Zielsprache** — ihre Anweisungen sind in ihr geschrieben, sodass das System urteilt wie ein muttersprachlicher Lektor und sein Urteil nicht über das Englische umleitet (eine der Hauptarten, auf die nichtenglische Qualität still verfällt). **Jede Sprache hat ein literarisches Profil** — eine konkrete Leserschaft, Referenzautoren, ein theologisches Glossar. Und **die Aufnahme einer Sprache ist selbst eine Pflichtprüfung**: Stilvorgaben, ausgearbeitete Musterbeispiele, Glossar, Grammatikwerkzeug und ein Vergleichsbestand, bevor eine Sprache an den Start geht.

Wo wir stehen: **Deutsch und Polnisch sind am weitesten, Englisch dicht dahinter; eine breitere Gruppe europäischer Sprachen ist in aktiver Aufnahme.** Lieber benennen wir ein paar solide Sprachen, als viele fertige vorzutäuschen.

> *Bewertung je Sprachraum, nicht ein englisch geformter Qualitätsmaßstab für jede Sprache.*

## Wo der Mensch ins Spiel kommt

Die Frage, auf die es am meisten ankommt, klar beantwortet — und dazu, wie sie sich mit unserem Wachstum verändert.

**In der Erprobungsphase, in der wir jetzt stehen, trägt das System jede Passage bis zum Vision-Maßstab, und dann liest ein Mensch sie, bevor sie veröffentlicht wird** — eine Prüfung mit der Befugnis, alles zu ändern, durch jemanden, der die Ausgangs- wie die Zielsprache kennt. So lernen wir, wo dem System zu trauen ist, und darum beginnen wir mit einer kleinen Auswahl von Kapiteln, statt überstürzt eine ganze Bibel hinauszuwerfen.

**Im großen Maßstab kann diese Lesung vor der Veröffentlichung nicht dieselbe bleiben — und sie sollte es auch nicht.** Der Sinn von Aperto ist, Gemeinschaften zu erreichen, die seit Generationen genau deshalb warten, weil Zeile-für-Zeile-Übersetzung von Hand für sie nicht skaliert. Deshalb ist das System so gebaut, dass es *nicht von ihr abhängt*: Menschen setzen die Methode und die Maßstäbe und kuratieren jeden einzelnen Kritiker; die Schwelle garantiert, dass nie etwas Defektes oder Anachronistisches veröffentlicht wird; schwächere Passagen erscheinen markiert, nicht verborgen.

**Hier hat eine digitale Übersetzung einen Vorteil, den eine gedruckte nie hatte: Sie kann lebendig sein statt endgültig.** Jeder Übersetzer weiß, dass am Ende nicht das eigene Urteil darüber entscheidet, ob eine Wiedergabe trägt, sondern die Aufnahme durch das Publikum — ob die Worte bei den Menschen ankommen, die sie lesen —, und das ist das Eine, was keine Prüfung vor der Veröffentlichung im Voraus vollständig messen kann. Eine gedruckte Bibel friert ihre beste Vermutung für eine Generation ein; eine digitale muss das nicht. So wird die Prüfung zu einem Gespräch, das nach der Veröffentlichung weitergeht: Unser Werkzeug unter [translate.aperto.bible](https://translate.aperto.bible) lädt jeden ein, eine Passage zu lesen, die Begründung hinter einer Wiedergabe einzusehen und uns zu sagen, wo sie stimmig klingt und wo nicht. Diese Rückmeldung fließt zurück — aus einer wiederkehrenden Verwirrung wird eine Korrektur, ein Tonfall, der knirscht, schreibt die Vorgaben eines Kritikers um. Teile dieser Schleife sind heute schon live; Teile sind noch im Aufbau.

So heißt „menschliches Urteil wird vervielfacht, nicht ersetzt" genau dies: Menschen entscheiden, wie *gut* aussieht, prüfen vor der Veröffentlichung, solange wir klein genug dafür sind, und hören — in jedem Maßstab — weiter auf die Menschen, für die die Übersetzung eigentlich gemacht ist. Die Maschine besorgt die Menge. Das Urteil bleibt menschlich.

> *Mensch in der Schleife mit einem selbstverstärkenden Rückkopplungskreislauf — echte Korrekturen, die die Maßstäbe mit der Zeit besser machen.*

## Was wir noch nicht fertig haben

Eine Seite, die nur beschriebe, was funktioniert, wäre Marketing. Ein paar Dinge sind tatsächlich noch in Arbeit:

- Mehrere Kritiker — sprachübergreifende Konsistenz, Rückübersetzung, die statistische Prüfung „liest sich wie muttersprachliche Literatur" — sind erst teilweise gebaut und noch nicht überall verlässlich.
- Die volle Abdeckung reicht ein paar Sprachen tief, nicht über die ganze Landkarte.
- Die Rückkopplungsschleife von einer Markierung zurück in die Maßstäbe ist teils live, teils noch im Aufbau.
- Manche Veröffentlichungsschritte zwischen unserem internen Repository und dieser Seite werden noch von Hand erledigt.

Nichts davon rührt an die Schwelle: Nichts Defektes oder Anachronistisches wird veröffentlicht. Diese Seite beschreibt ein System, an dem noch gebaut wird — aktuell gehalten, während sich die Lücken schließen.
