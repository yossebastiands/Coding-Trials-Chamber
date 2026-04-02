#On this file, we start with Booleans & Comparisons.
# ------------------------BOOLEANS---------------------------
# Another type in Python is the Boolean type. There are two Boolean values : True and False
# They can be created by comparing values, for instance by using the equal operator ==.
# Example :
my_boolean = True
print(my_boolean)           # Output : True
print(2==3)                 # Output : False
print("hello"=="hello")     # Output : True
# Be careful not to confuse assignment (one equals sign) with comparison (two equals signs).
# Two Boolean values are True and False.
print('')
# -----------------------COMPARISON--------------------------
# Another comparison operator, the not equal operator (!=), evaluates to True if the items being compared aren't equal, and False if they are. 
# Example :
print(1 != 1)               # Output : False
print("eleven" != "seven")  # Output : True
print(2 != 10)              # Output : True
# Comparison operators are also called Relational operators.
# Python also has operators that determine whether one number (float or integer) is greater than or smaller than another.
# These operators are > and < respectively.
print('')
# Example :
print(7 > 5)                # Output : True
print(10 < 10)              # Output : False
# Different numeric types can also be compared, for example, integer and float.
print('')
# The greater than or equal to, and smaller than or equal to operators are >= and <=.
# They are the same as the strict greater than and smaller than operators, except that they return True when comparing equal numbers.
# Example : 
print(7 <= 8)               # Output : True
print(9 >= 9.0)             # Output : True
# Greater than and smaller than operators can also be used to compare strings lexicographically.
# Lexicographically = (the alphabetical order of words is based on the alphabetical order of their component letters).
# Example :
print("Annie" > "Andy")     # Output : True
# The first two characters from "Annie" and "Andy" (A and A) are compared. 
# As they are equal, the second two characters are compared.
# Because they are also equal, the third two characters (n and d) are compared.
# And because n has greater alphabetical order value than d, "Annie" is greater than "Andy".

# This file is short because next file is about if statements.
