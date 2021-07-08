from crispy_forms.layout import Layout, Div, Row, Field
from crispy_forms.bootstrap import PrependedText, FieldWithButtons

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
