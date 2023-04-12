"""
Password_stars
"""


def main():
    get_password()


def get_password():
    minimum_length = 10
    password = " "
    password = input("Enter password:")
    while password != "":
        if len(password) < minimum_length:
            print("Password too short")
            print(password)
        else:
            print_stars(password)
        print()
        password = input("Enter password:")


def print_stars(password):
    print(password, "  ", end="", )
    for i in range(0, len(password)):
        print("*", end="")




main()
