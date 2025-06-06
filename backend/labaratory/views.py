from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import LaboratoryTest, LaboratoryResult, Sample
from .serializers import LaboratoryTestSerializer, LaboratoryResultSerializer, SampleSerializer
from labaratory.permissions import LaboratoryPermission
# from authentication.permissions import IsReceptionist, IsDoctor, IsNurse, IsPatient

class LaboratoryTestViewSet(viewsets.ModelViewSet):
    queryset = LaboratoryTest.objects.all()
    serializer_class = LaboratoryTestSerializer
    permission_classes = [IsAuthenticated, LaboratoryPermission,]

class LaboratoryResultViewSet(viewsets.ModelViewSet):
    queryset = LaboratoryResult.objects.all()
    serializer_class = LaboratoryResultSerializer
    permission_classes = [IsAuthenticated, LaboratoryPermission,]

class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
    permission_classes = [IsAuthenticated, LaboratoryPermission,]