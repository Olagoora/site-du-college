from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import (
    Menu,
    Rubrique,
    Navigation,
    SousNavigation,
    Content,
)

# Create your views here.
# menu_items = [
#     {
#         "id": 122,
#         "title": "ACCES & CONTACT",
#         "children": [
#             {"id": 69, "title": "CONTACTS - ACCES"},
#         ],
#     },
#     {
#         "id": 1,
#         "title": "L’ÉTABLISSEMENT",
#         "children": [
#             {
#                 "id": 2,
#                 "title": "FONCTIONNEMENT",
#                 "children": [
#                     {"id": 77, "title": "Conseil d’administration"},
#                     {"id": 124, "title": "Règlement intérieur"},
#                     {"id": 78, "title": "Sécurité"},
#                 ],
#             },
#             {"id": 70, "title": "PERSONNELS"},
#             {"id": 103, "title": "PROJET D’ETABLISSEMENT"},
#             {"id": 118, "title": "SECTORISATION"},
#             {"id": 140, "title": "VISITE VIRTUELLE"},
#         ],
#     },
#     {
#         "id": 3,
#         "title": "PÉDAGOGIE",
#         "children": [
#             {
#                 "id": 12,
#                 "title": "CDI",
#                 "children": [
#                     {"id": 56, "title": "Informations pratiques"},
#                 ],
#             },
#             {
#                 "id": 32,
#                 "title": "EXAMENS ET CERTIFICATIONS",
#                 "children": [
#                     {"id": 33, "title": "D.N.B."},
#                 ],
#             },
#             {
#                 "id": 128,
#                 "title": "MATIÈRES DISCIPLINAIRES",
#                 "children": [
#                     {"id": 67, "title": "Allemand"},
#                     {"id": 91, "title": "Arts plastiques"},
#                     {"id": 58, "title": "EPS"},
#                     {"id": 4, "title": "Français"},
#                     {"id": 5, "title": "Histoire-Géo"},
#                     {"id": 121, "title": "Italien"},
#                     {"id": 7, "title": "Langues vivantes"},
#                     {"id": 9, "title": "Physique Chimie"},
#                     {"id": 8, "title": "SVT"},
#                 ],
#             },
#             {
#                 "id": 129,
#                 "title": "OPTIONS ET CLASSES À PROJET",
#                 "children": [
#                     {"id": 154, "title": "Classe astronomie"},
#                     {"id": 133, "title": "Classe bilangue anglais-allemand"},
#                     {"id": 130, "title": "Classe Danse"},
#                     {"id": 132, "title": "Classe Défense et Sécurité Globale"},
#                     {"id": 141, "title": "Classe vélo"},
#                     {"id": 36, "title": "LCA - Latin"},
#                     {"id": 126, "title": "Sciences expertes"},
#                     {"id": 123, "title": "Section Sportive"},
#                     {"id": 125, "title": "Théâtre"},
#                 ],
#             },
#             {"id": 156, "title": "PAS"},
#             {"id": 117, "title": "ULIS"},
#             {
#                 "id": 14,
#                 "title": "VOYAGES ET SORTIES",
#                 "children": [
#                     {"id": 101, "title": "Sorties"},
#                     {"id": 109, "title": "Voyages scolaires"},
#                 ],
#             },
#         ],
#     },
#     {
#         "id": 84,
#         "title": "VIE AU COLLÈGE",
#         "children": [
#             {
#                 "id": 116,
#                 "title": "CLUBS & ATELIERS",
#                 "children": [
#                     {"id": 143, "title": "Club arts"},
#                     {"id": 145, "title": "Club échecs"},
#                     {"id": 152, "title": "Club jardin"},
#                     {"id": 142, "title": "Club journal"},
#                     {"id": 144, "title": "Club sciences"},
#                 ],
#             },
#             {
#                 "id": 115,
#                 "title": "ENGAGEMENT DES ÉLÈVES ET VIE CITOYENNE",
#                 "children": [
#                     {"id": 135, "title": "Ambassadeurs culture"},
#                     {"id": 137, "title": "Cellule bien-être et santé mentale"},
#                     {"id": 134, "title": "Cellule pHARe"},
#                     {"id": 138, "title": "Conseil de la Vie Collégienne"},
#                     {"id": 136, "title": "Eco-délégués"},
#                     {"id": 147, "title": "Egalité Filles-Garçons"},
#                     {"id": 146, "title": "Radio Camus - les podcasts"},
#                 ],
#             },
#             {
#                 "id": 71,
#                 "title": "FÉDÈRATIONS DES PARENTS D’ÉLÈVES",
#                 "children": [
#                     {"id": 86, "title": "INFORMATIONS"},
#                     {"id": 74, "title": "REUNIONS"},
#                 ],
#             },
#             {"id": 59, "title": "L’ASSOCIATION SPORTIVE"},
#             {"id": 15, "title": "LA DEMI-PENSION"},
#             {"id": 139, "title": "PARCOURS AVENIR"},
#             {"id": 90, "title": "RENTRÉE SCOLAIRE"},
#         ],
#     },
# ]

def recherche(request):
    recherche = request.GET.get("recherche", "")

    return render(
        request,
        "application/find/find.html",
        {
            "recherche": recherche,
        }
    )

def get_menu_items():
    menus = (
        Menu.objects.using("dynamic")
        .filter(actif=True)
        .prefetch_related(
            "rubriques__navigations__sous_navigations"
        )
        .order_by("ordre", "id")
    )

    menu_items = []

    for menu in menus:

        menu_item = {
            "id": menu.id,
            "key": f"menu-{menu.id}",
            "title": menu.nom,
            "children": [],
        }

        for rubrique in menu.rubriques.filter(actif=True):

            rubrique_item = {
                "id": rubrique.id,
                "key": f"rubrique-{rubrique.id}",
                "title": rubrique.nom,
                "children": [],
            }

            for navigation in rubrique.navigations.filter(actif=True):

                navigation_item = {
                    "id": navigation.id,
                    "key": f"navigation-{navigation.id}",
                    "title": navigation.nom,
                    "children": [],
                }

                for sous_navigation in navigation.sous_navigations.filter(
                    actif=True
                ):

                    navigation_item["children"].append({
                        "id": sous_navigation.id,
                        "key": f"sousnavigation-{sous_navigation.id}",
                        "title": sous_navigation.nom,
                    })

                rubrique_item["children"].append(navigation_item)

            menu_item["children"].append(rubrique_item)

        menu_items.append(menu_item)

    return menu_items

def menu(request):
    menu_items = get_menu_items()

    return render(
        request,
        "application/menu.html",
        {
            "menu_items": menu_items,
        },
    )

def home(request):
    menu_items = get_menu_items()

    return render(
        request,
        "application/home.html",
        {
            "menu_items": menu_items,
        },
    )

def rubrique(request, id):
    rubrique = get_object_or_404(
        Rubrique.objects.using("dynamic"),
        id=id,
        actif=True,
    )

    return render(
        request,
        "application/rubrique.html",
        {"rubrique": rubrique}
    )

def build_content_data(rubrique):
    contents = (
        Content.objects
        .using("dynamic")
        .filter(rubrique=rubrique)
        .order_by("id")
    )

    return [
        {
            "id": item.id,
            "title": item.title,
            "content": item.content,
            "img": item.img,
            "lien": item.lien,
            "type": item.type,
        }
        for item in contents
    ]


def build_navigation_data(navigation):
    """
    Transforme une Navigation SQL en élément envoyé au template.
    """

    sous_navigations = (
        SousNavigation.objects
        .using("dynamic")
        .filter(
            navigation=navigation,
            actif=True,
        )
        .order_by("ordre", "id")
    )

    return {
        "id": navigation.id,
        "nom": navigation.nom,
        "slug": navigation.slug,
        "type": "élément",
        "children": [
            {
                "id": item.id,
                "nom": item.nom,
                "slug": item.slug,
                "type": "sous-élément",
                "children": [],
            }
            for item in sous_navigations
        ],
    }


def build_rubrique_data(rubrique):
    navigations = (
        Navigation.objects
        .using("dynamic")
        .filter(rubrique=rubrique, actif=True)
        .order_by("ordre", "id")
    )

    return {
        "id": rubrique.id,
        "nom": rubrique.nom,
        "slug": rubrique.slug,
        "type": "sous-rubrique",

        "children": [
            build_navigation_data(navigation)
            for navigation in navigations
        ],

        "content": build_content_data(rubrique),
    }


def build_menu_data(menu):
    """
    Transforme un Menu SQL en rubrique pour rubrique.html.

    Menu SQL
        ↓
    rubrique HTML
    """

    rubriques = (
        Rubrique.objects
        .using("dynamic")
        .filter(
            menu=menu,
            actif=True,
        )
        .order_by("ordre", "id")
    )

    return {
        "id": menu.id,
        "nom": menu.nom,
        "slug": menu.slug,
        "type": "rubrique",

        "children": [
            build_rubrique_data(rubrique)
            for rubrique in rubriques
        ],
    }

def spip(request, id):
    """
    Construit la structure complète à partir d'un élément SQL.

    Correspondance :

        Menu            → rubrique
        Rubrique        → sous-rubrique
        Navigation      → élément
        SousNavigation  → sous-élément

    Le contenu est toujours séparé de children.
    """

    element = None
    structure = None
    type_element = None

    # ---------------------------------------------------------
    # 1. MENU
    # ---------------------------------------------------------

    try:
        menu = (
            Menu.objects
            .using("dynamic")
            .get(
                id=id,
                actif=True,
            )
        )

        element = menu
        type_element = "rubrique"
        structure = build_menu_data(menu)

    except Menu.DoesNotExist:

        # -----------------------------------------------------
        # 2. RUBRIQUE
        # -----------------------------------------------------

        try:
            rubrique = (
                Rubrique.objects
                .using("dynamic")
                .select_related("menu")
                .get(
                    id=id,
                    actif=True,
                )
            )

            element = rubrique
            type_element = "sous-rubrique"
            structure = build_rubrique_data(rubrique)

        except Rubrique.DoesNotExist:

            # -------------------------------------------------
            # 3. NAVIGATION
            # -------------------------------------------------

            try:
                navigation = (
                    Navigation.objects
                    .using("dynamic")
                    .select_related("rubrique")
                    .get(
                        id=id,
                        actif=True,
                    )
                )

                element = navigation
                type_element = "élément"
                structure = build_navigation_data(navigation)

            except Navigation.DoesNotExist:

                # ---------------------------------------------
                # 4. SOUS-NAVIGATION
                # ---------------------------------------------

                try:
                    sous_navigation = (
                        SousNavigation.objects
                        .using("dynamic")
                        .select_related("navigation")
                        .get(
                            id=id,
                            actif=True,
                        )
                    )

                    element = sous_navigation
                    type_element = "sous-élément"

                    structure = {
                        "id": sous_navigation.id,
                        "nom": sous_navigation.nom,
                        "slug": sous_navigation.slug,
                        "type": "sous-élément",
                        "children": [],
                    }

                except SousNavigation.DoesNotExist:
                    raise Http404("Élément introuvable.")

    # ---------------------------------------------------------
    # ENFANTS DIRECTS
    # ---------------------------------------------------------

    enfants = structure.get("children", [])

    # ---------------------------------------------------------
    # CONTENU
    # ---------------------------------------------------------

    content = structure.get("content", [])

    # ---------------------------------------------------------
    # CONTEXTE POUR rubrique.html
    # ---------------------------------------------------------

    context = {
        "element": element,
        "type_element": type_element,

        "structure": structure,

        "enfants": enfants,
        "content": content,
    }

    return render(
        request,
        "application/rubrique.html",
        context,
    )

def base(request):
    return render(request, "application/base.html")