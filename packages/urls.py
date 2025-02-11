from django.urls import path
from . import views

urlpatterns = [
    path('query/<str:package_id>/', views.PackageDetailView.as_view(), name='package_detail'),
]
