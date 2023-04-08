"""
Ascii table
"""

LOWER = 33
UPPER = 128


is_valid_character = False
while not is_valid_character:
    try:
        character = (input("Enter a single character: "))
        if len(character) != 1:
            is_valid_character = False
        else:
            is_valid_character = True
    except TypeError:
        print("Invalid - single character only: ")
print(f"The ASCII code for {character}, is {ord(character)}")

is_valid_number = False
while not is_valid_number:
    try:
        number = int(input("Enter a number between 33 and 127: "))
        if number < 33 or number > 127:
            is_valid_number = False
        else:
            is_valid_number = True
    except ValueError:
        print("Please enter a valid integer: ")
print (f"The character for ASCII code {number} is: {chr(number)}")


print("Ascii", "Character")
for i in range(LOWER, UPPER):
    print(f"{ord(chr(i))}    {chr(i):}")


