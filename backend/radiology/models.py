from django.db import models
from patient.models import Patient
from doctor.models import CustomUser

class RadiologyTest(models.Model):
    TEST_TYPE_CHOICES = (
        ('xray', 'X-Ray'),
        ('ct_scan', 'CT Scan'),
        ('mri', 'MRI'),
        ('ultrasound', 'Ultrasound'),
        ('blood_test', 'Blood Test'),
        ('other', 'Other'),
    )
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test_type = models.CharField(max_length=20, choices=TEST_TYPE_CHOICES)
    date_requested = models.DateTimeField(auto_now_add=True)
    date_performed = models.DateTimeField(null=True, blank=True)
    performed_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    results = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.test_type} for {self.patient.first_name} on {self.date_requested.strftime('%Y-%m-%d')}"


class RadiologyReport(models.Model):
    radiology_test = models.ForeignKey(RadiologyTest, on_delete=models.CASCADE)
    report_date = models.DateTimeField(auto_now_add=True)
    findings = models.TextField()
    recommendations = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Report for {self.radiology_test} on {self.report_date.strftime('%Y-%m-%d')}"