from django.contrib import admin
from .models import PatientReport, Report

@admin.register(Report)
class ReportModelAdmin(admin.ModelAdmin):
    list_display = ('patient', 'created_by', 'report_type', 'date_created', 'date_updated', 'content')

@admin.register(PatientReport)
class PatientReportModelAdmin(admin.ModelAdmin):
    list_display = ('report', 'patient', 'date_accessed')