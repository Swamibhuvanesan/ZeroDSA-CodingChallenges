# Function to remove vowels from a string
def remove_vowels(s):
    vowels = "aeiouAEIOU"
    result = ""
    
    for char in s:
        if char not in vowels:
            result += char
    
    return result

# Input string
s = input("Enter a string: ")

# Output the string after removing vowels
print(f"String after removing vowels: {remove_vowels(s)}")
