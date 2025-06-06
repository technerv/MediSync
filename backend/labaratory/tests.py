from django.test import TestCase
from .models import LaboratoryTest, TestResult
from patient.models import Patient
from doctor.models import CustomUser

class LaboratoryTestModelTest(TestCase):
    def setUp(self):
        self.patient = Patient.objects.create(
            first_name="John",
            second_name="Doe",
            email="john.doe@example.com",
            phone="1234567890",
            date_of_birth="1990-01-01",
            gender="M"
        )
        self.doctor = CustomUser.objects.create_user(
            username="doctor1",
            password="password123"
        )
        self.laboratory_test = LaboratoryTest.objects.create(
            patient=self.patient,
            test_name="Blood Test",
            assigned_doctor=self.doctor
        )

    def test_laboratory_test_creation(self):
        self.assertEqual(self.laboratory_test.test_name, "Blood Test")
        self.assertEqual(self.laboratory_test.patient.first_name, "John")
        self.assertEqual(self.laboratory_test.assigned_doctor.username, "doctor1")

class TestResultModelTest(TestCase):
    def setUp(self):
        self.patient = Patient.objects.create(
            first_name="Jane",
            second_name="Doe",
            email="jane.doe@example.com",
            phone="0987654321",
            date_of_birth="1992-02-02",
            gender="F"
        )
        self.doctor = CustomUser.objects.create_user(
            username="doctor2",
            password="password456"
        )
        self.laboratory_test = LaboratoryTest.objects.create(
            patient=self.patient,
            test_name="Urine Test",
            assigned_doctor=self.doctor
        )
        self.test_result = TestResult.objects.create(
            laboratory_test=self.laboratory_test,
            result="Normal",
            notes="All values are within normal range."
        )

    def test_test_result_creation(self):
        self.assertEqual(self.test_result.result, "Normal")
        self.assertEqual(self.test_result.laboratory_test.test_name, "Urine Test")
        self.assertEqual(self.test_result.notes, "All values are within normal range.")