# Generated by Django 4.2.7 on 2023-11-11 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('time_limit', models.CharField(max_length=50, null=True)),
                ('enabled', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('reward', models.PositiveIntegerField()),
                ('enabled', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50)),
                ('required', models.BooleanField(default=True)),
                ('time_limit', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GoalRequirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamification.goal')),
                ('requirement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamification.requirement')),
            ],
        ),
    ]