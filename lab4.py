"""
Ryan
SDEV 300
Lab 4


This python program will prompt the user to either to enter the program or exit. It will use numpy
and pandas for matrices and formatting. The User will have to input phone number and zip code for
validation before contiunuing to the matrices. After the numpy matrix the user
will be directed to the """

#import necessary extensions
#
import re
import sys
import numpy as np
import pandas as pd
#
def phonenumber():
    """This method will get phone number from user and validate their input using a while not
    loop instead of a while true to catch value errors. It will then use regular expressions
    to find the inputted pattern of 3 decimal digits a dash 3 decimal digits dash and
    4 decimal difits. It will then exit validation"""
    #Prompts user for input
    phone_number = input("\n\tPlease enter your phone number in format (XXX-XXX-XXXX):\n\n\t")
    #Runs a while not loops to keep prompting user for valid selection
    while not re.match(r'^\d{3}\-\d{3}\-\d{4}$', phone_number):
        #If number is not properly formatted will keep prompting the user for number.
        phone_number = input("\n\tInvalid phone number, please use format (XXX-XXX-XXXX):\n\n\t")
#
def zipcode():
    """This method will get the zip code from user and validate their input using a while not
    loop instead of a while true to catch value errors. It will then use regular expressions
    to find the inputted pattern of 5 decimal digits a dash and 4 decimal digits.
    It will then exit validation"""
    #Prompts user for input
    zip_code = input("\n\tPlease enter your zip code +4 in format (XXXXX-XXXX):\n\n\t")
    #Runs a while not loops to keep prompting user for valid selection
    while not re.match(r'^\d{5}\-\d{4}$', zip_code):
        #If number is not properly formatted will keep prompting the user for number.
        zip_code = input("\n\tInvalid zip code +4, please use format (XXXXX-XXXX):\n\n\t")
#
def matrix():
    """This method will use numpy to take the users input and create matrices
    Secondly the user will be able to choose whether to add, subtract,
    multiply, or element by element multiplication"""
    #Prompts user for input of 1st matrix
    while True:
        try:#creates a loop to catch value errors for matrix 1
            print("\n\tEnter your 1st 3x3 matrix by entering", end="")
            #prompts user for input, splits by space character and sends to list
            input1 = list (map(int,input(" 9 #'s with spaces in between:\n\n\t").split()))
            #Creates error for list not being 9 characters and prints message
            if len(input1) <9 or len(input1) > 9:
                print("\nInvalid input, use 9#'s in format X X X X etc., please try again:")
            #Breaks the while true loop and prints 1st array
            else:
                matrix1 = np.array(input1).reshape(3,3)
                print("\n\tYour 1st 3x3 matrix is:")
                print("\n",str(matrix1).replace('[[','\t').replace(']','').replace('[','\t'))
                break
        #Will catch if user does not enter integer number
        except ValueError:
            print("\nInput must be integers, please try again.")
    while True:
        try:#creates a loop to catch value errors for matrix 2
            print("\n\tEnter your 2nd 3x3 matrix by entering", end="")
            #prompts user for input, splits by space character and sends to list
            input2 = list (map(int,input(" 9 #'s with spaces in between:\n\n\t").split()))
            #Creates error for list not being 9 characters and displays message
            if len(input2) <9 or len(input2) > 9:
                print("\nInvalid input, use 9#'s in format X X X X etc., please try again:")
            #Breaks the while true loop and prints 2nd array
            else:
                matrix2 = np.array(input2).reshape(3,3)
                print("\n\tYour 2nd 3x3 matrix is:")
                print("\n",str(matrix2).replace('[[','\t').replace(']','').replace('[','\t'))
                break
        #Will catch if user does not enter integer number
        except ValueError:
            print("\nInput must be integers, please try again.")
    #Creates the menu to choose from
    print("\n\tSelect a Matrix Operation from the list below:\n\n\ta. Addition")
    print("\tb. Subtraction\n\tc. Matrix Multiplication")
    print("\td. Element by element multiplication")
    while True:
        try:
            #prompts user for their input to select from menu
            selection = input("\n\tPlease choose a, b, c, or d\n\n\t")
            #Creates if statements for selections
            if selection.lower() == 'a':#input is a will run addition
                #outputs what they selected
                print("\n\tYou selected Addition. The results are:\n")
                #uses numpy built in add feature
                total = np.add(matrix1, matrix2)
                #Will output the matrix stripping the array brackets and spacing it properly
                print(str(total).replace('[[','\t').replace(']','').replace('[','\t'))
                break
#
            elif selection.lower() == 'b':#input is a will run Subtraction
                #outputs what they selected
                print("\n\tYou selected Subtraction. The results are:\n")
                #uses numpy built in subtract feature
                total = np.subtract(matrix1, matrix2)
                #Will output the matrix stripping the array brackets and spacing it properly
                print(str(total).replace('[[','\t').replace(']','').replace('[','\t'))
                break
#
            elif selection.lower() == 'c':#input is a will run multiplication
                #outputs what they selected
                print("\n\tYou selected Multiplication. The results are:\n")
                #uses numpy built in multiply feature
                total = np.matmul(matrix1, matrix2)
                #Will output the matrix stripping the array brackets and spacing it properly
                print(str(total).replace('[[','\t').replace(']','').replace('[','\t'))
                break
#
            elif selection.lower() == 'd':#input is a will run elemeent multiplication
                #outputs what they selected
                print("\n\tYou selected Element by Elemenet Multiplication. The results are:\n")
                #uses numpy built in add feature
                total = np.multiply(matrix1, matrix2)
                #Will output the matrix stripping the array brackets and spacing it properly
                print(str(total).replace('[[','\t').replace(']','').replace('[','\t'))
                break
#
            else:#If user inputs anything other than a, b, c, d will output message and go back
                print("\n\nInvalid selection please try again")
        #Catches format errors
        except ValueError:
            print("\n\tInvalid input please try again:")
    transpose = np.transpose(total)#Uses built in transpose method
    print("\n\tYour Transpose is:\n")
    #prints transpose and indents it to match formatting
    print(str(transpose).replace('[[','\t').replace(']','').replace('[','\t'))
    #creates the pandas datframe to extract the means from
    meandata = pd.DataFrame(total)
    #extracts means from the columns, rounds it to 2 decimals, and converts it to string no index
    meanc = meandata.mean(0).round(2).to_string(index=False)
    #extracts means from the rows, rounds it to 2 decimals, and converts it to string with no index
    meanr = meandata.mean(axis = 1).round(2).to_string(index=False)
#
    print("\n\tYour row and column mean values of the results are:")
    print('\n\tRow:', end=' ')
    print(meanr.replace('\n', ', '))
    print('\n\tColumn:', end=' ')
    print(meanc.replace('\n',', '))
#
#
def menu():
    """Will display a simple yes or no menu"""
    print("\n******* Do you want to play the Matrix Game? *******")#opening message
    #prompts user for Y or N
    mensel = input("\n\tPlease make a selection Y for yes or N for no:\n\n\t")
    if mensel.lower() == 'y':
        phonenumber()#runs phonenumber
        zipcode()#runs zip code
        matrix()#runs matrix
        menu()#re-runs menu
    elif mensel.lower() == 'n':#runs for no
        print("*******Thanks for playing Python Numpy *******")
        sys.exit()#exits program
    else:
        print("\n\tPlease make a valid selection!")
        menu()# will reenter the menu selection
menu()
#(EOF)
