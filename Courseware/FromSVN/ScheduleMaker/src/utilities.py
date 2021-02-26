"""
"""
# TODO: Put a comment above.

# TODO: Figure out how to auto-indent the result of a call to
# to generic_repr.  That is, I want the result to look something like:
#   Grader(
#          WhatToGrade(
#                      Course(
#                             ...
#                      Project(
#                      ...
#          WhoToGrade(
#          ...

# TODO: Add an optional parameter that disables the line-breaking.


def generic_repr(instance_of_class, string_of_data_attributes):
    """
    Returns a generic representation of the given instance of a class,
    using the given string of data attributes that are stored in
    a data attribute, via (for example):
       self.blah = blah

    As such, this representation could (perhaps) be used to reconstruct
    the object if the class converts its arguments to data attributes.

    Here is an example.  For the  Foo  class that begins like this:

        class Foo(object):
            def __init__(blah, xxx, whatever=None):
                self.blah = blah
                self.xxx = xxx
                self.whatever = whatever

            def __repr__(self):
                return utilities.generic_repr(self, 'blah, ')

    the code snippet:
        foo = Foo(4, 'help')
        print(foo)

    prints:
    """
    # TODO: Indicate that the representation allows reconstruction
    # of the object only if the recursively-called representations
    # of the data attributes themselves use this generic_repr
    # (or its equivalent).

    # CONSIDER: Are there situations where  generic_repr  does NOT
    # return the intended string?  Where is breaks?  If so,
    # document those flaws.

    class_name = instance_of_class.__class__.__name__
    attribute_names = string_of_data_attributes.split()

    attributes = []
    for attribute_name in attribute_names:
        attributes.append(getattr(instance_of_class, attribute_name))

    format_string = '\n{}('
    format_string += (len(attributes) - 1) * '{!r}, \n'
    format_string += '{!r})\n'

    return format_string.format(class_name, *attributes)
