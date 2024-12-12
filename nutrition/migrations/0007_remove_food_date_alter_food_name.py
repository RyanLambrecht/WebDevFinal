# Generated by Django 5.1.3 on 2024-12-12 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nutrition", "0006_food_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="food",
            name="date",
        ),
        migrations.AlterField(
            model_name="food",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]