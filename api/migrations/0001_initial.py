# Generated by Django 5.0.6 on 2024-05-14 11:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Publication",
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
                ("title", models.CharField(max_length=100)),
                ("publisher", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "publication_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="api.publication",
                    ),
                ),
                ("author", models.CharField(max_length=50)),
                ("price", models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            bases=("api.publication",),
        ),
        migrations.CreateModel(
            name="Magazine",
            fields=[
                (
                    "publication_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="api.publication",
                    ),
                ),
                ("issue_number", models.IntegerField()),
            ],
            bases=("api.publication",),
        ),
    ]