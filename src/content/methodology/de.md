# Wie Aperto wirklich arbeitet

Wer [unsere Prozessseite](/process) gelesen hat, weiß, *warum* wir das tun. Diese Seite zeigt, *wie* — die eigentliche Maschinerie, samt der Teile, die noch im Bau sind.

„KI-Bibelübersetzung" ist ein Begriff, bei dem eine aufmerksame Leserin stutzen sollte. Auch uns lässt er stutzen. Die ehrliche Antwort auf dieses Misstrauen ist keine Beschwichtigung, sondern der offene Blick auf die Nähte. Nichts im Folgenden ist Metapher — es sind echte Prüfungen, echte Schwellen, echte Fehler, die wir aufgespürt und behoben haben. Wo etwas vorläufig oder noch nicht gebaut ist, sagen wir es.

## Das Problem, das wir lösen

Wer von „KI-Übersetzung" spricht, meint meist stillschweigend Englisch — und nimmt stillschweigend an, *gut genug* genüge. Beides gilt hier nicht.

**Jenseits des Englischen lässt die Qualität der Modelle nach.** Die heutigen Modelle sind in jener Sprache am stärksten, die sie am häufigsten gesehen haben. Dasselbe Modell, das flüssiges Englisch schreibt, kann — im Deutschen oder Polnischen und erst recht in kleineren Sprachen — Prosa hervorbringen, die grammatisch korrekt, aber unverkennbar *fremd* ist: der Tonfall einer Übersetzung, nicht die Stimme eines muttersprachlichen Autors. Wird das nicht in den Griff genommen, erbt eine Übersetzung genau diese Schwächen.

**Die Heilige Schrift verträgt kein „ungefähr".** Eine Paraphrase, die zu 95 Prozent stimmt, ist für die meisten KI-Produkte ein gutes Ergebnis. Bei einer Bibel bedeutet sie, zu 5 Prozent falsch über jenen Text zu liegen, auf den Menschen ihr Leben gründen — und diese 5 Prozent zeigen sich als geliehenes Kirchenvokabular, als untergeschobene Bedeutung, als modernes Ding, das in eine Szene des ersten Jahrhunderts fällt. Der Maßstab ist nicht *ungefähr*, sondern muttersprachliches literarisches Niveau ohne vermeidbaren Makel.

Das eigentliche Problem lautet also: Wie bringt man ein ungleichmäßiges, aufs Englische verzerrtes Werkzeug dazu, Sprache für Sprache wahrhaft muttersprachliche, wahrhaft genaue Schriftsprache hervorzubringen — und *zu erkennen*, wann das gelungen ist? Unsere Antwort ist nicht ein einzelnes kluges Modell. Sie ist ein System, das auffängt, was jedes einzelne Modell falsch macht, und das Ergebnis ehrlich misst. Wer selbst mit KI baut, kennt das Muster: mehrere Generierungen ziehen, sie mit automatischen Prüfern bewerten, Veröffentlichungen an harten Schranken stoppen, Ausgaben mit geringer Sicherheit markieren, den Menschen im Spiel halten. Wir benennen jeden Schritt, sobald wir ihn erreichen.

<!--DIAGRAM:pipeline-->

## Wir übersetzen aus dem Griechischen und Hebräischen — nicht aus dem Englischen

Jede Passage beginnt mit Wissenschaft, nicht mit Software. Zuerst sichtet ein Rechercheschritt die jüngere Fachliteratur zum Kapitel — aktuelle Kommentare, Forschung aus Fachzeitschriften, lexikalische Arbeiten, nicht bloß das, was alt genug ist, um frei zu sein — und trägt sie in einem Dossier zusammen. Dann arbeitet ein Übersetzer und Bibelwissenschaftler den griechischen oder hebräischen Originaltext an diesem Dossier durch: die Bedeutungsbreite jedes gewichtigen Wortes, alttestamentliche Anklänge, das Gewicht, das ein Begriff trägt, das kulturelle Detail, das ein Hörer des ersten Jahrhunderts als selbstverständlich voraussetzte. Daraus entsteht eine schriftliche Auslegung, der die gesamte Pipeline verpflichtet bleibt.

Klar gesagt: **Aperto ist aus den Quelltexten übersetzt, nicht aus der Übersetzung eines anderen umformuliert.** Die KI setzt beim Griechischen an, bei unserer Auslegung, einer Stilvorgabe und einem Glossar je Sprache — und schreibt frische Literatur in der Zielsprache.

## Quellen und Urheberrecht

Zwei berechtigte Fragen liegen all dem zugrunde: *Was* lese ich da — und *ist das überhaupt erlaubt?*

Unsere Auslegung ist unsere eigene Arbeit, zusammengeführt aus der besten Wissenschaft über alle Traditionen hinweg — katholisch, protestantisch, orthodox, pfingstkirchlich — für eine wahrhaft ökumenische Lesart. Wir ziehen sie zurate, wie es jeder Kommentator seit jeher tut: lesen, abwägen, die eigene Analyse schreiben. **Wir veröffentlichen keine ganzen urheberrechtlich geschützten Kommentare oder Bibeln erneut, und die Schrift, die wir herausgeben, enthält keine fremde Übersetzung — sie ist unsere eigene Wiedergabe aus den Ursprachen.** Wo unsere Auslegung eine bestimmte Quelle heranzieht, tut sie es wie jede Studienbibel: als kurzes, klar gekennzeichnetes Zitat. Wir stehen lieber auf der besten gegenwärtigen Wissenschaft, als uns auf das zu beschränken, was zufällig gemeinfrei und ein Jahrhundert veraltet ist.

> *Wie bei jedem Forschungswerkzeug: belegen, kurz zitieren und zusammenführen — ohne die Quellen selbst erneut bereitzustellen.*

## Viele Entwürfe, nicht einer

Ein einzelnes Modell hat einen einzigen Satz an Gewohnheiten. Deshalb erzeugen wir von jedem Kapitel mehrere unabhängige Entwürfe parallel — derzeit bis zu vier, von verschiedenen Anbietern (Anthropic, OpenAI, Google, Mistral) — alle mit identischen Eingaben. Verschiedene Modellfamilien haben verschiedene Stärken; zwischen Kandidaten zu wählen, ist besser, als einem einzigen zu vertrauen. Die Entwürfe werden nicht vermischt: Jeder ist eine vollständige Übersetzung, und die nächste Stufe entscheidet, welcher gewinnt — indem sie versucht, ihn zu zerlegen.

> *Ensemble-Sampling, um die Verzerrung eines einzelnen Modells auszugleichen.*

## Das Gremium, das den Text zu zerlegen versucht

Jeder Entwurf wird von einem Gremium unabhängiger Kritiker gelesen — getrennte Prüfer, jeder mit einer einzigen Aufgabe und angewiesen, schwer zufriedenzustellen zu sein. Sie fahnden nach: unnatürlicher Formulierung; Archaismen und Kirchenvokabular; Calque (in die Zielsprache eingeschmuggelter Grammatik der Ausgangssprache); Abdriften des Tonfalls ins Predigthafte oder Trockene; Verständnislücken; schädlichen Stereotypen; theologischer Untreue; und mechanischen Fehlern, die deterministische Werkzeuge aufspüren statt bloße Meinung. Jeder liefert konkrete Befunde zurück — Vers, Textstelle, warum sie scheitert, Schweregrad — und das Gremium legt Meinungsverschiedenheiten offen, statt sie wegzumitteln.

Die Auswahl ist ein einziger, unvoreingenommener Durchgang: Jeder Kandidat wird auf dieselbe Weise bewertet, und der Entwurf mit den wenigsten und am wenigsten schweren Makeln gewinnt — und tritt anschließend in die unten beschriebene Überarbeitungsschleife ein. Manche Kritiker laufen heute schon über unsere Kernsprachen; andere — sprachübergreifende Konsistenz, Rückübersetzung — sind erst teilweise gebaut, und wir verlassen uns noch nicht überall auf sie.

> *LLM-as-judge-Bewertung: viele eng gefasste, gegnerische Prüfungen statt einer vagen Gesamtnote.*

## Schranken, durch die er sich verdienen muss

Kritik ist beratend; manche Prüfungen sind es nicht. Einige Schranken sind hart — wer sie reißt, dessen Passage rückt nicht weiter.

Die **mechanische Schranke** ist die strengste: Jeder Grammatik-, Rechtschreib-, Zeichensetzungs- oder Strukturfehler hält den Text zurück, geprüft mit echtem Sprachwerkzeug, wo dieses Werkzeug ausgereift ist. Eine **Anachronismus-Schranke** fängt moderne Dinge in einer Szene des ersten Jahrhunderts ab — wenn sich eine Achtundzwanzigjährige in Berlin oder Warschau ein Auto, ein Telefon oder eine Euromünze vorstellen würde und es das im Judäa des ersten Jahrhunderts nicht gab, wird es abgewiesen. Ein echter Fund: In einem deutschen Entwurf „fuhr" Zacharias einst „nach Hause" — ein Auto, wo der Text einen Mann zu Fuß gehen lässt. Die Schranke blockiert nun diese ganze Fehlerklasse.

Das ist **der Boden**: Nichts Defektes oder sichtbar Fremdes wird je veröffentlicht. Doch es ist eben auch nur der Boden — solide, aber noch nicht singend.

> *CI-Regressionsschranken: automatische Prüfungen, die eine Veröffentlichung blockieren, nicht bloß warnen.*

<!--DIAGRAM:floorvision-->

## Vom Boden zur Vision

Wir halten bewusst zwei Maßstäbe. Der **Boden** ist mechanische Solidität. Die **Vision** ist muttersprachliches literarisches Niveau — Prosa, die sich liest, wie ein heutiger Romanautor in dieser Sprache schreibt. Die meisten Passagen nehmen den Boden im Nu; bis zur Vision braucht es Iteration: Die Befunde der Kritiker speisen eine Überarbeitungsschleife, die die markierten Stellen korrigiert und erneut prüft — ein paar Runden, bis es zusammenläuft.

Der ehrliche Teil: Eine Passage, die den Boden nimmt, aber die Vision noch nicht erreicht hat, wird dennoch veröffentlicht — mit einer **Markierung „geringe Sicherheit"**, sodass sie zuerst zum Feinschliff hervorgehoben und nicht als fertig ausgegeben wird. Text, der defekt oder sichtbar übersetzt ist, wird überhaupt nie veröffentlicht. Wir zeigen Ihnen lieber soliden, aber schlichten Text, den wir markiert haben, als die Grenze zwischen *korrekt* und *schön* zu verwischen. Das System ist darauf gebaut, zu wissen, was es noch nicht weiß.

> *Sicherheitsmarkierung, die schwache Ausgaben in die Prüfung leitet, statt sie stillschweigend auszuliefern.*

## Der Abgleich mit anderen Übersetzungen

Weil wir aus der Quelle übersetzen, prüfen wir unsere Arbeit auch *an* bestehenden Übersetzungen — aus zwei schützenden Gründen.

**Eigenständigkeit.** Wir vergleichen jeden Entwurf Vers für Vers mit etablierten Übersetzungen in dieser Sprache. Liegt unsere Formulierung zu nah an einer von ihnen, ist das ein Warnsignal: Meist hat sich geliehene Formulierung eingeschlichen, und die Passage wird in ihrer eigenen Stimme neu geschrieben. Es ist ein Stolperdraht, der zufällige Anklänge fängt — er bestätigt unsere Unabhängigkeit, er schafft keine Abhängigkeit.

**Klarheit.** Wir messen uns außerdem an den klarsten modernen Übersetzungen — nicht um sie nachzuahmen, sondern um sicherzugehen, dass wir mindestens ebenso klar sind. Liest sich eine glattere Fassung besser, wo unsere steif ist, ist das ein Mangel; ist unsere schwerer, weil sie eine Kante bewahrt, die die glattere abgeschliffen hat, geschieht das mit Absicht, und wir vermerken, warum.

Diese Texte stammen aus lizenzierten wissenschaftlichen Bibelschnittstellen — darunter die von YouVersion, die wir für nichtkommerzielle Arbeit wie unsere frei nutzen dürfen — und aus gemeinfreien Ausgaben, ausschließlich für interne Prüfungen verwendet. Die Bibel, die wir herausgeben, enthält nichts von diesem fremden Text.

> *Abgleich mit Referenzen, dazu eine Kontaminationsprüfung, dass die Ausgabe sie nicht nachhallt.*

## Der schwere Teil: andere Sprachen als Englisch

Hierhin fließt der Großteil unserer Entwicklungsarbeit, denn hier sind die Modelle am schwächsten. Das Deutsche kann den Geistertonfall der Lutherbibel aufnehmen; das Polnische kann in eine Kanzelstimme abgleiten, die Leser übelnehmen; manche Sprachen haben kaum eine Tradition der Bibel *als Literatur*. Eine Übersetzung kann grammatisch makellos sein und sich dennoch fremd anfühlen.

Unsere Gegenmaßnahmen sind konkret. **Die Kritiker denken in der Zielsprache** — ihre Anweisungen sind in ihr geschrieben, sodass das System urteilt wie ein muttersprachlicher Lektor, statt sein Urteil über das Englische umzuleiten (eine der Hauptarten, auf die nicht-englische Qualität still verfällt). **Jede Sprache hat ein literarisches Profil** — eine konkrete Leserschaft, Referenzautoren, ein theologisches Glossar. Und **die Aufnahme einer Sprache ist eine Schranke**: Stilvorgaben, ausgearbeitete Musterbeispiele, Glossar, Grammatikwerkzeug und ein Vergleichsbestand, bevor eine Sprache live geht.

Wo wir stehen: **Deutsch und Polnisch sind am weitesten, mit Englisch dicht dahinter; eine breitere Gruppe europäischer Sprachen befindet sich in aktiver Aufnahme.** Wir benennen lieber ein paar solide Sprachen, als viele fertige vorzutäuschen.

> *Bewertung je Sprachraum, nicht ein englisch geformter Qualitätsmaßstab für jede Sprache.*

## Wo der Mensch ins Spiel kommt

Die Frage, auf die es am meisten ankommt, klar beantwortet — auch, wie sie sich mit unserem Wachstum verändert.

**In der Erprobungsphase, in der wir jetzt stehen, trägt das System jede Passage bis zum Vision-Maßstab, und dann liest ein Mensch sie, bevor sie veröffentlicht wird** — eine Prüfung mit der Befugnis, alles zu ändern, durch jemanden, der sowohl die Ausgangs- als auch die Zielsprache kennt. So lernen wir, wo dem System zu trauen ist, und darum beginnen wir mit einer kleinen Auswahl von Kapiteln, statt eine ganze Bibel zu überstürzen.

**Im großen Maßstab kann diese Lesung vor der Veröffentlichung nicht dieselbe bleiben — und wir meinen, sie sollte es auch nicht.** Der Sinn von Aperto ist, Gemeinschaften zu erreichen, die genau deshalb seit Generationen warten, weil Zeile-für-Zeile-Übersetzung durch Menschen für sie nicht skaliert. Deshalb ist das System so gebaut, dass es *nicht davon abhängt*: Menschen setzen die Methode und die Maßstäbe und kuratieren jeden Kritiker; der Boden garantiert, dass nie etwas Defektes oder Anachronistisches veröffentlicht wird; schwächere Passagen erscheinen markiert, nicht verborgen.

**Hier hat eine digitale Übersetzung einen Vorteil, den eine gedruckte nie hatte: Sie kann lebendig sein statt endgültig.** Jeder Übersetzer weiß, dass am Ende nicht das eigene Urteil darüber entscheidet, ob eine Wiedergabe trägt, sondern die Aufnahme durch das Publikum — ob die Worte bei den Menschen ankommen, die sie lesen — und das ist das Eine, was keine Prüfung vor der Veröffentlichung vorab vollständig messen kann. Eine gedruckte Bibel friert ihre beste Vermutung für eine Generation ein; eine digitale muss das nicht. So wird die Prüfung zu einem Gespräch, das nach der Veröffentlichung weitergeht: Unser Werkzeug unter [translate.aperto.bible](https://translate.aperto.bible) lässt jeden eine Passage lesen, die Begründung hinter einer Wiedergabe einsehen und uns sagen, wo sie stimmig klingt und wo nicht. Diese Rückmeldung fließt zurück — aus einer wiederkehrenden Verwirrung wird eine Korrektur, ein Tonfall, der knirscht, aktualisiert das Aufgabenheft eines Kritikers. Teile dieser Schleife sind heute live; Teile werden noch verdrahtet.

So heißt „menschliches Urteil wird vervielfacht, nicht ersetzt" genau das: Menschen entscheiden, wie *gut* aussieht, prüfen vor der Veröffentlichung, solange wir klein genug dafür sind, und hören — in jedem Maßstab — weiter auf die Menschen, für die die Übersetzung eigentlich gedacht ist. Die Maschine besorgt die Menge. Das Urteil bleibt menschlich.

> *Mensch in der Schleife mit einem Rückkopplungsschwungrad — echte Korrekturen, die die Maßstäbe mit der Zeit verbessern.*

## Was wir noch nicht fertig haben

Eine Seite, die nur beschriebe, was funktioniert, wäre Marketing. Ein paar Dinge sind tatsächlich noch in Arbeit:

- Mehrere Kritiker — sprachübergreifende Konsistenz, Rückübersetzung, die statistische Prüfung „liest sich wie muttersprachliche Literatur" — sind erst teilweise gebaut, noch nicht überall verlässlich.
- Die volle Abdeckung reicht ein paar Sprachen tief, nicht über die ganze Landkarte.
- Die Rückkopplungsschleife von der Markierung einer Leserin zurück in die Maßstäbe ist teils live, teils noch im Aufbau.
- Manche Veröffentlichungsschritte zwischen unserem internen Repository und dieser Seite werden noch von Hand erledigt.

Nichts davon ändert den Boden: Nichts Defektes oder Anachronistisches wird veröffentlicht. Diese Seite beschreibt ein System, das noch gebaut wird — und wir halten sie aktuell, während sich die Lücken schließen.
