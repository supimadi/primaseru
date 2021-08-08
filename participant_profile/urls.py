from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="profile"),
    path('id-card/', views.id_card, name="id-card"),
    path('initial/', views.InitialFormView.as_view(), name="initial-form"),
    path('initial/photo', views.initial_photo, name="initial-photo"),

    path('participant/', views.ProfileView.as_view(), name="ajax-participant"),
    path('father/', views.FatherProfileView.as_view(), name="ajax-father"),
    path('mother/', views.MotherProfileView.as_view(), name="ajax-mother"),
    path('guardian/', views.GuardianProfileView.as_view(), name="ajax-guardian"),
    path('major/', views.MajorParticipantView.as_view(), name="ajax-major"),
    path('files/', views.ParticipantFilesView.as_view(), name="ajax-files"),

    path('lms/', views.ParticipantLMSAccount.as_view(), name="profile-lms"),
    path('graduation/', views.ParticipantGraduationView.as_view(), name="profile-graduation"),
    # path('add-participant/', views.insert_participant, name="insert-participant"),

    # path('j/pendaftaran/insert/', views.RegisterScheduleCreateView.as_view(), name='register-schedule-create'),
#     path('j/pendaftaran/delete/<int:pk>', views.RegisterSchduleDeleteView.as_view(), name='register-schedule-delete'),
#     path('j/pendaftaran/update/<int:pk>', views.RegisterSchduleUpdateView.as_view(), name='register-schedule-update'),
]
