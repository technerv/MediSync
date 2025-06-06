from django.test import TestCase
from .models import EmergencyContact

class EmergencyContactModelTest(TestCase):
    def setUp(self):
        self.contact = EmergencyContact.objects.create(
            name="John Doe",
            relationship="Brother",
            phone_number="1234567890",
            email="john.doe@example.com"
        )

    def test_emergency_contact_creation(self):
        self.assertEqual(self.contact.name, "John Doe")
        self.assertEqual(self.contact.relationship, "Brother")
        self.assertEqual(self.contact.phone_number, "1234567890")
        self.assertEqual(self.contact.email, "john.doe@example.com")

    def test_string_representation(self):
        self.assertEqual(str(self.contact), "John Doe")