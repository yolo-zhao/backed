# agent/urls.py
from django.urls import path
from .views import QueryLogList

urlpatterns = [
    path('query-logs/', QueryLogList.as_view(), name='query-log-list'),  # 查询日志的 URL 路径
]
