# Generated by Django 4.0.4 on 2022-04-28 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpers', '0003_alter_form_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faqs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('description', models.CharField(max_length=256, verbose_name='FAQS')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]