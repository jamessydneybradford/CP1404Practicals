"""
Guitar class
"""


class Guitar:
    def __init__(self, name="", year=0, price=0.0):
        self.name = name
        self.year = year
        self.price = price

    def __str__(self):
        # return f"{self.name},{self.year},{self.price}"
        return '{' + self.name + ', ' + str(self.year) + ', ' + str(self.price) + '}'

    def __repr__(self):
        return '{' + self.name + ', ' + str(self.year) + ', ' + str(self.price) + '}'

    def __lt__(self, other):
        return self.year < other.year

    def __getitem__(self, item):
        return '{' + self.name + ', ' + str(self.year) + ', ' + str(self.price) + '}'
    # def get_age(self):
    #     return 2023 - self.year
    #
    # def is_vintage(self):
    #     if (2023 - self.year) > 50:
    #         return True
    #     else:
    #         return False
