# Generated by Django 2.1.15 on 2023-04-12 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0022_remove_reportelab_toneladasprod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportelab',
            name='toneladasdesp',
        ),
        migrations.AddField(
            model_name='reportelab',
            name='tipo',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Tipo'),
        ),
        migrations.AddField(
            model_name='reportelab',
            name='toneladas',
            field=models.FloatField(blank=True, null=True, verbose_name='BM_Toneladas'),
        ),
    ]
