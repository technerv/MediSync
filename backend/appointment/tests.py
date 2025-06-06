from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Appointment
from patient.models import Patient
from customuser.models import CustomUser
from datetime import datetime, timedelta

class AppointmentModelTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.patient = Patient.objects.create(
            first_name='John',
            second_name='Doe',
            email='john.doe@example.com',
            date_of_birth=datetime.now() - timedelta(days=365 * 30),  # 30 years old
            gender='M',
            user_id=self.user
        )
        self.appointment = Appointment.objects.create(
            appointment_date_time=datetime.now() + timedelta(days=1),
            patient=self.patient,
            assigned_doctor=self.user,
            status='pending',
            reason='Routine check-up'
        )

    def test_appointment_creation(self):
        self.assertEqual(self.appointment.patient.first_name, 'John')
        self.assertEqual(self.appointment.status, 'pending')

    def test_appointment_str(self):
        self.assertEqual(str(self.appointment), f"Appointment #{self.appointment.patient.first_name}")

    def test_appointment_date_time(self):
        self.assertIsNotNone(self.appointment.appointment_date_time)
        self.assertGreater(self.appointment.appointment_date_time, datetime.now())

    def test_appointment_status_choices(self):
        self.appointment.status = 'confirmed'
        self.appointment.save()
        self.assertEqual(self.appointment.status, 'confirmed')

    def test_appointment_reason(self):
        self.assertEqual(self.appointment.reason, 'Routine check-up')