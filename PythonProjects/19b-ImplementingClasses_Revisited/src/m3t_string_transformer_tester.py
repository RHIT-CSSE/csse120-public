"""


       elsa = NameDropper("Elsa")
       sarah = NameDropper("Sarah")
       a = elsa.transform("Robots are fun.")
       b = elsa.transform("Crayons are fun too.")
       c = sarah.transform("You make me happy.")
       d = elsa.transform("I am unsure about rocks.")
       print(a, b, c, d, sep='\n')

       prints:
           Elsa says Robots are fun.
           Elsa says Crayons are fun too.
           Sarah says You make me happy.
           Elsa says I am unsure about rocks."
"""

"""
      
       elsa = Censor("a")
       sarah = Censor()
       a = elsa.transform("Alice in Wonderland")
       b = elsa.transform("Tweedledee and Tweedledum")
       c = sarah.transform("Tweedledee and Tweedledum")
       d = elsa.transform("Cats are naturally lazy")
       print(a, b, c, d, sep='\n')
       
       prints:
           Alice in Wonderl*nd
           Tw**dled** and Tw**dl*dum
           Tw**dled** and Tw**dl*dum
           C*ts a*e n*tur*lly l*zy

"""