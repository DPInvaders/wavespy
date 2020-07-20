import unittest

from wavespy import WavesAsyncClient
from wavespy.utils import WavesAddress
from wavespy.utils import WavesAddressGenerator
from wavespy.utils import WavesAsyncAddress


class AsyncAddressGeneratorTest(unittest.TestCase):

    def setUp(self):
        self.address_generator = WavesAddressGenerator(async_address=True)

    def test_generating_class(self):
        address = self.address_generator.generate()
        self.assertIsInstance(address, WavesAsyncAddress)
        address = self.address_generator.generate()
        self.assertNotIsInstance(address, WavesAddress)

    def test_address_client(self):
        address = self.address_generator.generate()
        self.assertIsInstance(getattr(address, '_api_client'), WavesAsyncClient)

