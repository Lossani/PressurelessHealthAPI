# Generated by Django 4.2.7 on 2023-11-17 21:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_challengehistory_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challengehistory',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]