# agent/urls.py
from django.urls import path
from .views import QueryLogView, RecommendView, LocationView

urlpatterns = [
    path('query-log/', QueryLogView.as_view(), name='query-log'),  # 查询日志接口
    path('recommend/', RecommendView.as_view(), name='recommend'),  # 商品推荐接口
    path('location/', LocationView.as_view(), name='location'),    # 货物位置接口
]
