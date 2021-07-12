from crispy_forms.layout import Layout, Div, Row, Field, Submit
from crispy_forms.bootstrap import PrependedText, FieldWithButtons

from participant_profile import forms_layout as forms_layout_participant

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
    Row(
        Div(Field('full_name'), css_class="col-md-4"),
        Div(Field('registration_number'), css_class="col-md-4"),
        Div(Field('participant_phone_number'), css_class="col-md-4"),
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
