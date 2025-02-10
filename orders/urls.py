# orders/urls.py
from django.urls import path,include
from .views import order_list, order_detail  # 确保使用正确的视图名称
from . import views  # 确保正确导入

urlpatterns = [
    path('', order_list, name='order_list'),  # 处理 /api/orders/
    path('<int:pk>/', order_detail, name='order_detail'),  # 处理 /api/orders/<int:pk>/
    # 其他路由...
    path('api/query-order-status/', views.order_status_query, name='order_status_query'),
    path('<int:order_id>/', views.QueryOrderStatus.as_view(), name='order_status_query'),
]