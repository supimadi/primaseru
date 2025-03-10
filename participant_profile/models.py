from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

from users.models import CustomUser

from . import choices

from dashboard.models import user_directory_path


def validate_two_digits_num(value):
    try:
        val = int(value)
        if val > 99:
            raise ValidationError(f"{value} lebih dari 3 digit", params={"value": value})
    except ValueError:
        raise ValidationError(f"{value} bukan angka", params={"value": value})

class ParticipantCert(models.Model):
    participant = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False, db_index=True)
    certificate = models.FileField('Sertifikat Penghargaan', upload_to=user_directory_path)
    certi_name = models.CharField('Nama Sertifikat', max_length=120, help_text="Tuliskan beserta nomor Juara", null=True)

    class Meta:
        ordering = ['participant']

    def __str__(self):
        return f'Sertifikat {self.participant}'

class ParticipantFamilyCert(models.Model):
    participant = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False, db_index=True)
    family_cert = models.FileField('Kartu Keluarga', upload_to=user_directory_path, null=True)
    birth_cert = models.FileField('Akta Kelahiran', upload_to=user_directory_path, null=True)

    class Meta:
        ordering = ['participant']

    def __str__(self):
        return f'KK dan Akta Kelahiran {self.participant}'

class StudentFile(models.Model):
    verified = models.BooleanField(default=False, db_index=True)
    participant = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    msg = models.CharField("Pesan", max_length=120, null=True, blank=True)

    color_blind_cert = models.FileField('Surat Keterangan Tidak Buta Warna', upload_to=user_directory_path, null=True)
    healty_cert = models.FileField('Surat Keterangan Sehat', upload_to=user_directory_path, null=True)
    good_behave_cert = models.FileField('Surat Kelakukan Baik', upload_to=user_directory_path, blank=True, null=True)
    ijazah = models.FileField('Ijazah SMP/MTS', upload_to=user_directory_path, null=True, blank=True, help_text="Ijazah SMP/MTS dapat menyusul.")
    ijazah_elem = models.FileField('Ijazah SD/MI', upload_to=user_directory_path, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['participant']

    def __str__(self):
        return f'Raport {self.participant}'

    @property
    def is_data_verified(self):
        return self.verified

class ReportFileParticipant(models.Model):
    verified = models.BooleanField(default=False, db_index=True)
    participant = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    raport = models.FileField('Berkas Raport', upload_to=user_directory_path, null=True, help_text="Harap meng-unggah hasil scan raport, bukan photo supaya terlihat dengan jelas.")
    semester = models.CharField('Raport Semester', max_length=5, choices=choices.RAPORT_SEMESTER, help_text="Pilih raport semester berapa yang di unggah.")

    class Meta:
        ordering = ['participant']

    def __str__(self):
        return f'Raport {self.participant}'

class PaymentUpload(models.Model):
    participant = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    verified = models.BooleanField('Verifikasi', default=False, db_index=True)
    payment = models.FileField('Upload Bukti Pembayaran', upload_to=user_directory_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['participant']

    def __str__(self):
        return self.participant

class PhotoProfile(models.Model):
    image = models.ImageField('Photo', default='default_photo.png', upload_to=user_directory_path)
    participant = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    class Meta:
        ordering = ['participant']

    def __str__(self):
        return f'Photo {self.participant}'

    # def save(self, *args, **kwargs):
    #     super(PhotoProfile, self).save(*args, **kwargs)
    #     img = Image.open(self.image.path)

    #     if img.height > 400 or img.width > 400:
    #         output_size = (400,400)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)


class ParticipantProfile(models.Model):

    verified = models.BooleanField('Verifikasi',default=False, db_index=True)
    participant = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    sex = models.CharField('Jenis Kelamin', max_length=1, choices=choices.SEX)
    religion = models.CharField('Agama', max_length=3, choices=choices.RELIGION)
    city_born = models.CharField('Kota Tempat Lahir', max_length=100, help_text='Contoh: Kabupaten Bandung', db_index=True)
    date_born = models.DateField('Tanggal Lahir', db_index=True)
    social_media = models.CharField('Alamat Sosial Media', max_length=50, help_text='Seperti Instagram atau FB')
    achievement = models.TextField('Prestasi yang Pernah diraih', null=True, blank=True, help_text='Contoh: Juara 1 Lomba Basket Tingkat Nasional')

    nisn = models.CharField('NISN', unique=True ,max_length=20, help_text='Isi NISN berdasarkan NISN yang diberikan sewaktu SMP.')
    nik = models.CharField('Nomor Induk Kependudukan (NIK)',max_length=20, unique=True, help_text='Bisa dicek di Kartu Keluarga')
    kk_number = models.CharField('Nomor Kartu Keluarga (KK)',max_length=20, help_text='Diisi berdasarkan Kartu Keluarga')
    kk_address = models.TextField('Alamat Kartu Keluarga (KK)', help_text='Contoh: Jalan Radio Palasari')

    city = models.CharField('Kota', max_length=120, help_text='Contoh: Kota Bandung')
    kecamatan = models.CharField('Kecamatan', max_length=120, help_text='Contoh: Kecamatan Dayeuhkolot')
    kelurahan = models.CharField('Kelurahan', max_length=120, help_text='Contoh: Desa Cieteureup')
    dusun = models.CharField('Dusun', max_length=120, help_text='Jika tidak tahu diisi dengan -')
    rt_rw = models.CharField('RT/RW', max_length=8, help_text='Contoh: 006/002')
    real_address = models.TextField('Alamat Sekarang', help_text='Contoh: Jalan Bojongsoang')
    resident = models.CharField('Tempat Tinggal', max_length=50, choices=choices.RESIDENT_CHOICES, help_text='Contoh: Rumah Pribadi, Kost, Rumah Keluarga (Keluarga Besar)')

    transport = models.CharField('Alat Transportasi', max_length=50, help_text="Contoh: Jalan Kaki, Motor, Ojek Online, Sepeda, Mobil, Angkot.")

    child_no = models.CharField('Anak Ke-',
                                max_length=2,
                                help_text="Masukan kamu anak ke berapa. Contoh: Anak ke 2 (<b>isi hanya dengan angka</b>)",
                                validators=[validate_two_digits_num],
                                null=True,
                                )
    siblings_no = models.CharField("Dari Berapa Bersaudara",
                                    max_length=2,
                                    help_text="Masukan jumlah saudara Anda (<b> isi hanya dengan angka </b>)",
                                    validators=[validate_two_digits_num],
                                    null=True,
                                    )

    # Previous School Information
    school_origin = models.CharField('Asal Sekolah', max_length=120, help_text="Isilah sesuai dengan asal sekolah Anda dan dituliskan seperti contoh berikut : SMP Telkom Bandung ")
    npsn_school_origin = models.PositiveIntegerField('Nomor NPSN Sekolah Asal', help_text="Bisa Cek <a href='https://referensi.data.kemdikbud.go.id/pendidikan/dikdas' target='_blank'><b>Disini</b></a>", null=True)

    # Medical Record
    medic_record = models.TextField('Riwayat Kesehatan', null=True, blank=True, help_text="Jika pernah mempunyai penyakit, silahkan ditulis disini")
    blood_type = models.CharField('Golongan Darah', choices=choices.BLOOD_TYPE, max_length=2)
    in_medicine = models.CharField('Dalam Pengobatan', max_length=120, null=True, blank=True)
    private_doctor = models.CharField('Nama Dokter Keluarga', max_length=120, null=True, blank=True, help_text="Jika kamu mempunyai dokter keluarga, silahkan input     disini")
    phone_doctor = models.CharField('No Telepon Dokter', max_length=15, null=True, blank=True, help_text="Isi jika memiliki dokter keluarga dan atau dalam masa pen    yambuhan penyakit")

    # Other
    special_needs = models.CharField('Berkebutuhan Khusus', choices=choices.SPESIAL_NEED_CHOICES, max_length=1,
                                     default='N', help_text="Apakah Anda memilika kebutuhan khusus?"
                                     )
    special_needs_text = models.TextField('Penjelasan Kebutuhan Khusus Anda', null=True, blank=True, help_text="Jelaskan seperti apa kebutuhan khusus Anda.")

    class Meta:
        ordering = ['participant']

    def __str__(self):
        return f'{self.id} profile'

    @property
    def is_data_verified(self):
        return self.verified


class MajorStudent(models.Model):
    # student = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False, db_index=True)
    participant = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    first_major = models.CharField('Pilihan Jurusan Pertama', choices=choices.MAJOR, max_length=10)
    second_major = models.CharField('Pilihan Jurusan Kedua', choices=choices.MAJOR, max_length=10)

    enter_smk = models.CharField('Keinginan Siapa Masuk SMK', max_length=25, null=True, choices=choices.ENTER_SMK_CHOICES)
    charity = models.CharField('Dana Sukarela', max_length=20, null=True, choices=choices.CHARITY_AMOUNT, help_text="Dana Sukarela nantinya akan dimanfaatkan untuk pengembangan siswa dibidang non akademik (kompetisi dan perlombaan-perlombaan).")
    way_in = models.CharField('Jalur Masuk', max_length=20, null=True, choices=choices.JALUR_MASUK)
    color_blind = models.CharField('Buta Warna', max_length=2, default='N', choices=choices.COLOR_BLIND, help_text="Apakah anda buta warna?")

    class Meta:
        ordering = ['participant']

    def __str__(self):
        return f'{self.participant} - {self.first_major}'

    @property
    def is_data_verified(self):
        return self.verified

class ProfileParent(models.Model):
    """
    Creating abstract models, so this models (field) can be use multiple time (inheritance).
    https://docs.djangoproject.com/en/3.1/topics/db/models/#abstract-base-classes
    """
    verified = models.BooleanField('Verifikasi', default=False, db_index=True)
    participant = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField('Nama Lengkap', max_length=120, db_index=True)
    city_born = models.CharField('Kota/Kabupaten Kelahiran', max_length=120, help_text="Contoh pengisian tempat lahir: Kab bandung")
    date_born = models.DateField('Tanggal Lahir', null=True)
    nik = models.CharField('Nomor Induk Kependudukan (NIK)',max_length=20, null=True, help_text="Diisi berdasarkan Kartu Keluarga")
    education = models.CharField(f'Pendidikan Terakhir', max_length=4, choices=choices.EDUCATION_LEVEL)
    job = models.CharField(f'Pekerjaan', max_length=100, null=True)
    salary = models.PositiveIntegerField(f'Penghasilan', null=True, help_text="Diisi dengan angka")
    email = models.EmailField(f'Email', null=True, blank=True)
    phone = models.CharField(f'No. HP', null=True, max_length=15, db_index=True)

    class Meta:
        ordering = ['participant']

    def __str__(self):
        return self.full_name

    @property
    def is_data_verified(self):
        return self.verified

    class Meta:
        abstract = True

class FatherStudentProfile(ProfileParent):
    pass

class MotherStudentProfile(ProfileParent):
    pass

class StudentGuardianProfile(ProfileParent):
    pass
