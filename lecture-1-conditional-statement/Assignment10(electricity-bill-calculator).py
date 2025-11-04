"""
Problem:
Input number of units consumed and calculate bill:
    ● Up to 100 units → 5 BDT per unit
    ● 101–200 units → 7 BDT per unit
    ● Above 200 units → 10 BDT per unit
Print total payable amount.
"""

electricity_unit = int(input("Your electricity unit in this month:"))

if electricity_unit <= 100 and electricity_unit >= 1 :
    print(f"Your electricity bill is {electricity_unit*5}")
elif electricity_unit > 100 and electricity_unit <= 200:
    print(f"Your electricity bill is {electricity_unit*7}")
elif electricity_unit > 200 :
    print(f"your electicity bill is {electricity_unit*10}")
else:
    print("sorry please input a positive number")