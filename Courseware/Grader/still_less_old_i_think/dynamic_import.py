import importlib.util


def import_source(module_name):
    module_file_path = module_name.__file__
    module_name = module_name.__name__
    print(module_file_path)
    print(module_name)
    import_from_pathname(module_file_path, module_name)


def import_from_pathname(module_file_path, module_name):
    module_spec = importlib.util.spec_from_file_location(
        module_name, module_file_path)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    print(dir(module))

    msg = 'The {module_name} module has the following methods:' \
        ' {methods}'
    print(msg.format(module_name=module_name,
                     methods=dir(module)))
    return module

if __name__ == '__main__':
    import warnings
    import_source(warnings)

    path = '/Users/david/EclipseWorkspaces/grading/201730/'
    subpath = 'Session07_Test1/mutchler/src/problem1.py'
    module_name = 'problem1'

    module = import_from_pathname(path + subpath, module_name)
    print(dir(module))
    problem = 'test_problem1a'
    result = getattr(module, problem)()
    print(result)
