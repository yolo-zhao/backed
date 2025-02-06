# vehicles/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Vehicle
from .serializers import VehicleSerializer

class VehicleList(APIView):
    def get(self, request):
        vehicles = Vehicle.objects.all()  # 查询所有车辆
        serializer = VehicleSerializer(vehicles, many=True)  # 将车辆数据转换为 JSON 格式
        return Response(serializer.data)  # 返回 JSON 数据
