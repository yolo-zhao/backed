from django.db import models


class Order(models.Model):
    order_id = models.CharField(max_length=20, unique=True)
    customer_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="pending")  # 添加默认值

    def __str__(self):
        return f"订单 {self.order_id} - {self.customer_name}"

class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=50)
    plate_number = models.CharField(max_length=20, unique=True, default="UNKNOWN")

    def __str__(self):
        return f"{self.vehicle_type} - {self.plate_number}"


class Warehouse:
    pass