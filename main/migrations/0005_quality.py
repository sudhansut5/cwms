﻿# Generated by Django 5.0.2 on 2024-02-15 17:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_production_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('analyst_name', models.CharField(max_length=100)),
                ('date_received', models.DateField()),
                ('transaction_number', models.CharField(max_length=50)),
                ('date_reviewed', models.DateField(blank=True, null=True)),
                ('process', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('sub_process', models.CharField(max_length=100)),
                ('tat', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('Complete', 'Complete'), ('In Progress', 'In Progress'), ('Query', 'Query')], max_length=20)),
                ('notes', models.TextField()),
                ('pause1', models.DateTimeField(blank=True, null=True)),
                ('resume1', models.DateTimeField(blank=True, null=True)),
                ('pause2', models.DateTimeField(blank=True, null=True)),
                ('resume2', models.DateTimeField(blank=True, null=True)),
                ('pause3', models.DateTimeField(blank=True, null=True)),
                ('resume3', models.DateTimeField(blank=True, null=True)),
                ('duration', models.CharField(blank=True, max_length=20, null=True)),
                ('idle_time', models.DurationField(blank=True, null=True)),
            ],
        ),
    ]
