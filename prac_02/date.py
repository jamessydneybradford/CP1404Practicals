"""
using * To unpack tuple - also uses function annotation
print(format_date(*date)) - notice the star *
format_date(day:int, month:int, year:int) -> str:/ Function will accept three integers and return a string
"""

def format_date(day:int, month:int, year:int) -> str:
    return f"{day}/{month}/{year}"


date = (2, 11, 1965)

print(format_date(*date))  # * Unpacks the tuple
