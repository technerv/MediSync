from django.contrib import admin
from .models import LaboratoryTest, LaboratoryResult, Sample

@admin.register(LaboratoryTest)
class LabaratoryTestModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_by', 'date_created')

@admin.register(LaboratoryResult)
class LabaratoryResultModelAdmin(admin.ModelAdmin):
    list_display = ('test', 'patient', 'result', 'date_performed', 'notes')

@admin.register(Sample)
class SampleModelAdmin(admin.ModelAdmin):
    list_display = ('patient', 'test', 'sample_type', 'date_collected', 'collected_by')

# admin.site.register(LaboratoryTest)
# admin.site.register(LaboratoryResult)
# admin.site.register(Sample)