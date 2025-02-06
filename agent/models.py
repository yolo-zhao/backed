# agent/models.py
from django.db import models

class QueryLog(models.Model):
    query_id = models.IntegerField(primary_key=True)  # 查询唯一标识
    user_id = models.IntegerField()  # 用户唯一标识
    query_text = models.CharField(max_length=255)  # 用户查询内容
    timestamp = models.DateTimeField(auto_now_add=True)  # 查询时间

    def __str__(self):
        return f"Query {self.query_id} - User {self.user_id} - {self.query_text}"
