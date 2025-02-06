# warehouses/urls.py
from django.urls import path
from .views import WarehouseList

urlpatterns = [
    path('warehouses/', WarehouseList.as_view(), name='warehouse-list'),  # 仓库列表的 URL 路径
]
