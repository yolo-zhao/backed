# exceptions/urls.py
from django.urls import path
from .views import LogisticsExceptionList

urlpatterns = [
    path('exceptions/', LogisticsExceptionList.as_view(), name='exception-list'),  # 异常列表的 URL 路径
]
