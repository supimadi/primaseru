from django.test import TestCase

from dashboard import forms, forms_layout, models

from participant_profile import models as participant_models


class SetPasswordDashboardFormTest(TestCase):
    FORM = forms.SetPasswordDashboardForm()

    def test_set_pass_differ_password(self):
        form = forms.SetPasswordDashboardForm(
            data = {
                'password1': "12345",
                'password2': "12342",
            },
        )
        self.assertFalse(form.is_valid())

    def test_form_helper_form_tag(self):
        self.assertFalse(self.FORM.helper.form_tag)

    def test_form_helper_layout(self):
        self.assertEqual(
            self.FORM.helper.layout,
            forms_layout.SET_PASSWORD_LAYOUT
        )

    def test_set_pass1_field_label(self):
        self.assertTrue(
            self.FORM.fields['password1'].label is None or
            self.FORM.fields['password1'].label == "Password Baru"
        )

    def test_set_pass1_field_max_length(self):
        self.assertEqual(
            self.FORM.fields['password1'].max_length, 120
        )

    def test_set_pass2_field_label(self):
        self.assertTrue(
            self.FORM.fields['password2'].label is None or
            self.FORM.fields['password2'].label == "Konfirmasi Password Baru"
        )

    def test_set_pass2_field_max_length(self):
        self.assertEqual(
            self.FORM.fields['password2'].max_length, 120
        )

class ParticipantGraduationFormTest(TestCase):
    FORM = forms.ParticipantGraduationForm()

    def test_form_helper_form_tag(self):
        self.assertFalse(self.FORM.helper.form_tag)

    def test_form_helper_layout(self):
        self.assertEqual(
            self.FORM.helper.layout,
            forms_layout.GRADUATION_FORM_DASHBOARD
        )

    def test_form_exclude_fields(self):
        self.assertEqual(
            self.FORM.Meta.exclude,
            ['participant', 'updated_at']
        )

    # REVIEW: is it needed? pls comment... 
    def test_form_model(self):
        self.assertEqual(
            self.FORM.Meta.model,
            models.ParticipantGraduation
        )

class RegisterStudentFormTest(TestCase):
    FORM = forms.RegisterStudentForm()

    def test_form_helper_form_tag(self):
        self.assertFalse(self.FORM.helper.form_tag)

    def test_form_helper_layout(self):
        self.assertEqual(
            self.FORM.helper.layout,
            forms_layout.REGISTER_STUDENT_LAYOUT
        )

    def test_form_exclude_fields(self):
        self.assertEqual(
            self.FORM.Meta.exclude,
            ['account', 'registration_number', 'updated_at', 'created_at']
        )

    # REVIEW: is it needed? pls comment... 
    def test_form_model(self):
        self.assertEqual(
            self.FORM.Meta.model,
            models.Participant
        )

class RegisterStudentFormDashboardTest(TestCase):
    FORM = forms.RegisterStudentFormDashboard()

    def test_form_helper_form_tag(self):
        self.assertFalse(self.FORM.helper.form_tag)

    def test_form_helper_layout(self):
        self.assertEqual(
            self.FORM.helper.layout,
            forms_layout.REGISTER_STUDENT_LAYOUT_DASHBOARD
        )

    def test_form_exclude_fields(self):
        self.assertEqual(
            self.FORM.Meta.exclude,
            ['account', 'updated_at', 'created_at']
        )

    # REVIEW: is it needed? pls comment... 
    def test_form_model(self):
        self.assertEqual(
            self.FORM.Meta.model,
            models.Participant
        )

class RegisterScheduleFormTest(TestCase):
    FORM = forms.RegisterScheduleForm()

    def test_form_start_date_label(self):
        self.assertEqual(
            self.FORM.fields['start_date'].label,
            'Tanggal Mulai'
        )

    def test_form_start_date_help_text(self):
        self.assertEqual(
            self.FORM.fields['start_date'].help_text,
            'Format: <em>DD/MM/YYYY</em>'
        )

    def test_form_end_date_label(self):
        self.assertEqual(
            self.FORM.fields['end_date'].label,
            'Tanggal Berakhir'
        )

    def test_form_end_date_help_text(self):
        self.assertEqual(
            self.FORM.fields['end_date'].help_text,
            'Format: <em>DD/MM/YYYY</em>'
        )

    def test_form_fields(self):
        self.assertEqual(
            self.FORM.Meta.fields,
            '__all__'
        )

    # REVIEW: is it needed? pls comment... 
    def test_form_model(self):
        self.assertEqual(
            self.FORM.Meta.model,
            models.RegisterSchedule
        )

class ParticipantProfileDashboardFormTest(TestCase):
    FORM = forms.ParticipantProfileDashboardForm()

    def test_form_helper_form_tag(self):
        self.assertFalse(self.FORM.helper.form_tag)

    def test_form_helper_layout(self):
        self.assertEqual(
            self.FORM.helper.layout,
            forms_layout.PARTICIPANT_PROFILE_LAYOUT_DASHBOARD
        )

    def test_form_exclude_fields(self):
        self.assertEqual(
            self.FORM.Meta.exclude,
            ['participant']
        )

    # REVIEW: is it needed? pls comment... 
    def test_form_model(self):
        self.assertEqual(
            self.FORM.Meta.model,
            participant_models.ParticipantProfile
        )

class ParticipantMajorDashboardTest(TestCase):
    FORM = forms.ParticipantMajorDashboard()

    def test_form_helper_form_tag(self):
        self.assertFalse(self.FORM.helper.form_tag)

    def test_form_helper_layout(self):
        self.assertEqual(
            self.FORM.helper.layout,
            forms_layout.MAJOR_FORM_DASHBOARD
        )

    def test_form_exclude_fields(self):
        self.assertEqual(
            self.FORM.Meta.exclude,
            ['participant']
        )

    # REVIEW: is it needed? pls comment... 
    def test_form_model(self):
        self.assertEqual(
            self.FORM.Meta.model,
            participant_models.MajorStudent
        )

class FatherParticipantDashboardForm(TestCase):
    FORM = forms.FatherParticipantDashboardForm()

    def test_form_helper_form_tag(self):
        self.assertFalse(self.FORM.helper.form_tag)

    def test_form_helper_layout(self):
        self.assertEqual(
            self.FORM.helper.layout,
            forms_layout.PARENT_FORM_LAYOUT_DASHBOARD
        )

    def test_form_exclude_fields(self):
        self.assertEqual(
            self.FORM.Meta.exclude,
            ['participant']
        )

    # REVIEW: is it needed? pls comment... 
    def test_form_model(self):
        self.assertEqual(
            self.FORM.Meta.model,
            participant_models.FatherStudentProfile
        )
