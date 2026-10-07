from django.urls import path
from . import views

# Create your urls here
urlpatterns = [
    path('', views.home, name='home'),
    path("find/", views.recherche, name="recherche"),
    path("spip/<int:id>/", views.spip, name="spip"),
]