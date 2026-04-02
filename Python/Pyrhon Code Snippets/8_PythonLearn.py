# This file is about else Statements.
# --------------------------else STATEMENTS-------------------------------
# The if statements allows you to check a condition and run some statements, if the condition is True
# The else statements can be used to run some statements when the condition of the if statements is False

# As with if statements, the code inside the block should be indented.

x = 4
if x == 5:
    print("x is 5")
else:
    print("x is 4")
print('')
# Notice the colon (:) after the "else" word.

# Try to guess the output of this code below :
if 1+1 == 2:
    if 2*2 == 8:
        print("2 times 2 is 8")
    else:
        print("2 times 2 is not 8")
print('')

# Every if condition block can have only one else statement.
# In order to make multiple checks, you can chain if and else statements.
# For example, the following program checks and outputs the num variable's value as text:

num = 3
if num == 1:
    print("3 is 1")
else:
    if num == 2:
        print("3 is 2")
    else:
        if num == 3:
            print("3 is 3")
        else:
            print("3 is not 3")
print('')
# Indentation determines which if/else statements the code blocks belong to.

# --------------------- elif STATEMENTS ------------------------------
# Multiple if/else statements make the code long and not very readable.
# The elif (short for else if) statement is a shortcut to use when chaining if and else statements, making the code shorter.

# The same example from the previous part can be rewritten using elif statements:

numa = 3
if numa == 1:
    print("3 is 1")
elif numa == 2:
    print("3 is 2")
elif numa == 3:
    print("3 is 3")
else:
    print("3 is not 3")
print('')

# As you can see in the example above, 
# A series of if elif statements can have a final else block, which is called if none of the if or elif expressions is True.
# The elif statement is equivalent to an else/if statement. 
# It is used to make the code shorter, more readable, and avoid indentation increase.

# Next file is about Boolean Logic
