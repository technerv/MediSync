from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import ElectronicHealthRecord
from .serializers import ElectronicHealthRecordSerializer
from authentication.permissions import IsDoctor, IsNurse, IsPatient, IsReceptionist
from ehr.permissions import CreateUpdateEHRPermission, ViewOwnEHRPermission, ViewPatientEHRPermission

class ElectronicHealthRecordViewSet(viewsets.ModelViewSet):
    queryset = ElectronicHealthRecord.objects.all()
    serializer_class = ElectronicHealthRecordSerializer
    permission_classes = [IsAuthenticated,ViewPatientEHRPermission]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()