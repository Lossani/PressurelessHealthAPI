# Generated by Django 4.2.7 on 2023-11-14 04:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_challengehistory_event_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challengehistory',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='challengehistory',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 13, 23, 42, 59, 784043)),
        ),
    ]
