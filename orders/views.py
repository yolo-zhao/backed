from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Order, Package
from .serializers import OrderSerializer
from django.http import JsonResponse



@api_view(['GET', 'POST'])
def order_list(request):
    """
    处理 /api/orders/ 路由：
    - GET: 获取所有订单列表
    - POST: 创建新的订单
    """
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def order_detail(request, pk):
    """
    处理 /api/orders/<int:pk>/ 路由：
    - GET: 获取特定订单
    - PUT: 更新订单信息
    - DELETE: 删除订单
    """
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
def order_status_query(request):
    return JsonResponse({"message": "Order status query working!"})
class QueryOrderStatus(APIView):
    def get(self, request, order_id, *args, **kwargs):
        try:
            package = Package.objects.get(order_id=order_id)
            return Response({
                'order_id': package.order_id,
                'user_id': package.user_id,
                'package_type': package.package_type,
                'status': package.status,
                'estimated_arrival': package.estimated_arrival
            }, status=status.HTTP_200_OK)
        except Package.DoesNotExist:
            return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)