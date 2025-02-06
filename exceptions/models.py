# exceptions/models.py
from django.db import models

class LogisticsException(models.Model):
    exception_id = models.IntegerField(primary_key=True)  # 异常唯一标识
    order_id = models.ForeignKey('orders.Order', on_delete=models.CASCADE)  # 关联订单
    description = models.TextField()  # 异常描述
    date_reported = models.DateTimeField(auto_now_add=True)  # 异常报告时间

    def __str__(self):
        return f"Exception {self.exception_id} - Order {self.order_id.order_id}"
