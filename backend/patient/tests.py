from django.test import TestCase
from .models import Patient, InsuranceCompany, ContactDetails

class PatientModelTest(TestCase):

    def setUp(self):
        self.insurance_company = InsuranceCompany.objects.create(name="Health Insurance Co.")
        self.contact_details = ContactDetails.objects.create(tel_no=1234567890, email_address="test@example.com", residence="123 Main St")
        self.patient = Patient.objects.create(
            first_name="John",
            second_name="Doe",
            email="john.doe@example.com",
            phone="555-555-5555",
            date_of_birth="1990-01-01",
            gender="M",
            insurance=self.insurance_company,
            user_id=None,  # Assuming user_id is set later
        )

    def test_patient_creation(self):
        self.assertEqual(self.patient.first_name, "John")
        self.assertEqual(self.patient.second_name, "Doe")
        self.assertEqual(self.patient.email, "john.doe@example.com")
        self.assertEqual(self.patient.phone, "555-555-5555")
        self.assertEqual(self.patient.gender, "M")
        self.assertEqual(self.patient.insurance.name, "Health Insurance Co.")

    def test_patient_age(self):
        self.assertEqual(self.patient.age, 33)  # Assuming the current year is 2023

    def test_patient_str(self):
        self.assertEqual(str(self.patient), "John")