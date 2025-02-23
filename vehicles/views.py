# vehicles/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Vehicle
from .serializers import VehicleSerializer
from django.http import JsonResponse
from .models import Vehicle  # 假设 Vehicle 模型包含车辆信息
from rest_framework import viewsets


# 通过车辆ID获取车辆状态详情

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
