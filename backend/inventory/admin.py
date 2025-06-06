from django.contrib import admin
from .models import Item, OrderBill, Inventory, Supplier, PurchaseOrder

# admin.site.register(Item)
# admin.site.register(OrderBill)

@admin.register(Item)
class ItemModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'quantity', 'unit_price', 'quantity')

@admin.register(OrderBill)
class OrderBillModelAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'total_amount', 'date_created')

@admin.register(Inventory)
class InventoryModelAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity_available', 'reorder_level')

@admin.register(Supplier)
class SupplierModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_person', 'phone', 'email', 'address')

@admin.register(PurchaseOrder)
class PurchaseOrderModelAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'item', 'quantity_ordered', 'order_date', 'status')