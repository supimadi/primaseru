from django import forms

from crispy_forms.helper import FormHelper

from .models import Participant, REPRESENTATIVE_CHOICES
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
