# Generated by Django 3.2.5 on 2021-08-18 05:12

import dashboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0027_alter_infosourceppdb_info_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantrepayment',
            name='payment_1',
            field=models.FileField(blank=True, null=True, upload_to=dashboard.models.user_directory_path, verbose_name='Pembayaran Ke 1'),
        ),
    ]