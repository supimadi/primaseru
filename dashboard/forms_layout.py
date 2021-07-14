from crispy_forms.layout import Layout, Div, Row, Field, Submit, Fieldset, HTML
from crispy_forms.bootstrap import PrependedText, FieldWithButtons

from participant_profile import forms_layout as forms_layout_participant


SET_PASSWORD_LAYOUT = Layout(
    Fieldset('Ganti Password',
        'password1',
        'password2',
        css_class="border p-3 rounded m-3 border-primary"
    ),
    Div(
        Submit('submit', 'Submit'),
        HTML('<a href="{% url "participant-detail" pk %}" class="btn btn-secondary">Kembali</a>'),
        css_class="ml-3"
    )
)


REGISTER_STUDENT_LAYOUT = Layout(
    Row(
        Div(Field('full_name'), css_class="col-md-6"),
        Div(Field('participant_phone_number'), css_class="col-md-6"),
    ),
    Row(
        Div(Field('password'), css_class="col-md-12"),
        Div(Field('homeroom_teacher_phone_number', place_holder='Boleh Dikosongkan'), css_class="col-md-12"),
    ),
    Row(
        Div(Field('parent_full_name'), css_class="col-md-12"),
        Div(FieldWithButtons('parent_phone_number', Field('representative')), css_class="col-md-12"),
    ),
)

REGISTER_STUDENT_LAYOUT_DASHBOARD = Layout(
    Div(
        Row(
            Div(Field('full_name'), css_class="col-md-4"),
            Div(Field('registration_number'), css_class="col-md-4"),
            Div(Field('participant_phone_number'), css_class="col-md-4"),
        ),
        Row(
            Div(Field('homeroom_teacher_phone_number', place_holder='Boleh Dikosongkan'), css_class="col-md-12"),
        ),
        Row(
            Div(Field('parent_full_name'), css_class="col-md-12"),
            Div(FieldWithButtons('parent_phone_number', Field('representative')), css_class="col-md-12"),
        ),
        Row(
            Div(
                Submit('submit', 'Submit'),
                css_class="col-sm-6"
                ),
        ), css_class="p-3 m-3 border border-primary rounded"
    )

)

PARTICIPANT_PROFILE_LAYOUT_DASHBOARD = Layout(
    forms_layout_participant.PARTICIPANT_PROFILE_FORM_LAYOUT,
    Row(
        Div('verified',
            Submit('submit', 'Submit'),
            css_class="col-sm-6 ml-3"
            ),
    ),
)


PARENT_FORM_LAYOUT_DASHBOARD = Layout(
    forms_layout_participant.PARENT_FORM_LAYOUT,
    Row(
        Div('verified',
            Submit('submit', 'Submit'),
            css_class="col-sm-6 ml-3"
            ),
    ),
)

MAJOR_FORM_DASHBOARD = Layout(
    forms_layout_participant.MAJOR_FORM_LAYOUT,
    Row(
        Div('verified',
            Submit('submit', 'Submit'),
            css_class="col-sm-6 ml-3"
            ),
    ),
)

FILES_FORM_DASHBOARD = Layout(
    forms_layout_participant.FILE_FORM_LAYOUT,
    Row(
        Div(Field('msg'), css_class="col-sm-12"), css_class="mx-3"
    ),
    Row(
        Div('verified',
            Submit('submit', 'Submit'),
            css_class="col-sm-6"
            ), css_class="mx-3"
    ),
)

GRADUATION_FORM_DASHBOARD = Layout(
    Div(
        'letter',
        'passed',
        'chose_major',
        css_class="rounded border border-primary p-3 m-3"
    ),
    Div(
        Submit('submit', 'Submit'),
        css_class="mx-3"
    )
)

LMS_FORM_LAYOUT = Layout(
    Fieldset('Akun Ujian LMS',
        Div(
            'username',
            'password',
            'schedule',
            'time',
        ),
        css_class=" rounded border border-primary p-3 m-3"
    ),
    Div(
        Submit('submit', 'Submit'),
        css_class="mx-3"
    ),
)

PAYMENY_FORM_DASHBOARD_LAYOUT = Layout(
    forms_layout_participant.PAYMENT_FORM_LAYOUT,
    Div(
        # Submit('submit', 'Submit'),
        'verified',
        css_class="mx-3"
    ),
)
