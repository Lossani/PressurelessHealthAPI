# Generated by Django 5.0.3 on 2024-05-30 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0012_remove_medicationfrequency_weekday'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]