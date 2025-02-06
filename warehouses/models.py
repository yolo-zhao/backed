# warehouses/models.py
from django.db import models

class Warehouse(models.Model):
    warehouse_id = models.IntegerField(primary_key=True)  # 仓库唯一标识
    inventory = models.IntegerField()  # 仓库库存

    def __str__(self):
        return f"Warehouse {self.warehouse_id} - Inventory: {self.inventory}"
