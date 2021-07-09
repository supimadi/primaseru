import datetime
from django import forms

from crispy_forms.helper import FormHelper

from .models import Participant, RegisterSchedule, REPRESENTATIVE_CHOICES
from . import forms_layout

class RegisterStudentForm(forms.ModelForm):

    representative = forms.ChoiceField(choices=REPRESENTATIVE_CHOICES, label="")
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = forms_layout.REGISTER_STUDENT_LAYOUT

    class Meta:
        model = Participant
        exclude = ['account', 'registration_number']

class RegisterScheduleForm(forms.ModelForm):
    start_date = forms.DateField(label='Tanggal Mulai',initial=datetime.date.today, widget=forms.DateInput(format="%d/%m/%Y"),
                                 help_text="Format: <em>DD/MM/YYYY</em>", input_formats=["%d/%m/%Y"])

    end_date = forms.DateField(label='Tanggal Berakhir',initial=datetime.date.today, widget=forms.DateInput(format="%d/%m/%Y"),
                               help_text="Format: <em>DD/MM/YYYY</em>", input_formats=["%d/%m/%Y"])
    class Meta:
        model = RegisterSchedule
        fields = '__all__'
