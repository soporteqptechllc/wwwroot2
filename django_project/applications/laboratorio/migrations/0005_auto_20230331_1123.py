# Generated by Django 2.1.15 on 2023-03-31 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0004_auto_20230331_1120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportelab',
            old_name='cargarPromedioid',
            new_name='cargarpromedioid',
        ),
    ]
