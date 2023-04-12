class Plant:
    def __init__(self, name="", height=0, growth_rate=1.0):
        self.name = name
        self.height = height
        self.growth_rate = growth_rate

    def __str__(self):
        return f"{self.name} {self.height} {self.growth_rate} __str__ used"

    def __repr__(self):
        return f"{self.name} {self.height} {self.growth_rate} __repr__ used"

    def feed(self, water):
        self.height += water * self.growth_rate


p1 = Plant('Siri', 10, 2.0)

print(p1)
# print will use the __str__
p1.feed(10)  # call the feed method/function
print(p1)  # using the __str__

# To use the __repr__ for printing a list of objects
plants = [p1]  # A list of plants populated with first plant object
p2 = Plant('Jimena', 20, 3.0)  # Second plant object
plants.append(p2)  # Append second plant object
print(plants)  # uses the __repr__


