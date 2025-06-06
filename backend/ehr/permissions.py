from rest_framework.permissions import BasePermission

# Create/Update EHR Permission
class CreateUpdateEHRPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['doctor', 'nurse']

# View Patient EHR Permission
class ViewPatientEHRPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['doctor', 'nurse']
    
# View Own EHR
class ViewOwnEHRPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['patient']