# Change List Items

List1 = ["aa","bb","cc","dd","ee","ff","gg"]
List1[1] = "zz"
print(List1)

# Change a range of item values
List1[1:3] = ["Abakadabra","Wow"] # Change value of the index 1 and index 2 --> into new value
print(List1)

List1[1:3] = ["New1","New2","New3"]
print(List1)

List1[1:3] = ["Newest"]
print(List1)

# Insert items
List1.insert(4, "Orange") # Insert it as index 4
print(List1)

