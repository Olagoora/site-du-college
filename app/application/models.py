from django.db import models

# Create your models here.
slug = models.SlugField(
    max_length=100,
    blank=True,
    null=True,
)

class Menu(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    ordre = models.PositiveIntegerField(default=0)
    actif = models.BooleanField(default=True)

    class Meta:
        ordering = ["ordre", "id"]

    def __str__(self):
        return self.nom


class Rubrique(models.Model):
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name="rubriques"
    )
    nom = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    ordre = models.PositiveIntegerField(default=0)
    actif = models.BooleanField(default=True)

    class Meta:
        ordering = ["ordre", "id"]
        unique_together = ["menu", "slug"]

    def __str__(self):
        return self.nom


class Navigation(models.Model):
    rubrique = models.ForeignKey(
        Rubrique,
        on_delete=models.CASCADE,
        related_name="navigations"
    )
    nom = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    ordre = models.PositiveIntegerField(default=0)
    actif = models.BooleanField(default=True)

    class Meta:
        ordering = ["ordre", "id"]

    def __str__(self):
        return self.nom


class SousNavigation(models.Model):
    navigation = models.ForeignKey(
        Navigation,
        on_delete=models.CASCADE,
        related_name="sous_navigations"
    )
    nom = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    ordre = models.PositiveIntegerField(default=0)
    actif = models.BooleanField(default=True)

    class Meta:
        ordering = ["ordre", "id"]

    def __str__(self):
        return self.nom