# Generated by Django 5.0.1 on 2024-01-24 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boquillas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boquillas',
            old_name='name_Producto',
            new_name='producto',
        ),
        migrations.AlterField(
            model_name='productos',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='id_Producto'),
        ),
    ]