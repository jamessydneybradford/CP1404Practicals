"""
guitars.py
"""
from guitar import Guitar

guitars = []

print("My guitars!")

'''
Uncomment lines below for data entry
'''
# name = input("Name: ")
# while name != "":
#     year = int(input("Year: "))
#     cost = float(input("Cost: "))
#     guitar = Guitar(name, year, cost)
#     guitars.append(guitar)
#     print(f"{name} ({year}) ${cost:.2f} added")
#     name = input("Name: ")

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
print("These are my guitars:")

guitar_count = 1
for guitar in guitars:
    if guitar.is_vintage():
        vintage = "(Vintage)"
    else:
        vintage = ""
    print(f"Guitar {guitar_count:}: {guitar.name}, worth ${guitar.cost} {vintage}")
    guitar_count += 1

