# orders/urls.py
from django.urls import path
from .views import order_list, order_detail  # 确保使用正确的视图名称

urlpatterns = [
    path('', order_list, name='order_list'),  # 处理 /api/orders/
    path('<int:pk>/', order_detail, name='order_detail'),  # 处理 /api/orders/<int:pk>/
]

