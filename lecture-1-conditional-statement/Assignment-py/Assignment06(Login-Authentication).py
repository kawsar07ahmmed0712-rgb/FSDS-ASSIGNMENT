"""
Problem:
Take a username and password input.
    ● If username == "admin" and password == "12345" → print "Login Successful"
    ● Else → print "Invalid Credentials"
"""
print("welcome to login authentication")

admin_username = "Kawsar Ahmmed"
admin_password = 12345

username = str(input("Enter Your Username:"))
password = int(input("Enter your password"))

if username == admin_username  and password ==  admin_password:
    print("Login successfull")
elif username == admin_username and password != admin_password:
    print("invalid password")
elif username != admin_username and password == admin_password:
    print("invalid username")
else:
    print("Invalid Credentials")
