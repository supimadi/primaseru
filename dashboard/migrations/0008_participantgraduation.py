# Generated by Django 3.2.5 on 2021-07-12 07:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0007_auto_20210711_0553'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParticipantGraduation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter', models.FileField(blank=True, null=True, upload_to='berkas_kelulusan/', verbose_name='Berkas Kelulusan')),
                ('chose_major', models.CharField(choices=[('TKJ', 'Teknik Komputer dan Jaringan'), ('TJAT', 'Teknik Jaringan Akses dan Telekomunikasi'), ('MM', 'Multimedia')], max_length=4, verbose_name='Pilihan Jurusan')),
                ('participant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
