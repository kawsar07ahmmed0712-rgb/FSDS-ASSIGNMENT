"""
Problem:
Take total bill amount from the user:
    ● If the bill is above 1000 → apply 10% discount
    ● Otherwise → no discount
    Then print the final bill amount.
"""

print("welcome to our resturant")

bill = float(input("Tell us your bill:"))
discount_bill = bill - (bill/100 * 10)

if bill > 1000:
    print(f"you will take apply you need to pay {discount_bill}")
else:
    print(f"Your final bill amout is {bill}")