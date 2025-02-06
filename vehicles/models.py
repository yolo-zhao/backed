# vehicles/models.py
from django.db import models

class Vehicle(models.Model):
    vehicle_id = models.IntegerField(primary_key=True)  # 车辆唯一标识
    current_location = models.CharField(max_length=100)  # 车辆当前位置

    def __str__(self):
        return f"Vehicle {self.vehicle_id} - {self.current_location}"
