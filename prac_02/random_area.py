"""
Random area given length
"""
# from random import randint
import random
length = int(input("Enter the length: "))
width = random.randint(1, length)
area = length * width
print(f"The length is {length}. The random width is {width}. So the area is {area}")

