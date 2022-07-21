from django.urls import path
from . import views
from . import fetch

urlpatterns = [
    path('', views.home, name="homepage"),

    path('prestasi/', views.achievements, name="achievements"),
    path('ekskul/', views.school_clubs, name="school_clubs"),
    path('komunitas/', views.school_community, name="school_community"),

    path('register/', views.register, name="register"),
    path('downloads/', views.download_menu, name="files-download"),
    path('fetch/school/<str:school>', fetch.fetch_school_list, name="fetch-school"),
]
