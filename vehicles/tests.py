from django.test import TestCase
from .models import Vehicle

class VehicleModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # 创建车辆实例
        Vehicle.objects.create(name="Vehicle A", type="Truck", capacity=50, current_location="Warehouse A")
        Vehicle.objects.create(name="Vehicle B", type="Van", capacity=30, current_location="Warehouse B")

    def test_vehicle_creation(self):
        # 测试车辆的创建
        vehicle = Vehicle.objects.get(name="Vehicle A")
        self.assertEqual(vehicle.type, "Truck")
        self.assertEqual(vehicle.capacity, 50)
