# Generated by Django 5.0.1 on 2024-02-06 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boquillas', '0015_remove_boquillas_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='peso',
            field=models.FloatField(blank=True, null=True, verbose_name='peso_kg'),
        ),
    ]
