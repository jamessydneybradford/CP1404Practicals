"""
Quick picks
"""
import random

PICKS_PER_GAME = 6
LOWEST_VALUE = 1
HIGHEST_VALUE = 45
number_of_picks = int(input("How many quick picks? "))

numbers = []
game_count = 0
duplicate_count=0

while game_count < number_of_picks:
    number_count = 0
    game_count += 1
    print(f"{game_count:>4})", end="")
    while number_count < PICKS_PER_GAME:
        number_count += 1
        pick = random.randint(LOWEST_VALUE, HIGHEST_VALUE)
        if pick not in numbers:
            numbers.append(pick)
        # print(pick)
        else:
            duplicate_count += 1
            number_count -= 1
    numbers.sort()
    for pick in numbers:
        print(f"{pick:>4}", end="")
    numbers.clear()
    print("")
print("duplicates =", duplicate_count)

