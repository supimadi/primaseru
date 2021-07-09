from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('add-participant/', views.insert_participant, name="insert-participant"),

    path('j/pendaftaran/', views.RegisterScheduleListView.as_view(), name='register-schedule'),
    path('j/pendaftaran/insert/', views.RegisterScheduleCreateView.as_view(), name='register-schedule-create'),
    path('j/pendaftaran/delete/<int:pk>', views.RegisterSchduleDeleteView.as_view(), name='register-schedule-delete'),
    path('j/pendaftaran/update/<int:pk>', views.RegisterSchduleUpdateView.as_view(), name='register-schedule-update'),
]
