# Generated by Django 3.2.13 on 2022-06-14 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='huerta',
            old_name='hotelano',
            new_name='hortelano',
        ),
    ]
