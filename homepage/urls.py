from django.urls import path
from . import views
from . import fetch

urlpatterns = [
    path('', views.home, name="homepage"),
    path('register/', views.register, name="register"),
    path('downloads/', views.download_menu, name="files-download"),
    path('fetch/school/<str:school>', fetch.fetch_school_list, name="fetch-school"),
]
