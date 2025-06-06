from django.contrib import admin
from .models import Drug, Prescription, PrescribedDrug, PharmacyOrder

@admin.register(Drug)
class DrugModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'stock_quantity')

@admin.register(Prescription)
class PrescriptionModelAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date_created', 'status')

@admin.register(PrescribedDrug)
class DrugModelAdmin(admin.ModelAdmin):
    list_display = ('prescription', 'drug', 'dosage', 'frequency', 'duration')

@admin.register(PharmacyOrder)
class PharmacyOrderModelAdmin(admin.ModelAdmin):
    list_display = ('patient', 'date_ordered', 'total_amount', 'status')

# admin.site.register(Drug)
# admin.site.register(Prescription)
# admin.site.register(PrescribedDrug)
# admin.site.register(PharmacyOrder)