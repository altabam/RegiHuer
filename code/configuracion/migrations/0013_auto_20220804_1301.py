# Generated by Django 3.2.13 on 2022-08-04 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0012_cultivos_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cultivos',
            name='enfermedades',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configuracion.enfermedades'),
        ),
        migrations.AlterField(
            model_name='cultivos',
            name='plagas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configuracion.plagas'),
        ),
        migrations.AlterField(
            model_name='cultivos',
            name='tierra',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configuracion.tierras_cultivo'),
        ),
    ]
