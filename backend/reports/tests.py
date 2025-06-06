from django.test import TestCase
from .models import Report  # Adjust the import based on your actual model name

class ReportModelTest(TestCase):

    def setUp(self):
        self.report = Report.objects.create(
            title="Annual Health Report",
            content="This is a test report content.",
            created_by="Test User"
        )

    def test_report_creation(self):
        self.assertEqual(self.report.title, "Annual Health Report")
        self.assertEqual(self.report.content, "This is a test report content.")
        self.assertEqual(self.report.created_by, "Test User")

    def test_string_representation(self):
        self.assertEqual(str(self.report), "Annual Health Report")  # Adjust based on your __str__ method

    def test_report_update(self):
        self.report.title = "Updated Health Report"
        self.report.save()
        self.assertEqual(self.report.title, "Updated Health Report")

    def test_report_deletion(self):
        report_id = self.report.id
        self.report.delete()
        with self.assertRaises(Report.DoesNotExist):
            Report.objects.get(id=report_id)