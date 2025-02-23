# backend/warehouses/tests.py

from django.test import TestCase
from .models import Warehouse

class WarehouseModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # 创建仓库实例
        Warehouse.objects.create(name="Warehouse A", location="Location 1", capacity=200)
        Warehouse.objects.create(name="Warehouse B", location="Location 2", capacity=150)

    def test_warehouse_creation(self):
        # 测试仓库的创建
        warehouse = Warehouse.objects.get(name="Warehouse A")
        self.assertEqual(warehouse.location, "Location 1")
        self.assertEqual(warehouse.capacity, 200)
