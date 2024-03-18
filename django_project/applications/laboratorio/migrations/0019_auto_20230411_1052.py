# Generated by Django 2.1.15 on 2023-04-11 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0018_auto_20230411_1031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportelab',
            old_name='_ai2o3',
            new_name='ai2o3',
        ),
        migrations.RenameField(
            model_name='reportelab',
            old_name='_fe2o3',
            new_name='fe2o3',
        ),
        migrations.RenameField(
            model_name='reportelab',
            old_name='_sio2',
            new_name='sio2',
        ),
        migrations.AddField(
            model_name='reportelab',
            name='cao',
            field=models.FloatField(blank=True, null=True, verbose_name='AW_%CaO'),
        ),
        migrations.AddField(
            model_name='reportelab',
            name='k2o',
            field=models.FloatField(blank=True, null=True, verbose_name='BA_%K2O'),
        ),
        migrations.AddField(
            model_name='reportelab',
            name='mgo',
            field=models.FloatField(blank=True, null=True, verbose_name='AX_%MgO'),
        ),
        migrations.AddField(
            model_name='reportelab',
            name='na2o',
            field=models.FloatField(blank=True, null=True, verbose_name='AZ_%Na2O'),
        ),
        migrations.AddField(
            model_name='reportelab',
            name='p2o5',
            field=models.FloatField(blank=True, null=True, verbose_name='BC_%P2O5'),
        ),
        migrations.AddField(
            model_name='reportelab',
            name='pi',
            field=models.FloatField(blank=True, null=True, verbose_name='BD_%PI'),
        ),
        migrations.AddField(
            model_name='reportelab',
            name='so3',
            field=models.FloatField(blank=True, null=True, verbose_name='AY_%SO3'),
        ),
        migrations.AddField(
            model_name='reportelab',
            name='tio2',
            field=models.FloatField(blank=True, null=True, verbose_name='BB_%TiO2'),
        ),
    ]