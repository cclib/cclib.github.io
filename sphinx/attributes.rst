    =================== ================================================================ =========================== =============================== 
    Name                Description                                                      Units                       Data type                       
    =================== ================================================================ =========================== =============================== 
    `aonames`_          atomic orbital names                                                                         list
    `aooverlaps`_       atomic orbital overlap matrix                                                                array of rank 2
    `atombasis`_        indices of atomic orbitals on each atom                                                      list of lists
    `atomcharges`_      atomic partial charges                                                                       dict of arrays of rank 1
    `atomcoords`_       atom coordinates                                                 angstroms                   array of rank 3
    `atommasses`_       atom masses                                                      daltons                     array of rank 1
    `atomnos`_          atomic numbers                                                                               array of rank 1
    `atomspins`_        atomic spin densities                                                                        dict of arrays of rank 1
    `charge`_           net charge of the system                                                                     integer
    `ccenergies`_       molecular energies with Coupled-Cluster corrections              eV                          array of rank 2
    `coreelectrons`_    number of core electrons in atom pseudopotentials                                            array of rank 1
    `etenergies`_       energies of electronic transitions                               1/cm                        array of rank 1
    `etoscs`_           oscillator strengths of electronic transitions                                               array of rank 1
    `etrotats`_         rotatory strengths of electronic transitions                     ??                          array of rank 1
    `etsecs`_           singly-excited configurations for electronic transitions                                     list of lists
    `etsyms`_           symmetries of electronic transitions                                                         list
    `fonames`_          fragment orbital names                                                                       list
    `fooverlaps`_       fragment orbital overlap matrix                                                              array of rank 2
    `fragnames`_        names of fragments                                                                           list
    `frags`_            indices of atoms in a fragment                                                               list of lists
    `gbasis`_           coefficients and exponents of Gaussian basis functions                                       PyQuante format
    `geotargets`_       targets for convergence of geometry optimization                                             array of rank 1
    `geovalues`_        current values for convergence of geometry optmization                                       array of rank 1
    `grads`_            current values of forces (gradients) in geometry optimization                                array of rank 3
    `hessian`_          elements of the force constant matrix                                                        array of rank 1
    `homos`_            molecular orbital indices of HOMO(s)                                                         array of rank 1
    `mocoeffs`_         molecular orbital coefficients                                                               list of arrays of rank 2
    `moenergies`_       molecular orbital energies                                       eV                          list of arrays of rank 1
    `mosyms`_           orbital symmetries                                                                           list of lists
    `mpenergies`_       molecular electronic energies with Moller-Plesset corrections    eV                          array of rank 2
    `mult`_             multiplicity of the system                                                                   integer
    `natom`_            number of atoms                                                                              integer
    `nbasis`_           number of basis functions                                                                    integer
    `nmo`_              number of molecular orbitals                                                                 integer
    `nocoeffs`_         natural orbital coefficients                                                                 array of rank 2
    `scfenergies`_      molecular electronic energies after SCF (Hartree-Fock, DFT)      eV                          array of rank 1
    `scftargets`_       targets for convergence of the SCF                                                           array of rank 2
    `scfvalues`_        current values for convergence of the SCF                                                    list of arrays of rank 2
    `vibanharms`_       vibrational anharmonicity constants                              1/cm                        array of rank 2
    `vibdisps`_         cartesian displacement vectors                                   delta angstrom              array of rank 3
    `vibfreqs`_         vibrational frequencies                                          1/cm                        array of rank 1
    `vibirs`_           IR intensities                                                   km/mol                      array of rank 1
    `vibramans`_        Raman intensities                                                A^4/Da                      array of rank 1
    `vibsyms`_          symmetries of vibrations                                                                     list
    `scannames`_        Names of varaibles scanned                                                                   list
    `scanenergies`_     energies of potential energy surface                                                         list
    `scanparm`_         values of parameters in potential energy surface                                             list of tuples
    `scancoords`_       Geometries of each scan step                                     angstroms                   array of rank 3
    `enthaply`_         Sum of electronic and thermal Enthalpie                                                      float hartree/particle
    `freeenergy`_       Sum of electronic and thermal Free Energies                                                  float hartree/particle
    `temperature`_      Tempature used for Thermochemistry                                                           float kelvin
    `entropy`_          Entropy                                                                                      float hartree/particle
    `optdone`_          Stores if an optimisation job has completed                                                  boolean
    =================== ================================================================ =========================== =============================== 

.. _`aonames`: data_notes.html#aonames
.. _`aooverlaps`: data_notes.html#aooverlaps
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
.. _`vibanharms`: data_notes.html#vibanharms
.. _`vibdisps`: data_notes.html#vibdisps
.. _`vibfreqs`: data_notes.html#vibfreqs
.. _`vibirs`: data_notes.html#vibirs
.. _`vibramans`: data_notes.html#vibramans
.. _`vibsyms`: data_notes.html#vibsyms
.. _`scannames`: data_notes.html#scannames
.. _`scanenergies`: data_notes.html#scanenergies
.. _`scanparm`: data_notes.html#scanparm
.. _`scancoords`: data_notes.html#scancoords
.. _`enthaply`: data_notes.html#enthaply
.. _`freeenergy`: data_notes.html#freeenergy
.. _`temperature`: data_notes.html#temperature
.. _`entropy`: data_notes.html#entropy
.. _`optdone`: data_notes.html#optdone
