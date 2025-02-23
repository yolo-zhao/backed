from django.db import models

class Vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)  # 车辆唯一标识
    name = models.CharField(max_length=100, default="Default Name")  # 车辆名称
    type = models.CharField(max_length=100, default="Default Type")  # 车辆类型
    capacity = models.IntegerField(default=50)  # 车辆容量
    current_location = models.CharField(max_length=100)  # 车辆当前位置



    def __str__(self):
        return f"Vehicle {self.vehicle_id} - {self.current_location}"

