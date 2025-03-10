# Generated by Django 3.2.13 on 2022-08-23 04:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participant_profile', '0044_alter_participantprofile_resident'),
    ]

    operations = [
        migrations.AddField(
            model_name='participantprofile',
            name='child_no',
            field=models.CharField(help_text='Masukan kamu anak ke berapa. Contoh: Anak ke 2 (<b>isi hanya dengan angka</b>)', max_length=2, null=True, validators=[django.core.validators.DecimalValidator(2, 0)], verbose_name='Anak Ke-'),
        ),
        migrations.AddField(
            model_name='participantprofile',
            name='relatives_no',
            field=models.CharField(help_text='Masukan jumlah saudara Anda (<b> isi hanya dengan angka </b>)', max_length=2, null=True, validators=[django.core.validators.DecimalValidator(2, 0)], verbose_name='Dari Berapa Bersaudara'),
        ),
    ]
