import datetime
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from . import models, forms_layout

DATE_BORN = forms.DateField(label='Tanggal Lahir',initial=datetime.date.today, widget=forms.DateInput(format="%d/%m/%Y"),
                                help_text="Format: <em>DD/MM/YYYY</em>", input_formats=["%d/%m/%Y"])

SUBMIT_BUTTON = Submit('submit', 'Submit', css_class="ml-3 mb-0")

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


class ParticipantPaymentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = forms_layout.PAYMENT_FORM_LAYOUT

    class Meta:
        model = models.PaymentUpload
        exclude = ['participant', 'verified', 'created_at', 'updated_at']
