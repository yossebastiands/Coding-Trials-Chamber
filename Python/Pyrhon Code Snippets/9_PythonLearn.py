# This is about Boolean Logic
# ----------------------- Boolean Logic -------------------------
# Boolean logic is used to make more complicated conditions for if statements that rely on more than one condition.
# Python's Boolean operators are and, or, and not.
# The and operator takes two arguments, and evaluates as True if, and only if, both of its arguments are True. 
# Otherwise, it evaluates to False.

# True and True = True
# True and False = False
# False and False = False

print(1 == 1 and 2 == 2)    # Output : True     
print(1 == 1 and 2 == 3)    # Output : False
print(1 != 1 and 2 == 2)    # Output : False
print(2 < 1 and 3 > 6)      # Output : False

# Boolean operators can be used in expression as many times as needed.
print('')
# Try to guess the output of the code below :
if (1==1) and (2+2>3):
    print("True")
else :
    print("False")
print('')

# ---------------- BOOLEAN or----------------------
# The or operator also takes two arguments. 
# It evaluates to True if either (or both) of its arguments are True, and False if both arguments are False
# True or True = True
# True or False = True
# Falsa or False = False

print(1 == 1 or 2 == 2)     # Output : True
print(1 == 1 or 2 == 3)     # Output : True
print(1 != 1 or 2 == 2)     # Output : True
print(2 < 1 or 3 > 6)       # Output : False
print('')
# Besides values, you can also compare variables. 

# ---------------- BOOLEAN not -------------------
# Unlike other operators we've seen so far, not only takes one argument, and inverts it.
# The result of not True is False, and not False goes to True

print(not 1 == 1)   # Output : False
print(not 1 > 7)    # Output : True
# You can chain multiple conditional statements in an if statement using the Boolean operators.

# Try to guess the output of the following code :
if not True:
    print("1")
elif not(1+1==3):
    print("2")
else:
    print("3")

# The next file is a list of Python Operators from w3schools.
