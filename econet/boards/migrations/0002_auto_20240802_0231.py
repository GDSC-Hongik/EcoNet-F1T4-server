# Generated by Django 3.2.25 on 2024-08-02 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Board',
            new_name='Gathering',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='board',
            new_name='gathering',
        ),
    ]
