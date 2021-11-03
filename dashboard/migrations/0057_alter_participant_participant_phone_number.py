# Generated by Django 3.2.5 on 2021-11-02 02:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0056_alter_participantgraduation_chose_major'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='participant_phone_number',
            field=models.CharField(db_index=True, max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message='Masukan nomor HP, tanpa spasi dan strip.', regex='/(\\+62[0-9]{10,12})|(08[0-9]{10,12})/g')], verbose_name='No. HP Calon Siswa'),
        ),
    ]