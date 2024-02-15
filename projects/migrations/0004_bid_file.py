# Generated by Django 5.0.2 on 2024-02-15 12:22

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0003_bid_slug_project_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="bid",
            name="file",
            field=cloudinary.models.CloudinaryField(
                blank=True, max_length=255, null=True, verbose_name="proposal"
            ),
        ),
    ]