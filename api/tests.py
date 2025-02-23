# backend/api/tests.py
from django.test import TestCase
from .models import APIModel  # 假设你有一个API模型
from django.urls import reverse


class APITest(TestCase):

    def test_api_response(self):
        response = self.client.get('/api/some_views')
        self.assertEqual(response.status_code, 200)
