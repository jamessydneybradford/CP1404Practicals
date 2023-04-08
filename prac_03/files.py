file_in = open('data.txt', 'r')
line = file_in.read()
print(line)  # prints the whole file
file_in.close

file_in = open('data.txt', 'r')
line = file_in.readline()
print(line)  # prints first line
file_in.close

file_in = open('data.txt', 'r')
line = file_in.readlines()
print(line)  # prints first 2 lines
file_in.close


file_in = open('data.txt', 'r')
for line in file_in:
    line_string = str(line)
    print(line_string)
file_in.close