from rest_framework.permissions import BasePermission

# View/Generate Invoice Permission
class GenerateInvoiceBillingPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['receptionist', 'doctor']

# View Own Bills Permission
class ViewBillingPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['patient']

# Process Payment Invoice Permission
class ProcessPaymentBillingPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['receptionist']