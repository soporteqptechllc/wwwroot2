# Generated by Django 4.1 on 2023-10-05 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_em_sp_ingrediente_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='operaciones',
            name='reproceso',
            field=models.FloatField(blank=True, null=True, verbose_name='reproceso'),
        ),
    ]
