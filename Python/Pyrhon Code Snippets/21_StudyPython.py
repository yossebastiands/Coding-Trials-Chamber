# Python - Join List
# Join Two Lists
# There are several ways to join, or concatenate, two or more lists in Python.
# One of the easiest ways are by using the + operator.

# Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Another way to join two lists is by appending all the items from list2 into list1, one by one:
# Append list2 into list1:
list4 = ["a", "b" , "c"]
list5 = [1, 2, 3]

for x in list5:
  list4.append(x)

print(list4)

# Or you can use the extend() method, which purpose is to add elements from one list to another list:
# Use the extend() method to add list2 at the end of list1:
list6 = ["a", "b" , "c"]
list7 = [1, 2, 3]

list6.extend(list7)
print(list6)