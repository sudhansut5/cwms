﻿# Generated by Django 4.2.6 on 2023-11-29 12:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_production_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
