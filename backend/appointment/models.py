from django.db import models
from patient.models import Patient
# from authentication.models import CustomUser
from inventory.models import OrderBill

class Appointment(models.Model):
    class Meta:
        ordering = ("-date_created",)

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )
    appointment_date_time = models.DateTimeField(null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient_appoinments')
    assigned_doctor = models.ForeignKey("doctor.Doctor", on_delete=models.SET_NULL, null=True, blank=True, related_name='doctor_appointments')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    reason = models.TextField(max_length=300, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)
    # item_id = models.ForeignKey("item.Item", on_delete=models.SET_NULL, blank=True, null=True, related_name='item_appointments')
    fee = models.CharField(max_length=40, default="0")
    order_bill_ID = models.ForeignKey(
        OrderBill, on_delete=models.CASCADE, null=True, related_name='order_bill_appointments')

    def __str__(self):
        return f"Appointment #{self.patient.first_name}-{self.assigned_doctor}"