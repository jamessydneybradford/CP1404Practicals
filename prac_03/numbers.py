# file_in = open('numbers.txt', 'r')
# total = 0
# for i in range(0, 2):
#     number = int(file_in.readline())
#     total = total + number
# print("Total is", total)
# file_in.close()


file_in = open('numbers.txt', 'r')
line_count = 0
for line in file_in:
    line_count += 1
    print(line_count, " ", line)
file_in.close()

file_in = open('numbers.txt', 'a')
print("Total lines ", line_count, file=file_in)
print("Total lines ", line_count)
file_in.close()
