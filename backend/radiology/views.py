from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import RadiologyTest, RadiologyReport
from .serializers import RadiologyTestSerializer, RadiologyReportSerializer
from radiology.permissions import RadiologyPermission
from authentication.permissions import IsReceptionist, IsDoctor, IsNurse, IsPatient

class RadiologyTestViewSet(viewsets.ModelViewSet):
    queryset = RadiologyTest.objects.all()
    serializer_class = RadiologyTestSerializer
    permission_classes = [IsAuthenticated, RadiologyPermission,]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

class RadiologyReportViewSet(viewsets.ModelViewSet):
    queryset = RadiologyReport.objects.all()
    serializer_class = RadiologyReportSerializer
    permission_classes = [IsAuthenticated, RadiologyPermission,]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()