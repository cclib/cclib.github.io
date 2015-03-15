# -*- coding: utf-8 -*-

import inspect
import os
import sys

from attributes import check_cclib


def check_coverage(attr, tests):
    """Determine whether an attribute is covered by the provided tests.

    The current idea of coverage is that a test parses needs to parse an attribute
    and also use it in at least one test method. This is not rock solid since
    the attribute may be mentioned in the source but not actually tested.
    """
    for t in tests:

        # If the attribute is parsed by the test, it will end up in its ccData object.
        if attr in t.data.__dict__:

            methods = [m for m in dir(t) if callable(getattr(t, m))]
            testmethods = [m for m in methods if m[:4] == "test"]

            # Ideally we would like to have the attribute inside an assertion, but that
            # often does not happen if it's used to derive some value.
            if any([attr in inspect.getsource(getattr(t, tm)) for tm in testmethods]):
                return True

    return False


if __name__ == "__main__":

    # Import cclib and check we are using the version from a subdirectory.
    import cclib
    check_cclib(cclib)

    # Change directory to where tests are and import testall correctly.
    # Because there are separate directories for different branches/versions,
    # we are taking the easy way out and require the directory containing
    # tests to be passed as an argument (the only one).
    thispath = os.path.dirname(os.path.realpath(__file__))
    testpath = sys.argv[1]
    os.chdir(testpath)
    sys.path.append('.')
    from testall import parsers, testall

    # Try running all unit tests, and dump output to a file. In case there is some
    # rogue output from the tests, switch sys.stdout to the open log, too.
    logpath = thispath + "/coverage.tests.log"
    try:
        with open(logpath, "w") as flog:
            stdout_backup = sys.stdout
            sys.stdout = flog
            alltests = [testall([p], stream=flog) for p in parsers]
            sys.stdout = stdout_backup
    except Exception as e:
        print("Unit tests did not run correctly. Check log file for errors:")
        print(open(logpath, 'r').read())
        print(e)
        sys.exit(1)

    ncols = len(parsers)+1
    colwidth = 18
    colfmt = "%%-%is" % colwidth
    dashes = ("="*(colwidth-1) + " ") * ncols

    print(dashes)
    print(colfmt*ncols % tuple(["attributes"] + parsers))
    print(dashes)

    # Eventually we want to move this to cclib.
    not_applicable = {
        'ADF' : ['aonames', 'ccenergies', 'mpenergies'],
        'DALTON' : ['aooverlaps'],
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
        'Psi' : ['aooverlaps'],
    }

    # For each attribute, get a list of Boolean values for each parser that flags
    # if it has been parsed by at least one unit test. Substitute an OK sign or
    # T/D appropriately, with the exception of attributes that have been explicitely
    # designated as N/A. Note that the OK checkmark is Unicode, so we will need to
    # decode it and them encode the line before printing.
    attributes = sorted(cclib.parser.data.ccData._attrlist)
    for attr in attributes:
        parsed = [check_coverage(attr, tests) for tests in alltests]
        for ip, p in enumerate(parsed):
            if p:
                parsed[ip] = "√".decode('utf-8')
            else:
                if attr in not_applicable.get(parsers[ip], []):
                    parsed[ip] = "N/A"
                elif attr in not_possible.get(parsers[ip], []):
                    parsed[ip] = "N/P"
                else:
                    parsed[ip] = "T/D"
        print((colfmt*ncols % tuple(["`%s`_" % attr] + parsed)).encode('utf-8'))

    print(dashes)
    print("")

    for attr in attributes:
        print(".. _`%s`: data_notes.html#%s" % (attr, attr))
