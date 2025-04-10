# Generated by Django 3.2.13 on 2023-04-13 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0033_auto_20230411_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cultivos',
            name='familia',
            field=models.CharField(choices=[('COM', 'Compuestas'), ('CRU', 'Cruciferas (Brásicas)'), ('UMB', 'Cruciferas'), ('SOL', 'Solanaceas'), ('GRA', 'Gramineas'), ('LEG', 'Leguminosas'), ('QUE', 'Quenopoidaceas'), ('ALL', 'Alliaceas'), ('CUC', 'Cucurbitaceas'), ('CON', 'Convolvulaceas'), ('ASP', 'Asparagaceae')], max_length=3),
        ),
        migrations.AlterField(
            model_name='cultivos',
            name='imagen',
            field=models.ImageField(default='cultivo/', upload_to='cultivos'),
            preserve_default=False,
        ),
    ]
