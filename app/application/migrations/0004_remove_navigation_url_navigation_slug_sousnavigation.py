import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("application", "0003_navigation"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.RemoveField(
                    model_name="navigation",
                    name="url",
                ),
                migrations.AddField(
                    model_name="navigation",
                    name="slug",
                    field=models.SlugField(
                        max_length=100,
                        blank=True,
                        null=True,
                    ),
                ),
                migrations.CreateModel(
                    name="SousNavigation",
                    fields=[
                        (
                            "id",
                            models.BigAutoField(
                                auto_created=True,
                                primary_key=True,
                                serialize=False,
                                verbose_name="ID",
                            ),
                        ),
                        (
                            "nom",
                            models.CharField(max_length=100),
                        ),
                        (
                            "slug",
                            models.SlugField(max_length=100),
                        ),
                        (
                            "ordre",
                            models.PositiveIntegerField(default=0),
                        ),
                        (
                            "actif",
                            models.BooleanField(default=True),
                        ),
                        (
                            "navigation",
                            models.ForeignKey(
                                on_delete=django.db.models.deletion.CASCADE,
                                related_name="sous_navigations",
                                to="application.navigation",
                            ),
                        ),
                    ],
                    options={
                        "ordering": ["ordre", "id"],
                    },
                ),
            ],
        ),
    ]