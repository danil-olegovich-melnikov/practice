# Generated by Django 4.0.4 on 2022-04-12 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='categories',
            field=models.ManyToManyField(blank=True, to='menu.category', verbose_name='Категории'),
        ),
    ]
