import datetime
from django import forms
from django.contrib.auth.forms import SetPasswordForm

from crispy_forms.helper import FormHelper

from .models import Participant, RegisterSchedule, RegisterStep, ParticipantGraduation, REPRESENTATIVE_CHOICES
from . import forms_layout

from participant_profile import models as participant_models


class SetPasswordDashboardForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = forms_layout.SET_PASSWORD_LAYOUT

class ParticipantGraduationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = forms_layout.GRADUATION_FORM_DASHBOARD

    class Meta:
        model = ParticipantGraduation
        exclude = ['participant']

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

class RegisterStudentFormDashboard(forms.ModelForm):
    representative = forms.ChoiceField(choices=REPRESENTATIVE_CHOICES, label="")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = forms_layout.REGISTER_STUDENT_LAYOUT_DASHBOARD

    class Meta:
        model = Participant
        exclude = ['account']


class RegisterScheduleForm(forms.ModelForm):
    start_date = forms.DateField(label='Tanggal Mulai',initial=datetime.date.today, widget=forms.DateInput(format="%d/%m/%Y"),
                                 help_text="Format: <em>DD/MM/YYYY</em>", input_formats=["%d/%m/%Y"])
    end_date = forms.DateField(label='Tanggal Berakhir',initial=datetime.date.today, widget=forms.DateInput(format="%d/%m/%Y"),
                               help_text="Format: <em>DD/MM/YYYY</em>", input_formats=["%d/%m/%Y"])
    class Meta:
        model = RegisterSchedule
        fields = '__all__'

class RegisterStepForm(forms.ModelForm):
    class Meta:
        model = RegisterStep
        fields = '__all__'

class ParticipantProfileDashboardForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = forms_layout.PARTICIPANT_PROFILE_LAYOUT_DASHBOARD

    class Meta:
        model = participant_models.ParticipantProfile
        exclude = ['participant']

class ParticipantMajorDashboard(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = forms_layout.MAJOR_FORM_DASHBOARD

    class Meta:
        model = participant_models.MajorStudent
        exclude = ['participant']

class ParticipantParentProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = forms_layout.PARENT_FORM_LAYOUT_DASHBOARD

class FatherParticipantDashboardForm(ParticipantParentProfileForm):
    class Meta:
        model = participant_models.FatherStudentProfile
        exclude = ['participant']

class MotherParticipantDashboardForm(ParticipantParentProfileForm):
    class Meta:
        model = participant_models.MotherStudentProfile
        exclude = ['participant']

class GuardianParticipantDashboardForm(ParticipantParentProfileForm):
   class Meta:
       model = participant_models.StudentGuardianProfile
       exclude = ['participant']

class ParticipantFilesDashboardForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = forms_layout.FILES_FORM_DASHBOARD

    class Meta:
        model = participant_models.StudentFile
        exclude = ['participant', 'created_at', 'updated_at']
