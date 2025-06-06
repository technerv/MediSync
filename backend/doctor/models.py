from django.db import models
from authentication.models import CustomUser

class Doctor(models.Model):
    SPECIALIZATION_CHOICES = (
        ('general', 'General Practitioner'),
        ('cardiologist', 'Cardiologist'),
        ('neurologist', 'Neurologist'),
        ('orthopedist', 'Orthopedist'),
        ('pediatrician', 'Pediatrician'),
        ('psychiatrist', 'Psychiatrist'),
        ('surgeon', 'Surgeon'),
        ('dentist', 'Dentist'),
    )

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(unique=True)
    specialization = models.CharField(max_length=30, choices=SPECIALIZATION_CHOICES)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} - {self.specialization}"


class DoctorAvailability(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = ('doctor', 'day_of_week')

    def __str__(self):
        return f"{self.doctor} - {self.day_of_week} ({self.start_time} to {self.end_time})"