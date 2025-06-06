from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, DoctorAvailabilityViewSet

# Create a router and register the DoctorViewSet
router = DefaultRouter()
router.register(r'doctor', DoctorViewSet, basename='doctor')
router.register(r'doctor_availability', DoctorAvailabilityViewSet, basename='doctor-availability' )

urlpatterns = [
    path('', include(router.urls)),  # Include router URLs
]
