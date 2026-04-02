# Python numbers

# Int, Float, Complex

x = 1   # Int
y = 2.1 # Float
z = 1j  # Complex

print(type(x))
print(type(y))
print(type(z))

# Int --> whole number, positive, negative, without decimals, of unlimited length
# Float --> number, positive, negative, containing one or more decimals
# Complex --> numbers with j as imaginary

# Float
p = 35e3
q = 12E4
r = -90.2e100
print(p)
print(q)
print(r)

# Convert numbers
a = float(x)
b = int(y)
c = complex(x)

print(a)
print(b)
print(c)
# You cannot convert complex numbers into another number type

# ---------------
# Random number

import random # This is a built in module called random that can be used to make random numbers
print(random.randrange(1,10)) # Print ONE random number between 1 to 10, but 10 is excluded.


