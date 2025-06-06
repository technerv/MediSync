from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FeedbackViewSet

# Create a router and register the EmergencyContactViewSet
router = DefaultRouter()
router.register(r'feedback', FeedbackViewSet, basename='feedback')

urlpatterns = [
    path('', include(router.urls)),  # Include router URLs
]