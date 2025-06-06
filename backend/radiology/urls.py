from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RadiologyTestViewSet, RadiologyReportViewSet

# Create a router and register the RadiologyTestViewSet
router = DefaultRouter()
router.register(r'radiologytest', RadiologyTestViewSet, basename='radiologytest')
router.register(r'radiologyreport', RadiologyReportViewSet, basename='radiologyreport')

urlpatterns = [
    path('', include(router.urls)),  # Include router URLs
]