# Generated by Django 3.2.5 on 2021-08-27 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0036_paymentbanner'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrimaseruContacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wa_number', models.CharField(max_length=20, verbose_name='Nomor Whatsapp')),
                ('link_wa', models.CharField(max_length=100, verbose_name='Link Wa')),
            ],
        ),
    ]
