from django.db import models
from patient.models import Patient
from doctor.models import CustomUser

class ElectronicHealthRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey("doctor.Doctor", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(null=True, blank=True)
    allergies = models.TextField(null=True, blank=True)
    medications = models.TextField(null=True, blank=True)
    medical_history = models.TextField(null=True, blank=True)
    vital_signs = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Health Record for {self.patient.first_name} {self.patient.second_name} on {self.date_created.strftime('%Y-%m-%d')}"


class Immunization(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    vaccine_name = models.CharField(max_length=100)
    date_administered = models.DateField()
    administered_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.vaccine_name} for {self.patient.first_name} on {self.date_administered}"


class LabResult(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=100)
    result = models.TextField()
    date_of_test = models.DateField()
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.test_name} result for {self.patient.first_name} on {self.date_of_test}"


class RadiologyReport(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    report_type = models.CharField(max_length=100)
    report_details = models.TextField()
    date_of_report = models.DateField()
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.report_type} report for {self.patient.first_name} on {self.date_of_report}"


class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='ehr_prescriptions')
    medication_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    prescribed_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ehr_doctor_prescriptions')
    date_prescribed = models.DateField()

    def __str__(self):
        return f"Prescription for {self.patient.first_name} - {self.medication_name}"