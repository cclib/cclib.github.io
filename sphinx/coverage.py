import os
import sys

from attributes import check_cclib


if __name__ == "__main__":

    import cclib
    check_cclib(cclib)

    thispath = os.path.dirname(os.path.realpath(__file__))

    testpath = thispath + '/_build/cclib/test/'
    os.chdir(testpath)
    sys.path.append('.')

    from testall import parsers, testall

    ncols = len(parsers)+1
    print("%-20s"*ncols % tuple(["attributes"] + parsers))

    logpath = thispath + "/coverage.tests.log"
    with open(logpath, "w") as flog:
        alltests = [testall([p], stream=flog) for p in parsers]
    attributes = sorted(cclib.parser.data.ccData._attrlist)
    for attr in attributes:
        print("%-20s"*ncols % tuple([attr] + [any([attr in t.data.__dict__ for t in tests]) for tests in alltests]))