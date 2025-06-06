from django.test import TestCase
from .models import RadiologyTest, Patient

class RadiologyTestModelTests(TestCase):

    def setUp(self):
        self.patient = Patient.objects.create(
            first_name="John",
            second_name="Doe",
            email="john.doe@example.com",
            phone="1234567890",
            date_of_birth="1990-01-01",
            gender="M"
        )
        self.radiology_test = RadiologyTest.objects.create(
            patient=self.patient,
            test_type="X-Ray",
            date_performed="2023-01-01",
            results="Normal"
        )

    def test_radiology_test_creation(self):
        self.assertEqual(self.radiology_test.patient, self.patient)
        self.assertEqual(self.radiology_test.test_type, "X-Ray")
        self.assertEqual(self.radiology_test.results, "Normal")

    def test_str_method(self):
        self.assertEqual(str(self.radiology_test), f"{self.radiology_test.test_type} for {self.patient.first_name} {self.patient.second_name}")