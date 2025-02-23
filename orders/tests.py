from django.test import TestCase
from .models import Product
from django.urls import reverse


class InventoryQueryTests(TestCase):
    def setUp(self):
        # 创建测试商品数据
        Product.objects.create(name="Product A", price=100, quantity=50)
        Product.objects.create(name="Product B", price=150, quantity=30)

    def test_query_inventory_success(self):
        response = self.client.get(reverse('query_inventory') + '?query=Product')
        self.assertEqual(response.status_code, 200)
        self.assertIn('products', response.json())

    def test_query_inventory_empty(self):
        response = self.client.get(reverse('query_inventory') + '?query=Nonexistent')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['products'], [])  # 检查返回的 products 为空列表

    def test_query_inventory_no_query(self):
        response = self.client.get(reverse('query_inventory'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['error'], '查询参数不能为空')

    def test_query_inventory_pagination(self):
        response = self.client.get(reverse('query_inventory') + '?query=Product&page=1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('products', response.json())
        self.assertIn('total_pages', response.json())

    def test_query_inventory_sorting(self):
        response = self.client.get(reverse('query_inventory') + '?query=Product&sort_by=price')
        self.assertEqual(response.status_code, 200)
        self.assertIn('products', response.json())
