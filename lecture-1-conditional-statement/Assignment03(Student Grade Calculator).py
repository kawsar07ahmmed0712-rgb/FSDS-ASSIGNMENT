"""
Problem:
Input marks (0-100) and print grade based on:
    ● 90-100 → A+
    ● 80-89 → A
    ● 70-79 → B
    ● 60-69 → C
    ● Below 60 → Fail
"""
print("Welcome to Student Grade Calculator")

mark = float(input("Enter mark (0-100): "))

if mark < 0 or mark > 100:
    print("Invalid mark")
elif mark >= 90:
    print("You got A+")
elif mark >= 80:
    print("You got A")
elif mark >= 70:
    print("You got B")
elif mark >= 60:
    print("You got C")
else:
    print("You failed")