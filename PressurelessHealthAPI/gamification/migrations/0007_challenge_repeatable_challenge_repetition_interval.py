# Generated by Django 4.2.7 on 2023-11-16 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamification', '0006_challenge_reward'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='repeatable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='challenge',
            name='repetition_interval',
            field=models.PositiveIntegerField(null=True),
        ),
    ]