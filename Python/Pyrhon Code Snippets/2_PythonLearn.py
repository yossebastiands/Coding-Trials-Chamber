#This is the second file into PythonLearn
#---------------STRING------------------
#If you want to use test in Python, you have to use string.
#A string is created by entering text between two single or double quotation marks.

print('')
print("Python is amazing!")
print('You are the universe experiencing itself')
print('')

#The delimiter (" or ') used for a string doesn't affect how it behaves in any way.

#Some characters can't be directly included in a string. For instance, double quotes can't be directly included in a double string; this would cause it to end prematurely.
#Characters like these must be escaped by placing a backslash before them.
#Double quotes only need to be escaped in double quote strings, and the same is true for single quote strings.
#Example:
print("Below is example for using backslash")
print("Dan\'s mother says, \"He is not a good boy!\"")
print('')
#Backslashes can also be used to escape tabs, arbitrary Unicode characters, and various other things that can't be reliably printed.

#----------------------NEWLINES-------------------------------
#Type "\n" to create a new line. It can be used in strings to create multi-line output:
print("Below is example for using \"Backslash + n\" ")
print('One\nTwo\nThree')
print('')
#Similarly, \t represents a tab
print("Below is example for using \"Backslash + t\" ")
print('One\tTwo\tThree')
print('')

#Newlines will be automatically added for strings that are created using three quotes.
#Example :
print("""This
is a
multiline
text""")
print()

#-------------------------STRING OPERATIONS---------------------------
#Concatenation.
#As with integers and floats, strings in Python can be added, using a process called CONCATENATION
#which can be done on any two strings.
print("Spam" + 'Eggs')
#Even if your strings contain numbers, they are still added as strings rather than integers.
print("2"+"2")
#Adding a string to a number prodcues an error, as even though they might look similar, they are two different entities.

#String Operations
#Strings can also be multiplied by integers. This produces a repeated version of the original string. The order and the integer doesn't matter, but the string usually comes first.
print('')
print("Result of multiplying strings :")
print("Spam"*3)
print(4*'2')
print('')

#Next file is about Variable, so it will be seperated into other python file.
