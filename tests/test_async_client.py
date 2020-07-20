import asyncio
from aiohttp import web
from unittest.mock import patch

from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop

from wavespy.async_client import WavesAsyncClientResponse, WavesAsyncClient
from wavespy.client import WavesClientResponse
from wavespy.utils import WavesAddressGenerator


class WavesAsyncClientTest(AioHTTPTestCase):

    def setUp(self):
        super().setUp()
        address = "http://{}:{}".format(self.server.host, self.server.port)
        self.api_client = WavesAsyncClient(node_address=address, matcher_address=address)

    async def get_application(self):

        async def node_version(request):
            return web.json_response({"version": "v99999"})

        async def matcher_public_key(request):
            return web.json_response("public_key")

        app = web.Application()
        app.router.add_get('/node/version', node_version)
        app.router.add_get('/matcher', matcher_public_key)
        return app

    @unittest_run_loop
    async def test_node_request_response(self):
        node_version_response = await self.api_client.node_version()
        self.assertIsInstance(node_version_response, WavesClientResponse)
        self.assertTrue(node_version_response)
        self.assertEqual(node_version_response.response_data, {"version": "v99999"})

    @unittest_run_loop
    async def test_matcher_request_response(self):
        node_version_response = await self.api_client.matcher()
        self.assertIsInstance(node_version_response, WavesClientResponse)
        self.assertTrue(node_version_response)
        self.assertEqual(node_version_response.response_data, "public_key")

    @patch('wavespy.async_client.WavesAsyncClient')
    def test_mocked_request_response(self, mocked_client):
        client = mocked_client()
        data = {"version": "v99999"}
        request_future = self.loop.create_future()
        request_future.set_result(
            WavesAsyncClientResponse(successful=True, endpoint='/node/version', response_data=data)
        )
        client.node_version.return_value = request_future
        node_version_response = self.loop.run_until_complete(client.node_version())
        self.assertIsInstance(node_version_response, WavesClientResponse)
        self.assertTrue(node_version_response)
        self.assertEqual(node_version_response.response_data, data)
        self.assertEqual(node_version_response.endpoint, '/node/version')

    @unittest_run_loop
    async def test_offline_client(self):
        client = WavesAsyncClient(online=False)
        request = await client.node_version()
        self.assertIsInstance(request, dict)
        self.assertIn('url', request)
        self.assertIn('headers', request)

    @unittest_run_loop
    async def test_client_session_context(self):
        client = self.api_client
        current_session = client.session
        await client.node_version()
        self.assertIs(client.session, current_session)
        await client.close_session()
        self.assertIsNone(self.api_client.session)

    @unittest_run_loop
    async def test_client_session_context(self):
        async with self.api_client as context_client:
            current_session = context_client.session
            await context_client.node_version()
            self.assertIs(context_client.session, current_session)

        self.assertIsNone(self.api_client.session)
        await self.api_client.node_version()
        self.assertIsNone(self.api_client.session)

    @unittest_run_loop
    async def test_offline_async_client(self):
        client = WavesAsyncClient(online=False)
        request = await client.node_version()
        self.assertIsInstance(request, dict)
        self.assertIn('url', request)
        self.assertIn('headers', request)

    @unittest_run_loop
    async def test_offline_address(self):
        address_generator = WavesAddressGenerator(async_address=True)
        address = address_generator.generate(online=False)
        balance_result = await address.get_balance()
        self.assertIsInstance(balance_result, dict)
        transfer_result = await address.transfer_waves('3P9omatqc8CMnZLSrY8XEcDRwB1rxdgrqEb', 1000, attachment="test")
        self.assertIsInstance(transfer_result, dict)
