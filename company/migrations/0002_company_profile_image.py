# Generated by Django 5.0.4 on 2024-04-21 01:57

import company.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("company", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="profile_image",
            field=models.ImageField(
                blank=True, null=True, upload_to=company.models.rename_image
            ),
        ),
    ]
