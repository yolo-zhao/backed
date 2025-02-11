"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.http import JsonResponse

# 主页视图（可用于API首页）
def home_view(request):
    return JsonResponse({'message': 'Welcome to the Backend API!'})

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin
    path('api/', include('api.urls')),  # 这里引入 api.urls
    path('', home_view),  # 主页
    path('api/inventory/', include('inventory.urls')),  # 引入库存查询的 URL 路由
]
