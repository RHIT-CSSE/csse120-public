'''
Created on Mar 15, 2014

@author: mutchler
'''

def main():
    session = 1
    grader = Grader(session)


class Grader(object):
    def __init__(self, session_number_or_project_name,
                 module_name=None, function_name=None):
        self.project = self.get_project(session_number_or_project_name)
        self.original_module = self.get_modules()


    def get_project(self, session_or_project):
        if type(session_or_project) == int:
            return None
        else:
            return None

    def get_modules(self, module_name):
        self.original = None

    def grade(self):
        students = self.get_students()
        self.checkout_projects(students)
        for module in self.modules:
            self.grade_module(module)

    def get_students(self):
        pass

    def grade_module(self, module):
        pass

    def checkout_projects(self):
        pass

class Evaluator:
    def __init__(self, modules_to_evaluate):
        self.modules_to_evaluate = modules_to_evaluate

    def run(self, module_to_test):
        pass

class ResultsEvaluator(Evaluator):
    def __init__(self, modules_to_evaluate):
        pass

if __name__ == '__main__':
    main()
