"""
languages.py
estimated time 30 mins
actual time 38 mins
"""
from programming_language import ProgrammingLanguage
from operator import itemgetter


python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(python)
languages = [python, ruby, visual_basic]
# print(languages)

# practicing with loop
print("The dynamically typed languages are:")

for language in languages:
    if language.is_dynamic():
        print(language.name)

# practicing with a list comprehension
print("The dynamically typed languages are:")
dynamic_typed_languages = [language for language in languages if language.is_dynamic()]

for dynamic_typed_language in dynamic_typed_languages:
    print(dynamic_typed_language.name)
