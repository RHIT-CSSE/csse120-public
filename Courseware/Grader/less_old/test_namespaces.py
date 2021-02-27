"""
<describe what this module has/does>

Created on May 10, 2015.
Written by: mutchler.
"""

import importlib.util
import importlib.machinery


def main():
    """ Calls the   TEST   functions in this module. """
    blah('test_namespaces1.py')
    blah('test_namespaces2.py')
    blah('test_namespaces3.py')
    blah('test_namespaces2.py')


def blah(module):
    try:
        module_name = 'mod_' + module
        loader = importlib.machinery.SourceFileLoader(module_name, module)
        mod = loader.load_module(module_name)
        x = mod.tryme()
        print(x)
    except:
        print('skipping')

    pathname = '../test_namespaces/' + module
    spec = importlib.util.spec_from_file_location(module_name,
                                                  pathname)
    module = spec.loader.load_module(module_name)
    x = mod.tryme()
    print(x)

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
