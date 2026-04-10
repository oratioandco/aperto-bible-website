#!/usr/bin/env python3
"""Create pericopes JSON files for all 20 new languages."""

import json
import os

content_dir = "/Users/ttreppmann/StudioProjects/aperto-website/src/content"

# Pericope structure: id, verses, color, accentColor, image
pericope_structure = [
    {"id": "prolog",             "verses": "1-4",   "color": "#E8E4DC", "accentColor": "#8B7355", "image": "luke_01_prologue.jpeg"},
    {"id": "zacharias-elisabeth","verses": "5-25",  "color": "#E4E8E4", "accentColor": "#6B8E7F", "image": "luke_01_zechariah_temple.jpeg"},
    {"id": "verkuendigung",      "verses": "26-38", "color": "#F0EAE0", "accentColor": "#8B6F5E", "image": "luke_01_annunciation.jpeg"},
    {"id": "heimsuchung",        "verses": "39-45", "color": "#E8F0E8", "accentColor": "#5A7A6A", "image": "luke_01_visitation.jpeg"},
    {"id": "magnificat",         "verses": "46-56", "color": "#EAE4F0", "accentColor": "#7A6A8B", "image": "luke_01_magnificat.jpeg"},
    {"id": "johannes-geburt",    "verses": "57-66", "color": "#E8ECF0", "accentColor": "#6A7A8B", "image": "luke_01_birth_john.jpeg"},
    {"id": "benedictus",         "verses": "67-79", "color": "#F0E8E4", "accentColor": "#8B6A5A", "image": "luke_01_benedictus.jpeg"},
    {"id": "johannes-kindheit",  "verses": "80",    "color": "#E8F0EC", "accentColor": "#5A8B7A", "image": "luke_01_wilderness.jpeg"},
]

lang_data = {
    "nl": {
        "book": "Lucas",
        "titles": [
            "Waarom ik dit schrijf",
            "De aankondiging van de geboorte van Johannes",
            "De aankondiging van de geboorte van Jezus",
            "Maria bij Elisabet",
            "Het lied van Maria",
            "Zijn naam is Johannes",
            "Het lied van Zacharias",
            "Johannes in de woestijn",
        ]
    },
    "ro": {
        "book": "Luca",
        "titles": [
            "De ce scriu",
            "Un preot b\u0103tr\u00e2n \u015fi o promisiune imposibil\u0103",
            "Maria spune da",
            "Dou\u0103 femei, dou\u0103 minuni",
            "C\u00e2ntecul Mariei",
            "Numele lui e Ioan",
            "Profe\u021bia lui Zaharia",
            "\u00cen pustie",
        ]
    },
    "cs": {
        "book": "Luk\u00e1\u0161",
        "titles": [
            "Pro\u010d to p\u00ed\u0161u",
            "Star\u00fd kn\u011bz a nemo\u017en\u00fd slib",
            "Marie \u0159\u00edk\u00e1 ano",
            "Dv\u011b \u017eeny, dva z\u00e1zraky",
            "Mariina p\u00edse\u0148",
            "Jmenuje se Jan",
            "Zachari\u00e1\u0161ovo proroctv\u00ed",
            "Na pust\u00fdch m\u00edstech",
        ]
    },
    "el": {
        "book": "\u039b\u03bf\u03c5\u03ba\u03ac\u03c2",
        "titles": [
            "\u0393\u03b9\u03b1\u03c4\u03af \u03b3\u03c1\u03ac\u03c6\u03c9 \u03b1\u03c5\u03c4\u03ac",
            "\u00c9\u03bd\u03b1\u03c2 \u0393\u03ad\u03c1\u03bf\u03c2 \u0399\u03b5\u03c1\u03ad\u03b1\u03c2 \u03ba\u03b1\u03b9 \u03bc\u03b9\u03b1 \u0391\u03b4\u03cd\u03bd\u03b1\u03c4\u03b7 \u03a5\u03c0\u03cc\u03c3\u03c7\u03b5\u03c3\u03b7",
            "\u0397 \u039c\u03b1\u03c1\u03af\u03b1 \u039b\u03ad\u03b5\u03b9 \u039d\u03b1\u03b9",
            "\u0394\u03cd\u03bf \u0393\u03c5\u03bd\u03b1\u03af\u03ba\u03b5\u03c2, \u0394\u03cd\u03bf \u0398\u03b1\u03cd\u03bc\u03b1\u03c4\u03b1",
            "\u03a4\u03bf \u03a4\u03c1\u03b1\u03b3\u03bf\u03cd\u03b4\u03b9 \u03c4\u03b7\u03c2 \u039c\u03b1\u03c1\u03af\u03b1\u03c2",
            "\u0399\u03c9\u03ac\u03bd\u03bd\u03b7\u03c2 \u0395\u03af\u03bd\u03b1\u03b9 \u03c4\u03bf \u038c\u03bd\u03bf\u03bc\u03ac \u03a4\u03bf\u03c5",
            "\u0397 \u03a0\u03c1\u03bf\u03c6\u03b7\u03c4\u03b5\u03af\u03b1 \u03c4\u03bf\u03c5 \u0396\u03b1\u03c7\u03b1\u03c1\u03af\u03b1",
            "\u03a3\u03c4\u03b1 \u0395\u03c1\u03b7\u03bc\u03b9\u03ba\u03ac \u039c\u03ad\u03c1\u03b7",
        ]
    },
    "hu": {
        "book": "Luk\u00e1cs",
        "titles": [
            "Mi\u00e9rt \u00edrom ezt",
            "Egy \u00f6reg pap \u00e9s egy lehetetlen \u00eag\u00e9ret",
            "M\u00e1ria igent mond",
            "K\u00e9t asszony, k\u00e9t csoda",
            "M\u00e1ria \u00e9neke",
            "A neve: J\u00e1nos",
            "Zak\u00e1ri\u00e1s pr\u00f3f\u00e9ci\u00e1ja",
            "A puszt\u00e1ban n\u0151 fel",
        ]
    },
    "bg": {
        "book": "\u041b\u0443\u043a\u0430",
        "titles": [
            "\u041f\u0440\u043e\u043b\u043e\u0433",
            "\u041e\u0431\u0435\u0449\u0430\u043d\u0438\u0435\u0442\u043e \u0437\u0430 \u0419\u043e\u0430\u043d",
            "\u0411\u043b\u0430\u0433\u043e\u0432\u0435\u0441\u0442\u0438\u0435\u0442\u043e \u043d\u0430 \u041c\u0430\u0440\u0438\u044f",
            "\u041c\u0430\u0440\u0438\u044f \u043f\u0440\u0438 \u0415\u043b\u0438\u0441\u0430\u0432\u0435\u0442\u0430",
            "\u041f\u0435\u0441\u0435\u043d\u0442\u0430 \u043d\u0430 \u041c\u0430\u0440\u0438\u044f \u2014 \u041c\u0430\u0433\u043d\u0438\u0444\u0438\u043a\u0430\u0442",
            "\u0420\u0430\u0436\u0434\u0430\u043d\u0435\u0442\u043e \u043d\u0430 \u0419\u043e\u0430\u043d",
            "\u041f\u0440\u043e\u0440\u043e\u0447\u0435\u0441\u0442\u0432\u043e\u0442\u043e \u043d\u0430 \u0417\u0430\u0445\u0430\u0440\u0438\u044f \u2014 \u0411\u0435\u043d\u0435\u0434\u0438\u043a\u0442\u0443\u0441",
            "\u0414\u0435\u0442\u0441\u0442\u0432\u043e\u0442\u043e \u043d\u0430 \u0419\u043e\u0430\u043d",
        ]
    },
    "hr": {
        "book": "Luka",
        "titles": [
            "Za\u0161to ovo pi\u0161em",
            "Najava Ivanova ro\u0111enja",
            "Najava Isusova ro\u0111enja",
            "Marijin posjet Elizabeti",
            "Marijina pjesma",
            "Ro\u0111enje Ivana Krstitelja",
            "Zaharijino proro\u010danstvo",
            "Odrastanje u pustinji",
        ]
    },
    "fi": {
        "book": "Luukas",
        "titles": [
            "Miksi kirjoitan t\u00e4m\u00e4n",
            "Vanha pappi ja mahdoton lupaus",
            "Maria sanoo kyll\u00e4",
            "Kaksi naista, kaksi ihmett\u00e4",
            "Marian laulu",
            "H\u00e4nen nimens\u00e4 on Johannes",
            "Sakariaan profetia",
            "Er\u00e4maa",
        ]
    },
    "sk": {
        "book": "Luk\u00e1\u0161",
        "titles": [
            "Pre\u010do to p\u00ed\u0161em",
            "Star\u00fd kn\u011bz a nemo\u017en\u00fd pr\u00eds\u013eub",
            "M\u00e1ria hovor\u00ed \u00e1no",
            "Dve \u017eeny, dva z\u00e1zraky",
            "M\u00e1riina pies\u0148",
            "Vol\u00e1 sa J\u00e1n",
            "Zachari\u00e1\u0161ovo proroctvo",
            "Rastie na p\u00fa\u0161ti",
        ]
    },
    "lt": {
        "book": "Luko",
        "titles": [
            "Kod\u0117l ra\u0161au",
            "Senas kunigas ir ne\u012fmanomas pa\u017eadas",
            "Marija sako \u201etaip\u201c",
            "Dvi moterys, du stebuklai",
            "Marijos giesm\u0117",
            "Jo vardas \u2014 Jonas",
            "Zacharijo prana\u0161yst\u0117",
            "Augimas dykumoje",
        ]
    },
    "sl": {
        "book": "Luka",
        "titles": [
            "Zakaj pi\u0161em",
            "Napoved Janezovega rojstva",
            "Napoved Jezusovega rojstva",
            "Marijin obisk pri Elizabeti",
            "Magnifikat",
            "Janezov rojstni dan",
            "Zaharijeva prero\u0161ka pesem",
            "Otrok odra\u0161\u010da",
        ]
    },
    "lv": {
        "book": "L\u016bka",
        "titles": [
            "K\u0101p\u0113c es to rakstu",
            "Vecs priesteris un neiespējams sol\u012bjums",
            "Marija saka j\u0101",
            "Divas sievietes, divi br\u012bn\u016bmi",
            "Marijas dziesma",
            "Vi\u0146a v\u0101rds ir J\u0101nis",
            "Zaharijas pravietojums",
            "Aug\u0161ana tuksnes\u012b",
        ]
    },
    "et": {
        "book": "Luuka",
        "titles": [
            "Miks ma seda kirjutan",
            "Vana preester ja v\u00f5imatu lubadus",
            "Maarja \u00fctleb jah",
            "Kaks naist, kaks imet",
            "Maarja laul",
            "Tema nimi on Johannes",
            "Sakariase laul",
            "Kasvamine k\u00f5rbes",
        ]
    },
    "ga": {
        "book": "L\u00fac\u00e1s",
        "titles": [
            "C\u00e9n f\u00e1th a scr\u00edobhaim \u00e9 seo",
            "F\u00f3gairt Bhreith Eoin",
            "F\u00f3gairt Bhreith \u00cdosa",
            "Muire ag Tabhairt Cuairte ar Eil\u00eds",
            "Amhr\u00e1n Mhuire",
            "Breith agus Ainmi\u00fa Eoin",
            "F\u00e1idhe\u00f3ireacht Zacharias",
            "\u00d3ige Eoin",
        ]
    },
    "mt": {
        "book": "Luqa",
        "titles": [
            "G\u0127aliex Qed Nikteb Dan",
            "Qassis Xi\u0127 u We\u0121\u0127da Impossibbli",
            "Marija Tg\u0127id Iva",
            "\u017bew\u0121 Nisa, \u017bew\u0121 Mirakli",
            "L-G\u0127anja ta\u2019 Marija",
            "Ismu \u0120wanni",
            "Il-Profezija ta\u2019 \u017bakkarija",
            "Jikber fid-De\u017cert",
        ]
    },
    "nb": {
        "book": "Lukas",
        "titles": [
            "Hvorfor jeg skriver dette",
            "En gammel prest og et umulig l\u00f8fte",
            "Maria sier ja",
            "To kvinner m\u00f8tes",
            "Marias sang",
            "Johannes blir f\u00f8dt",
            "Sakarjas sang",
            "Oppvekst i \u00f8demarken",
        ]
    },
    "ru": {
        "book": "\u041b\u0443\u043a\u0438",
        "titles": [
            "\u0417\u0430\u0447\u0435\u043c \u044f \u044d\u0442\u043e \u043f\u0438\u0448\u0443",
            "\u0421\u0442\u0430\u0440\u044b\u0439 \u0441\u0432\u044f\u0449\u0435\u043d\u043d\u0438\u043a \u0438 \u043d\u0435\u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0435 \u043e\u0431\u0435\u0449\u0430\u043d\u0438\u0435",
            "\u041c\u0430\u0440\u0438\u044f \u0433\u043e\u0432\u043e\u0440\u0438\u0442 \u00ab\u0434\u0430\u00bb",
            "\u0414\u0432\u0435 \u0436\u0435\u043d\u0449\u0438\u043d\u044b, \u0434\u0432\u0430 \u0447\u0443\u0434\u0430",
            "\u041f\u0435\u0441\u043d\u044c \u041c\u0430\u0440\u0438\u0438",
            "\u0415\u0433\u043e \u0437\u043e\u0432\u0443\u0442 \u0418\u043e\u0430\u043d\u043d",
            "\u041f\u0440\u043e\u0440\u043e\u0447\u0435\u0441\u0442\u0432\u043e \u0417\u0430\u0445\u0430\u0440\u0438\u0438",
            "\u0414\u0435\u0442\u0441\u0442\u0432\u043e \u0432 \u043f\u0443\u0441\u0442\u044b\u043d\u0435",
        ]
    },
    "ar": {
        "book": "\u0644\u0648\u0642\u0627",
        "titles": [
            "\u0644\u0645\u0627\u0630\u0627 \u0623\u0643\u062a\u0628 \u0647\u0630\u0627",
            "\u0643\u0627\u0647\u0646 \u0639\u062c\u0648\u0632 \u0648\u0648\u0639\u062f \u0645\u0633\u062a\u062d\u064a\u0644",
            "\u0645\u0631\u064a\u0645 \u062a\u0642\u0648\u0644 \u0646\u0639\u0645",
            "\u0627\u0645\u0631\u0623\u062a\u0627\u0646\u060c \u0645\u0639\u062c\u0632\u062a\u0627\u0646",
            "\u0646\u0634\u064a\u062f \u0645\u0631\u064a\u0645",
            "\u0627\u0633\u0645\u0647 \u064a\u0648\u062d\u0646\u0651\u0627",
            "\u0646\u0634\u064a\u062f \u0632\u0643\u0631\u064a\u0651\u0627",
            "\u0627\u0644\u0637\u0641\u0644 \u064a\u0643\u0628\u0631",
        ]
    },
    "ca": {
        "book": "Lluc",
        "titles": [
            "Per qu\u00e8 escric aix\u00f2",
            "Un sacerdot vell i una promesa impossible",
            "Maria diu s\u00ed",
            "Dues dones, dos miracles",
            "El cant de Maria",
            "El seu nom \u00e9s Joan",
            "La profecia de Zacaries",
            "Creixent al desert",
        ]
    },
}

for lang, data in lang_data.items():
    pericopes = []
    titles = data["titles"]

    for i, p in enumerate(pericope_structure):
        title = titles[i] if i < len(titles) else ""
        pericope = {
            "id": p["id"],
            "title": title,
            "subtitle": "",
            "verses": p["verses"],
            "color": p["color"],
            "accentColor": p["accentColor"],
            "image": p["image"],
            "exegesis": None,
            "media": {}
        }
        pericopes.append(pericope)

    output = {
        "book": data["book"],
        "chapter": 1,
        "pericopes": pericopes
    }

    output_path = os.path.join(content_dir, f"luke-1-pericopes-{lang}.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"Created luke-1-pericopes-{lang}.json")

print("All pericopes JSON files created!")
