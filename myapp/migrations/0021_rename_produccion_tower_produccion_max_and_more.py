# Generated by Django 4.2.5 on 2024-03-29 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_registrocompra_habilitado_farmear_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tower',
            old_name='produccion',
            new_name='produccion_max',
        ),
        migrations.AddField(
            model_name='tower',
            name='produccion_min',
            field=models.IntegerField(default=0),
        ),
    ]