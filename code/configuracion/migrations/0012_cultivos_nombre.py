# Generated by Django 3.2.13 on 2022-08-04 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0011_auto_20220804_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='cultivos',
            name='nombre',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
