# Generated by Django 3.2.5 on 2021-07-14 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_alter_participantlms_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='participantgraduation',
            name='passed',
            field=models.CharField(choices=[('L', 'Lulus'), ('TL', 'Tidak Lulus')], default='TL', max_length=2, verbose_name='Lulus/Tidak Lulus'),
        ),
    ]
