"""
Guessing game with files and exceptions
"""

FILENAME = "secret.txt"


def load_number(filename):
    # load integer from file named filename.
    try:
        infile = open(filename, "r")
        number = int(infile.read())
    except ValueError:
        print(f"Invalid contents in file {filename}")
        number = 6
    except FileNotFoundError:
        print(f"File {filename} not found")
        number = 4
    else:
        infile.close()
    return number


def main():
    secret = load_number(FILENAME)
    guess = get_valid_number()
    while guess != secret:
        guess = get_valid_number()

    print("You got it!!")


def get_valid_number():
    is_valid_input = False
    while not is_valid_input:
        try:
            guess = int(input("Guess: "))
            is_valid_input = True
        except ValueError:
            print("Invalid integer")
    return guess


main()
