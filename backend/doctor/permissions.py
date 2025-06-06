from rest_framework.permissions import BasePermission

# Profile/Schedule Permission
class DoctorProfileSchedulePermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['doctor']

# View Assigned Patients Permission
class ViewAssignedPatientsPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['doctor']