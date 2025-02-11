# orders/models.py
from django.db import models

class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)  # 订单唯一标识
    user_id = models.IntegerField()  # 用户唯一标识
    package_type = models.CharField(max_length=50)  # 包裹类型
    status = models.CharField(max_length=50)  # 当前订单状态

    def __str__(self):
        return f"Order {self.order_id} - {self.status}"


class Package:
    pass

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name