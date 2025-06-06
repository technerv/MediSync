from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, OrderBillViewSet, InventoryViewSet, PurchaseOrderViewSet

# Create a router and register the InventoryViewSet
router = DefaultRouter()
router.register(r'item', ItemViewSet, basename='item')
router.register(r'orderbill', OrderBillViewSet, basename='orderbill')
router.register(r'inventory', InventoryViewSet, basename='inventory')
router.register(r'purchaseorder', PurchaseOrderViewSet, basename='purchase-order')

urlpatterns = [
    path('', include(router.urls)),  # Include router URLs
]