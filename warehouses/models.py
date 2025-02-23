from django.db import models

class Warehouse(models.Model):
    warehouse_id = models.AutoField(primary_key=True)  # 或者直接使用 Django 默认的 id

    name = models.CharField(max_length=100, default="Unknown")  # 仓库名称
    location = models.CharField(max_length=255, default="Unknown")  # 仓库位置
    capacity = models.IntegerField(default=0)  # 仓库容量
    inventory = models.IntegerField(default=0)  # 库存数量，假设是一个整数

    class Meta:
        db_table = 'warehouses_warehouse'  # 确保表名正确v

    def __str__(self):
        return f"Warehouse {self.warehouse_id} - Inventory: {self.inventory}"
