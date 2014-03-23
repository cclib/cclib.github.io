import os
import sys


def check_cclib(cclib):
    """Make sure we are importing code from a subdirectory, which should exist
    and should have been updated just before running this script. Note that
    this script does not assume any version in the module and just takes
    what it finds... so an appropriate checkout should be done first."""
    if cclib.__file__[:len(os.getcwd())] != os.getcwd():
        print("Do not seem to be importing from current directory")
        sys.exit(1)


if __name__ == "__main__":

    import cclib
    check_cclib(cclib)

    # Need to parse the ccData docstring, since only that currently
    # contains all the information needed for this table.
    data_doc = cclib.parser.data.ccData.__doc__
    attributes = [line for line in data_doc.split('\n') if line[:8].strip() == '']
    attributes = [line for line in attributes if "--" in line]

    # These are the widths of the columns in the table
    wattr = 20
    wdesc = 65
    wunit = 28
    wtype = 32

    dashes = "    "
    for w in [wattr, wdesc, wunit, wtype]:
        dashes += "="*(w-1) + " "
    header = "    "
    header += "Name".ljust(wattr)
    header += "Description".ljust(wdesc)
    header += "Units".ljust(wunit)
    header += "Data type".ljust(wtype)
    print(dashes)
    print(header)
    print(dashes)

    names = []
    for line in attributes:

        # There is always a double dash after the name.
        attr, desc = line.strip().split(' -- ')
        names.append(attr)

        # The type and unit are in parentheses, but these
        # are not always the only parentheses on the line.
        other = desc.split('(')[-1]
        desc = desc[:-len(other)-1].strip()
        other = other.split(')')[0]

        # Furthermore, the unit is not always there.
        if "," in other:
            atype, aunit = other.split(", ")
        else:
            atype = other
            aunit = ''
        
        attr = ("`%s`_" % attr).ljust(20)
        desc = desc.ljust(65)
        aunit = aunit.ljust(28)
        for i in range(1,4):
            atype = atype.replace('[%i]' % i, ' of rank %i' % i)
        print("    " + attr + desc + aunit + atype)

    print(dashes)
    print()

    for n in names:
        print(".. _`%s`: data_notes.html#%s" % (n, n))
