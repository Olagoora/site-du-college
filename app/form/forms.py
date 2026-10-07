from django import forms

from application.models import Content, Rubrique


class ContentForm(forms.ModelForm):

    class Meta:
        model = Content

        fields = [
            "rubrique",
            "title",
            "content",
            "img",
            "lien",
            "type",
        ]

        widgets = {
            "rubrique": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),

            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Titre de l'actualité",
                }
            ),

            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Contenu de l'actualité",
                    "rows": 10,
                }
            ),

            "img": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "URL de l'image",
                }
            ),

            "lien": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Lien",
                }
            ),

            "type": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "content",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["rubrique"].queryset = (
            Rubrique.objects
            .using("dynamic")
            .filter(actif=True)
            .order_by("nom")
        )

        self.fields["type"].initial = "content"