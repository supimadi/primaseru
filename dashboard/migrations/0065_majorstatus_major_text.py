# Generated by Django 3.2.5 on 2022-04-06 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0064_majorstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='majorstatus',
            name='major_text',
            field=models.CharField(max_length=100, null=True, verbose_name='Kepanjangan dari Singkatan Jurusan'),
        ),
    ]
