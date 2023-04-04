# Generated by Django 3.2.13 on 2022-08-12 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0016_cultivos_luz'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ph_Suelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valores', models.CharField(blank=True, max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Temperaturas_Cultivos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50)),
                ('valores', models.CharField(blank=True, max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='cultivos',
            name='dias_germinacion',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='cultivos',
            name='ph',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configuracion.ph_suelo'),
        ),
        migrations.AddField(
            model_name='cultivos',
            name='temperaturas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configuracion.temperaturas_cultivos'),
        ),
    ]