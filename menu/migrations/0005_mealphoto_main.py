# Generated by Django 4.0.4 on 2022-04-18 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_remove_meal_photos_mealphoto_photos'),
    ]

    operations = [
        migrations.AddField(
            model_name='mealphoto',
            name='main',
            field=models.BooleanField(default=False, verbose_name='Главное фото'),
        ),
    ]