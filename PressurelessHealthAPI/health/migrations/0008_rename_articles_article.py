# Generated by Django 5.0.3 on 2024-04-13 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0007_articles'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Articles',
            new_name='Article',
        ),
    ]
