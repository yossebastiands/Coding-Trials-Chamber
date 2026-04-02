# Python Loop Lists

# Loop through a list
List1 = ["aa", "bb","cc","dd","ee","ff"]
print('')

for x in List1:
    print(x)
print('')

# Loop through the index numbers
for i in range(len(List1)):
    print(List1[i])
print('')

# Using a while loop
i = 0
while i < len(List1):
    print(List1[i])
    i = i + 1
print('')
# Loop using List Comprehension
[print(x) for x in List1]

