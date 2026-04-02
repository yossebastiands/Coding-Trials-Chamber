# Remove List Items

# Remove specified item
List1 = ["aa","bb","cc","dd","ee","ff","gg"]
List1.remove("aa")
print(List1)

# Remove specified index
List1.pop(1)
print(List1)
List1.pop() # Removes last item
print(List1)
del List1[0] # Removes index 0
print(List1)
del List1 # Removes the list

List2 = ["aa","bb","cc","dd","ee","ff","gg"]
List2.clear # Clears the list
print(List2)
