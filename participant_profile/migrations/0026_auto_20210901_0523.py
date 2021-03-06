# Generated by Django 3.2.5 on 2021-09-01 05:23

from django.db import migrations, models
import participant_profile.models


class Migration(migrations.Migration):

    dependencies = [
        ('participant_profile', '0025_auto_20210830_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportfileparticipant',
            name='part',
            field=models.CharField(choices=[('P_1', 'Lembar 1'), ('P_2', 'Lembar 2'), ('P_3', 'Lembar 3')], help_text='Pilih bagian ke berapa raport yang di unggah.', max_length=3, verbose_name='Bagian Raport'),
        ),
        migrations.AlterField(
            model_name='studentfile',
            name='color_blind_cert',
            field=models.FileField(blank=True, null=True, upload_to=participant_profile.models.user_directory_path, verbose_name='Surat Keterangan Tidak Buta Warna'),
        ),
        migrations.AlterField(
            model_name='studentfile',
            name='ijazah',
            field=models.FileField(blank=True, help_text='Ijazah dapat menyusul.', null=True, upload_to=participant_profile.models.user_directory_path, verbose_name='Ijazah'),
        ),
    ]
