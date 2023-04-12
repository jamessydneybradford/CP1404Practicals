"""
itemgetter demo - used for sorting lists based on a specific field
"""
from operator import itemgetter
data = [['Derek', 7], ['Carrie', 8], ['Bob', 6], ['Aaron', 9]]
print(data)
data.sort(key=itemgetter(1))
print(data)

