# Generated by Django 4.2.7 on 2023-11-17 21:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_challengehistory_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challengehistory',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 17, 21, 7, 52, 180876)),
        ),
    ]