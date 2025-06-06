from rest_framework.permissions import BasePermission

# Create/Edit/Delete Appointment Permissions
class CEDAppointmentPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['receptionist', 'doctor']

# View All Appointment Permissions
class ViewAppointmentPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['patient', 'doctor']

# Manage All Appointment Permissions
class ManageAllAppointmentPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['receptionist']