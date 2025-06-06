from django.db import models
from patient.models import Patient
from authentication.models import CustomUser

class LaboratoryTest(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class LaboratoryResult(models.Model):
    test = models.ForeignKey(LaboratoryTest, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    result = models.TextField()
    date_performed = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Result for {self.patient.first_name} - {self.test.name}"

class Sample(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test = models.ForeignKey(LaboratoryTest, on_delete=models.CASCADE)
    sample_type = models.CharField(max_length=100)
    date_collected = models.DateTimeField(auto_now_add=True)
    collected_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"Sample for {self.patient.first_name} - {self.sample_type}"