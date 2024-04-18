# Generated by Django 5.0.3 on 2024-04-04 18:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resume", "0002_resume_skills_education_pastroles"),
    ]

    operations = [
        migrations.AlterField(
            model_name="education",
            name="end_year",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="education",
            name="start_year",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="pastroles",
            name="end_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="pastroles",
            name="start_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
