"""
Problem :
Write a program that takes the current temperature as input and prints:
    ● "It's too cold!" if below 10°C
    ● "It's cool outside" if between 10°C and 25°C
    ● "It's hot outside!" if above 25°C
"""
print("Welcome to Temperature Checker")

cold = 10
hot = 25

present_temperature = float(input("what is the temperature now :"))

if present_temperature < cold :
    print("It's too cold")
elif present_temperature > hot:
    print("It's hot outside")
else:
    print("It's cool outside")
