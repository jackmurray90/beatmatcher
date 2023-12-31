# Generated by Django 4.2.5 on 2023-09-29 07:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("beatmatcher", "0002_alter_interest_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="SignUp",
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
                ("email", models.EmailField(max_length=254)),
                ("code", models.CharField(max_length=23)),
                ("expiry", models.DateTimeField()),
            ],
        ),
    ]
