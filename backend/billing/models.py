from django.db import models
from patient.models import Patient
from django.contrib.auth import get_user_model

User = get_user_model()

class Invoice(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
        ('pending', 'Pending'),
    ], default='unpaid')

    def __str__(self):
        return f"Invoice #{self.id} for {self.patient.first_name}-{self.patient.second_name}"

class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50, choices=[
        ('cash', 'Cash'),
        ('credit_card', 'Credit Card'),
        ('insurance', 'Insurance'),
    ])

    def __str__(self):
        return f"Payment of {self.amount} for Invoice #{self.invoice.id} {self.invoice.patient.first_name} {self.invoice.patient.second_name}"

class BillingRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    service_description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_service = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Billing Record for {self.patient.first_name} - {self.service_description}"