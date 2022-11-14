from crispy_forms.layout import Layout, Div, Row, Field, Submit, Fieldset, HTML, Button
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
    ),
    Row(
        Div(
            Div(Field('previous_school', autocomplete="off"), css_class='col-12 p-0'),
            Div(css_class='autocom-box'),
            css_class="search-input col-12 input-group"
        )
    ),
    Row(
        Div(Field('parent_full_name'), css_class="col-md-6"),
        Div(Field('parent_phone_number'), css_class="col-md-6"),
        # Div(FieldWithButtons('parent_phone_number', Field('representative')), css_class="col-md-12"),
    ),
    Row(
        Div(Field('homeroom_teacher_phone_number', place_holder='Boleh Dikosongkan'), css_class="col-md-6"),
        Div(Field('bk_teacher_phone_number', place_holder='Boleh Dikosongkan'), css_class="col-md-6"),
    ),
    Row(
        Div(Field('info', css_class="custom-select custom-select"), css_class="col-md-12"),
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
            Div(
                Div(Field('previous_school', autocomplete="off"), css_class='col-12 p-0'),
                Div(css_class='autocom-box'),
                css_class="search-input col-12 input-group"
            )
        ),
        Row(
            Div(Field('parent_phone_number'), css_class="col-md-6"),
            Div(Field('parent_full_name'), css_class="col-md-6"),
            # Div(FieldWithButtons('parent_phone_number', Field('representative')), css_class="col-md-12"),
        ),
        Row(
            Div(Field('homeroom_teacher_phone_number', place_holder='Boleh Dikosongkan'), css_class="col-md-6"),
            Div(Field('bk_teacher_phone_number', place_holder='Boleh Dikosongkan'), css_class="col-md-6"),
        ),
        Row(
            Div('info', css_class="col-md-12"),
        ),
        Row(
            Div(Field('status'), css_class="col-md-12"),
            Div(Field('reason_resign'), css_class="col-md-12"),
            Div(Field('verified'), css_class="col-md-12"),
        ),
        Row(
            Div(
                Submit('submit', 'Submit'),
                HTML('<button type="button" id="generate-registration" class="btn btn-danger">Buat No. Pendaftaran</button>'),
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
        'date_announce',
        'clock_announce',
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

FAMILY_CERT_DASHBOARD_FORM = Layout(
    Fieldset('KK dan Akta Kelahiran',
        Div(
            'family_cert',
            'birth_cert',
        ),
        css_class=" rounded border border-primary p-3 m-3"
    ),
    Row(
        Div('verified',
            Submit('submit', 'Submit'),
            css_class="col-sm-6"
            ), css_class="mx-3"
    ),
)

RE_PAYMENT_DASHBOARD_FORM = Layout(
    Fieldset('Pembayaran Daftar Ulang',
        Row(Div('paid_off', css_class="col-12"), css_class="px-3"),
        Row(Div('virt_acc_number', css_class="col-12"), css_class="pb-3 px-3"),
        Row(Div('whom_acc', css_class="col-12"), css_class="pb-3 px-3"),
        Row(
            Div('payment_1', css_class="col-12"),
            Div('comment_1', css_class="col-12"),
            Div('deadline_1', css_class="col-12"),
            Div('pay_mount_1', css_class="col-12"),
            Div('verified_1', css_class="col-12"),
            css_class="border border-dark rounded p-3 mx-3 mb-3"
        ),
        #  Row(
        #      Div('payment_2', css_class="col-12"),
        #      Div('comment_2', css_class="col-12"),
        #      Div('deadline_2', css_class="col-12"),
        #      Div('pay_mount_2', css_class="col-12"),
        #      Div('verified_2', css_class="col-12"),
        #      css_class="border border-dark rounded p-3 mx-3 mb-3"
        #  ),
        #  Row(
        #      Div('payment_3', css_class="col-12"),
        #      Div('comment_3', css_class="col-12"),
        #      Div('deadline_3', css_class="col-12"),
        #      Div('pay_mount_3', css_class="col-12"),
        #      Div('verified_3', css_class="col-12"),
        #      css_class="border border-dark rounded p-3 mx-3 mb-3"
        #  ),
        css_class=" rounded border border-primary p-3 m-3"
    ),
    Div(
        Submit('submit', 'Submit'),
        css_class="mx-3"
    ),
)

RAPORT_DASHBOARD_FORM = Layout(
    Fieldset('Raport',
        Div(
            'raport',
            'semester',
            # 'part',
        ),
        css_class=" rounded border border-primary p-3 m-3"
    ),
    Row(
        Div(
            Submit('submit', 'Submit'),
            css_class="col-sm-6"
            ), css_class="mx-3"
    ),
)

CERT_DASHBOARD_FORM = Layout(
    Fieldset('Raport',
        Div(
            'certificate',
            'certi_name',
        ),
        css_class=" rounded border border-primary p-3 m-3"
    ),
    Row(
        Div(
            Submit('submit', 'Submit'),
            css_class="col-sm-6"
            ), css_class="mx-3"
    ),
)
