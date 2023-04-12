class Student:
    # Constructor : polulates the variable local to the function
    def __init__(self, first_name="", last_name="", student_id=0):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

    # A default string function to return data - usually used in development
    # It returns a human-readable, or informal, string representation of an object.
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"

    # The destructor is not needed but is here for reference
    # Python has garbage collection
    def __del__(self):
        print('Student is deleted.')


# Simple example class usage (client code)
first_name = input("First name: ")
last_name = input("Last name: ")
student_id = int(input("ID: "))
s1 = Student(first_name, last_name, student_id)
print(s1.first_name, "has ID", s1.student_id)

print(str(s1))
print(type(str(s1)))
del s1


                                                                                