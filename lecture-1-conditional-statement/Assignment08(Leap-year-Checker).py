"""
Problem:
Take a year as input and check:
    ● If it is divisible by 400 → Leap Year
    ● Else if divisible by 4 but not by 100 → Leap Year
    ● Otherwise → Not a Leap Year
"""
print("welcome to leap year checker:")

input_year = int(input("what is the year you want to check:"))

if input_year//400 == 0:
    print("your input year is a leap year")
elif input_year//4 == 0 and input_year//100 !=0:
    print("Your input year is a leap year")
else:
    print("your input year is not a leap year")