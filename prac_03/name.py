file_out = open('name.txt', 'w')

name = input("Enter your name: ")
print(name, file=file_out)  # prints the whole file

file_out.close
