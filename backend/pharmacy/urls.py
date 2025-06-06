from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DrugViewSet, PrescriptionViewSet, PrescribedDrugViewSet, PharmacyOrderViewSet

# Create a router and register the DrugViewSet and PrescriptionViewSet
router = DefaultRouter()
router.register(r'drug', DrugViewSet, basename='drug')
router.register(r'prescription', PrescriptionViewSet, basename='prescription')
router.register(r'prescribed_drug', PrescribedDrugViewSet, basename='prescribed_drug')
router.register(r'pharmacy_order', PharmacyOrderViewSet, basename='pharmacy_order')

urlpatterns = [
    path('', include(router.urls)),  # Include router URLs
]