from django import forms
from django.contrib.auth.forms import UserCreationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Div, Field

from users.models import CustomUser
from dashboard.models import Participant


class UserRegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.disable_csrf = True
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Div('password1', css_class='col-12 col-sm-6 input-group'),
                Div('password2', css_class='col-12 col-sm-6 input-group'),
            )
        )

    class Meta:
        model = CustomUser
        fields = ['password1', 'password2']

class ParticipantRegisterForm(forms.Form):
    full_name = forms.CharField(label='Nama Lengkap', help_text='Isi sesuai dengan akta kelahiran')
    place_born = forms.CharField(label='Tempat Lahir', help_text='Isi sesuai dengan akta kelahiran.')
    date_born = forms.DateField(label='Tanggal Lahir', help_text='Isi sesuai dengan akta kelahiran.')
    school = forms.CharField(label='Asal Sekolah')
    participant_phone_number = forms.CharField(label='No. HP Calon Siswa')
    parent_phone_number = forms.CharField(label='No. HP Orang Tua/Wali')
    homeroom_teacher_phone_number = forms.CharField(label='No. HP Wali Kelas', help_text='Isi dengan nomor hp wali kelas, kelas 9 di SMP.', required=False)
    family_card = forms.FileField(label='Kartu Keluarga')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.disable_csrf = True
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Div('full_name', css_class='col-12 input-group'),
            ),
            Row(
                Div('place_born', css_class='col-12 col-sm-6 input-group'),
                Div('date_born', css_class='col-12 col-sm-6 input-group'),
            ),
            Row(
                Div(
                    Div(Field('school', autocomplete="off"), css_class=''),
                    Div(css_class='autocom-box'),
                    css_class="search-input col-12 input-group"
                )
            ),
            Row(
                Div('participant_phone_number', css_class='col-12 input-group'),
            ),
            Row(
                Div('parent_phone_number', css_class='col-12 input-group'),
            ),
            Row(
                Div('homeroom_teacher_phone_number', css_class='col-12 input-group'),
            ),
            Row(
                Div('family_card', css_class='col-12 input-group'),
            ),
        )
