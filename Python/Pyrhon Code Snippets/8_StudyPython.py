# Pything strings part 2

# Slicing Strings
# Return a range of characters by using the slice syntax.
# Specify the start index and the end index, seperated by a colon, to return a part of the string.

b = "Hallo World"
print(b[2:5])   # Get the characters from position 2 to pos 5 (not included)
# First character starts with 0

# Slice from the start
print(b[:5])

# Slice to the end
print(b[2:])

# Negative indexing
# Indexing from behind
print(b[-5:-2]) # Pos -2 is not included
# -5 is the fifth character from behind "W"
# -2 is the second character from behind "l"

# Modify Strings

# Upper case
a = "JanGkaRiya"
print(a.upper())
# Lower case
print(a.lower())

# Remove whitespace
# Whitespace is the space before and/or after the actual text, and very often you want to remove it.
c = "   Aloha Kambe!   "
print(c.strip())
# Replace String
print(a.replace("a","Z"))

# Split string
d = "Good, Morning, My, Friend"
print(d.split(","))
