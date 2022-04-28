from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpers', '0002_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='description',
            field=models.CharField(max_length=512, verbose_name='Описание'),
        ),
    ]
