# -*- coding: utf-8 -*-

from __future__ import print_function

import os
import sys

from attributes import check_cclib


if __name__ == "__main__":

    # Import cclib and check we are using the version from a subdirectory.
    import cclib
    check_cclib(cclib)

    # Change directory to where tests are and add it to the path. Because there are
    # separate directories for different branches/versions, and we use a symlink to
    # point to the one we want, we need to test the real path this link resolves to.
    if "cclib_prod" in os.path.realpath('cclib'):
        testpath = "_build/cclib_prod/test"
    else:
        assert "cclib_dev" in os.path.realpath('cclib')
        testpath = "_build/cclib_dev/test"

    os.chdir(testpath)
    sys.path.append('.')

    # The unittest code has changed in cclib, so try to run tests the new way and
    # revert to the old way if that fails. The code in both cases is very similar,
    # but don't merge it here at all. That's because cclib now generates coverage
    # information during data tests, so we want to save it to a file and commit
    # it along with the code, keeping the essence of this documentation closer
    # to the code. Then we can just read it back here to generate the table.
    #
    # Warning! This code is quite fragile, because the test code adds attributes
    # to classes dynamically (bad idea), so they get overwritten when we reuse
    # classes for unittests. See bellow how we collect ccData instances to sidestep
    # this issue; although that doesn't alleviate the issue entirely, and the fix
    # needs to happen in the cclib code.
    try:
        from test_data import all_modules
        from test_data import all_parsers
        from test_data import parser_names
        from test_data import DataSuite
        import inspect
        ds_args = inspect.getargspec(DataSuite.__init__).args
        thispath = os.path.dirname(os.path.realpath(__file__))
        logpath = thispath + "/coverage.tests.log"
        try:
            with open(logpath, "w") as flog:
                stdout_backup = sys.stdout
                sys.stdout = flog
                alltests = {}
                for p in parser_names:
                    # newer versions, changed in rev 17b5b263
                    if 'parsers' in ds_args:
                        suite = DataSuite(parsers={p: all_parsers[p]}, modules=all_modules, stream=flog)
                    else:
                        assert 'argv' in ds_args
                        suite = DataSuite(argv=[p], stream=flog)
                    suite.testall()
                    alltests[p] = [{'data': t.data} for t in suite.alltests]
                sys.stdout = stdout_backup
        except Exception as e:
            print("Unit tests did not run correctly. Check log file for errors:")
            print(open(logpath, 'r').read())
            print(e)
            sys.exit(1)

    except ImportError:
        from testall import parsers as parser_names
        from testall import testall
        thispath = os.path.dirname(os.path.realpath(__file__))
        logpath = thispath + "/coverage.tests.log"
        try:
            with open(logpath, "w") as flog:
                stdout_backup = sys.stdout
                sys.stdout = flog
                alltests = {}
                for p in parser_names:
                    tests = testall(parsers=[p], stream=flog)
                    alltests[p] = [{'data': t.data} for t in tests]
                sys.stdout = stdout_backup
        except Exception as e:
            print("Unit tests did not run correctly. Check log file for errors:")
            print(open(logpath, 'r').read())
            print(e)
            sys.exit(1)

    ncols = len(parser_names)+1
    colwidth = 20
    colfmt = "%%-%is" % colwidth
    dashes = ("="*(colwidth-1) + " ") * ncols

    print(dashes)
    print(colfmt*ncols % tuple(["attributes"] + parser_names))
    print(dashes)

    # Eventually we want to move this to cclib, too.
    not_applicable = {
        'ADF' : ['aonames', 'ccenergies', 'mpenergies'],
        'DALTON' : ['fonames', 'fooverlaps', 'fragnames', 'frags'],
        'GAMESS' : ['fonames', 'fooverlaps', 'fragnames', 'frags'],
        'GAMESSUK' : ['fonames', 'fooverlaps', 'fragnames', 'frags'],
        'Gaussian' : ['fonames', 'fooverlaps', 'fragnames', 'frags'],
        'Jaguar' : ['fonames', 'fooverlaps', 'fragnames', 'frags'],
        'Molpro' : ['fonames', 'fooverlaps', 'fragnames', 'frags'],
        'NWChem' : ['fonames', 'fooverlaps', 'fragnames', 'frags'],
        'ORCA' : ['fonames', 'fooverlaps', 'fragnames', 'frags'],
        'Psi' : ['fonames', 'fooverlaps', 'fragnames', 'frags'],
        'QChem' : ['fonames', 'fooverlaps', 'fragnames', 'frags'],
    }
    not_possible = {
        'Psi' : ['aooverlaps', 'vibirs'],
        'QChem' : ['aooverlaps'],
    }

    # For each attribute, get a list of Boolean values for each parser that flags
    # if it has been parsed by at least one unit test. Substitute an OK sign or
    # T/D appropriately, with the exception of attributes that have been explicitely
    # designated as N/A. Note that the OK checkmark is Unicode, so we will need to
    # decode it and them encode the line before printing.
    attributes = sorted(cclib.parser.data.ccData._attrlist)
    for attr in attributes:
        parsed = [any([attr in t['data'].__dict__ for t in alltests[p]]) for p in parser_names]
        for ip, p in enumerate(parsed):
            if p:
                parsed[ip] = "√".decode('utf-8')
            else:
                if attr in not_applicable.get(parser_names[ip], []):
                    parsed[ip] = "N/A"
                elif attr in not_possible.get(parser_names[ip], []):
                    parsed[ip] = "N/P"
                else:
                    parsed[ip] = "T/D"
        print((colfmt*ncols % tuple(["`%s`_" % attr] + parsed)).encode('utf-8'))

    print(dashes)
    print("")

    for attr in attributes:
        print(".. _`%s`: data_notes.html#%s" % (attr, attr))
