from datetime import date
from django.db import models
from django.utils import timezone
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
    return f'berkas_{instance.participant.username}/{filename}'

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

    updated_at = models.DateTimeField(default=timezone.now)

class ParticipantCount(models.Model):
    count = models.CharField(max_length=10, db_index=True)

    def __str__(self):
        return self.count

class InfoSourcePPDB(models.Model):
    info_source = models.CharField('Sumber Info Primaseru', max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.info_source

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

    info = models.ManyToManyField(InfoSourcePPDB)

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

class ParticipantRePayment(models.Model):
    participant = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    virt_acc_number = models.CharField('Nomor Virtual Account', max_length=30, null=True, help_text="Nomor Virtual Account Bank Mandiri atau CIMB Niaga.")
    paid_off = models.BooleanField('Lunas', default=False)

    # FIXME need to make seperate model
    payment_1 = models.FileField('Pembayaran Ke 1', upload_to=user_directory_path, null=True, blank=True)
    verfied_1 = models.BooleanField('Verifikasi Pembayaran 1', default=False)
    comment_1 = models.CharField('Komentar Pembayaran 1', max_length=100, null=True, blank=True)
    pay_mount_1 = models.CharField('Nominal Pembayaran Ke 1', max_length=100, null=True, blank=True, help_text="Isi Dengan Angka Saja.")
    deadline_1 = models.DateField('Tengat Pembayaran Ke 1', null=True, blank=True)

    payment_2 = models.FileField('Pembayaran Ke 2', null=True, blank=True, upload_to=user_directory_path)
    verfied_2 = models.BooleanField('Verifikasi Pembayaran 2', default=False)
    comment_2 = models.CharField('Komentar Pembayaran 2', max_length=100, null=True, blank=True)
    pay_mount_2 = models.CharField('Nominal Pembayaran Ke 2', max_length=100, null=True, blank=True, help_text="Isi Dengan Angka Saja.")
    deadline_2 = models.DateField('Tengat Pembayaran Ke 2', null=True, blank=True)

    payment_3 = models.FileField('Pembayaran Ke 3', null=True, blank=True, upload_to=user_directory_path)
    verfied_3 = models.BooleanField('Verifikasi Pembayaran 3', default=False)
    comment_3 = models.CharField('Komentar Pembayaran 3', max_length=100, null=True, blank=True)
    pay_mount_3 = models.CharField('Nominal Pembayaran Ke 3', max_length=100, null=True, blank=True, help_text="Isi Dengan Angka Saja.")
    deadline_3 = models.DateField('Tengat Pembayaran Ke 3', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Pembayaran {self.participant}'
