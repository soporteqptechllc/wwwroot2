# Generated by Django 2.1.15 on 2023-03-31 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0003_auto_20230331_1115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportelab',
            old_name='CargarPromedioId',
            new_name='cargarPromedioid',
        ),
        migrations.RenameField(
            model_name='reportelab',
            old_name='Cemento',
            new_name='cemento',
        ),
        migrations.RenameField(
            model_name='reportelab',
            old_name='Comentarios',
            new_name='comentarios',
        ),
        migrations.RenameField(
            model_name='reportelab',
            old_name='FAnalista',
            new_name='fanalista',
        ),
        migrations.RenameField(
            model_name='reportelab',
            old_name='Molino',
            new_name='molino',
        ),
        migrations.RenameField(
            model_name='reportelab',
            old_name='ProductoId',
            new_name='productoid',
        ),
        migrations.RenameField(
            model_name='reportelab',
            old_name='QAnalista',
            new_name='qanalista',
        ),
        migrations.RenameField(
            model_name='reportelab',
            old_name='Silo',
            new_name='silo',
        ),
    ]