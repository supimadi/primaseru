import datetime
from django import forms
from django.core.exceptions import ValidationError

from crispy_forms.helper import FormHelper

from .models import (
    Participant, RegisterSchedule, RegisterStep,
    ParticipantGraduation, REPRESENTATIVE_CHOICES, ParticipantLMS,
    ParticipantRePayment, InfoSourcePPDB, PaymentBanner
    )
from . import forms_layout

from homepage.models import FilesPool

from participant_profile import models as participant_models
from participant_profile.choices import INFORMATION_PRIMASERU


class PaymentBannerForm(forms.ModelForm):
    class Meta:
        model = PaymentBanner
        fields = '__all__'

class InfoSourcePPDBForm(forms.ModelForm):
    class Meta:
        model = InfoSourcePPDB
        fields = ['info_source']

class FilesPoolForm(forms.ModelForm):
    class Meta:
        model = FilesPool
        fields = '__all__'

class SetPasswordDashboardForm(forms.Form):
    password1 = forms.CharField(max_length=120, widget=forms.PasswordInput, label="Password Baru")
    password2 = forms.CharField(max_length=120, widget=forms.PasswordInput, label="Konfirmasi Password Baru")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = forms_layout.SET_PASSWORD_LAYOUT

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2:
            # Only do something if both fields are valid so far.
            if not password1 == password2:
                raise ValidationError(
                    "Password tidak sama. "
                )


class ParticipantGraduationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = forms_layout.GRADUATION_FORM_DASHBOARD

    class Meta:
        model = ParticipantGraduation
        exclude = ['participant', 'updated_at']

class RegisterStudentForm(forms.ModelForm):
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

class ParticipantLMSAccountForm(forms.ModelForm):

    schedule = forms.DateField(help_text="Tanggal dimulai ujian.", label="Tanggal")
    time = forms.CharField(help_text="Pukul saat ujian dimulai.", label="Pukul")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = forms_layout.LMS_FORM_LAYOUT

    class Meta:
        model = ParticipantLMS
        exclude = ['participant']

class ParticipantPaymentDashboardForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = forms_layout.PAYMENT_FORM_DASHBOARD_LAYOUT

    class Meta:
        model = participant_models.PaymentUpload
        exclude = ['participant', 'created_at', 'updated_at']

class ParticipantRePaymentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = forms_layout.RE_PAYMENT_DASHBOARD_FORM

    class Meta:
        model = ParticipantRePayment
        exclude = ['participant', 'created_at', 'updated_at']

class ParticipantFamilyCertForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = forms_layout.FAMILY_CERT_DASHBOARD_FORM

    class Meta:
        model = participant_models.ParticipantFamilyCert
        fields = ['verified', 'family_cert', 'birth_cert']

class RaportFileDashboardForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = forms_layout.RAPORT_DASHBOARD_FORM

    class Meta:
        model = participant_models.ReportFileParticipant
        exclude = ['participant', 'verified']

class RaportFileVerifyForm(forms.ModelForm):
    verified = forms.BooleanField(label="")
    class Meta:
        model = participant_models.ReportFileParticipant
        fields = ['verified']
