from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
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