from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('add-participant/', views.insert_participant, name="insert-participant"),
    path('export/', views.export_to_excel, name="export"),
    path('analytic/', views.analytic_view, name="analytic"),
    path('export/files/<int:pk>/', views.files_download, name="export-files"),
    path('delete-participant/<int:pk>/', views.ParticipantDeleteView.as_view(), name="delete-participant"),
    path('banner/payment/', views.BannerPayment.as_view(), name="banner-payment"),

    path('cap/', views.school_cap, name="school-cap-chart"),

    path('school-capacity/', views.school_cap_view, name="school-cap"),
    path('school-capacity/update/<int:pk>/', views.school_cap_update, name="school-cap-update"),

    path('major-capacity/create/', views.major_cap_create, name="major-cap-create"),
    path('major-capacity/delete/<int:pk>/', views.MajorCapDeleteView.as_view(), name="major-cap-delete"),
    path('major-capacity/update/<int:pk>/', views.major_cap_update, name="major-cap-update"),

    path('reg-num/', views.get_register_number, name="register-number"),
    path('reg-num/reset/', views.reset_registration_number, name="register-number-reset"),
    path('reg-num/update/', views.RegisterNumberUpdateView.as_view(), name="register-number-update"),

    path('info/ppdb/', views.InfoSourcePPDBView.as_view(), name='info-ppdb'),
    path('info/ppdb/insert/', views.InfoSourcePPDBCreate.as_view(), name='info-ppdb-create'),
    path('info/ppdb/delete/<int:pk>/', views.InfoSourcePPDBDelete.as_view(), name='info-ppdb-delete'),
    path('info/ppdb/update/<int:pk>/', views.InfoSourcePPDBUpdate.as_view(), name='info-ppdb-update'),

    path('files/pool/', views.FilesPoolView.as_view(), name='files-pool'),
    path('files/pool/create/', views.FilesPoolCreateView.as_view(), name='files-pool-create'),
    path('files/pool/update/<int:pk>/', views.FilesPoolUpdateView.as_view(), name='files-pool-update'),
    path('files/pool/delete/<int:pk>/', views.FilesPoolDeleteView.as_view(), name='files-pool-delete'),

    path('files/register/', views.RegisterFileView.as_view(), name='files-register'),
    path('files/register/create/', views.RegisterFileCreateView.as_view(), name='files-register-create'),
    path('files/register/update/<int:pk>/', views.RegisterFileUpdateView.as_view(), name='files-register-update'),
    path('files/register/delete/<int:pk>/', views.RegisterFileDeleteView.as_view(), name='files-register-delete'),

    path('files/re-register/', views.ReRegisterFileView.as_view(), name='files-re-register'),
    path('files/re-register/create/', views.ReRegisterFileCreateView.as_view(), name='files-re-register-create'),
    path('files/re-register/update/<int:pk>/', views.ReRegisterFileUpdateView.as_view(), name='files-re-register-update'),
    path('files/re-register/delete/<int:pk>/', views.ReRegisterFileDeleteView.as_view(), name='files-re-register-delete'),

    path('primaseru/contacts/', views.PrimaseruContactsView.as_view(), name='primaseru-contacts'),
    path('primaseru/contacts/delete/<int:pk>/', views.PrimaseruContactsDeleteView.as_view(), name='primaseru-contacts-delete'),
    path('primaseru/contacts/update/<int:pk>/', views.PrimaseruContactsUpdateView.as_view(), name='primaseru-contacts-update'),
    path('primaseru/contacts/create/', views.PrimaseruContactsCreateView.as_view(), name='primaseru-contacts-create'),

    path('raport/verified/', views.verified_raport, name="verify-raport"),
    path('raport/<int:account>/', views.RaportFilesView.as_view(), name='raport-list'),
    path('raport/<int:account>/create/', views.RaportFileCreate.as_view(), name='raport-create'),
    path('raport/<int:account>/<int:pk>/delete/', views.RaportFileDelete.as_view(), name='raport-delete'),

    path('sertifikat/verified/', views.verified_cert, name="verify-cert"),
    path('sertifikat/<int:account>/', views.CertFilesView.as_view(), name='cert-list'),
    path('sertifikat/<int:account>/create/', views.CertFileCreate.as_view(), name='cert-create'),
    path('sertifikat/<int:account>/<int:pk>/delete/', views.CertFileDelete.as_view(), name='cert-delete'),

    path('jadwal/pendaftaran/', views.RegisterScheduleListView.as_view(), name='register-schedule'),
    path('jadwal/pendaftaran/insert/', views.RegisterScheduleCreateView.as_view(), name='register-schedule-create'),
    path('jadwal/pendaftaran/delete/<int:pk>/', views.RegisterSchduleDeleteView.as_view(), name='register-schedule-delete'),
    path('jadwal/pendaftaran/update/<int:pk>/', views.RegisterSchduleUpdateView.as_view(), name='register-schedule-update'),

    path('langkah/pendaftaran/', views.RegisterStepListView.as_view(), name='register-step'),
    path('langkah/pendaftaran/insert/', views.RegisterStepCreateView.as_view(), name='register-step-create'),
    path('langkah/pendaftaran/delete/<int:pk>/', views.RegisterStepDeleteView.as_view(), name='register-step-delete'),
    path('langkah/pendaftaran/update/<int:pk>/', views.RegisterStepUpdateView.as_view(), name='register-step-update'),

    path('ganti-password/<int:pk>/', views.PasswordChangeViewDashboard.as_view(), name='participant-change-password'),

    path('peserta/<int:pk>/', views.ParticipantUpdateView.as_view(), name='participant-detail'),
    path('peserta/profile/<int:pk>/', views.ParticipantProfileView.as_view(), name='participant-profile'),
    path('peserta/ayah/<int:pk>/', views.ParticipantFatherProfileView.as_view(), name='participant-father'),
    path('peserta/ibu/<int:pk>/', views.ParticipantMotherProfileView.as_view(), name='participant-mother'),
    path('peserta/wali/<int:pk>/', views.ParticipantGuardianProfile.as_view(), name='participant-guardian'),
    path('peserta/berkas/<int:pk>/', views.ParticipantFilesView.as_view(), name='participant-files'),
    path('peserta/kk/<int:pk>/', views.ParticipantFamilyCertView.as_view(), name='participant-family-cert'),
    path('peserta/jurusan/<int:pk>/', views.ParticipantMajorView.as_view(), name='participant-major'),
    path('peserta/kelulusan/<int:pk>/', views.ParticipantGradiationView.as_view(), name='participant-graduation'),
    path('peserta/lms/<int:pk>/', views.ParticipantLMSView.as_view(), name='participant-lms'),
    path('peserta/pembayaran/<int:pk>/', views.RePaymentDView.as_view(), name='participant-payment'),
]
