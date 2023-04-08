"""
List manipulation a list of names and scores
"""
from operator import itemgetter

score_pairs = [['Derek', 7], ['Carrie', 8], ['Bob', 6]]

name, score = input("Enter the name and score:").split(",")
score = int(score)
print(type(name))
print(type(score))
score_pairs.append([name, score])

print(score_pairs)
score_pairs.sort(key=itemgetter(1), reverse=True)  # sort using second part of list pair
print(score_pairs)

for score_pair in score_pairs:
    print(f"{score_pair[0]:.3} {score_pair[1]}")


