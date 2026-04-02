
# Python variables

# Variables are containers for storing data values.

number = 5
name = "Yos"
print(number)
print(name)

# -------------------------------------- 
# Casting

p = str(3) # p will be '3'
q = int(3) # q will be 3
r = float(3) # r will be 3.0

print(type(p))
print(type(q))
print(type(r))

# ---------------------------------------
# Multi Words Variable Names
# Camel Case
theRedCar = "Toyota"
# Pascal Case
TheRedCar = "Toyota"
# Snake Case
the_red_car = "Toyota"

# ---------------------------------------
# Many values to multiple variables

x, y, z = "Orange","Banana","Cherry"
print(x)
print(y)
print(z)

# Unpack a collection
fruits = ["apple","banana","cherry"]
a,b,c = fruits
print(a)
print(b)
print(c)

# You can seperate outputs in print with comma
print(a, b, c)

# Can also use + operator
print(a+b+c)
# For numbers, the + operator works as a mathematical operator
# When using + on a string with number --> error
# When combining string wtih number --> use comma

