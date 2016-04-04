Examples
========

This page describes how to use ccget to obtain data from output files.

Input
-----

The output file used as an example is a Benzeneselenol(C6H5-SeH) molecule optimized using Gaussian09. The input geometry was optimized at the ``B3LYP + 6-311++g(3df,3pd)`` level of calculation.

The input file used is given below:

.. code-block:: bash

   %mem=2800MB
    %nprocshared=4
    %chk=BSe-B1-2.chk
    # opt freq rb3lyp/6-311++g(3df,3pd)

    BenzeneSelenol B3LYP-6311++g(3df,3pd)

    0 1
     C                 -2.89824687   -0.00233690    0.00407979
     C                 -2.20110587    1.20427657   -0.03738778
     C                 -0.80680301    1.20847251   -0.04207404
     C                 -0.10598800    0.00030600    0.00497800
     C                 -0.80441513   -1.20928578    0.04103186
     C                 -2.19910287   -1.20752072    0.04123846
     H                 -3.98978249   -0.00323448    0.00435505
     H                 -2.74390344    2.15073101   -0.07049588
     H                 -0.25959615    2.15143883   -0.08256300
     H                 -0.25533702   -2.15154247    0.07059511
     H                 -2.74005799   -2.15513767    0.07078971
     Se                 1.82625500   -0.00367200   -0.04339300
     H                  1.97993148    1.08839585    0.93442872


Output
------
The data types that can be parsed from the output file depends on the type of simulation being conducted. The name of the output file used to show example usage is ``Benzeneselenol.out``.

Data type can be parsed from the output file by following this format

.. code-block:: bash

    ccget <attribute> [<attribute>] <CompChemLogFile> [<CompChemLogFile>]

where attribute can be any one of the attribute names available `here`_

.. _`here`: data_dev.html

1. Atomic Charges
  The atomic orbital names are obtained by using the ``atomcharges`` attribute with ``ccget``

.. code-block:: bash

    $ ccget atomcharges Benzeneselenol.out
    Attempting to read Benzeneselenol.out
    atomcharges:
    {'mulliken': array([-0.49915 ,  0.056965,  0.172161,  0.349794, -0.153072,  0.094583,
        0.016487,  0.050249,  0.002149,  0.01161 ,  0.053777, -0.173671,
        0.018118])}

2. Enthalpy
  The molecular electronic energies after SCF (DFT) optimization of the input molecule is obtained by using the ``scfenergies`` attribute with ``ccget``

.. code-block:: bash

    $ ccget scfenergies Benzeneselenol.out
    Attempting to read Benzeneselenol.out
    scfenergies:
    [-71671.43702915 -71671.4524142  -71671.4534768  -71671.45447492
    -71671.4556548  -71671.45605671 -71671.43194906 -71671.45761021
    -71671.45850275 -71671.39630296 -71671.45915119 -71671.45935854
    -71671.4594614  -71671.45947338 -71671.45948807 -71671.4594946
    -71671.4594946 ]


3. Geometry Targets
  The targets for convergence of geometry optimization can be obtained by using the ``geotargets`` attribute with ``ccget``

.. code-block:: bash

    $ ccget  geotargets Benzeneselenol.out
    Attempting to read Benzeneselenol.out
    geotargets:
    [ 0.00045  0.0003   0.0018   0.0012 ]

Chaining of attributes
----------------------

ccget provides the user with the option to chain attributes to obtain more than one type of data with a command call. The attributes can be chained in any particular order. A few chained examples are provided below.

1. Molecular Orbitals and Multiplicity
  The number of molecular orbitals and the number of basis functions used to optimize the molecule can be obtained by running the following command

.. code-block:: bash

    $ ccget nmo nbasis Benzeneselenol.out
    Attempting to read Benzeneselenol.out
    nmo:
    405
    nbasis:
    407

2. Enthalpy and Vibrational Frequency
  The enthalpy and the vibrational frequencies of the optimized molecule is conducted is obtained below:

.. code-block:: bash

    $ ccget enthalpy vibfreqs Benzeneselenol.out
    Attempting to read Benzeneselenol.out
    enthalpy:
    -2633.77264
    vibfreqs:
    [  129.5512   170.6681   231.4278   304.8614   407.8299   472.5026
       629.9087   679.9032   693.2509   746.7694   812.5113   850.2578
       915.8742   987.1252   988.1785  1002.8922  1038.1073  1091.4005
      1102.3417  1183.3857  1209.2727  1311.3497  1355.6441  1471.4447
      1510.1919  1611.9088  1619.0156  2391.2487  3165.1596  3171.3909
      3182.0753  3188.5786  3198.0359]
