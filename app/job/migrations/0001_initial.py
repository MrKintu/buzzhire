# Generated by Django 5.0.3 on 2024-03-27 02:44

import django.db.models.deletion
import job.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("company", "0001_initial"),
        ("resume", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="JobPost",
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
                ("job_title", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "job_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Remote", "Remote"),
                            ("Onsite", "Onsite"),
                            ("Hybrid", "Hybrid"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "industry",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Transportation", "Transportation"),
                            ("Pharmaceutical", "Pharmaceutical"),
                            ("Telecommunications", "Telecommunications"),
                            ("Manufacturing", "Manufacturing"),
                            ("Mining", "Mining"),
                            ("Hospitality", "Hospitality"),
                            ("Media and News", "Media and News"),
                            ("Agriculture", "Agriculture"),
                            ("Computer and Technology", "Computer and Technology"),
                            ("Education", "Education"),
                            ("Finance and Economics", "Finance and Economics"),
                            ("Health Care", "Health Care"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                ("city", models.CharField(blank=True, max_length=100, null=True)),
                ("state", models.CharField(blank=True, max_length=100, null=True)),
                ("country", models.CharField(blank=True, max_length=100, null=True)),
                ("pay", models.PositiveIntegerField(blank=True, null=True)),
                ("describe", models.TextField()),
                ("tasks", models.TextField()),
                ("ideal_candidate", models.TextField()),
                ("available", models.BooleanField(default=True)),
                (
                    "download",
                    models.FileField(
                        blank=True, null=True, upload_to=job.models.rename_file
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "company",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="company.company",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ApplyJob",
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
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Approved", "Approved"),
                            ("Declined", "Declined"),
                            ("Pending", "Pending"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "reference",
                    models.CharField(blank=True, max_length=20, null=True, unique=True),
                ),
                (
                    "resume",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="resume.resume",
                    ),
                ),
                (
                    "user_info",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.userinfo",
                    ),
                ),
                (
                    "job",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="job.jobpost",
                    ),
                ),
            ],
        ),
    ]
