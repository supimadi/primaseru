# Generated by Django 3.2.5 on 2021-08-30 03:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0041_participant_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
