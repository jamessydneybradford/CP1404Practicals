"""
Word occurrences
word_occurrences.py
Estimated time 20 mins
Actual time 30 mins
"""

text = input("Enter the words please : ").strip()
while text != "":
    words = text.split(' ')
    words.sort()
    word_to_occurrences = {}  # Empty dictionary

    # Work out the biggest word
    max_word_length = -1
    for word in words:
        if len(word) > max_word_length:
            max_word_length = len(word)
    # Add the number of occurrences of each word to the dictionary
    for word in words:
        word_to_occurrences[word] = words.count(word)
    # print the number of occurrences of each word neatly
    for word, occurrences in word_to_occurrences.items():
        print(f"{word:{max_word_length}} : {occurrences}")
    text = input("Enter the words please : ").strip()

