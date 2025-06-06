from django.contrib import admin
from .models import BillingRecord, Invoice, Payment


@admin.register(Invoice)
class InvoiceModelAdmin(admin.ModelAdmin):
    list_display = ('patient', 'date_created', 'total_amount', 'status')

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'amount', 'date_paid', 'payment_method')

@admin.register(BillingRecord)
class BillingRecordModelAdmin(admin.ModelAdmin):
    list_display = ('patient', 'service_description', 'amount', 'date_of_service')
# admin.site.register(BillingRecord)
# admin.site.register(Invoice)
# admin.site.register(Payment)