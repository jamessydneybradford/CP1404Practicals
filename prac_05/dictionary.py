"""
Dictionary
"""

name_to_age = {"Bill": 21, "Jane": 34, "Sven": 56}

print(name_to_age["Bill"])

name_to_age["Bill"] = 22

print(name_to_age["Bill"])

name_to_age["Bill"] += 1

print(name_to_age["Bill"])

name_to_age["Bill"] = 'blah'

print(name_to_age["Bill"])

name_to_age["Bill"] = 22

print(name_to_age["Bill"])

print(name_to_age.keys())

print(len(name_to_age))

name_to_age["Zara"] = 90

print(name_to_age["Zara"])

print(name_to_age)

del name_to_age["Zara"]

print(name_to_age)

name_to_age["Xara"] = 90

print(name_to_age)

name_to_age["Zara"] = name_to_age.pop("Xara")

print(name_to_age)

keys = name_to_age.keys()

print(keys)

print(type(keys))

print(list(keys))

print(type(list(keys)))

name_to_age["Tom"] = 13

print(keys)

print(len(keys))

# two different ways of iterating
for name in name_to_age:
    print(f"{name} is {name_to_age[name]}")

# the most useful
for firstname, age in name_to_age.items():
    print(f"{firstname} is {age}")
# Convert to list
ages = list(name_to_age.values())
ages.sort()
print(ages)
