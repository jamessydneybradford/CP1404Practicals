"""
Wimbledon Demo
"""

in_file = open('wimbledon.txt')

lines = [line.strip() for line in in_file.readlines()]
print(lines)
winners = set(lines)
print(winners)
print(len(winners))
in_file.close()
