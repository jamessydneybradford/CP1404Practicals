"""
List exercises
"""

# number_of_numbers = int(input("Enter the number of numbers you are going to use:"))
# numbers = []
# for i in range(0, number_of_numbers):
#     numbers.append(int(input(f"Enter item {i + 1} of the {number_of_numbers} numbers:")))
# print(f"The first number is {numbers[0]}")
# print(f"The last number is {numbers[-1]}")
# print(f"The smallest number is {min(numbers)}")
# print(f"The largest number is {max(numbers)}")
# average = sum(numbers) / len(numbers)
# print(f"The average of the numbers is {average}")


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter a username: ")

if username in usernames:
    print("Access granted!")
else:
    print("Access denied!")
    