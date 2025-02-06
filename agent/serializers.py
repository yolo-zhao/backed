# agent/serializers.py
from rest_framework import serializers
from .models import QueryLog

class QueryLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueryLog
        fields = ['query_id', 'user_id', 'query_content']
