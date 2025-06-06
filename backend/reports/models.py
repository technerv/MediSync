from django.db import models
from patient.models import Patient
from doctor.models import CustomUser

class Report(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    report_type = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.report_type} Report for {self.patient.first_name} {self.patient.second_name}"

class PatientReport(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_accessed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Accessed {self.report} by {self.patient.first_name}"