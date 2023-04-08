"""
Parallel lists 1
"""


def main():
    run_tests()


def find_oldest(names, ages):
    return names[ages.index(max(ages))]
    oldest_age = -1
    oldest_index = -1
    for i, age in enumerate(ages):
        if age > oldest_age:
            oldest_age = age
            oldest_index = i
        if age == oldest_age:
            oldest_indexes.append(i)
    return names[oldest_index]


def run_tests():
    i = 0
    names = ["Bill", "Jane", "Sven"]
    ages = [21, 34, 56]
    oldest_indexes = []
    #    print(names[i], "is", ages[i], "years old")
    print("The oldest is: ", find_oldest(names, ages))


main()
