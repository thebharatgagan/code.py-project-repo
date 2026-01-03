given_username = "bharatgit01" # User name for login
given_password = "git@#1234" # Password for login

#Now , we will create a function to validate the login credentials using take a user input.

username = input("enter your user name: ")
if(username != given_username):
    print("invalid user name")
    username = input("enter your user name: ")
    
elif(username == given_username):
    password = input("enter your password: ")

    if(password == given_password):
        print("login successful\n")
    else:
        print("Invalid password\n")

print("Disclaimer: This is a simple login validation script for demonstration purposes only. In real-world applications, never store passwords in plain text and always use secure authentication methods.\n")

print("Please Fill the Basic Details to proceed further:\n")

name = input("Enter your Full Name: ")
age = int(input("Enter your Age: "))
if(age > 18):
    print("You are eligible to vote.\n")
elif(age == 18):
    print("Please Apply for UniqueID.\n")
else:
    print("You are not eligible to vote.\n")

Gender = input("Enter Your Gender: ")
UniqueID = int(input("Enter your Unique ID: "))


#Thanks Message:

print("\nThank you so much", name,"we have received your details.")
print("\nThank you for providing your details. You are now eligible to vote!\n")

#End the program

