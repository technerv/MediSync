from django.contrib import admin
from .models import Doctor, DoctorAvailability


@admin.register(Doctor)
class DoctorModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'phone', 'email', 'specialization', 'date_joined')

@admin.register(DoctorAvailability)
class DoctorAvailabilityModelAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'day_of_week', 'start_time', 'end_time')
# admin.site.register(Doctor)
# admin.site.register(DoctorAvailability)