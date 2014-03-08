Tutorial
========

This page describes how to download, install and use cclib.

Requirements
------------

Before you install cclib, you need to make sure that you have the following:
 * Python (at least version 2.4)
 * NumPy

Python is an open-source programming language available from http://www.python.org. It is available for Windows as well as being included in most Linux distributions. In Debian it is installed as follows: (as root)

.. code-block:: bash

    apt-get install python python-dev

NumPy (Numerical Python) adds a fast array facility and linear algebra routines to Python. It is available from http://www.numpy.org. Windows users should use the most recent NumPy installation for the Python version they have (e.g. numpy-1.0.3.1.win32-py2.4.exe for Python 2.4). Linux users are recommended to find a binary package for their distribution rather than compiling it themselves. In Debian it is installed as follows: (as root)

.. code-block:: bash

    apt-get install python-numpy

To test whether Python is on the PATH, open a command prompt window and type:

.. code-block:: bash

    python

If Python is not on the PATH and you use Windows, add the full path to the directory containing it to the end of the PATH variable under Control Panel/System/Advanced Settings/Environment Variables. If you use Linux and Python is not on the PATH, put/edit the appropriate line in your .bashrc or similar startup file.

To test that Numpy is working, try importing it at the Python prompt. You should see something similar to the following:

.. code-block:: bash

    C:\Documents and Settings\user>python
    ActivePython 2.4.1 Build 247 (ActiveState Corp.) based on
    Python 2.4.1 (#65, Jun 20 2005, 17:01:55) [MSC v.1310 32 bit (Intel)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import numpy
    >>> numpy.__version__
    '1.0.1'
    >>>

(To exit, press CTRL+Z,Enter in Windows or CTRL+D in Linux)

Download and install cclib
--------------------------

The source code of cclib 1.1 is distributed as:
 * a .zip file, [http://prdownloads.sourceforge.net/cclib/cclib-1.1.zip?download cclib-1.1.zip] 
 * a .tar.gz file, [http://prdownloads.sourceforge.net/cclib/cclib-1.1.tar.gz?download cclib-1.1.tar.gz] 
 * a Windows binary installer, [http://prdownloads.sourceforge.net/cclib/cclib-1.1-py2.x.exe?download cclib-1.1-py2.x.exe]

Even for Windows users we recommend using the zip file, as this includes the example files. However, if you choose to download the .exe files instead, you can install simply by doubleclicking on the file. To uninstall, use the "Add and Remove Programs" menu in the Control Panel.

If you are using the .zip or .tar.gz files, extract the contents of the file at an appropriate location, which we will call INSTALLDIR. Open a command prompt and change directory to INSTALLDIR. Next, run the following commands to install cclib:

.. code-block:: bash

    python setup.py build
    python setup.py install # (as root)

To test, trying importing '''cclib''' at the Python prompt. You should see something similar to the following:

.. code-block:: python

    $ python
    Python 2.4.1 (#2, Sep  4 2005, 22:01:42)
    [GCC 3.3.5 (Debian 1:3.3.5-13)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
      Press ESC for command-line completion (twice for guesses).
      History is saved to ~/.pyhistory.
    >>> import cclib
    >>> cclib.__version__
    '1.1'

Getting the latest version
--------------------------

You can access the latest development code of cclib by downloading the last revision from our subversion repository. In the case of the svn command line client, the command would be the following:
<pre>svn co https://svn.code.sf.net/p/cclib/code/trunk</pre>

Debian GNU/Linux systems
------------------------

If you're using [http://www.debian.org Debian GNU/Linux] or a similar distribution, there are official [http://packages.debian.org/src:cclib cclib packages] (in the current testing distribution, aka wheezy) that you can install in any package manager (should as synaptic) or with one simple command:

.. code-block:: bash

    aptitude install cclib

There are in fact two packages, [http://packages.debian.org/wheezy/python-cclib python-cclib] containing the Python module, and [http://packages.debian.org/wheezy/cclib cclib] which installs just user scripts. If you also need to also install the unittests and logfiles we distribute, you will need to install the [http://packages.debian.org/wheezy/cclib-data cclib-data] package from the non-free repositories (due to license issues).

What next?
----------

 * Read the [[Using cclib|Tutorial]]
 * Read the list and specifications of the [[Parsed_Data|extracted data]]
 * Test the program using the example data files included in the distribution in the data directory.
 * Run the unit and regression tests in the test directory (testall.py and regression.py).
 * Send any questions to the cclib-users mailing list at	https://lists.sourceforge.net/lists/listinfo/cclib-users.
 * Write some computational chemistry algorithms using information parsed from cclib and donate the code to the project.
