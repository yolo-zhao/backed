from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)  # 商品名称
    description = models.TextField()  # 商品描述
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 商品价格
    stock = models.IntegerField(null=True)  # 商品库存数量
    quantity = models.IntegerField(default=0)  # 确保定义了 quantity 字段

    def __str__(self):
        return self.name
