from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, NextOfKinViewSet, TriageViewSet

# Create a router and register the PatientViewSet
router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'next_of_kin', NextOfKinViewSet, basename='next-of-kin')
router.register(r'triage', TriageViewSet, basename='triage' )

urlpatterns = [
    path('', include(router.urls)),  # Include router URLs
]
