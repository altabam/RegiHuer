# Generated by Django 3.2.13 on 2023-03-31 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0024_auto_20230330_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='cultivos',
            name='imagen',
            field=models.ImageField(default=' ', upload_to='archivos/cultivos'),
            preserve_default=False,
        ),
    ]
