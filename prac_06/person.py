"""
person.py
Notice the case. This is the module person.
The Class person can be imported from another program such as person_client_code
"""


class Person:
    def __init__(self, name="", height=0.0):
        self.name = name
        self.height = height

    def __str__(self, ):
        return f"{self.name} {self.height}"

    def __repr__(self):
        return f"[{self.name}, {self.height}]"
