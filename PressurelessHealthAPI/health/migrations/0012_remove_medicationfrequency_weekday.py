# Generated by Django 5.0.3 on 2024-04-24 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0011_medicationfrequency_friday_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicationfrequency',
            name='weekday',
        ),
    ]