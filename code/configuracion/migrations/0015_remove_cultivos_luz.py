# Generated by Django 3.2.13 on 2022-08-04 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0014_auto_20220804_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cultivos',
            name='luz',
        ),
    ]
