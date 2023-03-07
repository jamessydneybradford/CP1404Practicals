"""
age
"""
age = int(input("Enter your age:"))
while age <= 0 or age > 120:
    print("Invalid age!")
    age = int(input("Enter your age:"))
    if age < 5:
        category = "baby"
    elif age < 18:
        category = "child"
    elif age < 66:
        category = "adult"
    else:
        category = "older"
print(f"Your age {age} is considered as {category}.")
