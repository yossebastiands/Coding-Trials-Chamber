#-------------------------IN-PLACE OPERATORS--------------------------
# In-place operators allow you to write code like 'x=x+3' more concisely, as 'x += 3'.
# The same thing is possible with other operators such as -,*,/ and % as well.
# In-Place operators can be used for any numerical operation (+,-,*,/,%,**,//)

x = 2
print("First value of x is ")
print(x)
print("Then we change the value of x with +3")
x += 3    # This means x + 3. The x was taken from previous value, which is 2.
print(x)  # Output is 5
print("Then we change the value with + 5")
x += 5    # This means x + 3 or 5 + 5, because the previous x has been changed to 5.
print(x)  # Output is 10
print('')

# These operators can be used on types other than numbers, as well, such as strings.
x = "spam"
print("First value of x is")
print(x)
x += "Egg"
print("This is the value after change")
print(x)
print('')
# Strings can't be modified mathematically with another string.
y = "a"
print("y has a value of a")
print("y is multiplied by 3")
y *= 3
print(y)
print('')

#-------------------WALRUS OPERATOR-----------------------
# Walrus Operator (:=) allows you to assign values to variables within an expression, including variables that do not exist yet.
# Let's suppose we want to take an integer from the user, assign it to a variable num and output it :

print("Put an input for variable num")
num = int(input())
print("Output of num :")
print(num)
print('')
# The walrus operator accomplishes these operations at once :
# Below is the output for using walrus operator for the variable bla
print('Give input for bla :')
print('Output for bla :')
print(bla:=int(input()))
# The walrus operator makes code more readable and can be useful in many situations.
