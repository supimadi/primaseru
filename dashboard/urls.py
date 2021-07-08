from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('add-participant/', views.insert_participant, name="insert_participant"),
]
