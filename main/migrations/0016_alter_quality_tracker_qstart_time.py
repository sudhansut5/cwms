﻿# Generated by Django 5.0.3 on 2024-04-09 13:55

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_rename_q1_quality_tracker_q10_result_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quality_tracker',
            name='qstart_time',
            field=models.DateTimeField(verbose_name=django.utils.timezone.now),
        ),
    ]
