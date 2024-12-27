# Generated by Django 5.0.7 on 2024-07-23 00:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Client",
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
                ("company_name", models.CharField(blank=True, max_length=255)),
                ("industry", models.CharField(blank=True, max_length=100)),
                ("notes", models.TextField(blank=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="client_profile",
                        to="accounts.user",
                    ),
                ),
            ],
        ),
    ]
