# Generated by Django 4.2.5 on 2024-03-31 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_historialgold_tower_alter_historialgold_guerrero'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='gold_Total',
            field=models.IntegerField(default=0),
        ),
    ]
