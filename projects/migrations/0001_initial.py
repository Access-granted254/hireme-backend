# Generated by Django 5.0.2 on 2024-02-15 11:49

import cloudinary.models
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=1000)),
                (
                    "project_timeline",
                    models.CharField(
                        choices=[
                            ("FT", "Full Time"),
                            ("PT", "Part Time"),
                            ("CT", "Contract"),
                        ],
                        default="FT",
                        max_length=2,
                    ),
                ),
                (
                    "project_category",
                    models.CharField(
                        choices=[
                            ("WB", "Web Development"),
                            ("DB", "Database"),
                            ("ML", "Machine Learning"),
                            ("AI", "Artificial Intelligence"),
                            ("DS", "Data Science"),
                        ],
                        default="WB",
                        max_length=2,
                    ),
                ),
                ("description", models.TextField()),
                (
                    "project_duration",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "file",
                    cloudinary.models.CloudinaryField(
                        blank=True, max_length=255, null=True, verbose_name="file"
                    ),
                ),
                (
                    "min_price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "max_price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="projects",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Bid",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("proposal", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("P", "Pending"),
                            ("A", "Accepted"),
                            ("R", "Rejected"),
                        ],
                        default="P",
                        max_length=1,
                    ),
                ),
                (
                    "developer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bids",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bids",
                        to="projects.project",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
