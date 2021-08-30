# Generated by Django 3.2.5 on 2021-08-27 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('homepage', '0002_auto_20210710_0757'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilesPool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nama File')),
                ('files', models.FileField(help_text='Silahkan Upload File yang Diinginkan.', upload_to='files_pool/', verbose_name='File')),
            ],
        ),
    ]