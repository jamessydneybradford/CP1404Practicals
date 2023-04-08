# in_file = open("names_and_ages.txt", "r")

with open("names_and_ages.txt", "r") as in_file:
    in_file.readline()  # read first line to ignore the header
    for line in in_file:
        # print(line)
        parts = line.strip().split(",")
        name = parts[0]
        age = int(parts[1])
        print(f"{name}, will be {age+1} in one year's time)")

