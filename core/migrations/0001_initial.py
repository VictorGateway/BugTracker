# Generated by Django 4.1.5 on 2023-02-12 02:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Developer",
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
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("email", models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name="BugTracker",
            fields=[
                (
                    "project_number",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                (
                    "priority",
                    models.CharField(
                        choices=[
                            ("low", "low"),
                            ("medium", "medium"),
                            ("high", "high"),
                        ],
                        max_length=10,
                    ),
                ),
                ("title", models.CharField(max_length=70)),
                ("summary", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Open", "Open"),
                            ("Closed", "Closed"),
                            ("In Progress", "In Progress"),
                        ],
                        default="Open",
                        max_length=20,
                    ),
                ),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "assignee",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.developer",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
