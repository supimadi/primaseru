from django import forms
from django.contrib.auth.forms import UserCreationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Div, Field, HTML

from users.models import CustomUser
from dashboard.models import Participant, InfoSourcePPDB

from participant_profile.choices import INFORMATION_PRIMASERU


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

class ParticipantRegisterForm(forms.Form):
    full_name = forms.CharField(label='Nama Lengkap', help_text='Isi sesuai dengan akta kelahiran')
    school = forms.CharField(label='Asal Sekolah', help_text="Harus sesuai dengan data yang muncul (ketika mengetik nama sekolah).")
    participant_phone_number = forms.CharField(label='No. HP atau WA Calon Siswa')
    parent_full_name = forms.CharField(label='Nama Lengkap Orang Tua')
    parent_phone_number = forms.CharField(label='No. HP Orang Tua/Wali')
    homeroom_teacher_phone_number = forms.CharField(label='No. HP Wali Kelas', help_text='Isi dengan nomor HP wali kelas, kelas 9 di SMP.')
    bk_teacher_phone_number = forms.CharField(label='No. HP Guru BK', help_text='Isi dengan nomor HP BK, kelas 9 di SMP.', required=False)
    info = forms.ModelMultipleChoiceField(label='Info Primaseru (PPDB)', queryset=InfoSourcePPDB.objects.all(), help_text="Pilih dari mana Anda pengetahui Primaseru.")

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
                    Div(Field('school', autocomplete="off"), css_class=''),
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
