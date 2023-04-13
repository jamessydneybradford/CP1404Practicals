"""
overloading
"""

# x = 12  # int
# x = 23.9  # float
# x = "jim"  # str
# x = 'jim'  # str
# x = [12, 12]  # list
# x = (23, 12)  # tuple
# x = {23, 29}  # set
x = False

print(isinstance(x, object))
print(isinstance(x, int))
print(isinstance(x, float))
print(isinstance(x, str))
print(isinstance(x, list))
print(isinstance(x, tuple))
print(isinstance(x, set))
print(isinstance(x, bool))

# when do object for type comparison ise the isinstance(obj, int) NOT if type(object) is type(1)

# example
y = {34, 37}  # set
z = [34, 37]  # set

print(isinstance(y, type(z)))  # Comparing a set to a list is False

a = "12"
b = "3"
print(a + b)
print(a * 5)


# What is a+b? the answer depends on the type
# The + operator has two operands. What are their types
# Python uses introspection to find the type and then select the correct operator
# The + operator is overloaded

class Point:
    """A Cartesian point (x, y) - all values are floats unless otherwise stat"""

    def __init__(self, x=0.0, y=0.0):
        """Initialise a point with x and y coordinates."""
        self.x = x
        self.y = y

    def __add__(self, other):
        """Add two points together to form a new Point."""
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        """Determine if two Points are equal based on location."""
        return self.x == other.x and self.y == other.y


print("Comparing Points")
here = Point(1, 2)
there = Point(2, 3)
print(here + there)  # This will call the __add__

if here == there:  # This will call the __eq__
    print("Same")
else:
    print("Not same")

# How does x + y map to __add__?
# These are equivalent expressions.
# The first object calls the __add__ method with the second object passed as an argument
# x is bound to self; y is bound to the method parameter
# You rarely need to use the latter syntax. Avoid using "unbound" syntax like str.upper("string")


"""
Do this now comparing objects
"""

"""
In Python, dunder methods are methods that allow instances of a class to interact 
with the built-in functions and operators of the language. 
The word “dunder” comes from “double underscore”.
They are also called magic methods 
"""

class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


print("Comparing Person objects")
person1 = Person("Jim", 40)
person2 = Person("Jim", 40)

if person1 == person2:  # This will call the __eq__
    print("Same")
else:
    print("Not same")

"""
Cities
"""


class City:
    def __init__(self, name="", population=0, percent=0.0):
        self.name = name
        self.population = population
        self.percent = percent

    def __repr__(self):
        return f"{self.name}, {self.population}, {self.percent}"

    def __lt__(self, other):
        return self.population < other.population  # population decides who is greatest

    def __eq__(self, other):
        return self.population == other.population

    def __le__(self, other):
        return self.population <= other.population

    def __add__(self, other):
        return City(self.name + other.name, self.population + other.population, 100.00)


def run_test():
    print("Cities")
    c1 = City("Tokyo", 13921000, 11.20)
    c2 = City("Rome", 2761632, 4.7)
    print(c1)
    print(c2)
    print("Comparing Cities")
    print(c1 < c2)  # the < INVOKES the __lt__ magic function
    print(c1+c2)


if __name__ == '__main__':
    run_test()
