text = """
CP1404
CP1504
CP1223
CP1404"""
print("The text")
print(text.split())
print("The text in a set (notice NO DUPLICATES")
print(set(text.split()))
print("The text comma-separated")
print(",".join(set(text.split())))

things = set()  # empty set
things.add(3)
things.add('Jimmy')
things.add(True)
things.add(True)  # no duplicates

print(things)
# Convert to a list
items = list(things)
items.append(3)
items.append(3)
items.append(3)  # Duplicates allowed

print(items)

# convert back to set
test_set = set(items)
print(test_set)  # No duplicates
