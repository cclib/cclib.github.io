Development parsed data
=======================

This is a list of all the data parsed by the `current development code of cclib`_. For the same information for the current official release, see the regular `parsed data`_ page. Note that the information on this page may be outdated.

.. _`current development code of cclib`: https://github.com/cclib/cclib
.. _`parsed data`: data.html

Description of parsed data
--------------------------

Click the attribute name in the table below for the specifications for a particular attribute. All arrays are Numpy arrays of type 'd' (if containing floats) or 'i' (if containing integers).

.. include:: attributes_dev.rst

Details of current implementation
---------------------------------

**N/A** = not applicable, **N/P** = applicable, but not possible, **T/D** = to do

=============== =========== =============== =========== =========== =========== =========== =========== ============
attribute       ADF         GAMESS          GAMESS-UK   Gaussian    Jaguar      Molpro      ORCA        Turbomole
=============== =========== =============== =========== =========== =========== =========== =========== ============
aonames         N/A         √               √           √           √           √           √           T/D         
aooverlaps      N/A         √               √           √           √           √           √           T/D         
atomcharges     √           √               √           √           T/D         T/D         √           T/D         
atomcoords      √           √               √           √           √           √           √           T/D         
atombasis       T/D         √               √           √           √           √           T/D         T/D         
atommasses      √           T/D             T/D         √           T/D         T/D         T/D         ?           
atomnos         √           √               √           √           √           √           √           T/D         
atomspins       T/D         T/D             T/D         T/D         T/D         T/D         √           T/D 
ccenergies      N/A         √               T/D         √           N/A         T/D         T/D         T/D         
charge          √           √               √           √           √           √           √           T/D         
coreelectrons   √           √               T/D         √           T/D         T/D         T/D         T/D         
etenergies      √           √               N/A         √           √           T/D         T/D         T/D         
etoscs          √           √               N/A         √           √           T/D         T/D         T/D         
etrotats        √           T/D(?)          N/A         √           T/D         T/D         T/D         T/D         
etsecs          √           √               N/A         √           √           T/D         T/D         T/D         
etsyms          √           √               N/A         √           √           T/D(?)      T/D         T/D
fonames         √           N/A             N/A         N/A         N/A         N/A         N/A         N/A         
fooverlaps      √           N/A             N/A         N/A         N/A         N/A         N/A         N/A         
fragnames       √           N/A             N/A         N/A         N/A         N/A         N/A         N/A         
frags           √           N/A             N/A         N/A         N/A         N/A         N/A         N/A         
gbasis          N/A         √               √           √           N/P         √           T/D         T/D         
geotargets      √           √               √           √           √           T/D(?)      √           T/D         
geovalues       √           √               √           √           √           T/D(?)      √           T/D         
grads           N/A         N/A             N/A         √           N/A         N/A         N/A         N/A
hessian         T/D         T/D             T/D         T/D         T/D         √           T/D         T/D         
homos           √           √               √           √           √           √           √           T/D         
mocoeffs        √           √               √           √           √           √           √           T/D         
moenergies      √           √               √           √           √           √           √           T/D         
mosyms          √           √               √           √           √           T/D(?)      T/D         T/D         
mpenergies      N/A         √               √           √           √           √           T/D         T/D         
mult            √           √               √           √           √           √           √           T/D         
natom           √           √               √           √           √           √           √           T/D         
nbasis          √           √               √           √           √           √           √           T/D         
nmo             √           √               √           √           √           √      (?)  √           T/D         
nocoeffs        T/D         √               T/D         √           T/D         T/D         T/D         T/D
scfenergies     √           √               √           √           √           √           T/D         T/D         
scftargets      √           √               √           √           √           √           T/D         T/D         
scfvalues       √           √               √           √           √           T/D(?)      T/D         T/D         
vibanharms      N/A         N/A             N/A         √           N/A         N/A         N/A         N/A         
vibdisps        √           √               √           √           √           T/D(?)      T/D         T/D         
vibfreqs        √           √               √           √           √           √           √           T/D         
vibirs          √           √               √           √           √           √           √      (?)  T/D
=============== =========== =============== =========== =========== =========== =========== =========== ============
