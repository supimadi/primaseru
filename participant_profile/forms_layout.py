from crispy_forms.layout import Layout, Fieldset, Row, Div, HTML, Field
from crispy_forms.bootstrap import TabHolder, Tab, Accordion, AccordionGroup


FIELDSET_CLASS = "border p-3 rounded m-3 border-primary"


PARTICIPANT_PROFILE_FORM_LAYOUT = Layout(
    Fieldset("Data Diri",
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
        ),
        css_class=FIELDSET_CLASS
    ),

    Fieldset("Alamat",
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
        css_class=FIELDSET_CLASS
    ),

    Fieldset('Catatan Kesehatan',
        Row(
            Div(Field("blood_type", css_class='custom-select custom-select-sm'), css_class="col-sm-6"),
            Div(Field("in_medicine", css_class='custom-select custom-select-sm'), css_class="col-sm-6"),
        ),
        Row(
            Div(Field("private_doctor", css_class='form-control-sm'), css_class="col-sm-6"),
            Div(Field("phone_doctor", css_class='form-control-sm'), css_class="col-sm-6"),
        ),
        Row(
            Div(Field('medic_record', css_class='form-control-sm  auto-size'), css_class="col-sm-12"),
        ),
        css_class=FIELDSET_CLASS
    )
)

PARENT_FORM_LAYOUT = Layout(
    Fieldset('Data Pribadi',
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
        css_class=FIELDSET_CLASS
    )
)


FILE_FORM_LAYOUT = Layout(
    Fieldset("Berkas",
        Row(
            Div('ra_sem_1', css_class='col-md-12')
        ),
        Row(
            Div('ra_sem_2', css_class='col-md-12')
        ),
        Row(
            Div('ra_sem_3', css_class='col-md-12')
        ),
        Row(
            Div('ra_sem_4', css_class='col-md-12')
        ),
        Row(
            Div('ra_sem_5', css_class='col-md-12')
        ),
        Row(
            Div('color_blind_cert', css_class='col-md-12')
        ),
        Row(
            Div('healty_cert', css_class='col-md-12')
        ),
        css_class=FIELDSET_CLASS
    )

)

MAJOR_FORM_LAYOUT = Layout(
    Fieldset("Pilihan Jurusan",
        Field('first_major', css_class="custom-select custom-select-sm"),
        Field('second_major', css_class="custom-select custom-select-sm"),
        Field('info', css_class="custom-select custom-select-sm"),
        css_class=FIELDSET_CLASS
    )
)