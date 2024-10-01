# Function to return the ASCII value of a character
def find_ascii_value(c):
    return ord(c) #built-in Python function that returns the ASCII value of the character

# Input character
c = input("Enter a character: ")

# Output the ASCII value
print(f"ASCII value of '{c}' is {find_ascii_value(c)}")
