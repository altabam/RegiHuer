# Generated by Django 3.2.13 on 2023-04-10 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0030_alter_cultivos_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cantero_cultivos',
            name='fechaCosecha',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cantero_cultivos',
            name='fechaSiembra',
            field=models.DateField(blank=True, null=True),
        ),
    ]
