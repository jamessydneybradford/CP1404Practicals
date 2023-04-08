"""List of names with eception handling
"""

names = ["Jim", "Lindsay", "Bruce", "Dmitry"]

# is_valid_number = False
#
# while not is_valid_number:

keep_going = "y"
while keep_going != "q":
    try:
        number = int(input(f"Enter the position number of the name you want to print from the list (1-{len(names)}): "))
        invalid_number = "n"
    except ValueError:
        print(f"Invalid. Enter a number between 1 and (1-{len(names)}): ")
        invalid_number = "y"
    if invalid_number == "n":
        if 1 <= number <= len(names):
            try:
                print(f"Name {number} in the list is {names[number - 1]}")
            except IndexError:
                print(f"Must be a number between 1 and {len(names)}")
        else:
            print(f"{number} is not in the correct number range 1 to {len(names)}.")
            is_valid_number = False
    keep_going = input("Press a key to continue, or q to quit: ")

