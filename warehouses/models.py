# warehouses/models.py
from django.db import models


class Warehouse(models.Model):
    warehouse_id = models.AutoField(primary_key=True)  # 自动生成主键
    inventory = models.IntegerField()  # 仓库库存


    def __str__(self):
        return f"Warehouse {self.warehouse_id} - Inventory: {self.inventory}"