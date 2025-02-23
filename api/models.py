from django.db import models
from .wenxin_api import query_wenxin_model


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


class APIModel:
    pass


class Product:
    pass

def handle_query(user_input):
    # 通过文心大模型查询用户的输入
    response = query_wenxin_model(user_input)
    return response.get("answer", "抱歉，我无法理解您的问题")