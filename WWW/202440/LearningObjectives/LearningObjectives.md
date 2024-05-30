COMMENT_BEGIN_INDICATOR = !!! BEGIN COMMENT
COMMEND_END_INDICATOR = !!! END COMMENT
COMMENT_INDICATOR = !!!
SESSION_INDICATOR = ^.*Session[ ]*[0-9]*:
EXAM_INDICATOR = Exam [0-9] | Final Exam

!!! BEGIN COMMENT:
### _READ THIS_ for the required format for this file:

The CSSE 120 Home Page is auto-generated from several files.
This file contains most of the data for generating the Course Schedule.

The first set of lines above must use the names per the assignments,
but the values for those names can be whatever this file itself uses
for those items.



The schedule is auto-generated from this file.  The Schedule Generator:

- Ignores any line that contains !!! in it (like this one).

- Ignores all lines between a line that contains the tag:
    >   !!! XXX COMMENT  <where XXX is in fact 'BEGIN'>

    and the next occurence thereafter of a line that contains the tag:
    >  !!! XXX COMMENT   <where XXX is in fact 'END'>

- Expects a line with the regular expression
    >  `Session[ ]*[0-9]*:`
    
    to mark the beginning of information about a Session.  These "Session lines" have HTML generated that is special to how a Session appears in the Schedule generated.  In particular:
    
    * Text prior to the word `Session` is ignored.
    * Treats the text from the colon `:` to the end of the line as the Session Title.
    * A slash `  /   ` in a Session Title forces a line break.

- Treats the information after each "Session line" as GitHub-Flavored Markdown.  See 
    - https://help.github.com/articles/markdown-basics/ for basics, and
    - https://help.github.com/articles/github-flavored-markdown/
      for GitHub's modifications.
      
- Inserts various HTML to format the Session beginning, number, title, top-level comments and lower-level contents.

- Uses the following additional markup:
    - Parenthetical expressions are rendered in smaller text.
    - But `((...))` is rendered in normal-sized text.
    - Ignores the Session numbering (it does it itself,
      numbering Sessions in the order that they appear in this file.

Notes:

For most of the first 15 or so sessions,
students are not expected to be solid on all of the learning objectives
listed for that session from that session alone.  Rather:

- Students are expected after the session to have
_SOME_ understanding of _MOST_ of the concepts.
- Forthcoming sessions will reinforce all the concepts of the session.
- Students will typically become solid on ALL the topics of a session by the end of the following 2 or 3 sessions for sessions early in the course, and sooner for sessions later in the course.

Throughout, to "use" a concept means to use that concept as needed
in a program, for solving a given problem.

!!! END COMMENT.

# Session 1: Introduction to Python, Objects, and Simple Loops

## Topics:
- The course as a _flipped classroom_
- What is _programming_?
  * What is _software engineering_?
  * What is _software development_ (aka _programming_)?
- What is a _programming language_?
    - Why have programming languages?
    - Why have so many different ones?
    - A short history of the evolution of programming languages (just for grins)
- Tools for software development
  * _PyCharm_, our _Integrated Development Environment (IDE)_
    - Getting a program from version control, New, from your computer
    - Editing a program.  Syntax errors (very briefly)
    - Running a program.  The console.  Run-time errors (very briefly).
  * _Git / Github_, our way to acquire and turn in work
    - _Version control_:  what, why
    - Version control, how:  FORK, CLONE, COMMIT, PUSH.
  * The Python _interpreter_
- Introduction to _Python_ (our programming language) and _objects_
DCM: FIX THE NEXT PART ala what Session 01 becomes.
  * Part 1:  Comments, Numbers, Strings, the _print_ function
    - Comments, e.g.  ```# Author: Bugs Bunny.```
    - Arithmetic expressions, e.g.,  ```3.1 * (4 + math.sin(1.83))```
    - Strings, e.g.  ```"May the Force be with you"```
    - The _print_ function
    - Sequential execution (line by line)
  * Part 2: _Names_ and _Assignment_
    - Assigning objects to names
    - Accessing objects referenced by names
    - ```import math```
    - Calling ```builtins``` functions
  * Part 3: Introduction to _using objects_
    - _Constructing_ (and initializing) objects.
    - Calling _methods_ on objects
    - Accessing and setting _instance variables_ of objects
  * Part 4: Definite loops (but with unused loop variables), e.g.
    ```for _ in range(40):```
    - Indentation to denote the body of the loop
- Application: Turtle graphics.
- Course policies
  - Academic Integrity
  - Welcoming Climate
  - Assessment (how you are graded)
  - Attendance and other policies

!!! BEGIN COMMENT

## Preparation:

- Preparation for Session 1: Summary.
- The Flipped Classroom.
- What is Software Engineering?  Software Development?  A Programming Language?
- Your First Programs:
     -- Part 1: Comments, Strings and the PRINT function — Video [5:04 minutes]
Part 2: Hello, World — YOUR first program — Video [4:13 minutes]
Part 3: Introduction to Objects via Turtle Graphics — Video [9:50 minutes]
Part 4: Loops (with Loopy Turtles) — Video [13:57 minutes]


   a. Hello, World
       -- Same as what students do in class for intro to PyCharm, PRINT et al, NAMES.
5. Objects:
     -- What they are
     -- Notation for constructing, applying methods, accessing/setting instance variables.
6. Your First OO Program:  Turtle graphics
     -- - Same as what students do in class, but abbreviated
7. Your First Loops
     -- with unused loop variable, in context of Turtle graphics)

2. Course Policies: Academic Honesty
3. Course Policies: Welcoming Climate
4. Course Policies: Assessment
5. Course Policies: Other (just a pointer to the documents)    
    3. Introduction to Objects via Turtle Graphics:
        - Constructing objects
        - Calling methods on objects
        - Accessing instance variables (fields) of objects
    4. Loops (with Loopy Turtles)
    
    !!! Should there be a video and exercise on calling FUNCTIONS?

9. What you need installed on your computer
[in the summer] 10. Special instructions for the Online version of this course


!!! Should there be a video that is "Introduction to Session 1"?

## In-class:

1. [10 minutes]
Quiz, welcome, what is a flipped classroom, answer questions, self-grade quiz.

2. [5 minutes]
Intro to PyCharm and **```m1e_comments_strings_print```**
   - via live-coding (and handout?)
   - Fork, clone and then open Session 1 project.
      > Students will have already done this, but demo it very briefly.
   - Examine and then run the code for ```m1e```:
     - Comments
     - Strings
     - Numbers
     - The _print_ function
     
3. [10 minutes]   **```m2_todo_and_commit_push```**
   - via live-coding (and handout?)
   - Do TODOs in ```m2```, marking them DONE.
   - Commit and push.
     > Some students will discover at this point that they failed
       to FORK the project.\
       ```VCS ~ Git ~ Remotes``` can verify this.\
       Have an assistant help them fix this AFTER doing the live-coding
       in the next item.
       
4. [10 minutes]   **```m3_names_and_expressions```**
   - begin via live-coding (first few TODOs)
   - Students experience:
     - ```import math```
     - arithmetic expressions
     - names
     - Other stuff similar to what was once "PyDev Console" work.  KISS.
     
5. [30 minutes]   **```m4_SimpleTurtle_objects```**
   - begin via live-coding, showing:
     - DOT trick
     - pop-up documentation
   - Students experience:
     - doc-strings
     - Constructing (and initializing) an object.  Assigning it a name.
     - Applying methods to objects.
     - Accessing/setting instance variables of objects.

6. [20 minutes] **```m5_putting_it_all_together```**

7. [15 or more minutes]
  **```m6e_LoopyTurtles```** and
  **```m7_your_way_cool_turtles```**
   - Example, then cool pictures using this strategy:
   
         Make a loop (no loop variable needed).
         Inside the loop:
           a. Draw something simple.
           b. Turn a bit; or pick up the pen, move a bit and put the pen back down.
              Maybe also change the Pen color or something.

!!! END COMMENT

### Session 2: Defining Functions, Calling Functions & Methods / Names, Scope and Lifetime / Using Objects / Correcting Syntax Errors

- Executing (aka _running_) a program:
    * Hardware:
        - Memory.  Addresses.
        - The Central Processing Unit (CPU).
    * Software:
        - Names, aka variables.  References.
        - Evaluating expressions, executing statements.
- Objects (types / values) and Names
    * Types (_float, int, string, function, module_) and values.
    * Names, aka variables.
        - Assignment.
        - Names are _references_ to objects.
        - Dynamic typing versus static typing.
        - The importance of choosing good names.
        - (Maybe) why "names" instead of "variables", in Python
- Expressions:
    * Arithmetic operators: ```+  -  *  /  **```
    * Relational operators: ```<  <=  >  >=  !=  ==```
    * Parentheses and precedence.
    * String arithmetic.
- Functions:
    * What are they, why are they important?
    * What is a function _call_?
        - Sending arguments to parameters.  Relationship to assignment.
        - Flow of control.
- Statements.
- Modules:
    * _import_ and the dot trick.
    * The _builtins_ module.
- Reading a simple program, II:
    * Function definitions:
        - In the module.
        - In _builtins_ and other modules.
    * The use of indentation for blocks of code.
    * The role of _main_.
    * Flow of control (sequential but interrupted by function calls).
- Coding to a specification:
    * What is it, why is it important?
    * Functions as black boxes.
    * Doc-strings.
- Object-Oriented Programming (OOP):
    * What is it, why use it (brief introduction).
    * vs Procedural Programming.
- Classes and objects:
    * Class vs instance of the class.
        - UML class diagrams (for a single class).
        - Object diagrams.
    * Methods (aka function attributes).
    * Instance variables (aka data attributes).
- Using objects:
    * Constructing instances of a class.
    * Applying methods to objects.
    * Referencing and setting instance variables of objects.
- Debugging techniques I: Correcting syntax (aka compile-time) errors.
- Application: Turtle graphics.

    * Calling _functions_ defined in _modules_.
    
!!! BEGIN COMMENT
Videos:

TRY 1. Introduction to Session 2.
MUST 2. What happens when a program runs: hardware and software
    - Hardware: Memory and addresses
    - Software: Objects, Names (aka variables): assigning and referencing
    - Hardware: CPU
    - Software: Evaluating expressions, executing statements
    - Hardware: Program counter, Fetch/Execute cycle.
    - Software: Sequential control flow, interrupted by function calls et al
WAIT 3. Summary of concepts from Session 1: (all EXCEPT oo and loops)
CURRENT OK? 4. Introduction to Functions:
     - What they are
     - Why they are valuable
         - Organize the program
         - Arguments/Parameters: Re-use functions.
     - Defining a function
     - Scope of names inside a function
     - The flow of control when you CALL a function
CURRENT OK?  5. Coding to a Specification
VALERIE IF NEED BE 6. The flow of control via functions that call functions: the STACK
   - First just for program flow (no arguments or local variables)
   - Then add arguments and local variables
VALERIE? 7. Tracing code by hand, with function calls (practice)
CURRENT OK? 8. Object oriented programming - What, Why
CURRENT OK? 9. Classes - what objects know and can do, UML class diagram
CURRENT OK? 10. Objects and Classes - using objects:
    - Constructing an object (and assigning a name to it)
    - Calling methods
    - Setting and referencing instance variables
TRY 11. Debugging techniques I: Correcting syntax (aka compile-time) errors
MUST 12. Live-coding Preview of Session 2  [NEEDS TO BE REDONE!]
WAIT 13. Reference video on PyCharm and Git/Github.

#### !!! Consider: Move the Rosebotics exercise OUT of Session 2, to avoid the jarring switch from Turtle graphics to it.

!!! END COMMENT

### Session 3: Definite Loops, Accumulators, Summing / Arguments and Parameters / Unit Testing, Test-Driven Development

- Namespaces, Scope:
    * Local scope (in functions).
    * Global scope (in a module).
    * Builtins scope.
- Lifetime of a name in a function:
    * When it comes into existence.
    * When it goes out of existence.
    * How a _stack_ implements function calls.
- Loops:
    * When is a loop needed?
    * What goes before the loop? Inside it? After it?
    * Implementing loops using ```for k in range(n): ...```.
    * Flow of control (revisited to allow FOR loops).
- Accumulators: Summing.
- Implementing and calling functions:
    * Sending arguments to parameters.  Relationship to assignment.
    * Local scope.
    * Side effects.
    * Returning a value (and capturing it in a variable).
    * Doc-strings and coding to a specification (revisited).
    * The _power_ of parameters.
- Using objects (reinforcing previous sessions).
- Testing:
    * Test-Driven Development (TDD).
    * Unit testing.
    * Writing simple tests.
- Coding: First Solve It By Hand.
- Debugging techniques II:
    * Identifying when a run-time exception has occurred.
    * Understanding a stack trace.
    * Tracing code by hand.
- Application:
    * RoseGraphics.
    * Using an Application Programming Interface (API) (brief introduction).

### Session 4: The Accumulator Pattern: Summing, Counting, in Graphics / Conditionals, Boolean Logic / Code Reviews, Tracing Code by Hand

- Conditionals:
    * boolean values (_True_ and _False_).
    * _if, if-else, if-elif..._ statements.
    * Flow of control (revisited to allow conditionals).
- Accumulators: Summing (revisited), Counting, Graphical Patterns.
    * Using the loop variable vs using accumulators.
- More practice tracing code by hand.
- Code Reviews:
    * What are they, why do them.
    * How to do them (brief introduction).
    * Code inspection checklists.

### Session 5: Pair Programming / Debugging Run-Time Errors, Stack Traces / Robots and Motion

- Reinforce all concepts to date.
- Pair programming.
- Writing good unit tests.
!!! Maybe writing GOOD unit tests should go MUCH later in the course.
- Conventions and advice for choosing names.
- More practice tracing code by hand.
- Debugging techniques III:
    * Understanding simple run-time error messages.
    * Using such messages to correct errors.
- Application:
    * Robots and Motion.
    * Using an Application Programming Interface (API) (brief revisit).
    * Using the RoseBot API.

### Session 6: More Debugging Tools / Practice for Exam 1

- More practice tracing code by hand.
- More practice using pop-up help and the dot trick in Eclipse/PyDev.
- Exam 1 Practice.
- Debugging techniques IV:
    * Using the _stack trace_ to know where to start.
    * Using _print_ statements.
    * Using a _debugger_.

### Session 7: Names are _References_ to Objects / Box-and-Pointer Diagrams / Mutating Objects

- Names are _references_ to objects (revisited).
- Mutation:
    * What is it?
    * Why is it dangerous if abused?
    * Why is it useful?
    * Functions and methods that mutate their arguments.
- _is_ and _not is_ versus _==_ and _!=_.
- Box-and-pointer diagrams.
- More practice tracing code by hand.
- Floating point arithmetic, roundoff (basic introduction).
- Integer arithmetic: % and //.
- Multiple arguments in _range_ expressions.

### Session 8: Exam 1 (Evening Exam: 8:30 p.m. to 11 p.m.)

#### !!! Do a careful look for anything else that we skipped over that needs to be here!

### Session 9: Implementing Classes, I

- Reading a simple class definition:
    * _class_ expression.
    * The *__init__* method.
    * The *__repr__* method.
    * The _self_ parameter.
- Implementing classes I:
    * Writing a _class_ expression.
    * Defining constructor (*__init__*) methods.
    * Defining instance variables (aka data attributes):
        - For parameters of *__init__*.
        - For "remembering" attributes of the object.
    * Defining methods (aka function attributes) that:
        - Reference and/or set instance variables.
        - Call other methods.
        - Require the introduction of an instance variable.
        - Have parameters (other than _self_) that are instances of the class.
        - Return an instance of the class.
    * What _self_ means and how to use it.
- Testing class implementations.
- More practice tracing code by hand.

### Session 10: Implementing Classes, II

- Implementing classes II:
    * A deeper understanding of _self_.
- More practice implementing classes.
- Debugging techniques V: Deciphering more complicated run-time error messages.

### Session 11: Sequences, I / What is a Sequence? / Patterns for Sequences: Iterating Through All or Part of a Sequence

- Sequences and indices.
    * Lists, tuples, strings.
    * The index vs the item at that index.
- Patterns for iterating through sequences, I:
    * Forward/backwards, with steps.  Using three-argument _range_ expressions.
    * Selecting items.
    * Counting/summing/etc.
- Debugging techniques VI: Locating the source of a run-time error.

### Session 12: Sequences, II / Patterns for Sequences: Find, Building a Sequence, and Max-Min

- Patterns for iterating through sequences, II:
    * Find (using linear search).
    * Max/min.
    * Building sequences using the + operator.
- Debugging techniques VII: Debugging loops.

### Session 13: Waiting for Events, Indefinite Loops / Input from a Console / The RoseRobot class (Drive Motors)

- *** This will cover the Drive Motors exercises ***

- Reinforce concepts re implementing classes.
- Reinforce concepts re sequences.
- Implementing classes that involve immutable sequences.
- Conditionals (revisited):
    * Boolean (Logical) operators.
    * Bitwise operators.
    * When to use ```elif``` and/or ```else```.  When not to them.
    * Nested conditionals.
    * Pitfalls.

### Session 14: Debugging (again) / Practice for Exam 2

- Revisiting in the context of classes and sequences:
    * Names are _references_ to objects (revisited).
    * Mutation:
    * What is it?
    * Why is it dangerous if abused?
    * Why is it useful?
    * Functions and methods that mutate their arguments.
    * _is_ and _not is_ versus _==_ and _!=_.
    * Box-and-pointer diagrams.
- More practice tracing code by hand.

  **!!! On MWR terms, Exam 2 should be Session 16.  During Session 15, do what would otherwise be Session 16.  The material of Session 15 is NOT on Exam 2.**

### Session 15: Sequences, III / More Patterns / Mutating Sequences

- Waiting for Events.
- Indefinite Loops.
    * Flow of control (revisited to allow WHILE loops).
    * ```while True: ... if <condition>: break``` vs ```while <condition>...```
- Loops (revisited):
    * When is a loop needed?
    * What goes before the loop? Inside it? After it?
    * Use a definite or indefinite loop?
    * Implementing loops using ```for k in range(n): ...```.
    * Implementing loops using ```while True: ... if <condition>: break ...```
- Input from the Console
    * The _input_ function
    * The _int_ and _float_ functions
- Application: Robots and Sensors.
    * Waiting for events.
    * Augmenting the RoseBot library.


### Session 16: Exam 2.

### Session 17: The RoseRobot class (Digital Inputs)

- Patterns for iterating through sequences, III:
    * Find (using linear search) (revisited).
    * Max/min (revisited).
    * Two indices at each iteration.
    * Two sequences in parallel.
    * Building sequences:
    * Using the + operator.
    * Using mutation:
        - via _append_ (for lists).
        - plus _list_ and _tuple_ (for tuples).
        - plus _list_ and _join_ (for strings).
- Mutating sequences:
    * Which sequences are immutable?
    * Why both lists and tuples?
    * Mutating the (deep) insides of a tuple.
    * Deleting items from a list.
    * Copy vs deep copy.
- Using + versus _append_: comparing efficiencies.

### Session 18: Loops within Loops

- Loops revisited:
    * When is a loop needed?
    * What goes before the loop? Inside it? After it?
    * Use a definite or indefinite loop?
    * When is a _nested_ loop needed?
- Nested Loops:
    * Application: printing on the console.
    * Application: 2-d graphics.
    * Replacing the inner loop by a function call.  Helper functions.

### Session 19: Sequences within Sequences

- Nested Loops:
    * Application: printing on the console (revisited).
    * Application: 2-d graphics (revisited).
    * Application: sequences of sequences.
- Sequence, list and string methods.
- The _in_ and _not in_ relational operators.
- Application: String processing.
- Application: Talking and Singing Robots.
    * Augmenting the RoseBot library.
    * Blocking messages versus nonblocking messages.

### Session 20: Dictionaries / Looping (summary)

- Dictionaries
    * Attributes are implemented using dictionaries.
- More practice at nested loops.
- Finite state machines: Application to more complicated logic. 
- Looping patterns: Summary.

### Session 21: Practice for Exam 3

### Session 22: Exam 3.

### Session 23: Event-Driven Programming / Graphical User Interface (GUI) Programming / Throw-away Project

- Project Teams.
    * Meet each other, establish goals and expectations.
    * How a team project works:
        - Team member responsibilities.
        - Individual accountability.
        - Divide and conquer. Integration of the parts.
- Event-Driven Programming.
- Tkinter I:
    * Root/mainloop.
    * Frame.
    * Button.  Using _lambda_ functions to respond to button-clicks.
    * Entry. Using _lambda_ functions and _get_ to acquire values from Entries.
- Using a shared repository effectively:
    * Avoiding conflicts.
    * Correcting conflicts.
    * When to commit (and when not to).
    * The importance of commit messages.
- Application: Throw-away project.
    * Using m0 and *my_frame* functions to structure the application.
    * Sharing a RoseBot object across modules.
    * Sharing functions across modules.

### Session 24: Project Kickoff / Sprint 1 begins

- Project Kickoff.
    * Project theme.
    * Project features.
    * How the project is graded.
- Agile/Scrum:
    * Sprints.
    * Features.
    * Sprint planning.
    * Stand-up meetings.
- Materials made available for applications, including:
    * More Tkinter GUI objects.
    * File IO (for text files)
    * Socket IO.
    * Multiple threads and processes.
    * Multiple implementations of the same interface.
    * PID line-following.
    * Following waypoints.
    * Image processing.
    * Robot conversation (via LEDs + camera with vision processing,
    or via IR emitters and receivers), protocols.
    
    ***!!! FIX THE ABOVE LIST TO MATCH REALITY.***

- Sprint 1 begins.

### Session 25: Procedural decomposition / Sprint 1 continues

- Procedural decomposition.

    ***!!! FIX THE FOLLOWIN TO MATCH REALITY.***
    
- Inheritance (brief introduction):
    * The concept.
    * Reading classes in an inheritance hierarchy:
        - How _self_ climbs the inheritance hierarchy.
        - Methods that override, in whole or in part.
        - Multiple inheritance (very, very brief introduction).
        - The _object_ class.
- Object-Oriented Design (OOD) (brief introduction):
    * The _IS-A_ and _HAS-A_ concepts.
    * Reading _IS-A_ and _HAS-A_ relationships in UML class diagrams.
- Implementing classes, III: Using _IS-A_ and _HAS-A_ relationships.
    * Application: Robots.
    * Augmenting simple classes in the RoseBot library that inherit (beyond just from _object_).
    * Implementing simple classes that _HAS_A_ RoseBot.
- Using an Application Programming Interface (API) (revisited).
- Implementing classes IV:
    * Implementing classes that inherit from (aka extend) other classes.
    * Application: extending Tkinter classes.
- Sprint 1 continues.

### Session 26: Sprint 1 ends, Sprint 2 begins

### Session 27: Sprint 2 continues.

### Session 28: Sprint 2 ends, Sprint 3 begins.

### Session 29: Sprint 3 continues.

### Session 30: Sprint 3 (and the project) ends.
