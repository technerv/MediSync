from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InsuranceCompanyViewSet, InsurancePolicyViewSet, ClaimViewSet

# Create a router and register the InsuranceCompanyViewSet
router = DefaultRouter()
router.register(r'insurancecompany', InsuranceCompanyViewSet, basename='insurancecompany')
router.register(r'insurancepolicy', InsurancePolicyViewSet, basename='insurancepolicy')
router.register(r'claim', ClaimViewSet, basename='claim')

urlpatterns = [
    path('', include(router.urls)),  # Include router URLs
]