from django.contrib import admin

from .models import FatherStudentProfile, StudentFile

# Register your models here.
admin.site.register(FatherStudentProfile)
admin.site.register(StudentFile)
