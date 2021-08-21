from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="profile"),
    path('id-card/', views.id_card, name="id-card"),
    path('files-upload/', views.upload_files, name="files-upload"),
    path('skl/', views.skl_view, name="skl"),
    path('photo-profile/', views.set_photo_profile, name="set-photo-profile"),
    # path('initial/', views.InitialFormView.as_view(), name="initial-form"),
    # path('initial/photo', views.initial_photo, name="initial-photo"),

    path('major/', views.MajorParticipantView.as_view(), name="participant-major"),
    path('participant/', views.ParticipantProfileView.as_view(), name="participant-profile"),
    path('ayah/', views.FatherProfileView.as_view(), name="participant-father"),
    path('ibu/', views.MotherProfileView.as_view(), name="participant-mother"),
    path('wali/', views.GuardianProfileView.as_view(), name="participant-guardian"),
    path('kk/', views.ParticipantKKView.as_view(), name="participant-kk"),
    path('pembayaran-daftar-ulang', views.RePaymentPage.as_view(), name="participant-payment"),

    path('lms/', views.ParticipantLMSAccount.as_view(), name="participant-lms"),
    path('graduation/', views.ParticipantGraduationView.as_view(), name="participant-graduation"),
]
