# Generated by Django 3.2.5 on 2022-02-08 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_testimonialmodel_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonialmodel',
            name='video_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Video ID'),
        ),
    ]