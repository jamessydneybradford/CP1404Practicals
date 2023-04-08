"""
Membership tests
"""


# Look before you leap LBYL
word_to_count = {}
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

# Easy to ask for forgiveness than permission EAFP
word_to_count = {}
for word in words:
    try word_to_count[word] += 1
    except KeyError
        word_to_count = 1


word_to_count = {}
for word in words:
    word_to_count[word]=word.to.count.get(word,0) + 1


