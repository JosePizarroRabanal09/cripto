# Generated by Django 4.2.5 on 2024-03-22 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_compra_habilitado_farmear'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guerrero',
            name='cooldown',
            field=models.IntegerField(default=0),
        ),
    ]