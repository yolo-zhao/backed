from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from django.http import JsonResponse

class ProductDetailView(APIView):
    def get(self, request, product_id, format=None):
        try:
            product = Product.objects.get(id=product_id)  # 根据商品ID获取商品信息
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product)  # 将商品信息序列化
        return Response(serializer.data, status=status.HTTP_200_OK)  # 返回商品库存信息


def query_inventory(request):
    query = request.GET.get('query', '')  # 获取查询参数

    if query:
        # 执行查询逻辑
        products = Product.objects.filter(name__icontains=query)  # 查询包含关键词的商品
        product_list = list(products.values())  # 获取查询结果的字段

        return JsonResponse(product_list, safe=False)
    else:
        return JsonResponse({"error": "No query parameter provided"}, status=400)