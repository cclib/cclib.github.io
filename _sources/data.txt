Parsed data
===========

This is a list of all the data parsed by the current official release of cclib (version |release|). For the same list for the development version, see `development parsed data`_. For details and miscellaneous notes on these attributes, see the `data notes`_ page.

.. _`development parsed data`: data_dev.html
.. _`data notes`: data_notes.html

Description of parsed data
--------------------------

Click the attribute name in the table below to go the notes for a particular attribute. All arrays are Numpy arrays of type 'd' (if containing floats) or 'i' (if containing integers).

.. include:: attributes.rst

Details of current implementation
---------------------------------

**N/A** = not applicable, **N/P** = applicable, but not possible, **T/D** = to do

=============== =========== =============== =========== =========== =========== =========== ========
attribute       ADF         GAMESS          GAMESS-UK   Gaussian    Jaguar      Molpro      ORCA 
=============== =========== =============== =========== =========== =========== =========== ========
aonames         N/A         √               √           √           √           √           √
aooverlaps      N/A         √               √           √           √           √           √           
atomcoords      √           √               √           √           √           √           √           
atombasis       T/D         √               √           √           √           √           T/D         
atommasses      √           T/D             T/D         √           T/D         T/D         T/D 
atomnos         √           √               √           √           √           √           √
ccenergies      N/A         √               T/D         √           N/A         T/D         T/D         
charge          √           √               √           √           √           √           √         
coreelectrons   √           √               T/D         √           T/D         T/D         T/D         
etenergies      √           √               N/A         √           √           T/D         T/D         
etoscs          √           √               N/A         √           √           T/D         T/D         
etrotats        √           T/D(?)          N/A         √           T/D         T/D         T/D         
etsecs          √           √               N/A         √           √           T/D         T/D         
etsyms          √           √               N/A         √           √           T/D(?)      T/D
ccenergies      N/A         √               T/D         √           N/A         T/D         T/D         
charge          √           √               √           √           √           √           √           
coreelectrons   √           √               T/D         √           T/D         T/D         T/D         
etenergies      √           √               N/A         √           √           T/D         T/D         
etoscs          √           √               N/A         √           √           T/D         T/D         
etrotats        √           T/D(?)          N/A         √           T/D         T/D         T/D         
etsecs          √           √               N/A         √           √           T/D         T/D         
etsyms          √           √               N/A         √           √           T/D(?)      T/D
fonames         √           N/A             N/A         N/A         N/A         N/A         N/A         
fooverlaps      √           N/A             N/A         N/A         N/A         N/A         N/A         
fragnames       √           N/A             N/A         N/A         N/A         N/A         N/A         
frags           √           N/A             N/A         N/A         N/A         N/A         N/A         
gbasis          N/A         √               √           √           N/P         √           T/D         
geotargets      √           √               √           √           √           T/D(?)      √           
geovalues       √           √               √           √           √           T/D(?)      √           
grads           N/A         N/A             N/A         √           N/A         N/A         N/A
hessian         T/D         T/D             T/D         T/D         T/D         √           T/D         
homos           √           √               √           √           √           √           √           
mocoeffs        √           √               √           √           √           √           √           
moenergies      √           √               √           √           √           √           √           
mosyms          √           √               √           √           √           T/D(?)      T/D         
mpenergies      N/A         √               √           √           √           √           T/D         
mult            √           √               √           √           √           √           √           
natom           √           √               √           √           √           √           √           
nbasis          √           √               √           √           √           √           √           
nmo             √           √               √           √           √           √(?)        √
scfenergies     √           √               √           √           √           √           T/D         
scftargets      √           √               √           √           √           √           T/D         
scfvalues       √           √               √           √           √           T/D(?)      T/D         
temperature     √           T/D             T/D         T/D         T/D         T/D         T/D         
vibdisps        √           √               √           √           √           T/D(?)      T/D         
vibfreqs        √           √               √           √           √           √           √           
vibirs          √           √               √           √           √           √           √(?)
vibramans       T/D         √ (PC GAMESS)   √           √           N/A         T/D(?)      T/D  
vibsyms         N/A         N/A             N/A         √           √           √           T/D    
=============== =========== =============== =========== =========== =========== =========== ========

