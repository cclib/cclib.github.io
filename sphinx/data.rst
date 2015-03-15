Parsed data (version |release|)
===============================

This is a list of all the data parsed by the current official release of cclib (namely version |release|). For the same list for the development version, see `development parsed data`_. For details and miscellaneous notes on these attributes, see the `data notes`_ page.

.. _`development parsed data`: data_dev.html
.. _`data notes`: data_notes.html

Description of parsed data
--------------------------

Click the attribute name in the table below to go the notes for a particular attribute. All arrays are Numpy arrays of type 'd' (if containing floats) or 'i' (if containing integers).

.. include:: attributes.rst

Details of current implementation
---------------------------------

The table below shows the coverage of attributes in the current production version of cclib. An attribute is marked as covered for a program only if it is parsed and used by at least one test. Other possible statuses are: **N/A** = not applicable, **N/P** = applicable, but not possible, **T/D** = to do.

.. include:: coverage.rst

