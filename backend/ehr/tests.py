from django.test import TestCase
from .models import YourModel  # Replace with your actual model
from django.urls import reverse

class YourModelTests(TestCase):

    def setUp(self):
        # Set up any initial data for your tests here
        self.instance = YourModel.objects.create(field1='value1', field2='value2')  # Adjust fields as necessary

    def test_model_creation(self):
        """Test that the model instance is created correctly."""
        self.assertEqual(self.instance.field1, 'value1')
        self.assertEqual(self.instance.field2, 'value2')

    def test_model_str(self):
        """Test the string representation of the model."""
        self.assertEqual(str(self.instance), 'Expected String Representation')  # Adjust as necessary

    def test_view_status_code(self):
        """Test that the view returns a 200 status code."""
        response = self.client.get(reverse('your_model_list'))  # Replace with your actual view name
        self.assertEqual(response.status_code, 200)

    def test_view_template_used(self):
        """Test that the correct template is used for the view."""
        response = self.client.get(reverse('your_model_list'))  # Replace with your actual view name
        self.assertTemplateUsed(response, 'your_template.html')  # Replace with your actual template name

    def tearDown(self):
        # Clean up any data after tests
        self.instance.delete()