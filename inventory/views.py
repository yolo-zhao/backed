from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from django.http import JsonResponse
from django.core.paginator import Paginator


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

    # 1. 如果查询参数为空，返回错误提示
    if not query:
        return JsonResponse({'error': '查询参数不能为空'}, status=400)

    try:
        # 2. 查询商品列表
        products = Product.objects.filter(name__icontains=query).order_by('name')  # 查询包含关键词的商品

        # 3. 如果没有找到商品，返回提示
        if not products.exists():
            return JsonResponse({'products': [], 'total_pages': 0}, status=200)

        # 分页：每页显示 10 个商品
        page_number = request.GET.get('page', 1)  # 获取当前页
        paginator = Paginator(products, 10)  # 分页，每页 10 个商品
        page_obj = paginator.get_page(page_number)

        # 4. 使用序列化器来序列化数据
        serializer = ProductSerializer(page_obj, many=True)

        # 5. 返回查询结果
        return JsonResponse({
            'products': serializer.data,  # 返回序列化后的产品数据
            'page': page_number,
            'total_pages': paginator.num_pages
        }, status=200)

    except Exception as e:
        # 6. 如果发生其他错误，返回错误信息
        return JsonResponse({'error': str(e)}, status=500)
