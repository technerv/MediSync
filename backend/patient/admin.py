from django.contrib import admin
from .models import Patient, NextOfKin, Appointment, Service, Triage, Consultation, Prescription, PrescribedDrug, Referral

# admin.site.register(Patient)
@admin.register(Patient)
class PatientModelAdmin(admin.ModelAdmin):
    list_display=('first_name', 'second_name', 'date_of_birth', 'gender', 'phone', 'email', 'insurance')

@admin.register(NextOfKin)
class NextOfKinModelAdmin(admin.ModelAdmin):
    list_display=('patient_id', 'first_name', 'second_name', 'relationship', 'tel_no', 'email_address', 'residence')


@admin.register(Triage)
class TriageModelAdmin(admin.ModelAdmin):
    list_display=('created_by', 'patient_id', 'date_created', 'temperature', 'height', 'weight', 'pulse',
                   'fee', 'notes')


# @admin.register(ContactDetails)
# class ContactDetailsModelAdmin(admin.ModelAdmin):
#     list_display=('tel_no', 'email_address', 'residence')


# admin.site.register(NextOfKin)
# admin.site.register(Appointment)
# admin.site.register(Service)
# admin.site.register(Triage)
# admin.site.register(Consultation)
# admin.site.register(Prescription)
# admin.site.register(PrescribedDrug)
# admin.site.register(Referral)