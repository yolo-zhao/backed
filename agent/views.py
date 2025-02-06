# agent/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import QueryLog
from .serializers import QueryLogSerializer

class QueryLogList(APIView):
    def get(self, request):
        query_logs = QueryLog.objects.all()  # 查询所有查询日志
        serializer = QueryLogSerializer(query_logs, many=True)  # 将查询日志转换为 JSON 格式
        return Response(serializer.data)  # 返回 JSON 数据
