===========
Development
===========

Basic instructions
===========================

The default cclib files distributed with a release, as described in the `tutorial`_, do not include any unit tests and logfiles necessary to run those tests. This section covers how to download the full source along with all test data and scripts, and how to use these for development and testing.

.. _`tutorial`: tutorial.html

Cloning cclib from github
~~~~~~~~~~~~~~~~~~~~~~~~~

cclib is hosted by the fantastic people at `GitHub`_ (previously at `Sourceforge`_) in a `git`_ repository. You can download a `zipped archive`_ of the current development version (called `master`) for installation and testing or browse the available `releases`_. In order to contribute any changes, however, you will need to create a local copy of the repository:

.. code-block:: bash

    git clone https://github.com/cclib/cclib.git cclib

.. _`GitHub`: https://github.com
.. _`Sourceforge`: https://sourceforge.net
.. _`git`: http://git-scm.com
.. _`zipped archive`: https://github.com/cclib/cclib/archive/master.zip
.. _`releases`: https://github.com/cclib/cclib/releases

Developer policy
~~~~~~~~~~~~~~~~

We follow a typical GitHub collaborative model, relying on `forks and pull requests`_. In short, the development process consists of:

* `Creating your own fork`_ of cclib in order to develop
* `Creating a pull request`_ to contribute your changes
* Reviewing and merging open pull requests (by someone else)
* Using `issues`_ to plan and prioritize future work

.. _`creating your own fork`: https://help.github.com/articles/fork-a-repo
.. _`creating a pull request`: https://help.github.com/articles/creating-a-pull-request
.. _`forks and pull requests`: https://help.github.com/articles/using-pull-requests
.. _`issues`: https://github.com/cclib/cclib/issues

Here are some general guidelines for developers who are contributing code:

* Run and review the unit tests (see below) before submitting a pull request
* There should normally not be more failed tests than before your changes
* For larger changes or features that take some time to implement, `using branches`_ is recommended

.. _`using branches`: https://help.github.com/articles/branching-out

Releasing a new version
~~~~~~~~~~~~~~~~~~~~~~~

The release cycle of cclib is irregular, with new versions being created as deemed necessary after significant changes or new features. We roughly follow semantic versioning with respect to the `parsed attributes`_.

When creating a new release on GitHub, the typical procedure include the following steps:

* Update the `CHANGELOG`_, `ANNOUNCE`_ and any other files that might change content with the new version
* Make sure that `setup.py`_ has the right version number, as well as __version__ in `__init__.py`_ and any other relevant files
* Run `manifest.py`_ to update the MANIFEST file if necessary
* Do a final merge of the trunk to the release branch
* Run the tests for a final time after removing cclib (for example, ``rm -rf $PYTHONDIR/lib/site-packages/cclib``) and reinstalling from the source distribution
* Tag the release (make sure to use an annotated tag using using ``git -a``) and upload it (``git push --tags``)
* Create the source distributions (``python setup.py sdist --formats=gztar,zip``) and Windows binary installers (``python setup.py bdist_wininst``)
* Create a release on Github (see `Creating releases`_) and upload the source distribiuions and Windows binaries
* Update the download and install instructions in the documentation, if appropriate
* Email the users and developers mailing list with the message in `ANNOUNCE`_
* Update the Python package index (https://pypi.python.org/pypi/cclib), normally done by ``python setup.py register``
* For a significant minor release, if appropriate, send an email to the `CCL list`_ and any mailing lists for computational chemistry packages supported by cclib

.. _`parsed attributes`: data.html

.. _`ANNOUNCE`: https://github.com/cclib/cclib/blob/master/ANNOUNCE
.. _`CHANGELOG`: https://github.com/cclib/cclib/blob/master/CHANGELOG
.. _`setup.py`: https://github.com/cclib/cclib/blob/master/setup.py
.. _`__init__.py`: https://github.com/cclib/cclib/blob/master/src/cclib/__init__.py
.. _`manifest.py`: https://github.com/cclib/cclib/blob/master/manifest.py

.. _`Creating releases`: https://help.github.com/articles/creating-releases

.. _`CCL list`: http://www.ccl.net

Testing
=======

.. index::
    single: testing; unit tests

Tests are a central part of cclib development, and work is often done in a test-driven fashion. The `test directory`_, which is not included in the default download, contains the test scripts that keep cclib working, and keep the developers sane. The corresponding data files, which are logfiles from computational chemistry programs, are located in the `data directory`_. 

.. _`data directory`: https://github.com/cclib/cclib/tree/master/test
.. _`test directory`: https://github.com/cclib/cclib/tree/master/test

Unit tests
~~~~~~~~~~

These basic logfiles, which are used for unit tests, are stored in folders like ``basicJaguar6.4`` and are standardized for all supported programs to the extent possible. These include B3LYP/STO-3G calculations on 1,4-divinylbenzene (dvb) with C2h symmetry, post-Hartree Fock calculations for water and others. These jobs represent typical computation types such as geometry optimisation, a single point calculation (closed and open shell), frequency calculation, a TD-DFT calculation. These data files are stored in the git repository alongside the source dode, but are not included in the distributed source packages.

In order to check whether our parsers extract information in the correct format, with the correct units, we have unit tests that parse a series of basic data files (see below) of the same calculation undertaken with different programs. Running testall.py in the test directory runs the whole test suite, but it is also possible to individually run the tests for GeoOpts (testGeoOpt.py), Single Point calculations, and so on.

Note that no change should be commited to the repository if it increases the number of failed tests (unless you are adding new tests, of course). 

.. index::
    single: testing; regressions

Regression tests
~~~~~~~~~~~~~~~~

Regression tests ensure that bugs, once fixed, stay fixed. These are real-life files that at some point broke a cclib parser, and are stored in folders like ``Jaguar6.4``. The files associated with regression tests are not stored stored together with the source code as they are often quite large. A separate repository on github, `cclib-data`_, is used to track and use these files, and we do not distribute them in releases.

For every bug found in the parsers, there should be a corresponding regression test that tests this bug stays fixed. The process is automated by `regression.py`_, which runs through all of our test data, both the basic data and regression files, opens them, tries to parse, and runs any relevant regression tests defined for that file.

New regression tests are added by creating a function ``testMyFileName_out`` following the examples at the start of `regression.py`_.

.. _`cclib-data`: https://github.com/cclib/cclib-data
.. _`regression.py`: https://github.com/cclib/cclib/blob/master/test/regression.py

| Production version (|release|): |travis_prod|
| Development branch (master): |travis_master|

.. |travis_prod| image:: https://travis-ci.org/cclib/cclib.svg?branch=v1.3
.. |travis_master| image:: https://travis-ci.org/cclib/cclib.svg?branch=master

Doc tests
~~~~~~~~~

Doc tests are a nice Python invention for unit testing individual functions. To run the doctests in a particular file, you need to run the script. For example, "python gaussianparser.py" runs the doctests contained in gaussianparser.py. To run all of the doctests at once, you need to install a testing tool like nose, and then use the following command (note that many errors may be due to missing libraries like BioPython):

.. code-block: bash

    > "C:\Program Files\Python24\Scripts\nosetests.exe" cclib --with-doctest -e test* -v
    ERROR
    ERROR
    Doctest: cclib.bridge.cclib2openbabel.makeopenbabel ... ok
    ERROR
    ERROR
    Doctest: cclib.parser.adfparser.ADF.normalisesym ... ok
    Doctest: cclib.parser.gamessparser.GAMESS.normalise_aonames ... ok
    Doctest: cclib.parser.gamessparser.GAMESS.normalisesym ... ok
    Doctest: cclib.parser.gamessukparser.GAMESSUK.normalisesym ... ok
    Doctest: cclib.parser.gaussianparser.Gaussian.normalisesym ... ok
    Doctest: cclib.parser.jaguarparser.Jaguar.normalisesym ... ok
    Doctest: cclib.parser.logfileparser.Logfile.float ... ok
    Doctest: cclib.parser.utils.PeriodicTable ... ok
    Doctest: cclib.parser.utils.convertor ... ok
    ERROR
    ERROR
    ......

Other useful pages
==================

* The `methods in the development version`_
* The `parsed data in the development version`_
* The `progress page`_, which describes where we are and what we are trying to do

.. _`methods in the development version`: methods_dev.html
.. _`parsed data in the development version`: data_dev.html
.. _`progress page`: progress.html

Websites related to cclib
=========================

* The official `cclib organization on github`_
* The `cclib project page on Sourceforge`_ (inactive now)
* The `cclib entry on Ohloh`_
* The `cclib entry on Cheeseshop`_

.. _`cclib organization on github`: https://github.com/cclib
.. _`cclib project page on Sourceforge`: http://sourceforge.net/projects/cclib/
.. _`cclib entry on Ohloh`: https://www.ohloh.net/p/cclib
.. _`cclib entry on Cheeseshop`: http://www.python.org/pypi/cclib

Developers
==========

**cclib** developers include the following (in alphabetical order):

* Eric Berquist
* `Karol M. Langner`_
* `Noel O'Boyle`_
* Christopher Rowley
* Adam Tenderholt 

.. _`Karol M. Langner`: http://mmqc.org
.. _`Noel O'Boyle`: http://www.redbrick.dcu.ie/~noel
