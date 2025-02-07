from django.urls import path,include
from .views import api_overview, order_list, vehicle_list, warehouse_list, order_detail

urlpatterns = [
    path('', api_overview, name='api_overview'),  # API 首页
    path('orders/', include('orders.urls')),  # 这里引入 orders.urls
    path('vehicles/', include('vehicles.urls')),
    path('warehouses/', include('warehouses.urls')),
]