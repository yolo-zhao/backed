from django.conf import settings
import requests  # 替换为正确的导入方式

from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import QueryLog
from .serializers import QueryLogSerializer

# 从 settings.py 中获取文心API的URL和密钥
API_URL = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"  # 文心API URL
API_KEY = settings.WENXIN_API_KEY  # 从 settings.py 获取API密钥


class QueryLogView(APIView):
    """
    用于记录和查询用户的查询日志。
    """

    def get(self, request):
        # 获取用户查询的内容
        user_query = request.GET.get('query')
        if user_query:
            # 调用文心API获取结果
            response = self.call_wenxin_api(user_query)
            return Response({"query_response": response['data']})
        return JsonResponse({"message": "No query provided"}, status=400)

    def call_wenxin_api(self, query):
        """
        调用文心API获取数据
        """
        # 构建请求参数
        params = {
            'api_key': API_KEY,
            'query': query
        }
        # 发送请求
        response = requests.get(API_URL, params=params)
        # 打印返回的数据，以便调试
        print(response.json())
        return response.json()


class RecommendView(APIView):
    """
    用于查询热门商品推荐。
    """

    def get(self, request):
        user_query = request.GET.get('query')
        if user_query:
            # 调用文心API获取热门商品推荐
            response = self.call_wenxin_api(user_query)
            recommended_items = response.get('items', [])  # 获取推荐的商品列表
            return Response({"recommended_items": recommended_items})
        return JsonResponse({"message": "No query provided"}, status=400)

    def call_wenxin_api(self, query):
        """
        调用文心API获取推荐商品
        """
        # 构建请求参数
        params = {
            'api_key': API_KEY,
            'query': query
        }
        # 发送请求获取推荐商品
        response = requests.get(f"{API_URL}/recommend", params=params)
        # 打印返回的数据，以便调试
        print(response.json())
        return response.json()


class LocationView(APIView):
    """
    用于查询货物的当前位置及预计到达时间。
    """

    def get(self, request):
        user_query = request.GET.get('query')
        if user_query:
            # 调用文心API获取货物位置
            location_info = self.get_location_info(user_query)
            return Response({"location": location_info})
        return JsonResponse({"message": "No query provided"}, status=400)

    def get_location_info(self, query):
        """
        根据查询信息获取货物的位置。
        """
        # 模拟的返回位置（实际情况中应该从API返回或根据数据库查询）
        return "Location A, Estimated time: 5 mins"
