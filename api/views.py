# import re
# from django.http import JsonResponse
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import Order, Vehicle, Warehouse, Product
# from .serializers import OrderSerializer, VehicleSerializer, WarehouseSerializer
#
# # API 总览
# @api_view(['GET'])
# def api_overview(request):
#     api_urls = {
#         'List Orders': '/api/orders/',
#         'Order Detail': '/api/orders/<int:pk>/',
#         'Create Order': '/api/orders/',  # 支持 POST
#     }
#     return Response(api_urls)
#
# # 获取所有订单列表
# @api_view(['GET', 'POST'])
# def order_list(request):
#     if request.method == 'GET':
#         orders = Order.objects.all()
#         serializer = OrderSerializer(orders, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# # 获取所有车辆列表
# @api_view(['GET', 'POST'])
# def vehicle_list(request):
#     if request.method == 'GET':
#         vehicles = Vehicle.objects.all()
#         serializer = VehicleSerializer(vehicles, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = VehicleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# # 获取所有仓库列表
# @api_view(['GET', 'POST'])
# def warehouse_list(request):
#     if request.method == 'GET':
#         warehouses = Warehouse.objects.all()
#         serializer = WarehouseSerializer(warehouses, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = WarehouseSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# # 查询任务状态
# @api_view(['GET'])
# def order_status_query(request):
#     query = request.GET.get('query', '')
#     if '包裹' in query and '状态' in query:
#         order_id_match = re.search(r'\d+', query)
#         if order_id_match:
#             order_id = order_id_match.group(0)
#             order = Order.objects.filter(order_id=order_id).first()
#             if order:
#                 return JsonResponse({
#                     'order_id': order.order_id,
#                     'status': order.status,
#                     'message': f"您的包裹 {order_id} 当前状态是: {order.status}"
#                 })
#             else:
#                 return JsonResponse({'message': '未找到此订单'}, status=404)
#         else:
#             return JsonResponse({'message': '请输入有效的订单ID'}, status=400)
#     return JsonResponse({'message': '无效查询'}, status=400)
#
# # 商品推荐 API
# class RecommendationAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         order_id = request.query_params.get('order_id')
#         user_id = request.query_params.get('user_id')
#         recommendations = self.get_recommendations(order_id, user_id)
#         return Response(recommendations, status=status.HTTP_200_OK)
#
#     def get_recommendations(self, order_id, user_id):
#         # 模拟推荐数据
#         recommendations = [
#             {
#                 "item_name": "高性能笔记本电脑",
#                 "item_description": "适合学生和办公使用，超长电池续航",
#                 "item_price": 4999,
#                 "item_link": "https://example.com/laptop"
#             },
#             {
#                 "item_name": "无线耳机",
#                 "item_description": "高音质无线耳机，适合运动使用",
#                 "item_price": 799,
#                 "item_link": "https://example.com/headphone"
#             }
#         ]
#         return recommendations
#
# # 发送通知 API
# class NotificationAPIView(APIView):
#     def post(self, request, *args, **kwargs):
#         user_id = request.data.get('user_id')
#         message = request.data.get('message')
#         self.send_notification(user_id, message)
#         return Response({'status': 'success'}, status=status.HTTP_200_OK)
#
#     def send_notification(self, user_id, message):
#         # 模拟发送通知
#         print(f"Sending notification to user {user_id}: {message}")
#
# # 库存查询 API
# @api_view(['GET'])
# def query_inventory(request):
#     query = request.GET.get('query', '')
#     if query:
#         products = Product.objects.filter(name__icontains=query)
#         product_list = list(products.values())
#         return JsonResponse(product_list, safe=False)
#     else:
#         return JsonResponse({"error": "No query parameter provided"}, status=400)
# @api_view(['GET'])
# def order_detail(request, pk):
#     try:
#         order = Order.objects.get(pk=pk)
#         data = {
#             'order_id': order.order_id,
#             'status': order.status,
#             'created_at': order.created_at,
#         }
#         return JsonResponse(data)
#     except Order.DoesNotExist:
#         return JsonResponse({'message': 'Order not found'}, status=404)
# def some_view(request):
#     return JsonResponse({'message': 'success'})










import re
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Order, Vehicle, Warehouse, Product
from .serializers import OrderSerializer, VehicleSerializer, WarehouseSerializer

# API 总览
@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List Orders': '/api/orders/',
        'Order Detail': '/api/orders/<int:pk>/',
        'Create Order': '/api/orders/',  # 支持 POST
    }
    return Response(api_urls)

# 获取所有订单列表
@api_view(['GET', 'POST'])
def order_list(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 获取所有车辆列表
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

# 获取所有仓库列表
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

# 查询包裹状态
@api_view(['GET'])
def order_status_query(request):
    query = request.GET.get('query', '').strip()
    if '包裹' in query and '状态' in query:
        order_id_match = re.search(r'\d+', query)
        if order_id_match:
            order_id = order_id_match.group(0)
            order = Order.objects.filter(order_id=order_id).first()
            if order:
                return JsonResponse({
                    'order_id': order.order_id,
                    'status': order.status,
                    'message': f"您的包裹 {order_id} 当前状态是: {order.status}"
                })
            else:
                return JsonResponse({'message': '未找到此订单'}, status=404)
        else:
            return JsonResponse({'message': '请输入有效的订单ID'}, status=400)
    return JsonResponse({'message': '无效查询'}, status=400)

# 商品推荐 API
class RecommendationAPIView(APIView):
    def get(self, request, *args, **kwargs):
        order_id = request.query_params.get('order_id')  # 获取订单ID作为参考
        user_id = request.query_params.get('user_id')    # 获取用户ID作为参考
        recommendations = self.get_recommendations(order_id, user_id)
        return Response(recommendations, status=status.HTTP_200_OK)

    def get_recommendations(self, order_id, user_id):
        # 这里可以添加真实的推荐逻辑，比如查询数据库或者根据历史订单推算
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

# 发送通知 API
class NotificationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        message = request.data.get('message')
        self.send_notification(user_id, message)
        return Response({'status': 'success'}, status=status.HTTP_200_OK)

    def send_notification(self, user_id, message):
        # 模拟发送通知
        print(f"Sending notification to user {user_id}: {message}")

# 库存查询 API
@api_view(['GET'])
def query_inventory(request):
    query = request.GET.get('query', '').strip()
    if query:
        products = Product.objects.filter(name__icontains=query)
        product_list = list(products.values())
        return JsonResponse(product_list, safe=False)
    else:
        return JsonResponse({"error": "没有提供查询参数"}, status=400)

# 查询订单详情
@api_view(['GET'])
def order_detail(request, pk):
    try:
        order = Order.objects.get(pk=pk)
        data = {
            'order_id': order.order_id,
            'status': order.status,
            'created_at': order.created_at,
        }
        return JsonResponse(data)
    except Order.DoesNotExist:
        return JsonResponse({'message': '订单未找到'}, status=404)

def some_view(request):
    return JsonResponse({'message': 'success'})

