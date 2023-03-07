"""
Shop Calculator
"""

total_price = 0
number_of_items = int(input("Enter the number of items: "))
while number_of_items >= 1:
    for i in range(1, number_of_items + 1):
        print("Item", i, end="")
        item_price = float(input(" - enter the price for item $: "))
        total_price = total_price + item_price
    print(f"The total price for the {number_of_items} item(s) is {total_price:.2f}")
    total_price = 0
    number_of_items = int(input("Enter the number of items: "))
print("Bye!")
