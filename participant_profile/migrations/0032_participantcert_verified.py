# Generated by Django 3.2.5 on 2021-09-12 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participant_profile', '0031_auto_20210912_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='participantcert',
            name='verified',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]
