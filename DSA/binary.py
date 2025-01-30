string = "hello"
char = list(string)  # Convert string to list of characters
a = 0
b = len(char) - 1
print(char)
# Swap characters until pointers meet
while a < b:
    char[a], char[b] = char[b], char[a]  # Correct swap
    a += 1
    b -= 1

# Convert the list back to a string
string1 = ''.join(char)
print(string1)
