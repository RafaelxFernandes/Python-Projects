#Simple calculator using multiple functions
#Original source: https://www.programiz.com/python-programming/examples/calculator

#Functions
#Add two numbers
def add(n1, n2):
    return n1 + n2

#Subtract two numbers
def sub(n1, n2):
    return n1 - n2

#Multiply two numbers
def multiply(n1, n2):
    return n1 * n2

#Divide two numbers
def divide(n1, n2):
    return n1/ n2


#Simple user interface
print("Welcome to my simple calculator 2! The first one bugged...\n")
print("Please, select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("9. Stop calculator")


#Start code
while True:

    #Take input from the user
    choice = input("Enter choice (1/ 2/ 3/ 4/ 9): ")

    #Check if 'choice' is a valid option
    if(choice in (1, 2, 3, 4, 9)):

        #Stop code
        if(choice == 9):
            print("Bye!")
            break

        #Continue
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))

        #I had to convert the integers to string so I could concatenate them
        if(choice == 1):
            print("Result: " + str(n1) + " + " + str(n2) + " = " + str(add(n1, n2)) + "\n")
        elif(choice == 2):
            print("Result: " + str(n1) + " - " + str(n2) + " = " + str(sub(n1, n2)) + "\n")
        elif(choice == 3):
            print("Result: " + str(n1) + " * " + str(n2) + " = " + str(multiply(n1, n2)) + "\n")
        elif(choice == 4):
            print("Result: " + str(n1) + " / " + str(n2) + " = " + str(divide(n1, n2)) + "\n")
    
    else:
        print("Invalid input.")