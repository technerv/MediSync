from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BillingViewSet, InvoiceViewSet, PaymentViewSet

# Create a router and register the BillingViewSet and InvoiceViewSet
router = DefaultRouter()
router.register(r'billing', BillingViewSet, basename='billing')
router.register(r'invoice', InvoiceViewSet, basename='invoice')
router.register(r'payment', PaymentViewSet, basename='payment')

urlpatterns = [
    path('', include(router.urls)),  # Include router URLs
]
