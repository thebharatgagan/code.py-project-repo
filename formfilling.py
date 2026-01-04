# Make Login Page With Given Username & Password;
user_name = '@git10'
pass_word = 'git01@'

while True: # It is used for, when username and password is incorrect, then reasked to correct username and password:
    username = input("\nEnter the Username: ")
    if(user_name == username):
        print(" ")
    else:
        print("please enter correct username\n")
    password = input("Enter the Password: ")
    if(pass_word == password):
        print("\nYou are Successfully Login in Your Account\n")
        break
    else:
        print("Incorrect Password, Please Try Again Later\n")
    
# Please Fill The Details Carefully:

name = str(input("Enter the Name: "))
Age = int(input("Enter the Age: "))
Gender = input("Enter the Male/female: ")
Address = input("Enter the Corresponding Address: ")
Email = input("Enter the Email: ")
Pno = int(input("Enter The 10- Digit Mobile Number: "))


print(name)
print(Age)
print(Gender)
print(Address)
print(Pno)
print(Email)

# Finally Write your Signature, if all the ready to submit:

#Ent the Program.