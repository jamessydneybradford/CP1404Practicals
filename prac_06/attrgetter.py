"""
attrgetter - demo - used for sorting objects based on a specific field
"""
from operator import attrgetter
from person import Person  # using the person module to create person data

# A list of persons
data = [Person(name="Bob", height=118), Person(name="J1m", height=186), Person(name="Mariana", height=143)]
print(data)
data.sort(key=attrgetter("height"))
print(data)
