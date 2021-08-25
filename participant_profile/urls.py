from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="profile"),
    path('id-card/', views.id_card, name="id-card"),
    path('skl/', views.skl_view, name="skl"),
    path('photo-profile/', views.set_photo_profile, name="set-photo-profile"),
    # path('initial/', views.InitialFormView.as_view(), name="initial-form"),
    # path('initial/photo', views.initial_photo, name="initial-photo"),

    path('major/', views.MajorParticipantView.as_view(), name="participant-major"),
    path('participant/', views.ParticipantProfileView.as_view(), name="participant-profile"),
    path('ayah/', views.FatherProfileView.as_view(), name="participant-father"),
    path('ibu/', views.MotherProfileView.as_view(), name="participant-mother"),
    path('wali/', views.GuardianProfileView.as_view(), name="participant-guardian"),

    path('pembayaran-daftar-ulang/', views.RePaymentPage.as_view(), name="participant-payment"),
    path('kk/', views.ParticipantKKView.as_view(), name="participant-kk"),
    path('raport/', views.RaportParticipantView.as_view(), name="participant-raport"),
    path('files-upload/delete/<int:pk>', views.ParticipantRaportDeleteView.as_view(), name="participant-raport-delete"),
    path('files-upload/', views.ParticipantFilesView.as_view(), name="participant-files"),

    path('lms/', views.ParticipantLMSAccount.as_view(), name="participant-lms"),
    path('graduation/', views.ParticipantGraduationView.as_view(), name="participant-graduation"),
]
