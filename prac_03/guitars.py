
with open("guitars.txt", "r") as in_file:
    in_file.readline()  # read first line to ignore the header
    for line in in_file:
        # print(line)
        parts = line.strip().split(",")
        make = parts[0]
        year = int(parts[1])
        price = float(parts[2])
        print(f"make {make}, year {year}, price {price:.f2} ")
