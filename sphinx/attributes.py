import sys

if __name__ == "__main__":

    # Make sure we are importing a module cloned into this directory,
    # which should be cloned right before calling this script in order
    # to make sure we are dealing with the most current version.
    sys.path = [p for p in sys.path if not 'usr/local' in p]
    sys.path.append('cclib/src/')
    import cclib

    data_doc = cclib.parser.data.ccData.__doc__
    print(data_doc)