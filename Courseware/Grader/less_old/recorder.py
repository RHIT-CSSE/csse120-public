"""
"""
# TODO: Put a comment above.

import main_for_testing


class Recorder(object):
    # TODO: Implement this class.
    def __init__(self):
        pass

    def record(self, result):
        pass

    def record_all_results(self, results):
        students = sorted(results.keys())
        for student in students:
            print(student, results[student])

    def record_failures(self, results):
        students = sorted(results.keys())
        for student in students:
            student_result = results[student].results_by_module
            problems = sorted(student_result.keys())
            for problem in problems:
                if not student_result[problem].wasSuccessful():
                    print(student, problem,
                          student_result[problem])

class StandardRecorder(Recorder):
    pass


def main():
    main_for_testing.main()

if __name__ == '__main__':
    main()
