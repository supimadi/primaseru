from crispy_forms.layout import Layout, Fieldset, Row, Div, Field, Submit
from crispy_forms.bootstrap import TabHolder, Tab, Accordion, AccordionGroup


# LAYOUT FORMS FOR INITIAL FORM
PARTICIPANT_PROFILE_FORM_LAYOUT = Layout(
    Div(
        'step',
        'model',
        Row(
            Div(Field("sex", css_class='custom-select custom-select-sm'), css_class="col-sm-6"),
            Div(Field('religion', css_class='custom-select custom-select-sm'), css_class="col-sm-6"),
        ),
        Row(
            Div(Field("social_media", css_class='form-control-sm'), css_class="col-sm-12"),
        ),
        Row(
            Div(Field("city_born", css_class='form-control-sm'), css_class="col-sm-6"),
            Div(Field('date_born', type="date", css_class='form-control-sm'), css_class="col-sm-6"),
        ),
        Row(
            Div(Field('school_origin', css_class='form-control-sm'), css_class="col-sm-6"),
            Div(Field("npsn_school_origin", css_class='form-control-sm'), css_class="col-sm-6"),
        ),
        Row(
            Div(Field('nisn', css_class='form-control-sm'), css_class="col-sm-12"),
        ),
        Row(
            Div(Field("nik", css_class='form-control-sm'), css_class="col-sm-6"),
            Div(Field('kk_number', css_class='form-control-sm'), css_class="col-sm-6"),
        ),
        Row(
            Div(Field('achievement', css_class='form-control-sm'), css_class="col-sm-12"),
        )#, css_class="border rounded pt-3 px-3",
    ),
)

PARTICIPANT_ADDRESS_LAYOUT = Layout(
    Div(
        'step',
        'model',
        Row(
            Div(Field("resident", css_class='form-control-sm'), css_class="col-sm-6"),
            Div(Field('transport', css_class='form-control-sm'), css_class="col-sm-6"),
        ),
        Row(
            Div(Field('city', css_class='form-control-sm'), css_class="col-sm-6"),
            Div(Field("kecamatan", css_class='form-control-sm'), css_class="col-sm-6"),
        ),
        Row(
            Div(Field("dusun", css_class='form-control-sm'), css_class="col-sm-4"),
            Div(Field("kelurahan", css_class='form-control-sm'), css_class="col-sm-4"),
            Div(Field("rt_rw", css_class='form-control-sm'), css_class="col-sm-4"),
        ),
        Row(
            Div(Field("kk_address", css_class='form-control-sm'), css_class="col-sm-6"),
            Div(Field("real_address", css_class='form-control-sm'), css_class="col-sm-6"),
        ),
    ),
)

PARTICIPANT_MEDIC_LAYOUT = Layout(
    Div(
        'step',
        'model',
        Row(
            Div(Field("blood_type", css_class='custom-select custom-select-sm'), css_class="col-sm-6"),
            Div(Field("in_medicine", css_class='form-control-sm'), css_class="col-sm-6"),
        ),
        Row(
            Div(Field("private_doctor", css_class='form-control-sm'), css_class="col-sm-6"),
            Div(Field("phone_doctor", css_class='form-control-sm'), css_class="col-sm-6"),
        ),
        Row(
            Div(Field('medic_record', css_class='form-control-sm  auto-size'), css_class="col-sm-12"),
        ),
    )
)

PARENT_PROFILE_LAYOUT = Layout(
    Div(
        'step',
        'model',
        Row(
            Div(Field('full_name', css_class='form-control-sm'), css_class="col-sm-12"),
        ),
        Row(
            Div(Field('city_born', css_class='form-control-sm'), css_class="col-sm-6"),
            Div(Field('date_born', css_class='form-control-sm'), css_class="col-sm-6"),
        ),
        Row(
            Div(Field('nik', css_class='form-control-sm'), css_class="col-sm-6"),
            Div(Field('education', css_class='custom-select custom-select-sm'), css_class="col-sm-6"),
        ),
        Row(
            Div(Field('job', css_class='form-control-sm'), css_class="col-sm-6"),
            Div(Field('salary', css_class='form-control-sm'), css_class="col-sm-6"),
        ),
        Row(
            Div(Field('email', css_class='form-control-sm'), css_class="col-sm-6"),
            Div(Field('phone', css_class='form-control-sm'), css_class="col-sm-6"),
        ),
    )
)

MAJOR_FORM = Layout(
    Div(
        'step',
        'model',
        Field('first_major', css_class="custom-select custom-select-sm"),
        Field('second_major', css_class="custom-select custom-select-sm"),
        Field('info', css_class="custom-select custom-select-sm"),
        Field('charity', css_class="custom-select custom-select-sm"),
    )
)
