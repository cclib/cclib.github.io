Parsed data
===========

This is a list of all the data parsed by the current official release of cclib (version 1.1). For the same list for the development version, see `development parsed data`_. For details and miscellaneous notes on these attributes, see the `data notes`_ page.

.. _`development parsed data`: data_dev.html
.. _`data notes`: data_notes.html

Description of parsed data
--------------------------

Click the attribute name in the table below to go the notes for a particular attribute. All arrays are Numpy arrays of type 'd' (if containing floats) or 'i' (if containing integers).

    =================== =============================================================== =========================== ====================
    Name                Description                                                     Units                       Data Structure  
    =================== =============================================================== =========================== ====================
    `aonames`_          atomic orbital names                                                                        list of strings
    `aooverlaps`_       atomic orbital overlap matrix                                                               array of rank 2
    `atombasis`_        indices of atomic orbitals on each atom                                                     list of lists
    `atomcoords`_       atom coordinates                                                Å                           array of rank 3
    `atommasses`_       atom masses                                                     daltons                     array of rank 1
    `atomnos`_          atomic numbers                                                                              array of rank 1
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
    `scfenergies`_      molecular electronic energies after SCF (Hartree-Fock, DFT)     eV                          array of rank 1
    `scftargets`_       targets for convergence of the SCF                                                          array of rank 2
    `scfvalues`_        current values for convergence of the SCF                                                   array of rank 3
    `temperature`_      temperature specified for thermochemistry analysis              K                           float
    `vibdisps`_         Cartesian displacement vectors                                  ΔÅ                          array of rank 3
    `vibfreqs`_         vibrational frequencies                                         cm :sup:`-1`                array of rank 1
    `vibirs`_           IR intensities                                                  km/mol                      array of rank 1
    `vibramans`_        Raman intensities                                               Å :sup:`4` amu :sup:`-1     array of rank 1
    `vibsyms`_          symmetries of vibrations                                                                    list of strings
    =================== =============================================================== =========================== ====================

.. _`aonames`: data_notes.html#aonames
.. _`aooverlaps`: data_notes.html#aonames
.. _`atombasis`: data_notes.html#atombasis
.. _`atomcoords`: data_notes.html#atomcoords
.. _`atommasses`: data_notes.html#atommasses
.. _`atomnos`: data_notes.html#atomnos
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
.. _`scfenergies`: data_notes.html#scfenergies
.. _`scftargets`: data_notes.html#scftargets
.. _`scfvalues`: data_notes.html#scfvalues
.. _`temperature`: data_notes.html#temperature
.. _`vibdisps`: data_notes.html#vibdisps
.. _`vibfreqs`: data_notes.html#vibfreqs
.. _`vibirs`: data_notes.html#vibirs
.. _`vibramans`: data_notes.html#vibramans
.. _`vibsyms`: data_notes.html#vibsyms

Details of current implementation
---------------------------------

'''N/A''' = not applicable, '''N/P''' = applicable, but not possible, '''T/D''' = to do

{| border="1" cellspacing="0" cellpadding="5" text-align="center" align="center"
|+'''Current implementation of parsers'''
!          !! width="80px" | ADF     !! width="80px" | GAMESS !! width="80px" | GAMESS-UK !! width="80px" | Gaussian !! width="80px" | Jaguar     !! width="80px" | Molpro !! width="80px" | ORCA 
 
! aonames  ||   N/A    ||    &radic;       ||   &radic;       ||    &radic;     ||   &radic;      ||      &radic;  || &radic; 

! aooverlaps  ||    N/A   ||    &radic;      ||    &radic;      ||  &radic;       ||     &radic;    ||   &radic;  || &radic;  

! atomcoords  ||  &radic;     ||   &radic;        ||    &radic;      ||   &radic;   ||    &radic;  ||       &radic; || &radic;

! atombasis ||   T/D    ||    &radic;     ||   &radic;     ||   &radic;      ||    &radic;     ||         &radic; || T/D  

! atommasses ||   &radic;     ||   T/D  ||     T/D    ||      &radic;      ||   T/D       ||     T/D      ||      T/D 

! atomnos  ||   &radic;    ||    &radic;       ||    &radic;      ||   &radic;      ||  &radic;       ||      &radic; || &radic;

! ccenergies ||      N/A        ||    &radic;  ||    T/D   || &radic; ||     N/A    ||    T/D || T/D 

! charge ||  &radic;    ||    &radic;       ||    &radic;      ||   &radic;      ||  &radic;       ||     &radic; || &radic; 

! coreelectrons ||     &radic;     ||     &radic;        ||        T/D         ||       &radic;   ||     T/D   ||  T/D || T/D 

! etenergies  ||   &radic;    ||    &radic;    ||   N/A      ||   &radic;      ||   &radic;     ||  T/D  ||  T/D

! etoscs  ||   &radic;    ||     &radic;       ||    N/A     ||   &radic;      ||   &radic;  || T/D ||  T/D   

! etrotats  ||   &radic;    ||     T/D(?)       ||     N/A     ||   &radic;      ||    T/D     || T/D ||  T/D 
 
! etsecs  ||   &radic;    ||     &radic;   ||    N/A     ||   &radic;      ||    &radic;    || T/D  || T/D   

! etsyms  ||   &radic;    ||     &radic;    ||   N/A      ||    &radic;     ||    &radic;    || T/D(?) || T/D 

! fonames  ||   &radic;   ||   N/A   ||   N/A   ||   N/A   ||   N/A  ||  N/A || N/A  

! fooverlaps ||   &radic;   ||   N/A ||   N/A   ||   N/A   ||   N/A  ||  N/A || N/A  

! fragnames ||   &radic;   ||   N/A ||   N/A   ||   N/A   ||   N/A  ||  N/A || N/A   

! frags ||   &radic;   ||   N/A ||   N/A   ||   N/A   ||   N/A  ||  N/A  || N/A   

! gbasis  ||   N/A    ||    &radic;      ||    &radic;    ||    &radic;     ||   N/P      ||  &radic;  || T/D   

! geotargets  ||   &radic;    ||    &radic;       ||   &radic;       ||    &radic;     ||    &radic;     ||  T/D(?) || &radic;  

! geovalues  ||   &radic;    ||     &radic;      ||     &radic;     ||   &radic;      ||  &radic; ||  T/D(?) || &radic;   

! grads || N/A   ||   N/A ||   N/A   || &radic; ||   N/A  ||  N/A || N/A   

! hessian || T/D || T/D || T/D || T/D  ||  T/D      ||    &radic;     || T/D  

! homos  ||   &radic;    ||      &radic;     ||     &radic;     ||    &radic;     ||     &radic;    ||  &radic; || &radic;   

! mocoeffs  ||   &radic;    ||    &radic;       ||    &radic;      ||   &radic;      ||    &radic;    ||       &radic;  || &radic;   

! moenergies  ||   &radic;    ||     &radic;      ||    &radic;      ||   &radic;      ||    &radic;    ||    &radic;  || &radic;   

! mosyms  ||   &radic;    ||    &radic;      ||    &radic;      ||    &radic;     ||   &radic;      ||  T/D(?) || T/D   

! mpenergies    || N/A     || &radic; ||  &radic;  || &radic; || &radic;  || &radic;  || T/D   

! mult ||  &radic;    ||    &radic;       ||    &radic;      ||   &radic;      ||  &radic;       ||     &radic;   || &radic;   

! natom  ||    &radic;   ||     &radic;     ||     &radic;     ||     &radic;    ||    &radic;     ||    &radic;  || &radic;      

! nbasis  ||   &radic;    ||     &radic;      ||     &radic;     ||     &radic;    ||   &radic;      ||    &radic;   || &radic;   

! nmo  ||   &radic;    ||    &radic;       ||     &radic;     ||   &radic;      ||    &radic;     ||  &radic;(?) || &radic;  

! scfenergies  ||   &radic;    ||     &radic;      ||    &radic;      ||    &radic;     ||  &radic;      || &radic; || T/D   

! scftargets  ||   &radic;    ||     &radic;      ||   &radic;       ||    &radic;     ||   &radic;      ||    &radic;   || T/D     

! scfvalues  ||    &radic;   ||     &radic;      ||   &radic;       ||   &radic;      ||    &radic;     ||  T/D(?) || T/D   

! temperature ||    &radic;   ||     T/D      ||   T/D       ||   T/D      ||    T/D     ||  T/D || T/D

! vibdisps  ||   &radic;       ||     &radic;      ||     &radic;        ||      &radic;        ||      &radic;   || T/D(?) || T/D   

! vibfreqs  ||   &radic;    ||     &radic;      ||   &radic;       ||   &radic;      ||   &radic;  ||      &radic;     || &radic;  

! vibirs  ||   &radic;    ||     &radic;      ||    &radic;      ||    &radic;     ||   &radic;      ||    &radic;     || &radic;(?)   

! vibramans  ||   T/D    ||     &radic; (PC GAMESS)   ||     &radic;     ||    &radic;     ||     N/A    ||  T/D(?)  || T/D  

! vibsyms  ||   N/A    ||    N/A       ||    N/A      ||  &radic;     ||    &radic;     ||    &radic;     || T/D    

!          !! width="80px" | ADF     !! width="80px" | GAMESS !! width="80px" | GAMESS-UK !! width="80px" | Gaussian !! width="80px" | Jaguar     !! width="80px" | Molpro !! width="80px" | ORCA }

[[Category:Parsed data| ]]
