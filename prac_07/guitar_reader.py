"""
Guitar reader
"""
from operator import attrgetter

from guitar import Guitar


def read_guitars(guit):
    """
    This function opens the file guitars.csv to read the data into a list of objects
    """
    try:
        in_file = open('guitars.csv', 'r')  # open for reading
    except FileNotFoundError:
        print("The file cannot be found")  # in case file is nit there
        exit(0)  # normal termination
    print("Guitars")
    print("")
    for line in in_file:
        # Strip newline from end split it into parts
        parts = line.strip().split(',')
        name = parts[0]
        year = parts[1]
        price = parts[2]
        # Create object with the parts
        guitar_obj = Guitar(name, year, price)
        # append object to list
        guitars.append(guitar_obj)
    in_file.close()  # close the file
    return guitars


def print_guitars(guit):
    """
    the function prints the list of guitar objects in a formatted manner
    """
    for guit in guitars:
        print(f"{guit.name:40}{guit.year:5}{float(guit.price):.2f}")


def main():
    """This program manipulates the guitar.csv file which is a list of guitar objects
    the following functionality is provided:
    list guitars  - lists the guitar objects contained in the file
    Sort guitars  - lists tne guitar objects in year order from oldest to newest
    Add guitars   - lists the guitars objects and give the user the option of adding guitars
                    When the user is finished the new guitars (if any) are written to the file.
    """


def print_menu():
    """Prints the menu"""
    print("")
    print("(L)ist guitars")
    print("(S)ort guitars")
    print("(A)dd guitars")
    print("(Q)uit")


print_menu()
choice = input("Enter your choice:")
choice = choice.upper()

while choice != "Q":
    if choice == "L":  # List the objects
        guitars = []  # list for objects
        read_guitars(guitars)  # call to read in the objects from file
        print_guitars(guitars)
        print_menu()
        choice = input("Enter your choice:")
        choice = choice.upper()
    elif choice == 'S':  # Sort the objects
        guitars = []  # list for objects
        read_guitars(guitars)  # call to read in the objects from file
        # Lambda expression for sort
        # guitars.sort(key=lambda x: x.year)
        # there are a number of ways this could be done. Possibly even a bubble sort.
        guitars.sort(key=attrgetter("year"))  # sort the objects in year order. Attrgetter is used for sorting objects
        print("Guitars (sorted by age oldest to newest)")
        print_guitars(guitars)
        print_menu()
        choice = input("Enter your choice:")
        choice = choice.upper()
    elif choice == 'A':
        guitars = []  # list for objects
        read_guitars(guitars)  # call to read in the objects from file
        print_guitars(guitars)
        out_file = open('guitars.csv', 'w')  # Creates an empty file. Hence the need to read in the data prior
        choice_to_continue = input("Add new guitar? (Y/n): ")  # Iteration to allow addition of multiple guitars
        choice_to_continue = choice_to_continue.upper()
        while choice_to_continue == 'Y':
            guitar_name = input("Guitar name: ")
            guitar_year = input("Year of manufacture: ")
            guitar_price = input("Price: ")
            guitar = Guitar(guitar_name, guitar_year, guitar_price)
            guitars.append(guitar)
            print_guitars(guitars)
            choice_to_continue = input("Add new guitar? (Y/n): ")
            choice_to_continue = choice_to_continue.upper()
        for guitar in guitars:
            # write each item on a new line in the correct format
            out_file.write(f"{guitar.name},{int(guitar.year)},{float(guitar.price)}\n")
        out_file.close()  # Close the file
        print_menu()
        choice = input("Enter your choice:")
        choice = choice.upper()
    else:
        print("Invalid choice")
        print_menu()
        choice = input("Enter your choice:")
        choice = choice.upper()


main()





# The sorting code
# print("Guitars")
# print_guitars(guitars)
# # Lambda expression for sort
# # guitars.sort(key=lambda x: x.year)
# guitars.sort(key=attrgetter("year"))
# print("Guitars (sorted by age oldest to newest)")
# print_guitars(guitars)


# in_file.close()

"""
Creating new guitar objects and writing to file
"""

# open the file to write to

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
