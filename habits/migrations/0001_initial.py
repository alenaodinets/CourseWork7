# Generated by Django 5.0.7 on 2024-07-21 14:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Habit",
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
                ("place", models.CharField(max_length=100, verbose_name="Место")),
                (
                    "time",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2024,
                            7,
                            21,
                            10,
                            40,
                            41,
                            424018,
                            tzinfo=datetime.timezone.utc,
                        ),
                        verbose_name="Время (YYYY-MM-DD hh-mm)",
                    ),
                ),
                ("action", models.CharField(max_length=100, verbose_name="Действие")),
                (
                    "is_pleasant",
                    models.BooleanField(
                        default=False, verbose_name="Признак приятной привычки"
                    ),
                ),
                (
                    "period",
                    models.PositiveIntegerField(
                        default=1, verbose_name="Периодичность (дней)"
                    ),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Вознаграждение",
                    ),
                ),
                (
                    "duration",
                    models.DurationField(
                        default=datetime.timedelta(seconds=120),
                        verbose_name="Время на выполение (секунд)",
                    ),
                ),
                (
                    "is_public",
                    models.BooleanField(
                        default=True, verbose_name="Признак публичности"
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
                "ordering": ("action",),
            },
        ),
    ]
