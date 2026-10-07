from django.urls import path
from . import views

# Create your urls here
urlpatterns = [
    path(
        "content/ajouter/",
        views.content_create,
        name="content_create",
    ),
    path(
        "content/supprimer/<int:id>/",
        views.content_delete,
        name="content_delete",
    ),
]