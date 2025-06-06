from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LaboratoryTestViewSet, LaboratoryResultViewSet, SampleViewSet

# Create a router and register the LaboratoryTestViewSet and LaboratoryResultViewSet
router = DefaultRouter()
router.register(r'laboratory', LaboratoryTestViewSet, basename='laboratory')
router.register(r'laboratory_result', LaboratoryResultViewSet, basename='laboratory_result')
router.register(r'sample', SampleViewSet, basename='sample')

urlpatterns = [
    path('', include(router.urls)),  # Include router URLs
]