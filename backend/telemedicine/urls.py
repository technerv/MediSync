from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TelemedicineSessionViewSet, TelemedicineFeedbackViewSet

# Create a router and register the TelemedicineSessionViewSet
router = DefaultRouter()
router.register(r'telemedicine', TelemedicineSessionViewSet, basename='telemedicine')
router.register(r'telemedicinefeedback', TelemedicineFeedbackViewSet, basename='telemedicinefeedback')

urlpatterns = [
    path('', include(router.urls)),  # Include router URLs
]