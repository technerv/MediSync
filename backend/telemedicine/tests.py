from django.test import TestCase
from .models import TelemedicineSession, Patient, Doctor

class TelemedicineSessionTests(TestCase):

    def setUp(self):
        self.patient = Patient.objects.create(
            first_name="John",
            second_name="Doe",
            email="john.doe@example.com",
            phone="1234567890",
            date_of_birth="1990-01-01",
            gender="M"
        )
        self.doctor = Doctor.objects.create(
            first_name="Jane",
            second_name="Smith",
            email="jane.smith@example.com",
            phone="0987654321",
            specialization="General Practitioner"
        )
        self.session = TelemedicineSession.objects.create(
            patient=self.patient,
            doctor=self.doctor,
            session_date_time="2023-10-01T10:00:00Z",
            status="scheduled",
            notes="Initial consultation"
        )

    def test_telemedicine_session_creation(self):
        self.assertEqual(self.session.patient, self.patient)
        self.assertEqual(self.session.doctor, self.doctor)
        self.assertEqual(self.session.status, "scheduled")

    def test_telemedicine_session_str(self):
        self.assertEqual(str(self.session), f"Telemedicine Session with {self.patient.first_name} on {self.session.session_date_time}")

    def test_session_status_update(self):
        self.session.status = "completed"
        self.session.save()
        self.assertEqual(self.session.status, "completed")