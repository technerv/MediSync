from django.db import models
from patient.models import Patient

class InsuranceCompany(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class InsurancePolicy(models.Model):
    insurance_company = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE)
    policy_number = models.CharField(max_length=50, unique=True)
    patient = models.ForeignKey('patient.Patient', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    coverage_details = models.TextField()

    def __str__(self):
        return f"{self.policy_number} - {self.insurance_company.name}-{self.patient}"

class Claim(models.Model):
    insurance_policy = models.ForeignKey(InsurancePolicy, on_delete=models.CASCADE)
    claim_number = models.CharField(max_length=50, unique=True)
    date_of_claim = models.DateField()
    amount_claimed = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], default='pending')
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Claim #{self.claim_number} - Status: {self.status}"