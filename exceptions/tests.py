# backend/exceptions/tests.py
from django.test import TestCase


class CustomExceptionTest(TestCase):

    def test_exception_handling(self):
        try:
            raise ValueError("Test Exception")
        except ValueError as e:
            self.assertEqual(str(e), "Test Exception")
