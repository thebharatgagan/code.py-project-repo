while True:
    num1 = float(input("\nEnter the First Value: "))
    num2 = float(input("Enter the Second Value: "))
    
    print("\nwhat you want to choose ( + , - , * , / )!\n")
    operator = input("Enter the Operator: ")
    
    if(operator == "+"):
        print('Result-', num1 + num2)
    elif(operator == "-"):
        print('Result-' , num1 - num2)
    elif(operator == "*"):
        print('Result-', num1 * num2)
    elif(operator == "/"):
        if(num2 != 0):
            print('Result-', num1 / num2)
    else:
        print("Invalid Operators")
    
# End the Program.