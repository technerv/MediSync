from rest_framework.permissions import BasePermission

class PatientPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['patient', 'receptionist', 'nurse', 'doctor']

class NextOfKinPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['receptionist']

class TriagePermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['doctor', 'nurse', 'receptionist']