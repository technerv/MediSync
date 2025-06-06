from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Drug, Prescription, PrescribedDrug, PharmacyOrder
from .serializers import DrugSerializer, PrescriptionSerializer, PrescribedDrugSerializer, PharmacyOrderSerializer
from pharmacy.permissions import PharmacyPermission
# from authentication.permissions import IsPatient, IsDoctor, IsNurse, IsReceptionist

class DrugViewSet(viewsets.ModelViewSet):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    permission_classes = [IsAuthenticated, PharmacyPermission,]

class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [IsAuthenticated, PharmacyPermission,]

class PrescribedDrugViewSet(viewsets.ModelViewSet):
    queryset = PrescribedDrug.objects.all()
    serializer_class = PrescribedDrugSerializer
    permission_classes = [IsAuthenticated, PharmacyPermission,]

class PharmacyOrderViewSet(viewsets.ModelViewSet):
    queryset = PharmacyOrder.objects.all()
    serializer_class = PharmacyOrderSerializer
    permission_classes = [IsAuthenticated, PharmacyPermission,]