# Generated by Django 4.2.7 on 2023-11-14 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamification', '0004_delete_goalrequirement'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='requirements',
            field=models.ManyToManyField(to='gamification.requirement'),
        ),
        migrations.DeleteModel(
            name='ChallengeRequirement',
        ),
    ]