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
            print(results[student])


class StandardRecorder(Recorder):
    pass


def main():
    main_for_testing.main()

if __name__ == '__main__':
    main()
