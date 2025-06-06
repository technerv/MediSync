from django.test import TestCase
from .models import Item, OrderBill

class ItemModelTest(TestCase):
    def setUp(self):
        self.item = Item.objects.create(name="Test Item", quantity=10, price=100.00)

    def test_item_creation(self):
        self.assertEqual(self.item.name, "Test Item")
        self.assertEqual(self.item.quantity, 10)
        self.assertEqual(self.item.price, 100.00)

    def test_item_str(self):
        self.assertEqual(str(self.item), "Test Item")

class OrderBillModelTest(TestCase):
    def setUp(self):
        self.order_bill = OrderBill.objects.create(total_amount=500.00)

    def test_order_bill_creation(self):
        self.assertEqual(self.order_bill.total_amount, 500.00)

    def test_order_bill_str(self):
        self.assertEqual(str(self.order_bill), f"Order Bill #{self.order_bill.id}")