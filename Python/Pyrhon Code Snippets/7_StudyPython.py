# Python Strings

print("AwAW")
print('WOWWW')

a = "Hey"
print(a)

b = '''Multiline strings are kinda awesome
I am not even sure what to say'''

print(b)

# Strings are arrays

c = "Hello, World"
print(c[1]) # Getting the character in position 1 of c. First character starts with number 0

# Looping through a string
for x in "Banana":
    print(x)

# String length
# len() function
print(len(c))

# Check String
# To check if a certain phrase or character is present in a string, use in

txt = "The best thing about you is magic!"
print("magic" in txt)

if "magic" in txt:
    print("You are magic!")
if "awful" not in txt:
    print("You are not awful!")