from django.test import TestCase
from .models import Billing, OrderBill, Patient

class BillingModelTests(TestCase):

    def setUp(self):
        self.patient = Patient.objects.create(
            first_name="John",
            second_name="Doe",
            email="john.doe@example.com",
            phone="1234567890",
            date_of_birth="1990-01-01",
            gender="M"
        )
        self.order_bill = OrderBill.objects.create(
            patient_ID=self.patient,
            total_amount=100.00,
            status="paid"
        )
        self.billing = Billing.objects.create(
            order_bill_ID=self.order_bill,
            amount_due=50.00,
            amount_paid=50.00,
            payment_date="2023-01-01",
            payment_method="credit_card"
        )

    def test_billing_creation(self):
        self.assertEqual(self.billing.amount_due, 50.00)
        self.assertEqual(self.billing.amount_paid, 50.00)
        self.assertEqual(self.billing.payment_method, "credit_card")
        self.assertEqual(self.billing.order_bill_ID.patient_ID, self.patient)

    def test_billing_str(self):
        self.assertEqual(str(self.billing), f"Billing for {self.billing.order_bill_ID}")