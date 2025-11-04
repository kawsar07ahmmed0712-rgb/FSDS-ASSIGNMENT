"""
Problem:
Input age and qualification.
    ● If age ≥ 18 and qualification is “graduate” → print "Eligible for Job"
    ● Else → "Not Eligible"
"""

your_age = int(input("The applicant age: "))
graduate = str(input("Is the applicant graduate (yes or no): "))

if your_age >= 18 and graduate == "yes":
    print("Eligible for Job")
elif your_age >= 18 and graduate == "no":
    print("Your are not eligible , cause you arenot graduate")
else:
    print("Not Eligigble")