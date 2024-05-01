# Generated by Django 5.0.3 on 2024-04-21 21:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_alter_contact_email_alter_contact_last_name'),
        ('health', '0009_alter_measurement_measurement_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='medication_frequency',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='health.medicationfrequency'),
        ),
    ]
