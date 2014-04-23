import os
import sys

from attributes import check_cclib


if __name__ == "__main__":

    # Import cclib and check we are using the version from a subdirectory.
    import cclib
    check_cclib(cclib)

    # Change directory to where tests are and import testall correctly.
    thispath = os.path.dirname(os.path.realpath(__file__))
    testpath = thispath + '/_build/cclib/test/'
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
    colwidth = 15
    colfmt = "%%-%is" % colwidth
    dashes = ("="*(colwidth-1) + " ") * ncols

    print(dashes)
    print(colfmt*ncols % tuple(["attributes"] + parsers))
    print(dashes)

    # Eventually we want to move this to cclib.
    not_applicable = {
        'ADF' : ['aonames', 'aooverlaps', 'ccenergies', 'mpenergies'],
        'GAMESS' : ['fonames', 'fooverlaps', 'fragnames', 'frags'],
        'GAMESSUK' : ['fonames', 'fooverlaps', 'fragnames', 'frags'],
        'Gaussian' : ['fonames', 'fooverlaps', 'fragnames', 'frags'],
        'Jaguar' : ['fonames', 'fooverlaps', 'fragnames', 'frags'],
        'Molpro' : ['fonames', 'fooverlaps', 'fragnames', 'frags'],
        'NWChem' : ['fonames', 'fooverlaps', 'fragnames', 'frags'],
        'ORCA' : ['fonames', 'fooverlaps', 'fragnames', 'frags'],
        'Psi' : ['fonames', 'fooverlaps', 'fragnames', 'frags'],
    }
    not_possible = {
        'Psi' : ['aooverlaps'],
    }

    # For each attribute, get a list of Boolean values for each parser that flags if it has
    # been parsed by at least one unit test. Substitute an OK sign or T/D string appropriately,
    # with the exception of attributes that have been designated as N/A.
    attributes = sorted(cclib.parser.data.ccData._attrlist)
    for attr in attributes:
        parsed = [any([attr in t.data.__dict__ for t in tests]) for tests in alltests]
        for ip, p in enumerate(parsed):
            if p:
                parsed[ip] = "√"
            else:
                if attr in not_applicable.get(parsers[ip], []):
                    parsed[ip] = "N/A"
                elif attr in not_possible.get(parsers[ip], []):
                    parsed[ip] = "N/P"
                else:
                    parsed[ip] = "T/D"
        print(colfmt*ncols % tuple([attr] + parsed))

    print(dashes)
