# Generated by Django 4.2.5 on 2024-03-26 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_guerrero_precio_alter_withdraw_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='life',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=50)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
