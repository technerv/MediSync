from rest_framework import viewsets
from rest_framework.response import Response
from .models import EmergencyContact, EmergencyCase, AmbulanceRequest
from .serializers import EmergencyContactSerializer, EmergencyCaseSerializer, AmbulanceRequestSerializer
from authentication.permissions import IsReceptionist, IsDoctor, IsNurse, IsPatient
from emergency.permissions import LogViewEmergencyPermission, RequestEmergencyCarePermission, EmergencyCasePermission

class EmergencyContactViewSet(viewsets.ModelViewSet):
    queryset = EmergencyContact.objects.all()
    serializer_class = EmergencyContactSerializer
    permission_classes = [LogViewEmergencyPermission,]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=201)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        emergency_contact = self.get_object()
        serializer = self.get_serializer(emergency_contact)
        return Response(serializer.data)

    def update(self, request, pk=None):
        emergency_contact = self.get_object()
        serializer = self.get_serializer(emergency_contact, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        emergency_contact = self.get_object()
        self.perform_destroy(emergency_contact)
        return Response(status=204)

class EmergencyCaseViewSet(viewsets.ModelViewSet):
    queryset = EmergencyCase.objects.all()
    serializer_class = EmergencyCaseSerializer
    permission_classes = [IsDoctor, IsNurse, EmergencyCasePermission,]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=201)
    
    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        emergency_case = self.get_object()
        serializer = self.get_serializer(emergency_case)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        emergency_case = self.get_object()
        serializer = self.get_serializer(emergency_case, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, pk=None):
        emergency_case = self.get_object()
        self.perform_destroy(emergency_case)
        return Response(status=204)

class AmbulanceRequestViewSet(viewsets.ModelViewSet):
    queryset = AmbulanceRequest.objects.all()
    serializer_class = AmbulanceRequestSerializer
    permission_classes = [IsPatient, RequestEmergencyCarePermission,]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=201)
    
    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        ambulance_request = self.get_object()
        serializer = self.get_serializer(ambulance_request)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        ambulance_request = self.get_object()
        serializer = self.get_serializer(ambulance_request, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, pk=None):
        ambulance_request = self.get_object()
        self.perform_destroy(ambulance_request)
        return Response(status=204)