"""
Grid
"""
import pylint


def main():
    number_of_rows = int(input("Enter number of rows: "))
    number_of_columns = int(input("Enter the number of columns: "))
    print_grid(number_of_rows, number_of_columns)
    run_tests()


def print_grid(number_of_rows, number_of_columns):
    # Version 3
    print(f"{'*' * number_of_columns}\n" * number_of_rows)
    # Version 2
    # for i in range(number_of_rows):
    #     print("*" * number_of_columns)
    # Version 1
    # for i in range(number_of_rows):
    #     for j in range(number_of_columns):
    #         print("* ", end="")
    #     print()


def get_limits():
    low = int(input("Low"))
    high = int(input("High"))
    return low, high


def run_tests():
    low, high = get_limits()
    print(low, high)
    print(type(low))


main()
