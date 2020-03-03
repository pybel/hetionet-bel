BEL Export of Hetionet
======================
This repository contains exports of `Hetionet <https://github.com/hetio/hetionet>`_
as `Biological Expression Language (BEL) <http://bel.bio>`_.

BEL is a domain specific language that enables the expression of biological relationships
in a machine-readable format. It is supported by the `PyBEL <https://github.com/pybel/pybel>`_
software ecosystem.

Download Hetionet as BEL
------------------------
The network is available in three BEL formats (see descriptions below):

- **BEL Script**
- **Nodelink JSON**
- **GraphDati JSON**

Cloning
~~~~~~~
Large files in this repository are stored using `Git LFS <https://git-lfs.github.com/>`_.
When cloning this repository, please make sure that Git LFS is installed on your system.
Otherwise, git will checkout text pointers for large files rather than the large files
themselves!

Differences from standard Hetionet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Edges have been mapped to BEL
- Molecular Activities and Cellular Components can't easily be represented in BEL, and are therefore removed

License
-------
This repository redistributes content from `hetio/hetionet <https://github.com/hetio/hetionet>`_
and is licensed in the same way. See the `License <https://github.com/hetio/hetionet#license>`_
section of the original Hetionet repository and moore information
on `Thinklab <https://thinklab.com/discussion/integrating-resources-with-disparate-licensing-into-an-open-network/107>`_.

Format Descriptions
-------------------
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

Example opening Nodelink JSON using `pybel.from_nodelink_gz()
<https://pybel.readthedocs.io/en/latest/reference/io.html#pybel.from_nodelink_gz>`_:

.. code-block:: python

    from pybel import from_nodelink_gz
    graph = from_nodelink_gz('hetionet-v1.0.bel.nodelink.json.gz')

GraphDati JSON
~~~~~~~~~~~~~~
GraphDati JSON is another JSON schema used for BEL by the `BEL.bio <https://bel.bio/>`_
and `BioDati <https://studio.demo.biodati.com/home>`_ projects (note: username/password
for the demo server are demo/demo).

In general, BEL graphs can be exported to GraphDati JSON then uploaded to BioDati via its
`API <https://nanopubstore.demo.biodati.com>`_. Note, this address will be different for
your instance of BioDati. More directly, BEL graphs in PyBEL can be uploaded
programatically with ``pybel.post_graphdati()``.
