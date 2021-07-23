from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from participant_profile import choices, forms_layout
from . import forms_layout

DATE_BORN = forms.DateField(label='Tanggal Lahir', widget=forms.DateInput(format="%d/%m/%Y"),
                                help_text="Format: <em>DD/MM/YYYY</em>", input_formats=["%d/%m/%Y"])

class ParticipantProfileForm(forms.Form):
    step = forms.CharField(widget=forms.HiddenInput)
    model = forms.CharField(widget=forms.HiddenInput, initial='ParticipantProfile')
    sex = forms.ChoiceField(label='Jenis Kelamin', choices=choices.SEX)
    religion = forms.ChoiceField(label='Agama', choices=choices.RELIGION)
    city_born = forms.CharField(label='Kota Tempat Lahir', max_length=100, help_text='Contoh: Kabupaten Bandung')
    date_born = forms.DateField(label='Tanggal Lahir', widget=forms.DateInput)
    school_origin = forms.CharField(label='Asal Sekolah', help_text="Isilah sesuai dengan asal sekolah Anda dan dituliskan seperti contoh berikut : SMP Telkom Bandung ")
    npsn_school_origin = forms.IntegerField(label='Nomor NPSN Sekolah Asal', help_text="Jika tidak tahu nomor NPSN sekolah, bisa cek <a href='https://referensi.data.kemdikbud.go.id/index11.php' target='_blank'><b>Disini</b></a>")
    social_media = forms.CharField(label='Alamat Sosial Media', max_length=50, help_text='Seperti Instagram atau FB')
    achievement = forms.CharField(label='Penghargaan', widget=forms.Textarea, required=False, help_text='Contoh: Juara 1 Lomba Basket Tingkat Nasional')
    nisn = forms.IntegerField(label='NISN', help_text='Isi NISN berdasarkan NISN yang diberikan sewaktu SMP.')
    nik = forms.IntegerField(label='Nomor Induk Kependudukan (NIK)', help_text='Bisa dicek di Kartu Keluarga')
    kk_number = forms.IntegerField(label='Nomor Kartu Keluarga (KK)', help_text='Diisi berdasarkan Kartu Keluarga')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = forms_layout.PARTICIPANT_PROFILE_FORM_LAYOUT

class ParticipantAddressForm(forms.Form):
    step = forms.CharField(widget=forms.HiddenInput)
    model = forms.CharField(widget=forms.HiddenInput, initial='ParticipantProfile')
    resident = forms.CharField(label='Tempat Tinggal', max_length=50, help_text='Contoh: Rumah Pribadi, Kost, Rumah Keluarga (Keluarga Besar)')
    transport = forms.CharField(label='Alat Transportasi', max_length=50, help_text="Contoh: Jalan Kaki, Motor, Ojek Online, Sepeda, Mobil, Angkot.")
    city = forms.CharField(label='Kota', max_length=120, help_text='Contoh: Kota Bandung')
    kecamatan = forms.CharField(label='Kecamatan', max_length=120, help_text='Contoh: Kecamatan Dayeuhkolot')
    dusun = forms.CharField(label='Dusun', max_length=120, help_text='Jika tidak tahu diisi dengan -')
    kelurahan = forms.CharField(label='Kelurahan', max_length=120, help_text='Contoh: Desa Cieteureup')
    rt_rw = forms.CharField(label='RT/RW', max_length=8, help_text='Contoh: 006/002')
    real_address = forms.CharField(label='Alamat Sekarang', help_text='Contoh: Jalan Bojongsoang')
    kk_address = forms.CharField(label='Alamat Kartu Keluarga (KK)', help_text='Contoh: Jalan Radio Palasari')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = forms_layout.PARTICIPANT_ADDRESS_LAYOUT

class ParticipantMedicalRecord(forms.Form):
    step = forms.CharField(widget=forms.HiddenInput)
    model = forms.CharField(widget=forms.HiddenInput, initial='ParticipantProfile')
    medic_record = forms.CharField(label='Riwayat Kesehatan', required=False, help_text="Jika pernah mempunyai penyakit, silahkan ditulis disini")
    blood_type = forms.ChoiceField(label='Golongan Darah', choices=choices.BLOOD_TYPE)
    in_medicine = forms.CharField(label='Dalam Pengobatan', max_length=120, required=False)
    private_doctor = forms.CharField(label='Nama Dokter Keluarga', max_length=120, required=False, help_text="Jika kamu mempunyai dokter keluarga, silahkan input     disini")
    phone_doctor = forms.CharField(label='No Telepon Dokter', max_length=15, required=False, help_text="Isi jika memiliki dokter keluarga dan atau dalam masa pen    yambuhan penyakit")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = forms_layout.PARTICIPANT_MEDIC_LAYOUT

class ParticipantParentProfileForm(forms.Form):
    step = forms.CharField(widget=forms.HiddenInput)
    model = forms.CharField(widget=forms.HiddenInput)
    full_name = forms.CharField(label='Nama Lengkap', max_length=120)
    city_born = forms.CharField(label='Kota/Kabupaten Kelahiran', max_length=120, help_text="Contoh pengisian tempat lahir: Kab bandung")
    date_born = forms.DateField(label='Tanggal Lahir', widget=forms.DateInput)
    nik = forms.IntegerField(label='Nomor Induk Kependudukan (NIK)', help_text="Diisi berdasarkan Kartu Keluarga")
    education = forms.ChoiceField(label='Pendidikan Terakhir', choices=choices.EDUCATION_LEVEL)
    job = forms.CharField(label='Pekerjaan', max_length=100, required=False)
    salary = forms.IntegerField(label='Penghasilan', required=False, help_text="Diisi dengan angka, 0 berarti kosong.", initial=0)
    email = forms.EmailField(label='Email', required=False)
    phone = forms.CharField(label='No. HP', max_length=15)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = forms_layout.PARENT_PROFILE_LAYOUT

class MajorParticipantForm(forms.Form):
    step = forms.CharField(widget=forms.HiddenInput)
    model = forms.CharField(widget=forms.HiddenInput)
    first_major = forms.ChoiceField(label='Pilihan Jurusan Pertama', choices=choices.MAJOR)
    second_major = forms.ChoiceField(label='Pilihan Jurusan Kedua', choices=choices.MAJOR)
    info = forms.ChoiceField(label='Info Primaseru (PPDB)', choices=choices.INFORMATION_PRIMASERU)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = forms_layout.MAJOR_FORM

class PhotoProfile(forms.Form):
    step = forms.CharField(widget=forms.HiddenInput)
    model = forms.CharField(widget=forms.HiddenInput)
    image = forms.ImageField(label='Photo')
