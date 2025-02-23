# backend/packages/tests.py
from django.test import TestCase
from .models import Package

class PackageModelTest(TestCase):
    def test_package_creation(self):
        # 创建一个包裹
        package = Package.objects.create(name="Package A", description="A test package")
        self.assertEqual(package.name, "Package A")  # 检查name字段
        self.assertEqual(package.description, "A test package")  # 检查description字段
