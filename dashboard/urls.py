from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('add-participant/', views.insert_participant, name="insert-participant"),
    path('export/', views.ExportToExcel.as_view(), name="export"),
    path('analytic/', views.analytic_view, name="analytic"),
    path('export/files/<int:pk>/', views.files_download, name="export-files"),
    path('reg-num/', views.get_register_number, name="register-number"),
    path('reg-num/reset', views.reset_registration_number, name="register-number-reset"),
    path('delete-participant/<int:pk>', views.ParticipantDeleteView.as_view(), name="delete-participant"),

    path('export/participant/', views.ExExcelParticipant.as_view(), name="export-participant"),
    path('export/ayah/', views.ExExcelFather.as_view(), name="export-father"),
    path('export/ibu/', views.ExExcelMother.as_view(), name="export-mother"),
    path('export/wali/', views.ExExcelGuardian.as_view(), name="export-guardian"),
    path('export/jurusan/', views.ExExcelMajor.as_view(), name="export-major"),

    path('info/ppdb/', views.InfoSourcePPDBView.as_view(), name='info-ppdb'),
    path('info/ppdb/insert/', views.InfoSourcePPDBCreate.as_view(), name='info-ppdb-create'),
    path('info/ppdb/delete/<int:pk>/', views.InfoSourcePPDBDelete.as_view(), name='info-ppdb-delete'),
    path('info/ppdb/update/<int:pk>/', views.InfoSourcePPDBUpdate.as_view(), name='info-ppdb-update'),

    path('jadwal/pendaftaran/', views.RegisterScheduleListView.as_view(), name='register-schedule'),
    path('jadwal/pendaftaran/insert/', views.RegisterScheduleCreateView.as_view(), name='register-schedule-create'),
    path('jadwal/pendaftaran/delete/<int:pk>/', views.RegisterSchduleDeleteView.as_view(), name='register-schedule-delete'),
    path('jadwal/pendaftaran/update/<int:pk>/', views.RegisterSchduleUpdateView.as_view(), name='register-schedule-update'),

    path('langkah/pendaftaran/', views.RegisterStepListView.as_view(), name='register-step'),
    path('langkah/pendaftaran/insert/', views.RegisterStepCreateView.as_view(), name='register-step-create'),
    path('langkah/pendaftaran/delete/<int:pk>', views.RegisterStepDeleteView.as_view(), name='register-step-delete'),
    path('langkah/pendaftaran/update/<int:pk>', views.RegisterStepUpdateView.as_view(), name='register-step-update'),

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
