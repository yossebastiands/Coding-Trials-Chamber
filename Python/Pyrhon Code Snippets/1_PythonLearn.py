#This is first test program in purpose of excersize.
#If you see this green writings with hashtag(#) in the beginning, it means this is just a comment and it does nothing to the programm.

#First we learn about "print" command. Line 4 will show "Hello World" in the output.
print("Hello World")
print("Python is fun")
#Actually print() is a function.

#Now let's solve a problem below.
#Today is a holiday at the children's camp, so all the children will be served ice cream.
#There are 68 children in the group, and each child should get 2 scoops of ice cream.
#Write a program to calculate and output the total number of ice cream scoops we need.
#You can use the multiplication operator * inside the print() function.
print("A child needs 2 scoops of ice cream")
print("This is how many scoops neeeded for 68 children")
print(68*2)
#The output would be 136

#Now we try mathematic operations.
print("Result of 2+2 is")
print(2+2)
print("Result of 5+4-3 is")
print(5+4-3)

#Plus (+) is for Addition
#Minus (-) is for Subtraction
#Asterisk (*) is for multiplication
#Forward Slash (/) is for Division
print("The result of 2*(3+4) is")
print(2*(3+4))
print("The result of 10/2 is")
print(10/2)
#Pay attention that on line 31, the result is 5.0

#That makes it a decimal number, in programming, it is called as float.
#Floats are used in Python to represent numbers that aren't integers (whole numbers).
print("Result of 3/4")
print(3/4)
print("Print a float")
print(0.42)
# Dividing any two integers produces a float.
# A float is also produced by running an operation on two floats, or on a float and an integer.
print("Result of 2 + 4.0 is")
print(2+4.0)

#Now we start with Exponentiation.
#Exponentiation, which is the raising of one number to the power of another. This operation is performed using two asterisks(**)
print("Result of 2^5 is")
print(2**5)
#What happens when you have multiple powers?
print("Result of 2^(2^2) is ")
print(2**2**2)
print("Result of 2^(3^3)")
print(2**3**3)
#Mathematically, the programm must first define the power first before apply it to our main number.
print("Result of 9**(1/2) is")
print(9**(1/2))
#The result will be in float.

#Now let's solve a problem with Exponentiation
#You are offered a choice of either $1.000.000 or $0.01 (one penny) doubled every day for 30 days (the resulting amount is doubled every day).
#Write a program to calculate the amount that will result from the doubling to understand which choice results in a larger amount.
#For example, if we want to calculate how much money we will have on the 5th day, we can use this expression: 0.01*(2**5) = 0.32 dollars (multiply the penny by 2 raised to the power of 5).
print("The amount of money you will have in 30 days by getting 0.01 USD on the first day and doubled every day for 30 days is")
print(0.01*(2**30))

#Now we start with Quotient and Reminder.
#Floor division is done using two forward slashes and is used to determine the quotient of a division (the quantity produced by the division of two numbers).
print("Quotient of 20/6 is")
print(20//6)
#Quotient is the amount of times that the Divisor can divide the Divident. 20 can be divided by 6 until 3 times with 2 remaining.
#The modulo operator is carried out with a percent symbol (%) and is used to get the remainder of a division.
print("The remainder of 20/6 is")
print(20%6)
#Now what happens when you combine them two?
print("Result of (7%(5//2)) is")
print(7%(5//2))
print("Result of (12//(5%3)) is")
print(12//(5%3))

print("This is the end of program. This should show you on using basic maths in Python.")
