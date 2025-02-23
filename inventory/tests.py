# backend/inventory/tests.py
from itertools import product

from django.test import TestCase
from .models import Product

class InventoryModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # 创建产品实例
        Product.objects.create(name="Product A", price=10.0, quantity=100)
        Product.objects.create(name="Product B", price=20.0, quantity=50)

    def test_product_creation(self):
        # 测试产品的创建
        new_product = Product.objects.create(name="Product A", price=10.0, quantity=100, stock=50)
        self.assertEqual(new_product.price, 10.0)
        self.assertEqual(new_product.quantity, 100)
