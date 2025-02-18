# Generated by Django 3.2.25 on 2024-08-01 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='TokenBlacklistOutstandingtoken',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('token', models.TextField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('expires_at', models.DateTimeField()),
                ('jti', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'token_blacklist_outstandingtoken',
                'managed': False,
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
