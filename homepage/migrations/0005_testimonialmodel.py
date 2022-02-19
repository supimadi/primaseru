# Generated by Django 3.2.5 on 2022-02-08 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_prostelkombandung'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestimonialModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_video', models.CharField(max_length=100, verbose_name='Link video')),
                ('full_name', models.CharField(max_length=100, verbose_name='Nama lengkap')),
                ('title', models.CharField(help_text='Contoh: Alumni TKJ Angkatan 7.', max_length=100, verbose_name='Title pemberi testimoni')),
                ('testimonial', models.TextField(verbose_name='Testimoni')),
            ],
        ),
    ]