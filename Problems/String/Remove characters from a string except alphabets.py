# Function to remove all characters except alphabets from a string
def remove_non_alphabets(s):
    result = ""
    
    for char in s:
        if char.isalpha():  # Check if the character is an alphabet
            result += char
    
    return result

# Input string
s = input("Enter a string: ")

# Output the string after removing non-alphabet characters
print(f"String after removing non-alphabet characters: {remove_non_alphabets(s)}")
