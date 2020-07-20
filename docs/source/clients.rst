API clients
===========

``wavespy`` provides sync client :class:`.WavesClient` and async :class:`.WavesAsyncClient`

Sync client
-----------

To make a request with sync client:

.. code:: python

        from wavespy.client import WavesClient

        client = WavesClient()
        node_version = client.node_version()

If request is successful you can get response data:


.. code:: python

        print(node_version.response_data)

Get response data items or iterate over response data:

.. code:: python

        print(node_version['version'])

Async client
------------

To make a request with async client:


.. code:: python

        import asyncio
        from wavespy.client import WavesAsyncClient

        async_client = WavesAsyncClient()
        node_version = asyncio.run(async_client.node_version())


Session reuse
-------------

By default API requests made in a new session. You can reuse same session with
:meth:`~wavespy.client.WavesClient.start_session` method:

.. code:: python

    import requests
    from wavespy import WavesClient

    client = WavesClient()
    client.start_session()
    node_version = client.node_version()
    node_time = client.utils_time()
    client.close_session()

For async:

.. code:: python

    import asyncio
    from aiohttp import ClientSession
    from wavespy import WavesAsyncClient

    loop = asyncio.get_event_loop()
    async_client = WavesAsyncClient()
    loop.run_until_complete(async_client.start_session())
    node_version = loop.run_until_complete(async_client.node_version())
    node_time = loop.run_until_complete(async_client.utils_time())
    loop.run_until_complete(async_client.close_session())


Or using context. For sync client:

.. code:: python

    from wavespy import WavesClient

    with WavesClient() as client:
        node_version = client.node_version()
        node_time = client.utils_time()


For async client:

.. code:: python

    import asyncio
    from wavespy import WavesAsyncClient

    async def get_data():
        async with WavesAsyncClient() as async_client:
            node_version = await async_client.node_version()
            node_time = await async_client.utils_time()

        return (node_version, node_time)

    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(get_data())

