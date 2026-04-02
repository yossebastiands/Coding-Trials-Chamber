# String Concatenation
a = "Wow"
b = "Cool"
c = a + b
print(c)

# String Format
# Combine string with integer

age = 22
txt = "My name is Yos, and I am {}"
print(txt.format(age))
txt2 = "This is very {}, such a {} view"
print(txt2.format(b, a))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) 
