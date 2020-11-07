from django.contrib import admin
from .models import DoctorProfile,PatientDocConfig
admin.site.register(DoctorProfile)
admin.site.register(PatientDocConfig)