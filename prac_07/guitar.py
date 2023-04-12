"""
Guitar class
"""


class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{name} ({year}) : ${cost}"

    def __repr__(self):
        return f"{name} {year} {cost}"

    def get_age(self):
        return 2023 - self.year

    def is_vintage(self):
        if (2023 - self.year) > 50:
            return True
        else:
            return False

