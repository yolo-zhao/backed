# vehicles/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Vehicle
from .serializers import VehicleSerializer
from django.http import JsonResponse
from .models import Vehicle  # 假设 Vehicle 模型包含车辆信息
class VehicleList(APIView):
    def get(self, request):
        vehicles = Vehicle.objects.all()  # 查询所有车辆
        serializer = VehicleSerializer(vehicles, many=True)  # 将车辆数据转换为 JSON 格式
        return Response(serializer.data)  # 返回 JSON 数据
# 获取所有车辆状态的视图
def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    vehicle_data = []
    for vehicle in vehicles:
        vehicle_data.append({
            'vehicle_id': vehicle.id,
            'status': vehicle.status,
            'current_location': vehicle.current_location,
            'destination': vehicle.destination,
        })
    return JsonResponse(vehicle_data, safe=False)

# 通过车辆ID获取车辆状态详情
def vehicle_detail(request, pk):
    try:
        vehicle = Vehicle.objects.get(pk=pk)
        vehicle_data = {
            'vehicle_id': vehicle.id,
            'status': vehicle.status,
            'current_location': vehicle.current_location,
            'destination': vehicle.destination,
        }
        return JsonResponse(vehicle_data)
    except Vehicle.DoesNotExist:
        return JsonResponse({'error': 'Vehicle not found'}, status=404)
