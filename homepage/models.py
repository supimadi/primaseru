from django.db import models

from PIL import Image

class RegisterSchedule(models.Model):
    name = models.CharField('Nama Gelombang Pendaftaran', max_length=120)
    start_date = models.DateField('Tanggal Dimulai Pendaftaran')
    end_date = models.DateField('Tanggal Berakhir Pendaftaran')

    def __str__(self):
        return self.name

    @property
    def is_ongoing(self):
        return date.today().month <= self.end_date.month and date.today().month >= self.start_date.month

    @property
    def is_past_date(self):
        return date.today() > self.end_date


class RegisterStep(models.Model):
    step = models.CharField('Langkap Pendaftaran', max_length=100)
    icon = models.ImageField('Icon', upload_to='register_step_icon')

    def __str__(self):
        return self.step
