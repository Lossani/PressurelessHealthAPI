# Generated by Django 4.2.7 on 2023-11-14 03:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_challengehistory_event_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challengehistory',
            name='event_date',
        ),
        migrations.AddField(
            model_name='challengehistory',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 13, 22, 19, 8, 317839)),
        ),
        migrations.AddField(
            model_name='challengehistory',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 13, 22, 19, 8, 317839)),
        ),
        migrations.AlterField(
            model_name='challengehistory',
            name='succeeded',
            field=models.BooleanField(default=False),
        ),
    ]
