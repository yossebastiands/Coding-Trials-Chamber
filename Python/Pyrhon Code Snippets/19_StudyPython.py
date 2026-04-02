# Python - Sort Lists

# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

# Sort the list alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort the list numerically:
thislist2 = [100, 50, 65, 82, 23]
thislist2.sort()
print(thislist2)

# Sort Descending
# To sort descending, use the keyword argument reverse = True:
# Sort the list descending:
thislist3 = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist3.sort(reverse = True)
print(thislist3)

# Sort the list descending:
thislist4 = [100, 50, 65, 82, 23]
thislist4.sort(reverse = True)
print(thislist4)

# Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.
# The function will return a number that will be used to sort the list (the lowest number first):
# Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)

thislist5 = [100, 50, 65, 82, 23]
thislist5.sort(key = myfunc)
print(thislist5)

# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
# Case sensitive sorting can give an unexpected result:
thislist6 = ["banana", "Orange", "Kiwi", "cherry"]
thislist6.sort()
print(thislist6)

# Luckily we can use built-in functions as key functions when sorting a list.
# So if you want a case-insensitive sort function, use str.lower as a key function:
# Perform a case-insensitive sort of the list:
thislist7 = ["banana", "Orange", "Kiwi", "cherry"]
thislist7.sort(key = str.lower)
print(thislist7)

# Reverse Order
# What if you want to reverse the order of a list, regardless of the alphabet?
# The reverse() method reverses the current sorting order of the elements.
# Reverse the order of the list items:
thislist8 = ["banana", "Orange", "Kiwi", "cherry"]
thislist8.reverse()
print(thislist8)