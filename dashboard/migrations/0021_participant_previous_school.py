# Generated by Django 3.2.5 on 2021-08-12 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0020_alter_participant_participant_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='previous_school',
            field=models.CharField(db_index=True, max_length=100, null=True, verbose_name='No. HP Calon Siswa'),
        ),
    ]
