﻿# Generated by Django 4.2.6 on 2023-11-28 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataUtility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('analyst_name', models.CharField(max_length=100)),
                ('date_received', models.DateField()),
                ('transaction_number', models.CharField(max_length=50)),
                ('date_reviewed', models.DateField(blank=True, null=True)),
                ('process', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('sub_process', models.CharField(max_length=100)),
                ('tat', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('Complete', 'Complete'), ('In Progress', 'In Progress'), ('Hold', 'Hold')], max_length=20)),
                ('query', models.CharField(choices=[('No Query', 'No Query'), ('Internal', 'Internal'), ('External', 'External')], max_length=20)),
                ('notes', models.TextField()),
                ('pause1', models.DateTimeField(blank=True, null=True)),
                ('resume1', models.DateTimeField(blank=True, null=True)),
                ('pause2', models.DateTimeField(blank=True, null=True)),
                ('resume2', models.DateTimeField(blank=True, null=True)),
                ('pause3', models.DateTimeField(blank=True, null=True)),
                ('resume3', models.DateTimeField(blank=True, null=True)),
                ('duration', models.DurationField(blank=True, null=True)),
                ('idle_time', models.DurationField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
            ],
        ),
    ]
