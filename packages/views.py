from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Package
from .serializers import PackageSerializer

class PackageDetailView(APIView):
    def get(self, request, package_id, format=None):
        try:
            package = Package.objects.get(package_id=package_id)
        except Package.DoesNotExist:
            return Response({"error": "Package not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PackageSerializer(package)
        return Response(serializer.data, status=status.HTTP_200_OK)
