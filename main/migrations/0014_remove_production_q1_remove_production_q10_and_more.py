﻿# Generated by Django 5.0.3 on 2024-04-05 12:45

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_production_q1_production_q10_production_q10_comment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='production',
            name='q1',
        ),
        migrations.RemoveField(
            model_name='production',
            name='q10',
        ),
        migrations.RemoveField(
            model_name='production',
            name='q10_comment',
        ),
        migrations.RemoveField(
            model_name='production',
            name='q1_comment',
        ),
        migrations.RemoveField(
            model_name='production',
            name='q2',
        ),
        migrations.RemoveField(
            model_name='production',
            name='q2_comment',
        ),
        migrations.RemoveField(
            model_name='production',
            name='q3',
        ),
        migrations.RemoveField(
            model_name='production',
            name='q3_comment',
        ),
        migrations.RemoveField(
            model_name='production',
            name='q4',
        ),
        migrations.RemoveField(
            model_name='production',
            name='q4_comment',
        ),
        migrations.RemoveField(
            model_name='production',
            name='q5',
        ),
        migrations.RemoveField(
            model_name='production',
            name='q5_comment',
        ),
        migrations.RemoveField(
            model_name='production',
            name='q6',
        ),
        migrations.RemoveField(
            model_name='production',
            name='q6_comment',
        ),
        migrations.RemoveField(
            model_name='production',
            name='q7',
        ),
        migrations.RemoveField(
            model_name='production',
            name='q7_comment',
        ),
        migrations.RemoveField(
            model_name='production',
            name='q8',
        ),
        migrations.RemoveField(
            model_name='production',
            name='q8_comment',
        ),
        migrations.RemoveField(
            model_name='production',
            name='q9',
        ),
        migrations.RemoveField(
            model_name='production',
            name='q9_comment',
        ),
        migrations.CreateModel(
            name='Quality_tracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qstart_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('qend_time', models.DateTimeField(blank=True, null=True)),
                ('q1', models.CharField(blank=True, choices=[('Pass', 'Pass'), ('Fail', 'Fail'), ('NA', 'NA')], default=None, max_length=20, null=True)),
                ('q1_comment', models.TextField(blank=True, default='', null=True)),
                ('q2', models.CharField(blank=True, choices=[('Pass', 'Pass'), ('Fail', 'Fail'), ('NA', 'NA')], default=None, max_length=20, null=True)),
                ('q2_comment', models.TextField(blank=True, default='', null=True)),
                ('q3', models.CharField(blank=True, choices=[('Pass', 'Pass'), ('Fail', 'Fail'), ('NA', 'NA')], default=None, max_length=20, null=True)),
                ('q3_comment', models.TextField(blank=True, default='', null=True)),
                ('q4', models.CharField(blank=True, choices=[('Pass', 'Pass'), ('Fail', 'Fail'), ('NA', 'NA')], default=None, max_length=20, null=True)),
                ('q4_comment', models.TextField(blank=True, default='', null=True)),
                ('q5', models.CharField(blank=True, choices=[('Pass', 'Pass'), ('Fail', 'Fail'), ('NA', 'NA')], default=None, max_length=20, null=True)),
                ('q5_comment', models.TextField(blank=True, default='', null=True)),
                ('q6', models.CharField(blank=True, choices=[('Pass', 'Pass'), ('Fail', 'Fail'), ('NA', 'NA')], default=None, max_length=20, null=True)),
                ('q6_comment', models.TextField(blank=True, default='', null=True)),
                ('q7', models.CharField(blank=True, choices=[('Pass', 'Pass'), ('Fail', 'Fail'), ('NA', 'NA')], default=None, max_length=20, null=True)),
                ('q7_comment', models.TextField(blank=True, default='', null=True)),
                ('q8', models.CharField(blank=True, choices=[('Pass', 'Pass'), ('Fail', 'Fail'), ('NA', 'NA')], default=None, max_length=20, null=True)),
                ('q8_comment', models.TextField(blank=True, default='', null=True)),
                ('q9', models.CharField(blank=True, choices=[('Pass', 'Pass'), ('Fail', 'Fail'), ('NA', 'NA')], default=None, max_length=20, null=True)),
                ('q9_comment', models.TextField(blank=True, default='', null=True)),
                ('q10', models.CharField(blank=True, choices=[('Pass', 'Pass'), ('Fail', 'Fail'), ('NA', 'NA')], default=None, max_length=20, null=True)),
                ('q10_comment', models.TextField(blank=True, default='', null=True)),
                ('final_score', models.IntegerField(blank=True, null=True)),
                ('qpause1', models.DateTimeField(blank=True, null=True)),
                ('qresume1', models.DateTimeField(blank=True, null=True)),
                ('qpause2', models.DateTimeField(blank=True, null=True)),
                ('qresume2', models.DateTimeField(blank=True, null=True)),
                ('qpause3', models.DateTimeField(blank=True, null=True)),
                ('qresume3', models.DateTimeField(blank=True, null=True)),
                ('qduration', models.CharField(blank=True, max_length=20, null=True)),
                ('qidle_time', models.DurationField(blank=True, null=True)),
                ('Production', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Quality_tracker', to='main.production')),
            ],
        ),
    ]
