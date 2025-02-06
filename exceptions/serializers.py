# exceptions/serializers.py
from rest_framework import serializers
from .models import LogisticsException

class LogisticsExceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogisticsException
        fields = ['exception_id', 'order_id', 'exception_detail']
