# Generated by Django 3.2.5 on 2021-08-15 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0025_auto_20210815_0641'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoSourcePPDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_source', models.CharField(max_length=100, verbose_name='Sumber Info Primaseru')),
            ],
        ),
        migrations.RemoveField(
            model_name='participant',
            name='info',
        ),
        migrations.AddField(
            model_name='participant',
            name='info',
            field=models.ManyToManyField(to='dashboard.InfoSourcePPDB'),
        ),
    ]
