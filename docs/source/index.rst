.. wavespy documentation master file, created by
   sphinx-quickstart on Tue Sep  3 14:56:55 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to WavesPy's documentation!
====================================

``wavespy`` is Python API client for Waves node. It provides sync HTTP client based
on `requests <https://2.python-requests.org>`_ module and async based on
`aiohttp <https://docs.aiohttp.org/en/stable/client.html>`_.
Also it has some useful features e.g. Waves address generation and validation, transaction data generation.

wavespy?
---------

Originally `pyacryl2 <https://github.com/acrylplatform/pyacryl2>`_

Installation
------------

.. code:: bash

      pip install wavespy

From source:

.. code:: bash

      python setup.py install

Tests:

From source:

.. code:: bash

      python setup.py test


Making requests to node API
---------------------------

Using sync client:

.. code:: python

      from wavespy.client import WavesClient
      client = WavesClient()
      print(client.node_version())

Or using async client:

.. code:: python

      import asyncio
      from wavespy.async_client import WavesAsyncClient
      client = WavesAsyncClient()

      # Python 3.6
      loop = asyncio.get_event_loop()
      print(loop.run_until_complete(client.node_version()))
      # Python 3.7
      print(asyncio.run(client.node_version()))


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   clients
   utilities
   wavespy_api



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
