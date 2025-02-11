# vehicles/urls.py
from django.urls import path
from .views import VehicleList
from . import views
urlpatterns = [
    path('vehicles/', VehicleList.as_view(), name='vehicle-list'),  # 车辆列表的 URL 路径
    path('vehicles/<int:pk>/', views.vehicle_detail, name='vehicle_detail'),
]
