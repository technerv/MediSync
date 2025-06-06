from django.db import models
from authentication.models import CustomUser

class Drug(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Prescription(models.Model):
    patient = models.ForeignKey('patient.Patient', on_delete=models.CASCADE, related_name='pharmacy_prescriptions')
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='pharmacy_doctor_prescriptions')
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('completed', 'Completed')], default='active')

    def __str__(self):
        return f"Prescription for {self.patient.first_name} by {self.doctor.username}"

class PrescribedDrug(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.dosage} of {self.drug.name} for {self.prescription.patient.first_name}"

class PharmacyOrder(models.Model):
    patient = models.ForeignKey('patient.Patient', on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending')

    def __str__(self):
        return f"Order #{self.id} for {self.patient.first_name}"