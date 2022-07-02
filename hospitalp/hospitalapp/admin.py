from django.contrib import admin

from hospitalapp.models import Appointment, Doctor, Patient
from .models import Patient,Doctor,Appointment
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)

