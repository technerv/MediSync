from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Doctor

class DoctorModelTest(TestCase):
    def setUp(self):
        self.doctor = Doctor.objects.create(
            first_name="John",
            last_name="Doe",
            specialization="Cardiology",
            phone="1234567890",
            email="john.doe@example.com"
        )

    def test_doctor_creation(self):
        self.assertEqual(self.doctor.first_name, "John")
        self.assertEqual(self.doctor.last_name, "Doe")
        self.assertEqual(self.doctor.specialization, "Cardiology")
        self.assertEqual(self.doctor.phone, "1234567890")
        self.assertEqual(self.doctor.email, "john.doe@example.com")

    def test_str_representation(self):
        self.assertEqual(str(self.doctor), "Dr. John Doe")  # Assuming __str__ method returns this format

    def test_doctor_email_unique(self):
        with self.assertRaises(Exception):
            Doctor.objects.create(
                first_name="Jane",
                last_name="Smith",
                specialization="Neurology",
                phone="0987654321",
                email="john.doe@example.com"  # Duplicate email
            )