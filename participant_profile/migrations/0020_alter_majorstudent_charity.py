# Generated by Django 3.2.5 on 2021-08-30 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participant_profile', '0019_alter_photoprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='majorstudent',
            name='charity',
            field=models.CharField(choices=[('0', 'Rp. 0'), ('50', 'Rp. 500.000,-'), ('100', 'Rp. 1.000.000,-'), ('150', 'Rp. 1.500.000,-'), ('200', 'Rp. 2.000.000,-'), ('250', 'Rp. 2.500.000,-'), ('300', 'Rp. 3.000.000,-')], help_text='Dana Sukarela nantinya akan dimanfaatkan untuk pengembangan siswa dibidang non akademik (kompetisi dan perlombaan-perlombaan).', max_length=4, null=True, verbose_name='Dana Sukarela'),
        ),
    ]