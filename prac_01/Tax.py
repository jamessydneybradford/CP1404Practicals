'''
Tax
'''

gross_pay = float(input("Gross pay $:"))
tax_rate = float(input("Tax rate (i.e. 0.3 is 30%):"))
tax_amount = gross_pay * tax_rate
net_pay = gross_pay - tax_amount
print(f"The Net pay is $ {net_pay:.2f}")
