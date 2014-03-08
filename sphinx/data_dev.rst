Development parsed data
=======================

This is a list of all the data parsed by the `current development code of cclib`_. For the same information for the current official release, see the regular `parsed data`_ page. Note that the information on this page may be outdated.

.. _`current development code of cclib`: https://github.com/cclib/cclib
.. _`parsed data`: data.html

Description of parsed data
--------------------------

Click the attribute name in the table below for the specifications for a particular attribute. All arrays are Numpy arrays of type 'd' (if containing floats) or 'i' (if containing integers).

    =================== =============================================================== =========================== ====================
    Name                Description                                                     Units                       Data Structure  
    =================== =============================================================== =========================== ====================
    `aonames`_          atomic orbital names                                                                        list of strings
    `aooverlaps`_       atomic orbital overlap matrix                                                               array of rank 2
    `atombasis`_        indices of atomic orbitals on each atom                                                     list of lists
    `atomcharges`_      atom partial charges                                                                        dict of arrays of rank 1
    `atomcoords`_       atom coordinates                                                Å                           array of rank 3
    `atommasses`_       atom masses                                                     daltons                     array of rank 1
    `atomnos`_          atomic numbers                                                                              array of rank 1
    `atomspins`_        atomic spin densities                                                                       dict of arrays of rank 1
    `charge`_           net charge of the system                                        *e*                         integer
    `ccenergies`_       molecular energies with coupled cluster corrections             eV                          array of rank 1
    `coreelectrons`_    numbers of core electrons atom pseudopotentials                                             array of rank 1
    `etenergies`_       energies of electronic transitions                              cm :sup:`-1`                array of rank 1
    `etoscs`_           oscillator strengths of electronic transitions                                              array of rank 1
    `etrotats`_         rotatory strengths of electronic transitions                    ??                          array of rank 1
    `etsecs`_           singly-excited configurations for electronic transitions                                    list of lists
    `etsyms`_           symmetries of electronic transitions                                                        list of strings
    `fonames`_          fragment orbital names                                                                      list of strings
    `fooverlaps`_       fragment orbital overlap matrix                                                             array of rank 2
    `fragnames`_        names of fragments                                                                          list of strings
    `frags`_            indices of atoms in a fragment                                                              list of lists
    `gbasis`_           coefficients of Gaussian basis functions                                                    PyQuante format
    `geotargets`_       targets for convergence of geometry optimization                                            array of rank 1
    `geovalues`_        current values for convergence of geometry optmization                                      array of rank 2
    `grads`_            current values of forces (gradients) in geometry optimization                               array of rank 3
    `hessian`_          force constant matrix                                                                       array of rank 1
    `homos`_            molecular orbital indices of HOMO(s)                                                        array of rank 1
    `mocoeffs`_         molecular orbital coefficients                                                              list of arrays of rank 2
    `moenergies`_       molecular orbital energies                                      eV                          list of arrays of rank 1
    `mosyms`_           orbital symmetries                                                                          list of lists
    `mpenergies`_       molecular electronic energies with Möller-Plesset corrections   eV                          array of rank 2
    `mult`_             multiplicity of the system                                      h/2π                        integer
    `natom`_            number of atoms                                                                             integer
    `nbasis`_           number of basis functions                                                                   integer
    `nmo`_              number of molecular orbitals                                                                integer
    `nocoeffs`_         natural orbital coefficients                                                                array of rank 2
    `scfenergies`_      molecular electronic energies after SCF (Hartree-Fock, DFT)     eV                          array of rank 1
    `scftargets`_       targets for convergence of the SCF                                                          array of rank 2
    `scfvalues`_        current values for convergence of the SCF                                                   array of rank 3
    `temperature`_      temperature specified for thermochemistry analysis              K                           float
    `vibanharms`_       Vibrational anharmonicity constants                             cm :sup:`-1`                array of rank 2
    `vibdisps`_         Cartesian displacement vectors                                  ΔÅ                          array of rank 3
    `vibfreqs`_         vibrational frequencies                                         cm :sup:`-1`                array of rank 1
    `vibirs`_           IR intensities                                                  km/mol                      array of rank 1
    `vibramans`_        Raman intensities                                               Å :sup:`4` amu :sup:`-1     array of rank 1
    `vibsyms`_          symmetries of vibrations                                                                    list of strings
    =================== =============================================================== =========================== ====================

.. _`aonames`: data_notes.html#aonames
.. _`aooverlaps`: data_notes.html#aonames
.. _`atombasis`: data_notes.html#atombasis
.. _`atomcharges`: data_notes.html#atomcharges
.. _`atomcoords`: data_notes.html#atomcoords
.. _`atommasses`: data_notes.html#atommasses
.. _`atomnos`: data_notes.html#atomnos
.. _`atomspins`: data_notes.html#atomspins
.. _`charge`: data_notes.html#charge
.. _`ccenergies`: data_notes.html#ccenergies
.. _`coreelectrons`: data_notes.html#coreelectrons
.. _`etenergies`: data_notes.html#etenergies
.. _`etoscs`: data_notes.html#etoscs
.. _`etrotats`: data_notes.html#etrotats
.. _`etsecs`: data_notes.html#etsecs
.. _`etsyms`: data_notes.html#etsyms
.. _`fonames`: data_notes.html#fonames
.. _`fooverlaps`: data_notes.html#fooverlaps
.. _`fragnames`: data_notes.html#fragnames
.. _`frags`: data_notes.html#frags
.. _`gbasis`: data_notes.html#gbasis
.. _`geotargets`: data_notes.html#geotargets
.. _`geovalues`: data_notes.html#geovalues
.. _`grads`: data_notes.html#grads
.. _`hessian`: data_notes.html#hessian
.. _`homos`: data_notes.html#homos
.. _`mocoeffs`: data_notes.html#mocoeffs
.. _`moenergies`: data_notes.html#moenergies
.. _`mosyms`: data_notes.html#mosyms
.. _`mpenergies`: data_notes.html#mpenergies
.. _`mult`: data_notes.html#mult
.. _`natom`: data_notes.html#natom
.. _`nbasis`: data_notes.html#nbasis
.. _`nmo`: data_notes.html#nmo
.. _`nocoeffs`: data_notes.html#nocoeffs
.. _`scfenergies`: data_notes.html#scfenergies
.. _`scftargets`: data_notes.html#scftargets
.. _`scfvalues`: data_notes.html#scfvalues
.. _`temperature`: data_notes.html#temperature
.. _`vibanharms`: data_notes.html#vibanharms
.. _`vibdisps`: data_notes.html#vibdisps
.. _`vibfreqs`: data_notes.html#vibfreqs
.. _`vibirs`: data_notes.html#vibirs
.. _`vibramans`: data_notes.html#vibramans
.. _`vibsyms`: data_notes.html#vibsyms

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
