from django.contrib import admin
from .models import RadiologyTest, RadiologyReport

@admin.register(RadiologyTest)
class RadiologyTestModelAdmin(admin.ModelAdmin):
    list_display = ('patient', 'test_type', 'date_requested', 'date_performed', 'performed_by', 'results', 'notes')

@admin.register(RadiologyReport)
class RadiologyReportModelAdmin(admin.ModelAdmin):
    list_display = ('radiology_test', 'report_date', 'findings', 'recommendations')