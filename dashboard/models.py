from django.db import models
from django.utils.translation import ugettext_lazy as _

from users.models import CustomUser


# PHONE_REGEX = '^(\+[62]{1,2}|0)[0-9]{10,12}\b'
REPRESENTATIVE_CHOICES = [
    ('B', 'Bapak'),
    ('I', 'Ibu'),
    ('W', 'Wali'),
]

class ParticipantCount(models.Model):
    count = models.CharField(max_length=6, db_index=True)

    def __str__(self):
        return self.count


class Participant(models.Model):
    full_name = models.CharField(_('Full Name'), max_length=100)
    account = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    registration_number = models.IntegerField(_('Registration Number'), unique=True, db_index=True)
    participant_phone_number = models.IntegerField(_('Participant Phone Number'))
    homeroom_teacher_phone_number = models.IntegerField(_('Homeroom Teacher Phone Number'), null=True, blank=True)
    parent_full_name = models.CharField(_('Parent Full Name'), max_length=100)
    representative = models.CharField(_('Representative'), max_length=1, choices=REPRESENTATIVE_CHOICES)
    parent_phone_number = models.IntegerField(_('Parent Phone Number'))

    def __str__(self):
        return f'{self.full_name}-{self.registration_number}'


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
