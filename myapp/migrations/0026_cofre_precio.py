# Generated by Django 4.2.5 on 2024-03-31 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_cofre'),
    ]

    operations = [
        migrations.AddField(
            model_name='cofre',
            name='precio',
            field=models.IntegerField(default=0),
        ),
    ]
