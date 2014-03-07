Development parsed data
=======================

This is a list of all the data parsed by the [http://cclib.svn.sourceforge.net/viewvc/cclib/ current development version of cclib]. For the same information for the current official release, see [[parsed data]]. Note that the information on this page may be outdated.

== Description of parsed data ==

Click the attribute name in the table below for the specifications for a particular attribute. All arrays are Numpy arrays of type 'd' (if containing floats) or 'i' (if containing integers).

{| border="1" cellspacing="0" cellpadding="5" align="center" style="text-align:left"
|+
! style="text-align:center" | Name    !!  style="text-align:center" | Description  !!  style="text-align:center" | Units  !!  style="text-align:center" | Data Structure  
|- 
| [[aonames]]  || atomic orbital names (not available for ADF files) || || List of strings
|-
| [[aooverlaps]] || atomic orbital overlap matrix (not available for ADF files) || || Array of rank 2
|-
| [[atombasis]] || indices of atomic orbitals on each atom || || List of lists
|-
| [[atomcharges]] || atom partial charges || || Dict of Arrays of rank 1
|-
| [[atomcoords]] || atom coordinates || &Aring; || Array of rank 3
|-
| [[atommasses]] || atom masses || Daltons || Array of rank 1
|-
| [[atomnos]] || atomic numbers || || Array of rank 1
|-
| [[atomspins]] || atomic spin densities || || Dict of Arrays of rank 1
|-
| [[charge]] || net charge of the system || ''e'' || Integer
|-
| [[ccenergies]] || molecular energies with Coupled Cluster corrections || eV || Array of rank 1
|-
| [[coreelectrons]] || numbers of core electrons atom pseudopotentials || || Array of rank 1
|-
| [[etenergies]] || energies of electronic transitions || cm<sup>-1</sup> || Array of rank 1
|-
| [[etoscs]] || oscillator strengths of electronic transitions ||   || Array of rank 1
|-
| [[etrotats]] || rotatory strengths of electronic transitions || ??  || Array of rank 1
|-
| [[etsecs]] || singly-excited configurations for electronic transitions || || List of Lists
|-
| [[etsyms]] || symmetries of electronic transitions || || List of strings
|-
| [[fonames]] || fragment orbital names (only for ADF) || || List of strings
|-
| [[fooverlaps]] || fragment orbital overlap matrix (only for ADF) || || Array of rank 2
|-
| [[fragnames]] || names of fragments (only for ADF) || || List of strings
|-
| [[frags]] || indices of atoms in a fragment (only for ADF) || || List of Lists
|-
| [[gbasis]] || coefficients of Gaussian basis functions || || PyQuante format
|-
| [[geotargets]] || targets for convergence of geometry optimization || || Array of rank 1
|-
| [[geovalues]] || current values for convergence of geometry optmization || || Array of rank 2
|-
| [[grads]] || current values of forces (gradients) in geometry optimization || || Array of rank 3
|-
| [[hessian]] || force constant matrix || || Array of rank 1
|-
| [[homos]] || molecular orbital indices of HOMO(s) || || Array of rank 1
|-
| [[mocoeffs]] || molecular orbital coefficients || || List of Arrays of rank 2
|-
| [[moenergies]] || molecular orbital energies || eV || List of Arrays of rank 1
|-
| [[mosyms]] || orbital symmetries || || List of Lists
|- 
| [[mpenergies]] || molecular electronic energies with Möller-Plesset corrections || eV || Array of rank 2
|-
| [[mult]] || multiplicity of the system || h/2&pi; || Integer
|-
| [[natom]] || number of atoms ||  || Integer
|-
| [[nbasis]] || number of basis functions ||  || Integer
|-
| [[nmo]] || number of molecular orbitals || || Integer
|-
| [[nocoeffs]] || natural orbital coefficients || || Array of rank 2
|-
| [[scfenergies]] || molecular electronic energies after SCF (Hartree-Fock, DFT) || eV || Array of rank 1
|-
| [[scftargets]] || targets for convergence of the SCF || || Array of rank 2
|-
| [[scfvalues]] || current values for convergence of the SCF || || Array of rank 3
|-
| [[vibanharms]] || vibrational anharmonicity constants || cm<sup>-1</sup> || Array of rank 2
|-
| [[vibdisps]] || cartesian displacement vectors || &Delta;&Aring; || Array of rank 3
|-
| [[vibfreqs]] || vibrational frequencies || cm<sup>-1</sup> || Array of rank 1
|-
| [[vibirs]] || IR intensities || km mol<sup>-1</sup> || Array of rank 1
|-
| [[vibramans]] || Raman intensities || A<sup>4</sup> amu<sup>-1</sup>  || Array of rank 1
|-
| [[vibsyms]] || symmetries of vibrations || || List of strings
|}

== Details of current implementation ==

'''N/A''' = not applicable, '''N/P''' = applicable, but not possible, '''T/D''' = to do

{| border="1" cellspacing="0" cellpadding="5" text-align="center" align="center"
|+'''Current implementation of parsers'''
!          !! width="80px" | ADF     !! width="80px" | GAMESS !! width="80px" | GAMESS-UK !! width="80px" | Gaussian !! width="80px" | Jaguar     !! width="80px" | Molpro !! width="80px" | ORCA !! width="80px" | Turbomole
|- 
! aonames  ||   N/A    ||    &radic;       ||   &radic;       ||    &radic;     ||   &radic;      ||      &radic;  || &radic; ||   T/D
|-
! aooverlaps  ||    N/A   ||    &radic;      ||    &radic;      ||  &radic;       ||     &radic;    ||   &radic;  || &radic;  ||   T/D
|-
! atomcharges || &radic; || &radic; || &radic; || &radic; || T/D || T/D || &radic; || T/D
|-
! atomcoords  ||  &radic;     ||   &radic;        ||    &radic;      ||   &radic;   ||    &radic;  ||       &radic; || &radic; ||   T/D
|-
! atombasis ||   T/D    ||    &radic;     ||   &radic;     ||   &radic;      ||    &radic;     ||     &radic; || T/D  ||   T/D
|-
! atommasses ||   &radic;     ||   T/D  ||     T/D    ||      &radic;      ||   T/D       ||     T/D      ||      T/D  || ?
|-
! atomnos  ||   &radic;    ||    &radic;       ||    &radic;      ||   &radic;      ||  &radic;       ||      &radic; || &radic; ||   T/D
|-
! atomspins || T/D || T/D || T/D || T/D || T/D || T/D || &radic; || T/D
|-
! ccenergies ||      N/A        ||    &radic;  ||    T/D   || &radic; ||     N/A    ||    T/D || T/D ||   T/D
|-
! charge ||  &radic;    ||    &radic;       ||    &radic;      ||   &radic;      ||  &radic;       ||     &radic; || &radic; ||   T/D
|-
! coreelectrons ||     &radic;     ||     &radic;        ||        T/D         ||       &radic;   ||     T/D   ||  T/D || T/D ||   T/D
|-
! etenergies  ||   &radic;    ||    &radic;    ||   N/A      ||   &radic;      ||   &radic;     ||  T/D  ||  T/D   ||   T/D
|-
! etoscs  ||   &radic;    ||     &radic;       ||    N/A     ||   &radic;      ||   &radic;  || T/D ||  T/D   ||   T/D
|-
! etrotats  ||   &radic;    ||     T/D(?)       ||     N/A     ||   &radic;      ||    T/D     || T/D ||  T/D   ||   T/D
|- 
! etsecs  ||   &radic;    ||     &radic;   ||    N/A     ||   &radic;      ||    &radic;    || T/D  || T/D   ||   T/D
|-
! etsyms  ||   &radic;    ||     &radic;    ||   N/A      ||    &radic;     ||    &radic;    || T/D(?) || T/D   ||   T/D
|-
! fonames  ||   &radic;   ||   N/A   ||   N/A   ||   N/A   ||   N/A  ||  N/A || N/A   ||  N/A
|-
! fooverlaps ||   &radic;   ||   N/A ||   N/A   ||   N/A   ||   N/A  ||  N/A || N/A   ||   N/A
|-
! fragnames ||   &radic;   ||   N/A ||   N/A   ||   N/A   ||   N/A  ||  N/A || N/A   ||   N/A
|-
! frags ||   &radic;   ||   N/A ||   N/A   ||   N/A   ||   N/A  ||  N/A  || N/A   ||   N/A
|-
! gbasis  ||   N/A    ||    &radic;      ||    &radic;    ||    &radic;     ||   N/P      ||  &radic;  || T/D   ||   T/D
|-
! geotargets  ||   &radic;    ||    &radic;       ||   &radic;       ||    &radic;     ||    &radic;     ||  T/D(?) || &radic;   ||   T/D
|-
! geovalues  ||   &radic;    ||     &radic;      ||     &radic;     ||   &radic;      ||  &radic; ||  T/D(?) || &radic;   ||   T/D
|-
! grads || N/A   ||   N/A ||   N/A   || &radic; ||   N/A  ||  N/A || N/A   ||   N/A
|-
! hessian || T/D || T/D || T/D || T/D  ||  T/D      ||    &radic;     || T/D   ||   T/D
|-
! homos  ||   &radic;    ||      &radic;     ||     &radic;     ||    &radic;     ||     &radic;    ||  &radic; || &radic;   ||   T/D
|-
! mocoeffs  ||   &radic;    ||    &radic;       ||    &radic;      ||   &radic;      ||    &radic;    ||       &radic;  || &radic;   ||   T/D
|-
! moenergies  ||   &radic;    ||     &radic;      ||    &radic;      ||   &radic;      ||    &radic;    ||    &radic;  || &radic;   ||   T/D
|-
! mosyms  ||   &radic;    ||    &radic;      ||    &radic;      ||    &radic;     ||   &radic;      ||  T/D(?) || T/D   ||   T/D
|-
! mpenergies    || N/A     || &radic; ||  &radic;  || &radic; || &radic;  || &radic;  || T/D   ||   T/D
|-
! mult ||  &radic;    ||    &radic;       ||    &radic;      ||   &radic;      ||  &radic;       ||     &radic;   || &radic;   ||   T/D
|-
! natom  ||    &radic;   ||     &radic;     ||     &radic;     ||     &radic;    ||    &radic;     ||    &radic;  || &radic;      ||   T/D
|-
! nbasis  ||   &radic;    ||     &radic;      ||     &radic;     ||     &radic;    ||   &radic;      ||    &radic;   || &radic;   ||   T/D
|-
! nmo  ||   &radic;    ||    &radic;       ||     &radic;     ||   &radic;      ||    &radic;     ||  &radic;(?) || &radic;   ||   T/D
|-
! nocoeffs || T/D || &radic; || T/D || &radic; || T/D || T/D || T/D || T/D
|-
! scfenergies  ||   &radic;    ||     &radic;      ||    &radic;      ||    &radic;     ||  &radic;      || &radic; || T/D   ||   T/D
|-
! scftargets  ||   &radic;    ||     &radic;      ||   &radic;       ||    &radic;     ||   &radic;      ||    &radic;   || T/D     ||   T/D
|-
! scfvalues  ||    &radic;   ||     &radic;      ||   &radic;       ||   &radic;      ||    &radic;     ||  T/D(?) || T/D   ||   T/D
|-
! vibanharms || N/A   ||   N/A ||   N/A   || &radic; ||   N/A  ||  N/A || N/A   ||   N/A
|-
! vibdisps  ||   &radic;       ||     &radic;      ||     &radic;        ||      &radic;        ||      &radic;   || T/D(?) || T/D   ||   T/D
|-
! vibfreqs  ||   &radic;    ||     &radic;      ||   &radic;       ||   &radic;      ||   &radic;  ||      &radic;     || &radic;   ||   T/D
|-
! vibirs  ||   &radic;    ||     &radic;      ||    &radic;      ||    &radic;     ||   &radic;      ||    &radic;     || &radic;(?)   ||   T/D
|-
! vibramans  ||   T/D    ||     &radic; (PC GAMESS)   ||     &radic;     ||    &radic;     ||     N/A    ||  T/D(?)  || T/D   ||   T/D
|-
! vibsyms  ||   N/A    ||    N/A       ||    N/A      ||  &radic;     ||    &radic;     ||    &radic;     || T/D    ||   T/D
|-
|}

[[Category:Development|Parsed data]]
[[Category:Parsed data| ]]
