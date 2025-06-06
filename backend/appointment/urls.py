from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppointmentViewSet

# Create a router and register the AppointmentViewSet
router = DefaultRouter()
router.register(r'appointment', AppointmentViewSet, basename='appointment')

# add link for creating/deleting appointments, managing appointments based on their permissions from views.py

urlpatterns = [
    path('', include(router.urls)),  # Include router URLs
]
