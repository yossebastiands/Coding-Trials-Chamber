# Python Tuples

# Tuple
# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values.

# Tuples allow duplicate values:
thistuple2 = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple2)

# Tuple Length
# To determine how many items a tuple has, use the len() function:
print(len(thistuple2))

# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

thistuple3 = ("apple",)
print(type(thistuple3))

#NOT a tuple
thistuple4 = ("apple")
print(type(thistuple4))

# Tuple Items - Data Types
# Tuple items can be of any data type:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)


# A tuple can contain different data types:
tuple4 = ("abc", 34, True, 40, "male")

# From Python's perspective, tuples are defined as objects with the data type 'tuple'

# It is also possible to use the tuple() constructor to make a tuple.
newtuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(newtuple)