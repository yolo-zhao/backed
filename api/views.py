from typing import re

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Order, Vehicle,Warehouse
from .serializers import OrderSerializer, VehicleSerializer, WarehouseSerializer


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List Orders': '/api/orders/',
        'Order Detail': '/api/orders/<int:pk>/',
        'Create Order': '/api/orders/',  # 这里要支持 POST
    }
    return Response(api_urls)


@api_view(['GET', 'POST'])  # 确保 DRF 视图装饰器正确应用
def order_list(request):
    print("Request method:", request.method)  # 添加这一行调试
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print("Received POST data:", request.data)  # 这里也添加调试信息
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def vehicle_list(request):
    if request.method == 'GET':
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def warehouse_list(request):
    if request.method == 'GET':
        warehouses = Warehouse.objects.all()
        serializer = WarehouseSerializer(warehouses, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = WarehouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def order_detail():
    return None


def api_overview():
    return None


def order_status_query(request):
    # 获取用户查询的关键词（例如"我的包裹在哪"）
    query = request.GET.get('query', '')

    # 简单的关键词匹配规则
    if '包裹' in query and '状态' in query:
        # 获取订单ID
        order_id = re.search(r'\d+', query)
        if order_id:
            order = Order.objects.filter(order_id=order_id.group(0)).first()
            if order:
                return JsonResponse({
                    'order_id': order.order_id,
                    'status': order.status,
                    'message': f"您的包裹 {order_id.group(0)} 当前状态是: {order.status}"
                })
            else:
                return JsonResponse({'message': '未找到此订单'}, status=404)
        else:
            return JsonResponse({'message': '请输入有效的订单ID'}, status=400)

    return JsonResponse({'message': '无效查询'}, status=400)
class RecommendationAPIView(APIView):
    def get(self, request, *args, **kwargs):
        order_id = request.query_params.get('order_id')
        user_id = request.query_params.get('user_id')
        recommendations = self.get_recommendations(order_id, user_id)
        return Response(recommendations, status=status.HTTP_200_OK)

    def get_recommendations(self, order_id, user_id):
        # 模拟推荐数据
        recommendations = [
            {
                "item_name": "高性能笔记本电脑",
                "item_description": "适合学生和办公使用，超长电池续航",
                "item_price": 4999,
                "item_link": "https://example.com/laptop"
            },
            {
                "item_name": "无线耳机",
                "item_description": "高音质无线耳机，适合运动使用",
                "item_price": 799,
                "item_link": "https://example.com/headphone"
            }
        ]
        return recommendations
class NotificationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        message = request.data.get('message')
        # 发送通知的具体实现，可以是推送消息等
        self.send_notification(user_id, message)
        return Response({'status': 'success'}, status=status.HTTP_200_OK)

    def send_notification(self, user_id, message):
        # 这里实现通知发送逻辑
        print(f"Sending notification to user {user_id}: {message}")
