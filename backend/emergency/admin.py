from django.contrib import admin
from .models import EmergencyContact, EmergencyCase, AmbulanceRequest

@admin.register(EmergencyContact)
class EmergencyContactModelAdmin(admin.ModelAdmin):
    list_display = ('patient', 'name', 'relationship', 'phone_number')

@admin.register(EmergencyCase)
class EmergencyCaseModelAdmin(admin.ModelAdmin):
    list_display = ('patient', 'created_by', 'date_created', 'description', 'status')

@admin.register(AmbulanceRequest)
class AmbulanceRequestModelAdmin(admin.ModelAdmin):
    list_display = ('patient', 'request_time', 'pickup_location', 'destination', 'status')

# admin.site.register(EmergencyContact)
# admin.site.register(EmergencyCase)
# admin.site.register(AmbulanceRequest)