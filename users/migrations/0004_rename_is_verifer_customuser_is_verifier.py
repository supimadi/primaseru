# Generated by Django 3.2.5 on 2022-05-12 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_is_verifer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='is_verifer',
            new_name='is_verifier',
        ),
    ]
