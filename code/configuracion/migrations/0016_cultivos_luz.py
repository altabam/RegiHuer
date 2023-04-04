# Generated by Django 3.2.13 on 2022-08-04 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0015_remove_cultivos_luz'),
    ]

    operations = [
        migrations.AddField(
            model_name='cultivos',
            name='luz',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configuracion.luz_necesaria_cultivo'),
        ),
    ]
