﻿# Generated by Django 5.0.3 on 2024-04-03 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_delete_quality_data_delete_quality_tracker_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='q1',
            field=models.CharField(choices=[('Pass', 'Pass'), ('Fail', 'Fail'), ('NA', 'NA')], max_length=20),
        ),
        migrations.AlterField(
            model_name='production',
            name='q10',
            field=models.CharField(choices=[('Pass', 'Pass'), ('Fail', 'Fail'), ('NA', 'NA')], max_length=20),
        ),
        migrations.AlterField(
            model_name='production',
            name='q2',
            field=models.CharField(choices=[('Pass', 'Pass'), ('Fail', 'Fail'), ('NA', 'NA')], max_length=20),
        ),
        migrations.AlterField(
            model_name='production',
            name='q3',
            field=models.CharField(choices=[('Pass', 'Pass'), ('Fail', 'Fail'), ('NA', 'NA')], max_length=20),
        ),
        migrations.AlterField(
            model_name='production',
            name='q4',
            field=models.CharField(choices=[('Pass', 'Pass'), ('Fail', 'Fail'), ('NA', 'NA')], max_length=20),
        ),
        migrations.AlterField(
            model_name='production',
            name='q5',
            field=models.CharField(choices=[('Pass', 'Pass'), ('Fail', 'Fail'), ('NA', 'NA')], max_length=20),
        ),
        migrations.AlterField(
            model_name='production',
            name='q6',
            field=models.CharField(choices=[('Pass', 'Pass'), ('Fail', 'Fail'), ('NA', 'NA')], max_length=20),
        ),
        migrations.AlterField(
            model_name='production',
            name='q8',
            field=models.CharField(choices=[('Pass', 'Pass'), ('Fail', 'Fail'), ('NA', 'NA')], max_length=20),
        ),
    ]
