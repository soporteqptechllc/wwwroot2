# Generated by Django 5.0.1 on 2024-01-25 18:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boquillas', '0009_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='boquillas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_boquilla', models.IntegerField(blank=True, null=True, verbose_name='#_boquilla')),
                ('name_producto', models.CharField(blank=True, max_length=60, null=True, unique=True, verbose_name='name_Producto')),
                ('idbq', models.BigIntegerField(blank=True, null=True, verbose_name='idBQ')),
                ('sp', models.FloatField(blank=True, null=True, verbose_name='setpoint')),
                ('peso', models.FloatField(blank=True, null=True, verbose_name='peso_kg')),
                ('sp_ajuste1', models.FloatField(blank=True, null=True, verbose_name='sp_ajuste1')),
                ('sp_ff', models.FloatField(blank=True, null=True, verbose_name='sp_ajuste2')),
                ('dia', models.IntegerField(blank=True, null=True, verbose_name='dia')),
                ('hora', models.IntegerField(blank=True, null=True, verbose_name='hora')),
                ('min', models.IntegerField(blank=True, null=True, verbose_name='min')),
                ('seg', models.IntegerField(blank=True, null=True, verbose_name='seg')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='feccha')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_producto', to='boquillas.productos')),
            ],
            options={
                'verbose_name': 'Boquilla',
                'verbose_name_plural': 'Boquillas',
            },
        ),
    ]
