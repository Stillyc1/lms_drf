# Generated by Django 5.1.6 on 2025-02-13 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
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
                (
                    "title",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Название"
                    ),
                ),
                (
                    "picture",
                    models.ImageField(
                        blank=True, null=True, upload_to="", verbose_name="Превью"
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Описание"),
                ),
                (
                    "amount",
                    models.PositiveIntegerField(
                        blank=True, default=0, null=True, verbose_name="сумма покупки"
                    ),
                ),
            ],
            options={
                "verbose_name": "Курс",
                "verbose_name_plural": "Курсы",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
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
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                (
                    "picture",
                    models.ImageField(
                        blank=True, null=True, upload_to="", verbose_name="Превью"
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Описание"),
                ),
                (
                    "video",
                    models.URLField(max_length=515, verbose_name="ссылка на видео"),
                ),
                (
                    "amount",
                    models.PositiveIntegerField(
                        blank=True, default=0, null=True, verbose_name="сумма покупки"
                    ),
                ),
            ],
            options={
                "verbose_name": "Урок",
                "verbose_name_plural": "Уроки",
            },
        ),
        migrations.CreateModel(
            name="SubscriptionCourse",
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
            ],
            options={
                "verbose_name": "Подписка",
                "verbose_name_plural": "Подписки",
            },
        ),
    ]
