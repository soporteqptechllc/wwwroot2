# Generated by Django 4.1 on 2023-09-04 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='em_sp',
            name='Ingrediente',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Ingrediente'),
        ),
        migrations.AlterField(
            model_name='productionorders1_sap',
            name='duedate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='DueDate'),
        ),
    ]
