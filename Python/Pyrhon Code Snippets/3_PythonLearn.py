#This is the third Python file for learning.
#-----------------VARIABLES-------------------
#Variables
# A variable allows you to store a value by assigning it to a name, which can be used to refer to the value later in the program.
# For example, in game development, you would use a variable to store the points of the player.
# To assign a variable, use one equals sign

user = "Yos"
# In given example, we assigned string "Yos" to the variable "user"
age = 22
# This "age" variable has been assigned with an integer of 22

#----------------VARIABLE NAMES---------------------
# Certain restrictions apply in regard to the characters that may be used in Python variable names.
# The only characters that are allowed are letters, numbers, and underscores.
# Also, they can't start with numbers.
# Not following these rules results in errors.

A_variable_name = 15
# If you write >>> 123abc = 7 will result in :
# SyntaxError : invalid syntax
# Python is a case sensitive programming language. Thus, Lastname and lastname are two different variable names in Python.
# Pay attention to the small or big letter of L.

#----------------WORKING WITH VARIABLES----------------
# You can use variables to perform corresponding operations, just as we did with numbers and strings :

x = 12
print(x)      # Output : 12
print(x+3)    # Output : 15
print(x*3)    # Output : 36
print(x)      # Output : 12
# Notice that the variable stores its value throughout the program.
print('')

# Now we try to multiply strings in variable
spam = "This"
print(spam*3)   # Output : ThisThisThis

# Variables can be reassigned as many times as you want, in order to change their value.
# In Python, variables don't have specific types, so you can assign a string to a variable, and later assign an integer to the same variable.
print('')
x = 928                     # It changes the value of x into 928
print(x)                    # Output : 928
x = "This is a string"      # It changes the value of x into a string.
print (x + "!")             # Output : This is a string!
print('')

#Doing mathematical operations with variables :
t = 3
q = 4
print(t+q)
print(t*q)
print('')

# The next file will be about User Input. Where you can input some strings or numbers into the program while it's running.
# Therefore, it will be seperated from this file.
