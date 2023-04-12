"""
programming_language.py
estimated time 30 minutes
actual time
"""


class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection=False, year=""):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} typing, reflection={self.reflection}, first appeared in {self.year}"

    # Python, Dynamic Typing, Reflection=True, First appeared in 1991

    def is_dynamic(self):
        if self.typing == 'Dynamic':
            return True
