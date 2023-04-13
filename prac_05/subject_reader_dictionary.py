"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subject_details = get_data_from_file()
    print(subject_details)
    print(type(subject_details))
    for subject_detail in subject_details:
        # print(*subject_detail)
        print(f"{} is taught by {12} and has {3} students on {}".format(*subject_detail))

# CP1401 is taught by Ada Lovelace and has 192 students

def get_data_from_file():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    parts_list = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        parts_list.append(parts)
    input_file.close()
    return parts_list

main()