"""
First Demos
"""
from math import pi

# name = input("name: ")
# print ("Hello ", name)

monthly_cost = float(input("Monthly Cost: "))
total_cost = monthly_cost * 12
print(f"At the monthly cost of {monthly_cost} the total is cost is ${total_cost:.2f}")

print(pi)
print(f"{pi:.4f}")
print(f"{pi:10.4f}")
print(f"{pi:.3f}")
# Rounding up - when the number precision of the string is changed
print(int(pi))
