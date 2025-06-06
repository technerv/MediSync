from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Appointment
from .serializers import AppointmentSerializer
from authentication.permissions import IsPatient, IsDoctor, IsReceptionist
from appointment.permissions import CEDAppointmentPermission, ViewAppointmentPermission, ManageAllAppointmentPermission

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated, ViewAppointmentPermission, ]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

""" Assign roles according to the user
 Create/Edit/Delete-Receptionist,Doctor
 View Open Appointments-Patient,Doctor 
 Manage All Appointments-Receptionist """