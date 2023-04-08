"""
Words list comprehension
"""

text = "The cat sat on the mat and was extremely happy that the dog was not home"

words = text.split(" ")

print(words)

long_words = [word for word in words if len(word) > 3]
print(long_words)

print("List of long words:")
for long_word in long_words:
    print(long_word)
