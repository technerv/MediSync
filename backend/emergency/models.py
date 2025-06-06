from django.db import models
from patient.models import Patient
from authentication.models import CustomUser

class EmergencyContact(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} ({self.relationship})"

class EmergencyCase(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    status = models.CharField(max_length=20, default='open')

    def __str__(self):
        return f"Emergency Case for {self.patient.first_name} - {self.status}"

class AmbulanceRequest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    request_time = models.DateTimeField(auto_now_add=True)
    pickup_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return f"Ambulance Request for {self.patient.first_name} - {self.status}"