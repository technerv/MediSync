from django.contrib import admin
from .models import Appointment

# admin.site.register(Appointment)
@admin.register(Appointment)
class AppointmentModelAdmin(admin.ModelAdmin):
    list_display = ('patient', 'appointment_date_time', 'assigned_doctor', 'status', 'reason', 'date_created', 'date_changed', 'fee', 'order_bill_ID')
