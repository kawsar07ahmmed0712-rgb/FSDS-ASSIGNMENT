"""
Problem:
    Ask the user for age and print ticket price:
    ● Below 5 → Free
    ● 5-18 → 50% Discount
    ● 60 or above → 30% Discount
    ● Others → Full Price
"""

print("Welcome to bus ticket center")

age = int(input("How old are you:"))


if age < 5:
    print("Your age is too low , you cant buy.")
elif age >= 5 and age <= 5 :
    print("You will get 50% discount")
elif age >= 60:
    print("You will get 30% discount")
else:
    print("You will pay full amoutnt")