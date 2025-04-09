# Generated by Django 5.0.3 on 2024-04-12 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_quality_tracker_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataExtraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='quality_tracker',
            old_name='notes',
            new_name='q_notes',
        ),
    ]
