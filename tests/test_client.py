import unittest
from unittest.mock import patch
from wavespy.client import WavesClientResponse, WavesClient


class WavesClientTest(unittest.TestCase):

    @patch('wavespy.client.WavesClient')
    def test_request_response(self, mocked_client):
        client = mocked_client()
        data = {"version": "v99999"}
        client.node_version.return_value = WavesClientResponse(
            successful=True, endpoint='/node/version', response_data=data
        )
        node_version = client.node_version()
        self.assertIsInstance(node_version, WavesClientResponse)
        self.assertTrue(node_version)
        self.assertEqual(node_version.response_data, data)
        self.assertEqual(node_version.endpoint, '/node/version')

    def test_offline_client(self):
        client = WavesClient(online=False)
        request = client.node_version()
        self.assertIsInstance(request, dict)
        self.assertIn('url', request)
        self.assertIn('headers', request)
