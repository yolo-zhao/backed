# orders/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer

class OrderList(APIView):
    def get(self, request):
        orders = Order.objects.all()  # 查询所有订单
        serializer = OrderSerializer(orders, many=True)  # 使用序列化器将订单列表转换为 JSON 格式
        return Response(serializer.data)  # 返回 JSON 数据
