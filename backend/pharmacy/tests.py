from django.test import TestCase
from .models import Item, OrderBill

class ItemModelTest(TestCase):
    def setUp(self):
        self.item = Item.objects.create(name="Aspirin", price=10.00, stock=100)

    def test_item_creation(self):
        self.assertEqual(self.item.name, "Aspirin")
        self.assertEqual(self.item.price, 10.00)
        self.assertEqual(self.item.stock, 100)

    def test_item_str(self):
        self.assertEqual(str(self.item), "Aspirin")

class OrderBillModelTest(TestCase):
    def setUp(self):
        self.order_bill = OrderBill.objects.create(total_amount=100.00)

    def test_order_bill_creation(self):
        self.assertEqual(self.order_bill.total_amount, 100.00)

    def test_order_bill_str(self):
        self.assertEqual(str(self.order_bill), f"OrderBill #{self.order_bill.id}")