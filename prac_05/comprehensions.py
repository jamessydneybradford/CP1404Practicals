"""
Comprehensions
"""


names = ["Bill", "Jane", "Sven"]
ages = [21, 34, 56]
numbers = [10, -10, 20, 30, -40, 20, 10, 10]

# print([number for number in numbers])

dictionary = dict(zip("abc", [1,2,3]))
print(dictionary)

dictionary_name_to_age = dict(zip(names, ages))

print(dictionary_name_to_age)
