# Generated by Django 4.2.11 on 2025-04-14 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0042_remove_cultivos_asociacion_beneficiosa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asociacion_cultivo',
            name='asociacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_asociacion', to='configuracion.cultivos'),
        ),
    ]
