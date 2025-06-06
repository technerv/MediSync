from rest_framework.permissions import BasePermission

class LaboratoryPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['lab_technician']
