# Slicing (cadenas y listas)
# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])

# Slice From the Start
# By leaving out the start index, the range will start at the first character:
# Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
# Example
# Get the characters:
# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2):
b = "Hello, World!"
print(b[-5:-2])
