"""
Menus
"""
name = input("Enter name: ")
print("[H]ello")
print("(G)oodbye")
print("(Q)uit")
choice = input("Enter choice: ")
while choice != "Q":
    if choice == "H" or choice == "h":
        print("Hello!", name)
        print()
    elif choice == "G" or choice == "g":
        print("Goodbye!", name)
        print()
    else:
        print("Invalid entry!")
        print()
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    choice = input("Enter choice: ")
print()
print("Finished - Bye!")
