from django.shortcuts import render

# Create your views here.

def menu(request):
    menu_items = [
        {
            "id": 122,
            "title": "ACCES & CONTACT",
            "children": [
                {"id": 69, "title": "CONTACTS - ACCES"},
            ],
        },
        {
            "id": 1,
            "title": "L’ÉTABLISSEMENT",
            "children": [
                {
                    "id": 2,
                    "title": "FONCTIONNEMENT",
                    "children": [
                        {"id": 77, "title": "Conseil d’administration"},
                        {"id": 124, "title": "Règlement intérieur"},
                        {"id": 78, "title": "Sécurité"},
                    ],
                },
                {"id": 70, "title": "PERSONNELS"},
                {"id": 103, "title": "PROJET D’ETABLISSEMENT"},
                {"id": 118, "title": "SECTORISATION"},
                {"id": 140, "title": "VISITE VIRTUELLE"},
            ],
        },
        {
            "id": 3,
            "title": "PÉDAGOGIE",
            "children": [
                {
                    "id": 12,
                    "title": "CDI",
                    "children": [
                        {"id": 56, "title": "Informations pratiques"},
                    ],
                },
                {
                    "id": 32,
                    "title": "EXAMENS ET CERTIFICATIONS",
                    "children": [
                        {"id": 33, "title": "D.N.B."},
                    ],
                },
                {
                    "id": 128,
                    "title": "MATIÈRES DISCIPLINAIRES",
                    "children": [
                        {"id": 67, "title": "Allemand"},
                        {"id": 91, "title": "Arts plastiques"},
                        {"id": 58, "title": "EPS"},
                        {"id": 4, "title": "Français"},
                        {"id": 5, "title": "Histoire-Géo"},
                        {"id": 121, "title": "Italien"},
                        {"id": 7, "title": "Langues vivantes"},
                        {"id": 9, "title": "Physique Chimie"},
                        {"id": 8, "title": "SVT"},
                    ],
                },
                {
                    "id": 129,
                    "title": "OPTIONS ET CLASSES À PROJET",
                    "children": [
                        {"id": 154, "title": "Classe astronomie"},
                        {"id": 133, "title": "Classe bilangue anglais-allemand"},
                        {"id": 130, "title": "Classe Danse"},
                        {"id": 132, "title": "Classe Défense et Sécurité Globale"},
                        {"id": 141, "title": "Classe vélo"},
                        {"id": 36, "title": "LCA - Latin"},
                        {"id": 126, "title": "Sciences expertes"},
                        {"id": 123, "title": "Section Sportive"},
                        {"id": 125, "title": "Théâtre"},
                    ],
                },
                {"id": 156, "title": "PAS"},
                {"id": 117, "title": "ULIS"},
                {
                    "id": 14,
                    "title": "VOYAGES ET SORTIES",
                    "children": [
                        {"id": 101, "title": "Sorties"},
                        {"id": 109, "title": "Voyages scolaires"},
                    ],
                },
            ],
        },
        {
            "id": 84,
            "title": "VIE AU COLLÈGE",
            "children": [
                {
                    "id": 116,
                    "title": "CLUBS & ATELIERS",
                    "children": [
                        {"id": 143, "title": "Club arts"},
                        {"id": 145, "title": "Club échecs"},
                        {"id": 152, "title": "Club jardin"},
                        {"id": 142, "title": "Club journal"},
                        {"id": 144, "title": "Club sciences"},
                    ],
                },
                {
                    "id": 115,
                    "title": "ENGAGEMENT DES ÉLÈVES ET VIE CITOYENNE",
                    "children": [
                        {"id": 135, "title": "Ambassadeurs culture"},
                        {"id": 137, "title": "Cellule bien-être et santé mentale"},
                        {"id": 134, "title": "Cellule pHARe"},
                        {"id": 138, "title": "Conseil de la Vie Collégienne"},
                        {"id": 136, "title": "Eco-délégués"},
                        {"id": 147, "title": "Egalité Filles-Garçons"},
                        {"id": 146, "title": "Radio Camus - les podcasts"},
                    ],
                },
                {
                    "id": 71,
                    "title": "FÉDÈRATIONS DES PARENTS D’ÉLÈVES",
                    "children": [
                        {"id": 86, "title": "INFORMATIONS"},
                        {"id": 74, "title": "REUNIONS"},
                    ],
                },
                {"id": 59, "title": "L’ASSOCIATION SPORTIVE"},
                {"id": 15, "title": "LA DEMI-PENSION"},
                {"id": 139, "title": "PARCOURS AVENIR"},
                {"id": 90, "title": "RENTRÉE SCOLAIRE"},
            ],
        },
    ]

    return render(request, "application/menu.html", {
        "menu_items": menu_items
    })

def home(request):
    return render(request, "application/home.html")