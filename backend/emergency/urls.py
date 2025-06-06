from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmergencyContactViewSet, EmergencyCaseViewSet, AmbulanceRequestViewSet

# Create a router and register the EmergencyContactViewSet
router = DefaultRouter()
router.register(r'emergency-contact', EmergencyContactViewSet, basename='emergency-contact')
router.register(r'emergency-case', EmergencyCaseViewSet, basename='emergency-case')
router.register(r'ambulance-request', AmbulanceRequestViewSet, basename='ambulance-request')

urlpatterns = [
    path('', include(router.urls)),  # Include router URLs
]