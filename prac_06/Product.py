class Thing:
    def __int__(self, name="", price=0.0, is_on_sale=False):
        self.name = name
        self.price = price
        self.is_on_sale = is_on_sale

    def __str__(self):
        return f"{self.name}, ${self.price} ({self.is_on_sale})"


p = Thing("Phone", 340, False)
print(p)
