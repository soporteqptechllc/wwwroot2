# Generated by Django 3.2.5 on 2023-02-27 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0013_valoressensores'),
    ]

    operations = [
        migrations.CreateModel(
            name='llegadas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('llegadas_id', models.BigIntegerField(blank=True, db_column='llegadas_id', null=True)),
                ('description', models.TextField(blank=True, db_column='description', null=True)),
                ('nivel_porcen', models.FloatField(blank=True, db_column='nivel_porcen', null=True)),
                ('fecha_fin', models.DateTimeField(blank=True, db_column='fecha_fin', null=True)),
                ('n_maximo', models.FloatField(blank=True, db_column='nivel_maximo', null=True)),
                ('n_minimo', models.FloatField(blank=True, db_column='nivel_minimo', null=True)),
                ('incremento', models.FloatField(blank=True, db_column='incremento', null=True)),
                ('fecha_min', models.DateTimeField(blank=True, db_column='fecha_min', null=True)),
                ('id_sensorLL', models.BigIntegerField(blank=True, db_column='sensor_id', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='pedidos',
            name='decremento',
            field=models.FloatField(blank=True, db_column='decremento', null=True),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='fecha_max',
            field=models.DateTimeField(blank=True, db_column='fecha_max', null=True),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='id_sensorP',
            field=models.BigIntegerField(blank=True, db_column='sensor_id', null=True),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='id_tablaLlegadas',
            field=models.BigIntegerField(blank=True, db_column='llegadas_id', null=True),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='n_maximo',
            field=models.FloatField(blank=True, db_column='nivel_maximo', null=True),
        ),
    ]