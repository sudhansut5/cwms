﻿# Generated by Django 5.0.3 on 2024-04-15 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_rename_notes_quality_tracker_q_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='quality_tracker',
            name='qdate_received',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quality_tracker',
            name='qdate_reviewed',
            field=models.DateField(blank=True, null=True),
        ),
    ]
