# Generated by Django 4.2 on 2023-04-28 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0002_producciondiaria'),
    ]

    operations = [
        migrations.AddField(
            model_name='producciondiaria',
            name='op14',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='producciondiaria',
            name='op5',
            field=models.FloatField(default=0),
        ),
    ]
