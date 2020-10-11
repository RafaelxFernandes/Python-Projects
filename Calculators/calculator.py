#Importing regex library
import re

#Simple user interface
print("Welcome to my simple calculator!")
print("Type 'exit' whenever you want to stop.\n")

#Previous value in screen
previous = 0

#Boolean value to check if calculator will keep or not running
run_boolean = True


def calculate():

    #Must define as global to keep working
    global run_boolean
    global previous

    #Initial equation
    equation = ""

    #Start code
    if(previous == 0):
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))
    
    #Stop code
    if(equation == 'exit'):
        print("Bye!")
        run_boolean = False

    #Continue
    else:
        #Removing possible non-numeric characters
        equation = re.sub('[a-zA-Z]', '', equation)

        if(previous == 0):
            #'eval' Transform what the user writes in true math equation
            previous = eval(equation)

        else:
            #Use previous value in the next equation
            previous = eval(str(previous) + equation)

        print("You typed: ", previous)

while(run_boolean):
    calculate()

'''
Problems detected
 * You can't write 'exit' alone. If the final result is '55',
   in the console must appear '55exit' to stop the code. '55 exit' won't work.
 * You can type letters, although they'll be ignored. 
   It would be better if the whole thing was cancelled and the user had to type properly. 
   Current output example:
   Enter equation: Hi 2 + World 3
   You typed:  5
 * This calculator is based on the thought that the user wants/ needs the previous result,
   just like a cientific one works. Multiple simple calculations are hard to make here
   because you'll need to type 'exit' several times.
 * Whenever the result you get is '0', the calculator resets.