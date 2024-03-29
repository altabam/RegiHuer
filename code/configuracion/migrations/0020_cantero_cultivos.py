# Generated by Django 3.2.13 on 2023-03-28 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0019_auto_20220812_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cantero_Cultivos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaSiembra', models.DateField()),
                ('fechaCosecha', models.DateField()),
                ('cantero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.canteros')),
                ('cultivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.cultivos')),
            ],
        ),
    ]
