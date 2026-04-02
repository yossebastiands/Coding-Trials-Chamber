# Access Items in List
# Access Items
List1 = ["aa","bb","cc"]
print(List1[1]) # First item index 0

# Negative indexing --> start from the end
# -1 --> last item
# -2 --> second last item

print(List1[-1])

# Range of indexes
# Can specify where to start where to end.
List2 = ["aa","bb","cc","dd","ee","ff","gg"]
print(List2[2:5]) # Returns the third, fourth and fifth
# Starts at 2 (not included) ends at 5 (included)

print(List2[:4]) # From index 0 to index 4 (not included)
print(List2[2:]) # From index 2 to end index (included)

# Range of negative indexes
# Start the search from the end
print(List2[-4:-1]) # From the fourth item from the end --to the---> 1st item from the end

# Check if item exist
if "bb" in List2:
    print("Yes bb in the list")
