import unittest

from src.app import app


class TestMetricsEndpoint(unittest.TestCase):
    """Test cases for the /metrics endpoint."""

    def setUp(self):
        """Set up test client."""
        self.app = app
        self.client = self.app.test_client()
        self.app.testing = True

    def test_metrics_endpoint_exists(self):
        """Test that /metrics endpoint exists and returns 200."""
        response = self.client.get('/metrics')
        self.assertEqual(response.status_code, 200)

    def test_metrics_endpoint_returns_prometheus_text(self):
        """Test that /metrics returns Prometheus text format."""
        response = self.client.get('/metrics')
        self.assertTrue(response.content_type.startswith('text/plain'))

    def test_metrics_endpoint_includes_http_metrics(self):
        """Test that /metrics includes HTTP request metrics."""
        self.client.get('/version')
        response = self.client.get('/metrics')
        body = response.data.decode('utf-8')
        self.assertIn('http_requests_total', body)
        self.assertIn('http_request_duration_seconds', body)
