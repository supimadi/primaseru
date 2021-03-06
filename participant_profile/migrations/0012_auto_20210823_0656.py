# Generated by Django 3.2.5 on 2021-08-23 06:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import participant_profile.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('participant_profile', '0011_auto_20210823_0336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentfile',
            name='family_cert',
        ),
        migrations.CreateModel(
            name='ParticipantFamilyCert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_cert', models.FileField(blank=True, null=True, upload_to=participant_profile.models.user_directory_path, verbose_name='Kartu Keluarga')),
                ('participant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
