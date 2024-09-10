# Generated by Django 5.0.7 on 2024-09-10 11:51

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiking', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='multidaytrialtrialmodel',
            options={'ordering': ['id'], 'verbose_name': 'BaseM2mModel', 'verbose_name_plural': 'BaseM2mModels'},
        ),
        migrations.AlterModelOptions(
            name='trialroutemodel',
            options={'ordering': ['id'], 'verbose_name': 'BaseM2mModel', 'verbose_name_plural': 'BaseM2mModels'},
        ),
        migrations.AlterField(
            model_name='multidaytrialmodel',
            name='ico',
            field=models.CharField(choices=[('fa-regular fa-user', 'Administrator'), ('bi bi-1-circle', 'Circle')], default='fa-regular fa-user', help_text='Graphical representation of the object. Default value is Administrator icon.', max_length=64, verbose_name='Object ico'),
        ),
        migrations.AlterField(
            model_name='multidaytrialtrialmodel',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique identifier for this object. It is automatically generated and cannot be modified.', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='routemodel',
            name='ico',
            field=models.CharField(choices=[('fa-regular fa-user', 'Administrator'), ('bi bi-1-circle', 'Circle')], default='fa-regular fa-user', help_text='Graphical representation of the object. Default value is Administrator icon.', max_length=64, verbose_name='Object ico'),
        ),
        migrations.AlterField(
            model_name='trialmodel',
            name='ico',
            field=models.CharField(choices=[('fa-regular fa-user', 'Administrator'), ('bi bi-1-circle', 'Circle')], default='fa-regular fa-user', help_text='Graphical representation of the object. Default value is Administrator icon.', max_length=64, verbose_name='Object ico'),
        ),
        migrations.AlterField(
            model_name='trialroutemodel',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique identifier for this object. It is automatically generated and cannot be modified.', primary_key=True, serialize=False),
        ),
    ]
