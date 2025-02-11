from django.urls import path
from . import views
from .views import query_inventory  # 确保 views.py 中有这个视图

urlpatterns = [
    path('query/<int:product_id>/', views.ProductDetailView.as_view(), name='product_detail'),  # 商品库存查询
    path('inventory/query/', query_inventory, name='query_inventory'),  # 确保 URL 配置正确
]
