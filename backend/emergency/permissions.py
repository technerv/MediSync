from rest_framework.permissions import BasePermission

# Log/View Emergency
class LogViewEmergencyPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['receptionist']
    
class EmergencyCasePermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['nurse, doctor']

# Request Emergency Care
class RequestEmergencyCarePermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['doctor', 'nurse', 'receptionist']