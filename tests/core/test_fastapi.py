import unittest
from fastapi.testclient import TestClient

from core.fastapi import CustomFastAPI


class CustomFastAPITestCase(unittest.TestCase):

    def setUp(self):
        self.app = CustomFastAPI()
        self.client = TestClient(self.app)

    def test_openapi_has_servers_key(self):
        """
        Tests that CustomFastAPI adds servers key to the openapi
        configuration.
        """
        response = self.client.get('/openapi.json')
        openapi = response.json()
        self.assertTrue("servers" in openapi)
        self.assertEqual(response.status_code, 200)

