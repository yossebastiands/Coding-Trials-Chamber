# This file is about if-statements.
# ----------------------- IF-STATEMENTS ------------------------
# You can use if statements to run code if a certain condition holds.
# If an expression evaluates to True, some statements are carried out.
# Otherwise, they aren't carried out.
# An if statement looks like this:
#   if <expression> :
#      <statements>
# Python uses indentation (white space at the beginning of a line) to delimit blocks of code.
# Depending on program's logic, indentation can be mandatory.
#  As you can see, the statements in the if should be indented.

# Example of if statement :
if 10>5:
    print("10 is greater than 5")

print("Program ended")  # This is not part of the if statement.
# The expression determines whether 10 is greater than 5.
# Since it is, the indented statement runs, and "10 greater than 5" is output.
# Then, the unindented statement, which is not part of the if statement, is run, and "Program ended" is displayed.
# Notice the colon at the end of the expression in the if statement.
print('')
# To perform more complex checks, if statements can be nested, one inside the other.
# This means that the inner if statement is the statement part of the outer one.
# This is one way to see whether multiple conditions are satisfied.
# Example :
num = 12        # A variable
if num > 5:
    print("Bigger than 5")
    if num <= 47:
        print("Between 5  and 47")
# Indentation is used to define the level of nesting.

# Next file will be about else statements
