BEL Export of Hetionet
======================
The `Biological Expression Language (BEL) <http://bel.bio>`_ is a domain specific language that enables the expression of
biological relationships in a machine-readable format. It is supported by the `PyBEL <https://github.com/pybel/pybel>`_
software ecosystem.

Differences from standard Hetionet
----------------------------------
- Edges have been mapped to BEL
- Molecular Activities and Cellular Components can't easily be represented in BEL, and are therefore removed

Files
-----
BEL Script
~~~~~~~~~~
BEL Script is the *de facto* standard for BEL, which all BEL-aware applications should be able to consume.
It contains informations about the nodes, edges, and their biological context in a domain-specific language.
It can be parsed with PyBEL or other BEL parsers.

Example opening BEL Script using `pybel.from_bel_script() <https://pybel.readthedocs.io/en/latest/reference/io.html#pybel.from_bel_script>`_:

.. code-block:: python

    import gzip
    from pybel import from_bel_script
    with gzip.open('hetionet-v1.0.bel.gz') as file:
        graph = from_bel_script(file)



Nodelink JSON
~~~~~~~~~~~~~
Node-link is the format popularized by Javascript frameworks like D3 for representing network
information. Since the main data structire in PyBEL is a network, it often makes sense to use
Nodelink JSON as a pre-compiled data structure for BEL (since parsing/compiling BEL takes a
lot longer than JSON). The schema is specific to PyBEL, but this is the fastest to load.

Example opening Nodelink JSON using `pybel.from_nodelink_gz() <https://pybel.readthedocs.io/en/latest/reference/io.html#pybel.from_nodelink_gz>`_:

.. code-block:: python

    from pybel import from_nodelink_gz
    graph = from_nodelink_gz('hetionet-v1.0.bel.nodelink.json.gz')

GraphDati JSON
~~~~~~~~~~~~~~
GraphDati JSON is another JSON schema used for BEL by the `BEL.bio <https://bel.bio/>`_
and `BioDati <https://studio.demo.biodati.com/home>`_ projects (note: username/password
for the demo server are demo/demo). Graphs in this format can be uploaded to the BioDati
API (or `pybel.post_graphdati()` can be used as a client for the BioDati API)

Example opening GraphDati JSON using `pybel.from_graphdati_gz() <https://pybel.readthedocs.io/en/latest/reference/io.html#pybel.from_graphdati_gz>`_:

.. code-block:: python

    from pybel import from_graphdati_gz
    graph = from_graphdati_gz('hetionet-v1.0.bel.graphdati.json.gz')
