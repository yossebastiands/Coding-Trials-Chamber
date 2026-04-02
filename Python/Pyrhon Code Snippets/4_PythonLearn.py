#This is the fourth file for PythonLearn. This is about User Input
#---------------Input-----------------
# To get input from the user in Python, you can use the intuitively named input function.
# For example, a game can ask for the user's name and age as input and use them in the game.
# The input function prompts the user for input, and returns what they enter as a string (with the contents automatically escaped.)

print("Give input for x :")
x = input()   # This lets the user to set the value for x
print(x)      # The value of x will be input here.

# Even if the user enters a number as input, it is processed as a string.

# The input statement needs to be followed by parentheses.
# You can provide a string to input() between the parentheses, producing a prompt message.
# Example
print('')
print("Give input for variable \'name\'")
name = input("Enter your name: ")
print("Hello, " + name)
print('')
# The prompt message helps to clarify what input the program is asking for.

#------------------WORKING WITH INPUT-----------------
# Let's assume we want to take the age of the user as input.
# We know that the input() function returns a string.
# To convert it to a number, we can use the int() function

print('')
print("Input the age of a male :")
userage = int(input())
print('His age is ')
print(userage)

# Similarly, in order to convert a numberto a string, the str() function is used.
# This can be useful if you need to use a number in string concatenation.
# For example :

print('')
print("A variable userage1 with value of 42")
userage1 = 42
print("His age is " + str(userage1))
# You can convert to float using the float() function
print('')
#Another example
m = "2"
n = "4"
z = int(m)+int(n)
print("The result of 4 + 2 is")
print(z)             # Output is 6
print('')

# You can use input() multiple times to take multiple user inputs.
# Example :


name = input("Your name is : ")
ageuser = input("Your age is : ")
print(name + " is " + ageuser)
print('')
# When input() function executes, program flow stops until a user enters some value.

# Next file will be about In-Place and Walrus Operators. 
