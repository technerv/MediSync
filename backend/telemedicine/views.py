from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import TelemedicineSession, TelemedicineFeedback
from .serializers import TelemedicineSessionSerializer, TelemedicineFeedbackSerializer
from telemedicine.permissions import TelemedicinePermission

class TelemedicineSessionViewSet(viewsets.ModelViewSet):
    queryset = TelemedicineSession.objects.all()
    serializer_class = TelemedicineSessionSerializer
    permission_classes = [IsAuthenticated, TelemedicinePermission,]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

class TelemedicineFeedbackViewSet(viewsets.ModelViewSet):
    queryset = TelemedicineFeedback.objects.all()
    serializer_class = TelemedicineFeedbackSerializer  
    permission_classes = [IsAuthenticated, TelemedicinePermission,]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)