# Generated by Django 3.2.25 on 2024-08-06 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0002_alter_information_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pictures',
            options={'managed': False},
        ),
        migrations.AlterModelTable(
            name='information',
            table='Information',
        ),
    ]
