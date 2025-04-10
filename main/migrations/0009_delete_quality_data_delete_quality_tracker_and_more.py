﻿# Generated by Django 5.0.3 on 2024-04-03 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_quality_tracker'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Quality_Data',
        ),
        migrations.DeleteModel(
            name='Quality_tracker',
        ),
        migrations.AddField(
            model_name='production',
            name='q1',
            field=models.CharField(choices=[('Pass', 'Pass'), ('Fail', 'Fail'), ('NA', 'NA')], default='Pass', max_length=20),
        ),
        migrations.AddField(
            model_name='production',
            name='q10',
            field=models.CharField(choices=[('Pass', 'Pass'), ('Fail', 'Fail'), ('NA', 'NA')], default='Pass', max_length=20),
        ),
        migrations.AddField(
            model_name='production',
            name='q10_comment',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='production',
            name='q1_comment',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='production',
            name='q2',
            field=models.CharField(choices=[('Pass', 'Pass'), ('Fail', 'Fail'), ('NA', 'NA')], default='Pass', max_length=20),
        ),
        migrations.AddField(
            model_name='production',
            name='q2_comment',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='production',
            name='q3',
            field=models.CharField(choices=[('Pass', 'Pass'), ('Fail', 'Fail'), ('NA', 'NA')], default='Pass', max_length=20),
        ),
        migrations.AddField(
            model_name='production',
            name='q3_comment',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='production',
            name='q4',
            field=models.CharField(choices=[('Pass', 'Pass'), ('Fail', 'Fail'), ('NA', 'NA')], default='Pass', max_length=20),
        ),
        migrations.AddField(
            model_name='production',
            name='q4_comment',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='production',
            name='q5',
            field=models.CharField(choices=[('Pass', 'Pass'), ('Fail', 'Fail'), ('NA', 'NA')], default='Pass', max_length=20),
        ),
        migrations.AddField(
            model_name='production',
            name='q5_comment',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='production',
            name='q6',
            field=models.CharField(choices=[('Pass', 'Pass'), ('Fail', 'Fail'), ('NA', 'NA')], default='Pass', max_length=20),
        ),
        migrations.AddField(
            model_name='production',
            name='q6_comment',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='production',
            name='q7',
            field=models.CharField(choices=[('Pass', 'Pass'), ('Fail', 'Fail'), ('NA', 'NA')], default='Pass', max_length=20),
        ),
        migrations.AddField(
            model_name='production',
            name='q7_comment',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='production',
            name='q8',
            field=models.CharField(choices=[('Pass', 'Pass'), ('Fail', 'Fail'), ('NA', 'NA')], default='Pass', max_length=20),
        ),
        migrations.AddField(
            model_name='production',
            name='q8_comment',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='production',
            name='q9',
            field=models.CharField(choices=[('Pass', 'Pass'), ('Fail', 'Fail'), ('NA', 'NA')], default='Pass', max_length=20),
        ),
        migrations.AddField(
            model_name='production',
            name='q9_comment',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
