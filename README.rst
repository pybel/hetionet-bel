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

Comparison to Original Hetionet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Edges have been mapped to BEL
- Molecular Activities and Cellular Components can't easily be represented in BEL, and are therefore removed

+--------------------------------------------------+------+-------------------------------------------------------------------------------------------------------------------------+
| Hetionet Metaedge                                | Abbr | BEL Edge Example                                                                                                        |
+==================================================+======+=========================================================================================================================+
| Anatomy - downregulates - Gene                   | AdG  | r(ncbigene:153572 ! IRX2) negativeCorrelation pop(uberon:"UBERON:0001296" ! myometrium)                                 |
+--------------------------------------------------+------+-------------------------------------------------------------------------------------------------------------------------+
| Anatomy - expresses - Gene                       | AeG  | r(ncbigene:147184 ! TMEM99) correlation pop(uberon:"UBERON:0001831" ! "parotid gland")                                  |
+--------------------------------------------------+------+-------------------------------------------------------------------------------------------------------------------------+
| Anatomy - upregulates - Gene                     | AuG  | r(ncbigene:55327 ! LIN7C) positiveCorrelation pop(uberon:"UBERON:0002107" ! liver)                                      |
+--------------------------------------------------+------+-------------------------------------------------------------------------------------------------------------------------+
| Compound - binds - Gene                          | CbG  | p(ncbigene:9513 ! FXR2) partOf complex(p(ncbigene:9513 ! FXR2), p(ncbigene:10445 ! MCRS1))                              |
+--------------------------------------------------+------+-------------------------------------------------------------------------------------------------------------------------+
| Compound - binds - Gene                          | CbG  | a(drugbank:DB01058 ! Praziquantel) partOf complex(a(drugbank:DB01058 ! Praziquantel), p(ncbigene:64816 ! CYP3A43))      |
+--------------------------------------------------+------+-------------------------------------------------------------------------------------------------------------------------+
| Compound - binds - Gene (modulates)              | CbG  | a(drugbank:DB00674 ! Galantamine) regulates p(ncbigene:1143 ! CHRNB4)                                                   |
+--------------------------------------------------+------+-------------------------------------------------------------------------------------------------------------------------+
| Compound - binds - Gene (activates/agonist)      | CbG  | a(drugbank:DB01074 ! Perhexiline) decreases act(p(ncbigene:51116 ! MRPS2))                                              |
+--------------------------------------------------+------+-------------------------------------------------------------------------------------------------------------------------+
| Compound - binds - Gene (decativates/antagonist) | CbG  | a(drugbank:DB00694 ! Daunorubicin) directlyDecreases act(p(ncbigene:4363 ! ABCC1))                                      |
+--------------------------------------------------+------+-------------------------------------------------------------------------------------------------------------------------+
| Compound - binds - Gene (unknown mechanism)      | CbG  | a(drugbank:DB00122 ! Choline) directlyIncreases complex(a(drugbank:DB00122 ! Choline), p(ncbigene:57153 ! SLC44A2))     |
+--------------------------------------------------+------+-------------------------------------------------------------------------------------------------------------------------+
| Compound - binds - Gene (agonist)                | CbG  | a(drugbank:DB00553 ! Methoxsalen) increases act(p(ncbigene:5829 ! PXN))                                                 |
+--------------------------------------------------+------+-------------------------------------------------------------------------------------------------------------------------+
| Compound - binds - Gene (agonist)                | CbG  | a(drugbank:DB00497 ! Oxycodone) directlyIncreases act(p(ncbigene:4988 ! OPRM1))                                         |
+--------------------------------------------------+------+-------------------------------------------------------------------------------------------------------------------------+
| Compound - causes - Side Effect                  | CcSE | a(drugbank:DB00273 ! Topiramate) increases path(umls:C1142412 ! "Vasodilation procedure")                               |
+--------------------------------------------------+------+-------------------------------------------------------------------------------------------------------------------------+
| Compound - palliates - Disease, Compound - treats - Disease | CpD, CtD  | a(drugbank:DB00635 ! Prednisone) decreases path(doid:"DOID:6364" ! migraine)                                            |
+--------------------------------------------------+------+-------------------------------------------------------------------------------------------------------------------------+
| Compound - resembles - Compound                  | CrC  | a(drugbank:DB00936 ! "Salicylic acid") association a(drugbank:DB00627 ! Niacin)                                         |
+--------------------------------------------------+------+-------------------------------------------------------------------------------------------------------------------------+
| Disease - associates - Gene                      | DaG  | p(ncbigene:348654 ! GEN1) association path(doid:"DOID:0050425" ! "restless legs syndrome")                              |
+--------------------------------------------------+------+-------------------------------------------------------------------------------------------------------------------------+
| Disease - downregulates - Gene                   | DdG  | r(ncbigene:2983 ! GUCY1B3) negativeCorrelation path(doid:"DOID:14330" ! "Parkinson's disease")                          |
+--------------------------------------------------+------+-------------------------------------------------------------------------------------------------------------------------+
| Disease - localizes - Anatomy                    | DlA  | pop(uberon:"UBERON:0001460" ! arm) association path(doid:"DOID:332" ! "amyotrophic lateral sclerosis")                  |
+--------------------------------------------------+------+-------------------------------------------------------------------------------------------------------------------------+
| Disease - presents - Symptom                     | DpS  | path(mesh:D003693 ! Delirium) association path(doid:"DOID:0050741" ! "alcohol dependence")                              |
+--------------------------------------------------+------+-------------------------------------------------------------------------------------------------------------------------+
| Disease - resembles - Disease                    | DrD  | path(doid:X) association path(doid:Y)                                                                                   |
+--------------------------------------------------+------+-------------------------------------------------------------------------------------------------------------------------+
| Disease - upregulates - Gene                     | DuG  | path(doid:"DOID:219" ! "colon cancer") positiveCorrelation r(ncbigene:29080 ! CCDC59)                                   |
+--------------------------------------------------+------+-------------------------------------------------------------------------------------------------------------------------+
| Gene - covaries - Gene                           | GcG  | r(ncbigene:162282 ! ANKFN1) correlation r(ncbigene:6098 ! ROS1)                                                         |
+--------------------------------------------------+------+-------------------------------------------------------------------------------------------------------------------------+
| Gene - interacts - Gene                          | GiG  | p(ncbigene:7416 ! VDAC1) directlyIncreases complex(p(ncbigene:8344 ! HIST1H2BE), p(ncbigene:7416 ! VDAC1))              |
+--------------------------------------------------+------+-------------------------------------------------------------------------------------------------------------------------+
| Gene - participates - Biological Process         | GpBP | p(ncbigene:9353 ! SLIT2) partOf bp(go:"GO:0051384" ! "response to glucocorticoid")                                      |
+--------------------------------------------------+------+-------------------------------------------------------------------------------------------------------------------------+
| Gene > regulates > Gene                          | Gr>G | p(ncbigene:356 ! FASLG) regulates p(ncbigene:1445 ! CSK)                                                                |
+--------------------------------------------------+------+-------------------------------------------------------------------------------------------------------------------------+
| Pharmacologic Class - includes - Compound        | PCiC | a(drugbank:DB00956 ! Hydrocodone) isA a(drugcentral:N0000000174 ! "Opioid Agonists")                                    |
+--------------------------------------------------+------+-------------------------------------------------------------------------------------------------------------------------+

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
