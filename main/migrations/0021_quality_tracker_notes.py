# Generated by Django 5.0.3 on 2024-04-09 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_production_qc_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='quality_tracker',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
