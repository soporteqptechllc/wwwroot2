# Generated by Django 2.1.15 on 2023-03-31 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportelab',
            name='proc_clinker',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Procencia_Clinker'),
        ),
        migrations.AlterField(
            model_name='reportelab',
            name='Comentarios',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='CC_Comentarios'),
        ),
    ]
