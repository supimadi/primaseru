# Generated by Django 3.2.5 on 2021-08-11 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_auto_20210811_0735'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='parnet_full_name',
            new_name='parent_full_name',
        ),
    ]
