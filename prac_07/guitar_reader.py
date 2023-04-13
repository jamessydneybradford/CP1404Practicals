"""
Guitar reader
"""
from operator import attrgetter

from guitar import Guitar
import csv

def print_guitars(guitars):
    for guitar in guitars:
        print(f"{guitar.name:40}{guitar.year:5}{float(guitar.price):>8.2f}")


def main():
    """Read file of guitar details, save as objects, display them in oldest to newest order"""


guitars = []
# Open the file for reading
try:
    in_file = open('guitars.csv', 'r')
except FileNotFoundError:
    print("The file cannot be found")
    exit(0)
for line in in_file:
    # Strip newline from end and split it into parts (CSV)
    parts = line.strip().split(',')
    name = parts[0]
    year = parts[1]
    price = parts[2]
    # Create object with the parts
    guitar = Guitar(name, year, price)
    # append object to list
    guitars.append(guitar)

# The sorting code
# print("Guitars")
# print_guitars(guitars)
# # Lambda expression for sort
# # guitars.sort(key=lambda x: x.year)
# guitars.sort(key=attrgetter("year"))
# print("Guitars (sorted by age oldest to newest)")
# print_guitars(guitars)


in_file.close()
#
"""
Creating new guitar objects and writing to file
"""
# open the file output append
out_file = open('guitars.csv', 'a')

print_guitars(guitars)

choice = input("Add new guitar? (Y/n): ")
while choice.upper() == "Y":
    guitar_name = input("Guitar name: ")
    guitar_year = input("year of manufacture: ")
    guitar_price = input("Price: ")
    guitar = Guitar(guitar_name, guitar_year, guitar_price)
    guitars.append(guitar)
    print_guitars(guitars)
    choice = input("Add new guitar? (Y/n)")





out_file.close()

main()

# Points to note

# if __name__ == '__main__'

# print("Got here")
# # get the length of the list
# n = len(guitars)
# # go through the list n number of times
# for i in range(n):
#     print("got here 1")
#     # variable to keep check for any swaps
#     swap = False
#     # traverse through all adjacent elements
#     for j in range(0, n - i - 1):
#         # if current element is less than guitar than next element, swap them
#         print("got here 2")
#         print(guitar[j].year < guitar[j + 1].year)
#         if guitar[j] < guitar[j + 1]:
#             print("swapping")
#             guitar[j], guitar[j + 1] = guitar[j + 1], guitar[j]
#             swap = True
#             print(swap)
#     # if no swaps, then break out of the loop
#     if swap == False:
#         print(swap)
#         break
