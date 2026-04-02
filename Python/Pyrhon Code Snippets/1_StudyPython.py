# Python Indentation

# Indentation refers to the space at the beginning of a code line.
# Where in other programming languages the indentation in code is for readability only,
# the indentation in Python is very important

if 5 > 2:
    print("Five is greater than two")

# The number of spaces is up to you, most common use is four, but it has at least to be one.

# You have to use the same number of spaces in the same block of code, otherwise Python will give you an error.

if 5>2:
    print("Five bigger than two!")
    print("Do you have a problem?")
if 5>2:
            print("I have a problem with you!")

# -------------------------------------------------------------------------------

# print Command

# A command to display the appointed result in the output.
# Use single, double, tripple quotes to denote string literals, as long as the same type of quote starts and ends the string.

print("Hello World")
print('Hello World')
print(2+2)