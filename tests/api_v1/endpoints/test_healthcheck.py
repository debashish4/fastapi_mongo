import unittest
from fastapi.testclient import TestClient

from main import app


class HealthCheckTestCase(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_healthcheck_ok(self):
        response = self.client.get('/api/v1/healthcheck')
        self.assertEqual(response.status_code, 200)
