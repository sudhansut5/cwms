﻿# Generated by Django 5.0.3 on 2024-04-09 13:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_quality_tracker_qstart_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quality_tracker',
            name='qstart_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
