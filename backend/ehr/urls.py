from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ElectronicHealthRecordViewSet

# Create a router and register the ElectronicHealthRecordViewSet
router = DefaultRouter()
router.register(r'ehr', ElectronicHealthRecordViewSet, basename='ehr')

urlpatterns = [
    path('', include(router.urls)),  # Include router URLs
]
