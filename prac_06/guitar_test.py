"""
guitar_test.py
"""
from guitar import Guitar

guitar1 = Guitar("Gibson L-5 CES", 1923, 16035.40)
guitar2 = Guitar("Another Guitar", 2013, 2000.00)

print(f"{guitar1.name}  : expected 100 - got {guitar1.get_age()}")
print(f"{guitar2.name}  : expected 10 - got {guitar2.get_age()}")
print(f"{guitar1.name}  : expected True - got {guitar1.is_vintage()}")
print(f"{guitar2.name}  : expected False - got {guitar2.is_vintage()}")


# guitars = [guitar1, guitar2]
#
# for guitar in guitars:
#     print(f"{guitar.name} {guitar.getage()} )
