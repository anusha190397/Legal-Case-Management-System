# Generated by Django 5.0.7 on 2024-07-23 00:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
        ("cases", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Document",
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
                ("title", models.CharField(max_length=255)),
                (
                    "document_type",
                    models.CharField(
                        choices=[
                            ("CONTRACT", "Contract"),
                            ("PLEADING", "Pleading"),
                            ("CORRESPONDENCE", "Correspondence"),
                            ("EVIDENCE", "Evidence"),
                            ("OTHER", "Other"),
                        ],
                        max_length=20,
                    ),
                ),
                ("file", models.FileField(upload_to="case_documents/")),
                ("upload_date", models.DateTimeField(auto_now_add=True)),
                ("description", models.TextField(blank=True)),
                (
                    "case",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="documents",
                        to="cases.case",
                    ),
                ),
                (
                    "uploaded_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="accounts.user"
                    ),
                ),
            ],
        ),
    ]
