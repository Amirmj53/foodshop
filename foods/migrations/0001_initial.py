# Generated by Django 4.1.1 on 2022-09-08 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Food",
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
                ("name", models.CharField(max_length=128)),
                (
                    "description",
                    models.CharField(max_length=128, verbose_name="توضیحات"),
                ),
                ("rate", models.IntegerField(verbose_name="امتیاز")),
                ("price", models.IntegerField()),
                ("time", models.IntegerField(verbose_name="زمان لازم")),
                (
                    "pub_date",
                    models.DateTimeField(auto_now_add=True, verbose_name="زمان انتشار"),
                ),
                ("photo", models.ImageField(upload_to="foods/")),
            ],
        ),
    ]
