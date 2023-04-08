"""
Testable functions - when writing functions think how they can be tested
Following the Single responsibility principle helps here.
The code is written just to determine the category - it does onl.y one thing
Now testing this is easy because you can code the tests and test them without manual input
at the command line
"""


def determine_category(age: int) -> str:
    if age < 18:
        return "child"
    elif age < 65:
        return "adult"
    else:
        return "geriatric"


print(determine_category(17))
print(determine_category(18))
print(determine_category(64))
print(determine_category(65))
print(determine_category(90))

# CLEVER testing
def is_adult(age: int) -> bool:
    return age >= 18

print(f"Got {is_adult(18)} - expected True")
print(f"Got {is_adult(17)} - expected False")

assert is_adult(20)
assert not is_adult(0)
