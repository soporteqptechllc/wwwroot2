# Generated by Django 2.1.15 on 2023-04-11 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0020_auto_20230411_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportelab',
            name='toneladasdesp',
            field=models.FloatField(blank=True, null=True, verbose_name='BM_ToneladasDesp'),
        ),
        migrations.AddField(
            model_name='reportelab',
            name='toneladasprod',
            field=models.FloatField(blank=True, null=True, verbose_name='BM_ToneladasProd'),
        ),
    ]