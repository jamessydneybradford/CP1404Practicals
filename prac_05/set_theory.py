"""
Set theory
"""

my_subjects = {'CP1401', 'CP1404', 'MA1000'}
your_subjects = {'CP1404', 'MA1008', 'NM1010'}
print("My subjects")
print(my_subjects)
print("Your subjects")
print(your_subjects)
print(f"{'union':21}: ", my_subjects | your_subjects)
# All of the subjects
print(f"{'difference':21}: ", my_subjects - your_subjects)
# subjects that I do that you don't do
print(f"{'intersection':21}: ", my_subjects & your_subjects)
# subjects that we both do
print(f"{'symmetric difference':21}: ", my_subjects ^ your_subjects)
# All of the subjects that only one of us does




