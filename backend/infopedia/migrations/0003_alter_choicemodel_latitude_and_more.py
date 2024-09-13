# Generated by Django 5.0.7 on 2024-09-13 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infopedia', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choicemodel',
            name='latitude',
            field=models.FloatField(blank=True, help_text='Latitude of the location.', null=True, verbose_name='Latitude'),
        ),
        migrations.AlterField(
            model_name='choicemodel',
            name='longitude',
            field=models.FloatField(blank=True, help_text='Longitude of the location.', null=True, verbose_name='Longitude'),
        ),
    ]
