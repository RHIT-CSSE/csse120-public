"""
Uses conventional stubbing to grade RoseGraphics projects.

See main() for examples of actual grading.

Created on Aug 27, 2015.
Written by: hays.
"""

# from unittest.mock import patch, MagicMock
import imp
import rosegraphics as rg
from sys import stderr

canvases = []

class RoseWindowStub():
    def __init__(self, width=400, height=300, title='Rose Graphics',
        color='black', canvas_color=None,
        make_initial_canvas=True):
        canvas_color = "white"  # FIXME
        self._is_closed = False
        self.width = width
        self.height = height
        self.initial_canvas = RoseCanvasStub(self, width, height, canvas_color)

    def render(self):
        pass

    def get_next_mouse_click(self):
        return rg.Point(0, 0)

    def close_on_mouse_click(self):
        return None

    def continue_on_mouse_click(self,
        message=
        'To continue, click anywhere in this window',
        x_position=None,
        y_position=None,
        close_it=False,
        erase_it=True):
        return None



class RoseCanvasStub():
    def __init__(self, window, width, height, canvas_color):
        # super().__init__(window, width, height, canvas_color)
        canvases.append(self)
        self.recordedshapes = []
        self.shapes = []

    def _draw(self, shape):
        # super()._draw(shape)
        self.recordedshapes.append(shape)

    def render(self, seconds_to_pause=None):
        # super().render()  # don't pause
        pass

class RoseGraphicsGrader:
    def __init__(self,
                 student_module_name,  # "problem3"
                 path_to_student_module,  # "problem3.py"
                 solution_module_name,  # "problem3_solution"
                 path_to_solution_module):  # "problem3_solution.py"
        rg.RoseCanvas = RoseCanvasStub
        rg.RoseWindow = RoseWindowStub
        self.student_module = imp.load_source(student_module_name, path_to_student_module)
        self.solution_module = imp.load_source(solution_module_name, path_to_solution_module)
        for module in [self.student_module, self.solution_module]:
            module.rg.RoseCanvas = RoseCanvasStub
            module.rg.RoseWindow = RoseWindowStub

    def runTest(self, runner):
        """
            Calls the given module runner on the student code and the solution code.
            Compares the generated shapes.
            
            For instance, if the students write a function that takes a window and an integer,
            your runner might look like:
            
            def run_problem3a(module):
                window=rg.RoseWindow(500,500)
                module.problem3a(window, 5)
            
            
        """
        global canvases
        canvases = []
        runner(self.student_module)
        student_canvases = canvases
        canvases = []
        runner(self.solution_module)
        solution_canvases = canvases

        # print("#canvases: ", len(student_canvases), len(solution_canvases))
        if not len(student_canvases) == len(solution_canvases):
            raise AssertionError("Wrong number of shapes: " + str(len(student_canvases)) + " vs " + str(len(solution_canvases)))

        # compare shapes
        for i in range(len(student_canvases)):
            # this canvas should have same shapes as solution
            student_canvas = student_canvases[i]
            solution_canvas = solution_canvases[i]
            # print(student_canvas.recordedshapes, solution_canvas.recordedshapes)
            for shape in student_canvas.recordedshapes:
                if not shape in solution_canvas.recordedshapes:
                    raise AssertionError("Unexpected shape: " + str(shape))

def main():
    """ This method is really a series of self-tests,
    but you can use them as a basis for your own grading. """

    # sanity check: compare a student's work against itself. Should pass!
    grader = RoseGraphicsGrader('problem3_student', 'tests/problem3_solution.py', 'problem3_solution', 'tests/problem3_solution.py')
    def myrunner(module):
        """"
        This runner runs the module's test_problem3 function as-is. 
        As you might imagine, this can be a BAD idea because 
        students often hack the test code.
        """
        module.test_problem3()

    grader.runTest(myrunner)
    print("Test 1 passed")

    try:
        # test 2: compare shape with wrong color against correct solution. Should fail!
        grader = RoseGraphicsGrader('problem3_student', 'tests/problem3_bugged.py', 'problem3_solution', 'tests/problem3_solution.py')
        def myrunner2(module):
            """
            This runner is a copy/paste from the solution module.
            This is a BETTER way to write a runner.
            """
            # rectangle tunnel
            window = rg.RoseWindow(400, 400)
            points = [rg.Point(10, 10), rg.Point(10, 350), rg.Point(390, 350), rg.Point(390, 10)]
            colors = ["red", "black", "white"]
            module.problem3(window, points, 3, colors)
            window.render()
            window.close_on_mouse_click()

            # triangle tunnel
            window = rg.RoseWindow(400, 400)
            points = [rg.Point(200, 10), rg.Point(100, 310), rg.Point(400, 110)]
            colors = ["red", "white", "black"]
            module.problem3(window, points, 5, colors)
            window.render()
            window.close_on_mouse_click()

            # pentagon tunnel
            window = rg.RoseWindow(400, 400)
            points = [rg.Point(200, 10), rg.Point(0, 110), rg.Point(100, 310), rg.Point(300, 310), rg.Point(400, 110)]
            colors = ["red", "orange", "yellow", "lightgreen", "blue", "purple"]
            module.problem3(window, points, 20, colors)
            window.render()
            window.close_on_mouse_click()


        grader.runTest(myrunner2)
        print("Test 2 FAILED to find the difference in color", file=stderr)
    except AssertionError:
        print("Test 2 passed")

    # test 3: compare a student's work that has the wrong number of shapes. Should fail!
    try:
        grader = RoseGraphicsGrader('problem3_student', 'tests/problem3_bugged.py', 'problem3_solution', 'tests/problem3_solution.py')
        def myrunner3(module):
            """
            In theory, you can change the context of a function, but I don't know how in Python.
            """
            # grader.solution_module.test_problem3.apply(module)
            module.test_problem3()


        grader.runTest(myrunner3)
        print("Test 3 FAILED to find the difference in # shapes", file=stderr)
    except AssertionError:
        print("Test 3 passed")


#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
