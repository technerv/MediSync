from rest_framework import serializers
from .models import Item, OrderBill, Inventory, PurchaseOrder

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class OrderBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderBill
        fields = '__all__'
    
class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '_all_'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '_all_'