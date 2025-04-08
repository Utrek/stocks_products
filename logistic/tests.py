from unittest import TestCase

from rest_framework.test import APIClient


class My_test(TestCase):
    def test_ok(self):
        self.assertTrue(True)

    def test_sample_view(self):
        url = "/api/v1/"
        client = APIClient()
        response = client.get(url)
        self.assertEqual(response.status_code, second=200)
