# Inheritance
# Of course, a language feature would not be worthy of the name “class” without
# supporting inheritance.

# Python has two built-in functions that work with inheritance:

# Use isinstance() to check an instance’s type: isinstance(obj, int) will be True only if obj.__class__ is int or some class derived from int.

# Use issubclass() to check class inheritance: issubclass(bool, int) is True since bool is a subclass of int. However, issubclass(float, int) is False since float is not a subclass of int.

# Multiple inheritance
# Python supports a form of multiple inheritance as well. A class definition with multiple base classes looks like this:

class Animals:

    alive = True

class Dog(Animals):
    pass

print(Dog.alive)
