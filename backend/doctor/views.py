from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Doctor, DoctorAvailability
from .serializers import DoctorSerializer, DoctorAvailabilitySerializer
from authentication.permissions import IsDoctor
from doctor.permissions import DoctorProfileSchedulePermission

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated, IsDoctor, DoctorProfileSchedulePermission]

    def perform_create(self, serializer):
        serializer.save() 

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

class DoctorAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = DoctorAvailability.objects.all()
    serializer_class = DoctorAvailabilitySerializer
    permission_classes = [IsAuthenticated, IsDoctor, DoctorProfileSchedulePermission]

    def perform_create(self, serializer):
        serializer.save() 

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()