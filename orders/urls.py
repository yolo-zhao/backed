# orders/urls.py
from django.urls import path
from .views import OrderList

urlpatterns = [
    path('orders/', OrderList.as_view(), name='order-list'),  # 订单列表的 URL 路径
]
