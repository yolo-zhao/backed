# warehouses/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Warehouse
from .serializers import WarehouseSerializer

class WarehouseList(APIView):
    def get(self, request):
        warehouses = Warehouse.objects.all()  # 查询所有仓库
        serializer = WarehouseSerializer(warehouses, many=True)  # 将仓库数据转换为 JSON 格式
        return Response(serializer.data)  # 返回 JSON 数据
