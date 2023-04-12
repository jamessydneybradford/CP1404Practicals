"""
This is the Person client code that will use the Person class
by importing the module person.
"""
# Notice the case. The Person class is imported from the person module.
from person import Person
from operator import itemgetter


p1 = Person("Jim", 186)
persons = [p1]
p2 = Person("Vinnie", 184)
persons.append(p2)
p3 = Person("Mariana", 169)
persons.append(p3)

print(persons)


