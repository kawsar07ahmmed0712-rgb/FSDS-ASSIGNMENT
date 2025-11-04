"""
Problem:
Ask the user for their account balance and the amount they want to withdraw.
    ● If the withdrawal amount is greater than the balance → print "Insufficient
    Balance"
    ● If the withdrawal amount is less than or equal to balance → print "Transaction
    Successful" and show the remaining balance.
"""

print("Welcome to ATM Withdrawal system")

Account_balance = float(input("Tell us your accout balance:"))
Withdraw_amount = float(input("How much money you want to withdraw:"))


if Withdraw_amount <= 0:
    print("Sorry, please enter a positive amount")
elif Withdraw_amount <= Account_balance:
    print("Transaction Successful")
else:
    print("Insufficient balance")