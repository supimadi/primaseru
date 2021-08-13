from datetime import date
from django.db import models
from django.utils.translation import ugettext_lazy as _

from users.models import CustomUser
from participant_profile.choices import MAJOR, INFORMATION_PRIMASERU


# PHONE_REGEX = '^(\+[62]{1,2}|0)[0-9]{10,12}\b'
REPRESENTATIVE_CHOICES = [
    ('B', 'Bapak'),
    ('I', 'Ibu'),
    ('W', 'Wali'),
]

PASSED_CHOICES = [
    ('L', 'Lulus'),
    ('TL', 'Tidak Lulus'),
]

def user_directory_path(instance, filename):
    return f'berkas_{instance.account.username}/{filename}'

class ParticipantLMS(models.Model):
    participant = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    username = models.CharField('Username', max_length=120)
    password = models.CharField('Password', max_length=120)
    schedule = models.DateField('Tanggal')
    time = models.CharField('Pukul', max_length=20)

class ParticipantGraduation(models.Model):
    participant = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    passed = models.CharField('Lulus/Tidak Lulus', max_length=2, choices=PASSED_CHOICES, default='TL')
    letter = models.FileField('Surat Kelulusan', null=True, blank=True, upload_to='berkas_kelulusan/')
    chose_major = models.CharField('Diterima di Jurusan:', max_length=4, choices=MAJOR, null=True, blank=True)

class ParticipantCount(models.Model):
    count = models.CharField(max_length=6, db_index=True)

    def __str__(self):
        return self.count

class Participant(models.Model):
    account = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    verified = models.BooleanField(_('Verified'), default=False, db_index=True)

    full_name = models.CharField(_('Nama Lengkap'), max_length=100)
    registration_number = models.CharField(_('Nomor Pendaftaran'), unique=True, db_index=True, max_length=20, null=True)
    participant_phone_number = models.CharField(_('No. HP Calon Siswa'), max_length=15, unique=True, db_index=True)
    previous_school = models.CharField(_('Nama Asal Sekolah'), max_length=100, db_index=True, null=True)

    parent_phone_number = models.CharField(_('No. HP Orang Tua/Wali'), max_length=15)
    parent_full_name = models.CharField(_('Nama Lengkap Orang Tua'), max_length=100, null=True)

    homeroom_teacher_phone_number = models.CharField(_('No. HP Wali Kelas'), null=True, blank=True, max_length=15)
    bk_teacher_phone_number = models.CharField(_('No. HP Guru BK'), null=True, blank=True, max_length=15)

    info = models.CharField(_('Info Primaseru (PPDB)'), max_length=3, choices=INFORMATION_PRIMASERU, null=True)

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

class RegisterStep(models.Model):
    step = models.CharField('Langkap Pendaftaran', max_length=100)

    def __str__(self):
        return self.step
