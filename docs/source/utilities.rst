Utilities
=========

With :mod:`wavespy.utils` you can easily create or verify Waves addresses, generate
transaction data and simplify API requests.


Addresses
---------

With :class:`~wavespy.utils.address.WavesAddress` you can create, sign and broadcast transactions.
For example Waves transfer transaction:

.. code:: python

    from wavespy.utils import WavesAddress
    address = WavesAddress('address_base58_value', 'address_private_key')
    print(address.transfer_waves('recipient_address', 1000))

Also it can be used to receive information from node, e.g. balance:

.. code:: python

    from wavespy.utils import WavesAddress
    address = WavesAddress('address_base58_value', 'address_private_key')
    print(address.get_balance())


:class:`~wavespy.utils.address.AsyncWavesAddress` provides the same functionality as
:class:`~wavespy.utils.address.WavesAddress` but with asynchronous API client:

.. code:: python

    from wavespy.utils import WavesAddress
    address = AsyncWavesAddress('address_base58_value', 'address_private_key')
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(
        address.transfer_waves('recipient_address', 1000))
    print(result)

Address generator
-----------------

:class:`~wavespy.utils.address.WavesAddressGenerator` provides functionality for address
creation and verification. Create new Waves address:

.. code:: python

    from wavespy.utils import WavesAddressGenerator
    new_address = WavesAddressGenerator()

Create from existing seed, private or public key:

.. code:: python

    address = WavesAddressGenerator().generate(seed="your_seed_here")
    address = WavesAddressGenerator().generate(private_key="your_private_key")
    address = WavesAddressGenerator().generate(public_key="your_public_key")

Validate address and get address object:

.. code:: python

    address_generator = WavesAddressGenerator()
    address = address_generator.generate(value="address", private_key="your_private_key",
                                         public_key="your_public_key")

By default :meth:`~wavespy.utils.address.WavesAddressGenerator.generate` returns :class:`.WavesAddress` object. If you
need address object with async API client :class:`~wavespy.utils.address.WavesAsyncAddress`

.. code:: python

    async_generator = WavesAddressGenerator(async_address=True)
    new_async_address = async_generator.generate()
