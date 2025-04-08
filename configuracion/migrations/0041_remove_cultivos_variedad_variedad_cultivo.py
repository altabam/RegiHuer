# Generated by Django 4.2.11 on 2025-04-08 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0040_remove_canteros_huerta_remove_huerta_hortelano_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cultivos',
            name='variedad',
        ),
        migrations.CreateModel(
            name='Variedad_Cultivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=255)),
                ('cultivo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configuracion.temperaturas_cultivos')),
            ],
        ),
    ]
