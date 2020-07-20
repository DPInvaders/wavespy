import unittest
from unittest.mock import patch

import base58

from wavespy import WavesClient
from wavespy.utils import WavesAddress
from wavespy.utils import WavesAddressGenerator
from wavespy.utils import WavesAsyncAddress


class AddressGeneratorTest(unittest.TestCase):

    def setUp(self):
        self.address_generator = WavesAddressGenerator()

    def test_generating_class(self):
        address = self.address_generator.generate()
        self.assertIsInstance(address, WavesAddress)
        address = self.address_generator.generate()
        self.assertNotIsInstance(address, WavesAsyncAddress)

    def test_address_client(self):
        address = self.address_generator.generate()
        self.assertIsInstance(getattr(address, '_api_client'), WavesClient)


class AddressMethodsTest(unittest.TestCase):

    @patch('wavespy.utils.address.WavesAddress')
    def test_address_from_alias(self, mocked_address):
        address = mocked_address()
        address.from_alias.return_value = None
        result = address.from_alias('wavesalias')
        self.assertIs(None, result)

    def test_offline_address(self):
        address_generator = WavesAddressGenerator()
        address = address_generator.generate(online=False)
        balance_result = address.get_balance()
        self.assertIsInstance(balance_result, dict)
        transfer_result = address.transfer_waves('3P9omatqc8CMnZLSrY8XEcDRwB1rxdgrqEb', 1000, attachment="test")
        self.assertIsInstance(transfer_result, dict)

    def test_base58_seed_encode(self):
        address_generator = WavesAddressGenerator()
        address = address_generator.generate()
        self.assertEqual(address.base58_seed, base58.b58encode(address.seed.encode('latin-1')).decode())

