from django.test import TestCase
from .models import InsuranceCompany

class InsuranceCompanyModelTest(TestCase):

    def setUp(self):
        self.insurance_company = InsuranceCompany.objects.create(name="Test Insurance")

    def test_insurance_company_creation(self):
        self.assertEqual(self.insurance_company.name, "Test Insurance")

    def test_str_representation(self):
        self.assertEqual(str(self.insurance_company), "Test Insurance")