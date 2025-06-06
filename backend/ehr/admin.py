from django.contrib import admin
from .models import ElectronicHealthRecord, Immunization, LabResult, RadiologyReport, Prescription

# Register your models here
@admin.register(ElectronicHealthRecord)
class ElectronicHealthRecordModelAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date_created', 'notes', 'allergies', 'medications', 'medical_history', 'vital_signs')

@admin.register(Immunization)
class ImmunizationModelAdmin(admin.ModelAdmin):
    list_display = ('patient', 'vaccine_name', 'date_administered', 'administered_by')

@admin.register(LabResult)
class LabResultModelAdmin(admin.ModelAdmin):
    list_display = ('patient', 'test_name', 'result', 'date_of_test')

@admin.register(RadiologyReport)
class RadiologyReportModelAdmin(admin.ModelAdmin):
    list_display = ('patient', 'report_type', 'report_details','date_of_report', 'doctor')

@admin.register(Prescription)
class PresciptionModelAdmin(admin.ModelAdmin):
    list_display = ('patient','medication_name', 'dosage', 'dosage', 'frequency', 'prescribed_by', 'date_prescribed')
# admin.site.register(ElectronicHealthRecord)
# admin.site.register(Immunization)
# admin.site.register(LabResult)
# admin.site.register(RadiologyReport)
# admin.site.register(Prescription)