# Add List Items

# Add item to the end of the list with append()
List1 = ["aa","bb","cc","dd","ee","ff","gg"]
List1.append("hh")
print("List1")

# Insert item
List1.insert(1, "ZZ") # Add "ZZ" as index 1
print("List1")

# Extend List
List2 = ["abc","def","ghi"]
List1.extend(List2) # Add elements from List2 to List1
print(List1)
print(List2)

# Add any iterable
Tuple1 = ("kiwi","apple")
List2.extend(Tuple1)
print(List2)
