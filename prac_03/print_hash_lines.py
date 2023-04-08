"""
Prints lines from file that start with a #
"""

FILENAME = "testfile.txt"


def main():
    try:
        infile = open(FILENAME, "r")
    except FileNotFoundError:
        print(f"File {FILENAME} not found")
        exit(0)
    line_count = 0
    hash_line_count = 0
    for line in infile:
        line_count += 1
        line_string = str(line)
        # print(line_string[0])
        if line_string[0] == "#":
            print(f"Line {line_count} : {line_string}")
            hash_line_count += 1
    infile.close()
    print("")
    print(f"There were {hash_line_count} occurrence(s) of #")


main()
