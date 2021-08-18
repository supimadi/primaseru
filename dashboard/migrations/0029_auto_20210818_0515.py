# Generated by Django 3.2.5 on 2021-08-18 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0028_alter_participantrepayment_payment_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='participantrepayment',
            name='pay_mount_1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nominal Pembayaran Ke 1'),
        ),
        migrations.AddField(
            model_name='participantrepayment',
            name='pay_mount_2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nominal Pembayaran Ke 2'),
        ),
        migrations.AddField(
            model_name='participantrepayment',
            name='pay_mount_3',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nominal Pembayaran Ke 3'),
        ),
    ]
