import datetime
from django import forms
from django.core.validators import FileExtensionValidator

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from . import models, forms_layout

from dashboard.models import ParticipantRePayment, MajorStatus, RegisterSchedule

DATE_BORN = forms.DateField(label='Tanggal Lahir',initial=datetime.date.today, widget=forms.DateInput(format="%d/%m/%Y"),
                                help_text="Format: <em>DD/MM/YYYY</em>", input_formats=["%d/%m/%Y"])

SUBMIT_BUTTON = Submit('submit', 'Submit', css_class="ml-3 mb-0")


class PhotoProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

    class Meta:
        model = models.PhotoProfile
        exclude = ['participant']

class ParticipantProfileForm(forms.ModelForm):
    date_born = DATE_BORN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.add_input(SUBMIT_BUTTON)
        self.helper.layout = forms_layout.PARTICIPANT_PROFILE_FORM_LAYOUT

    class Meta:
        model =  models.ParticipantProfile
        exclude = ['participant', 'verified']

class ParticipantMajorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        MAJOR = MajorStatus.objects.all()
        PATH = RegisterSchedule.objects.all()

        major_avail = [(m.major, m.major_text) for m in MAJOR if m.is_avail] 
        path_avail = [(p.name, p.name) for p in PATH if p.is_avail]

        self.fields['first_major'].choices = major_avail
        self.fields['second_major'].choices = major_avail
        self.fields['way_in'].choices = path_avail

        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.add_input(SUBMIT_BUTTON)
        self.helper.layout = forms_layout.MAJOR_FORM_LAYOUT

    class Meta:
        model = models.MajorStudent
        exclude = ['verified', 'participant']


class ParticipantParentProfileForm(forms.ModelForm):
    date_born = DATE_BORN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.add_input(SUBMIT_BUTTON)
        self.helper.layout = forms_layout.PARENT_FORM_LAYOUT


class FatherParticipantForm(ParticipantParentProfileForm):
    class Meta:
        model = models.FatherStudentProfile
        exclude = ['participant', 'verified']

class MotherParticipantForm(ParticipantParentProfileForm):
    class Meta:
        model = models.MotherStudentProfile
        exclude = ['participant', 'verified']

class GuardianParticipantForm(ParticipantParentProfileForm):
    class Meta:
        model = models.StudentGuardianProfile
        exclude = ['participant', 'verified']


class ParticipantFilesForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_tag = False
        self.helper.add_input(SUBMIT_BUTTON)
        self.helper.layout = forms_layout.FILE_FORM_LAYOUT

    class Meta:
        model = models.StudentFile
        exclude = ['participant', 'verified', 'msg', 'created_at', 'updated_at']

class ParticipantRaportForm(forms.ModelForm):
    raport = forms.FileField(label='Berkas Raport', validators=[FileExtensionValidator(['pdf'])], help_text="Harap meng-unggah hasil scan raport, bukan photo supaya terlihat dengan jelas, dan berformat pdf.")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_tag = False
        self.helper.add_input(SUBMIT_BUTTON)
        self.helper.layout = forms_layout.RAPORT_FORM_LAYOUT

    class Meta:
        model = models.ReportFileParticipant
        exclude = ['participant', 'verified']


class ParticipantKKForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_tag = False
        self.helper.add_input(SUBMIT_BUTTON)
        self.helper.layout = forms_layout.KK_FORM_LAYOUT

    class Meta:
        model = models.ParticipantFamilyCert
        fields = ['family_cert', 'birth_cert']

class ParticipantPaymentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = forms_layout.PAYMENT_FORM_LAYOUT

    class Meta:
        model = models.PaymentUpload
        exclude = ['participant', 'verified', 'created_at', 'updated_at']

class ParticipantRePaymentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.add_input(SUBMIT_BUTTON)
        self.helper.layout = forms_layout.RE_PAYMENT_FORM_LAYOUT

    class Meta:
        model = ParticipantRePayment
        #  fields = ['payment_1', 'payment_2', 'payment_3']
        fields = ['payment_1']

class ParticipantCertForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_tag = False
        self.helper.add_input(SUBMIT_BUTTON)
        self.helper.layout = forms_layout.CERT_FORM_LAYOUT

    class Meta:
        model = models.ParticipantCert
        exclude = ['participant', 'verified']
