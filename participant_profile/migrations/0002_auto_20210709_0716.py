# Generated by Django 3.2.5 on 2021-07-09 07:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('participant_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fatherstudentprofile',
            name='participant',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.customuser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='majorstudent',
            name='participant',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.customuser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='motherstudentprofile',
            name='participant',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.customuser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participantprofile',
            name='participant',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.customuser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photoprofile',
            name='participant',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.customuser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentfile',
            name='participant',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.customuser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentguardianprofile',
            name='participant',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.customuser'),
            preserve_default=False,
        ),
    ]
