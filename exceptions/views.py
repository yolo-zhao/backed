# exceptions/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import LogisticsException
from .serializers import LogisticsExceptionSerializer

class LogisticsExceptionList(APIView):
    def get(self, request):
        exceptions = LogisticsException.objects.all()  # 查询所有异常记录
        serializer = LogisticsExceptionSerializer(exceptions, many=True)  # 将异常记录转换为 JSON 格式
        return Response(serializer.data)  # 返回 JSON 数据
