# Generated by Django 4.2.7 on 2023-11-15 20:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_challengehistory_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challengehistory',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 15, 20, 29, 14, 724508)),
        ),
    ]
