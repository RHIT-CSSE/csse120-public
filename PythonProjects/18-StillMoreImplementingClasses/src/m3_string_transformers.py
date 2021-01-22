"""
This exercise specifies a bunch of classes, each of which has only:
  -- The constructor method  __init__  with whatever parameters it needs
  -- A  transform  method that takes a string and "transforms" it,
       returning the transformed string.

The exercise provide practice at determining what INSTANCE VARIABLES
are necessary in a class definition.

Authors: David Mutchler, Sana Ebrahimi, Sriram Mohan, Mohammed Noureddine,
         Vibha Alangar, Matt Boutell, Dave Fisher, their colleagues, and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
"""
A NameDropper has a name (string) associated with it.
Its  transform  method transforms the phrase that it is given by putting     
   "BLAH says "
in front of the phrase, where BLAH is the name associated with the NameDropper.

       elsa = NameDropper("Elsa")
       elsa.transform("Robots are fun.")
          returns     "Elsa says Robots are fun."
"""
# TODO: 2. Implement the NameDropper class and add some code that tests it.
###############################################################################


###############################################################################
"""
A Censor has a character (string) associated with it, that defaults to the
character "e". (Hint: Google for "python default parameter" to learn defaults.)
Its  transform  method transforms the phrase that it is given
by replacing each occurrence of its character with an asterisk ("*").

       elsa = Censor("a")
       elsa.transform("Cats are naturally lazy")
          returns     "C*ts *re n*tur*lly l*zy"
       
       sarah = Censor()
       sarah.transform("Tweedledee and Tweedledum")
           returns     "Tw**dl*d** and Tw**dl*dum"
 
"""
# TODO: 3. Implement the Censor class and add some code that tests it.
#   HINT:  Throughout, using string methods to do all the heavy lifting.
#   Type        "" then DOT           or, if you prefer,  "xxx" then DOT
#   and PAUSE to let the DOT trick show you string methods.
###############################################################################


###############################################################################
"""
A Counter's transform  method transforms the phrase that it is given
by putting a number in front of the phrase, that goes 1, 2, 3, ...

       elsa = Counter()
       elsa.transform("Hello")         returns "1. Hello"
       elsa.transform("Goodbye")       returns "2. Goodbye"
       elsa.transform("Sing for me")   returns "3. Sing for me"
"""
# TODO: 4. Implement the Counter class and add some code that tests it.
###############################################################################


###############################################################################
"""
A SlowThinker's transform  method transforms the phrase it is given into
the phrase that it was PREVIOUSLY given.  It returns "START" the first time.

       elsa = SlowThinker()
       elsa.transform("Hello")           returns "START"
       elsa.transform("Goodbye")         returns "Hello"
       elsa.transform("Sing for me")     returns "Goodbye"
       elsa.transform("What is next?")   returns "Sing for me"
"""
# TODO: 5. Implement the SlowThinker class and add some code that tests it.
###############################################################################


###############################################################################
"""
A Doubler's transform  method transforms the phrase it is given into
the phrase, followed by a space, followed by the phrase again.

       elsa = Doubler()
       elsa.transform("Hello")           returns "Hello Hello"
       elsa.transform("Goodbye")         returns "Goodbye Goodbye"
       elsa.transform("Sing for me")     returns "Sing for me Sing for me"
"""
# TODO: 6. Implement the Doubler class and add some code that tests it.
###############################################################################


###############################################################################
"""
A Repeater has a positive integer N, that defaults to 1.
Its transform  method:
  -- when called the first time, transforms the phrase it is given into
     N    copies of the phrase, one after the other.
  -- when called the second time, transforms the phrase it is given into
     N+1  copies of the phrase, one after the other.
  -- when called the third time, transforms the phrase it is given into
     N+2  copies of the phrase, one after the other.
  -- etc.

       elsa = Repeater(3)
       elsa.transform("Hello")
              returns "HelloHelloHello"
       elsa.transform("Goodbye")
              returns "GoodbyeGoodbyeGoodbyeGoodbye"
       elsa.transform("Watch me")
              returns "Watch meWatch meWatch meWatch meWatch me"
"""
# TODO: 7. Implement the Repeater class and add some code that tests it.
###############################################################################


###############################################################################
"""
An UpperLowerCaser's transform  method transforms the phrase it is given into:
  -- all upper-case the first time that it is called
  -- all lower-case the second time that it is called
  --  [alternates from there: upper-case, lower-case, upper-case, etc.]

       elsa = UpperLowerCaser()
       elsa.transform("Hello")        returns "HELLO"
       elsa.transform("Goodbye")      returns "goodbye"
       elsa.transform("Watch me")     returns "WATCH ME"
       elsa.transform("This Is OKK")  returns "this is okk"
       elsa.transform("This Is OKK")  returns "THIS IS OKK"
"""
# TODO: 8. Implement the UpperLowerCaser class and add some code that tests it.
###############################################################################
