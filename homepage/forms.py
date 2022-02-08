from django import forms
from django.contrib.auth.forms import UserCreationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Div, Field

from users.models import CustomUser
from dashboard.models import Participant, InfoSourcePPDB

from .models import ProsTelkomBandung, TestimonialModel  


class TestiModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

    class Meta:
        model = TestimonialModel
        exclude = ["video_id", ]

class ProsTelkomBandungForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

    class Meta:
        model = ProsTelkomBandung
        fields = '__all__'

class UserRegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.disable_csrf = True
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Div('password1', css_class='col-12 col-md-6 input-group'),
                Div('password2', css_class='col-12 col-md-6 input-group'),
            )
        )

    class Meta:
        model = CustomUser
        fields = ['password1', 'password2']

class ParticipantRegisterForm(forms.ModelForm):
    full_name = forms.CharField(label='Nama Lengkap', help_text='Isi sesuai dengan akta kelahiran')
    previous_school = forms.CharField(label='Asal Sekolah', help_text="Harus sesuai dengan data yang muncul (ketika mengetik nama sekolah).")

    participant_phone_number = forms.CharField(label='No. HP atau WA Calon Siswa', min_length=9)

    parent_full_name = forms.CharField(label='Nama Lengkap Orang Tua')
    parent_phone_number = forms.CharField(label='No. HP Orang Tua/Wali', min_length=9)

    homeroom_teacher_phone_number = forms.CharField(label='No. HP Wali Kelas', help_text='Isi dengan nomor HP wali kelas, kelas 9 di SMP.', min_length=9)
    bk_teacher_phone_number = forms.CharField(label='No. HP Guru BK', help_text='Isi dengan nomor HP BK, kelas 9 di SMP.', required=False, min_length=9)

    info = forms.ModelMultipleChoiceField(label='Info Primaseru (PPDB)', queryset=InfoSourcePPDB.objects.all(), help_text="Pilih dari mana Anda pengetahui Primaseru (boleh lebih dari 1 pilihan).")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.disable_csrf = True
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Div('full_name', css_class='col-12 col-md-6 input-group'),
                Div('participant_phone_number', css_class='col-12 col-md-6 input-group'),
            ),
            Row(
                Div(
                    Div(Field('previous_school', autocomplete="off"), css_class=''),
                    Div(css_class='autocom-box'),
                    css_class="search-input col-12 input-group"
                )
            ),
            Row(
                Div('parent_full_name', css_class='col-12 col-md-6 input-group'),
                Div('parent_phone_number', css_class='col-12 col-md-6 input-group'),
            ),
            Row(
                Div('homeroom_teacher_phone_number', css_class='col-12 col-md-6 input-group'),
                Div('bk_teacher_phone_number', css_class='col-12 col-md-6 input-group'),
            ),
            Row(
                Div(Field('info', css_class="custom-select custom-select"), css_class="col-md-12"),
            ),
        )

    class Meta:
        model = Participant
        exclude = ['account', 'registration_number', 'verified', 'updated_at', 'created_at']
