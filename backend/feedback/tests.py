from django.test import TestCase
from .models import Feedback

class FeedbackModelTest(TestCase):
    def setUp(self):
        self.feedback = Feedback.objects.create(
            patient_name="John Doe",
            email="john.doe@example.com",
            message="Great service!",
            rating=5
        )

    def test_feedback_creation(self):
        self.assertEqual(self.feedback.patient_name, "John Doe")
        self.assertEqual(self.feedback.email, "john.doe@example.com")
        self.assertEqual(self.feedback.message, "Great service!")
        self.assertEqual(self.feedback.rating, 5)

    def test_feedback_str(self):
        self.assertEqual(str(self.feedback), "Feedback from John Doe")