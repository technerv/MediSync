from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Item, OrderBill, Inventory, PurchaseOrder
from .serializers import ItemSerializer, OrderBillSerializer, InventorySerializer, PurchaseOrderSerializer
# from authentication.permissions import IsPatient, IsDoctor, IsNurse, IsReceptionist
from inventory.permissions import InventoryPermission

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated, InventoryPermission,]

class OrderBillViewSet(viewsets.ModelViewSet):
    queryset = OrderBill.objects.all()
    serializer_class = OrderBillSerializer
    permission_classes = [IsAuthenticated, InventoryPermission,]

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticated, InventoryPermission,]

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [IsAuthenticated, InventoryPermission,]