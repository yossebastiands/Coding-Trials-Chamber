# Global variables

# Variables that are created outside of a function are known as global variables.) Global variables can be used by everyone, both inside of functions and outside.

x = "wow"

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the python.
# The global variable with the same name wil remain as it was, global and with the original value.

def func():
    x = "awesome"
    print("You are " + x)

func()

print("Very " + x)

# Global keyword

# To create a global variable inside a function, you can use the global keyword

y = "cool"

def func2():
    global y
    y = "yuhuuu"   # This will replace the previous y outside the function

func2()

print("This is " + y)