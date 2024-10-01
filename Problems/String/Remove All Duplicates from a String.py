def remove_duplicates(s: str) -> str:
    # Set to store unique characters encountered in the string
    unique_chars = set()
    # List to collect the final result of unique characters
    result = []
    
    # Iterate over each character in the input string
    for char in s:
        # If the character is not already in the set, add it to the result list
        if char not in unique_chars:
            result.append(char)
            unique_chars.add(char)
    
    # Join the result list into a string and return it
    return ''.join(result)

# Test cases
string1 = "bcabc"
string2 = "cbacdcbc"

print("Input:", string1)
print("Output:", remove_duplicates(string1))  # Output: "bca"

print("Input:", string2)
print("Output:", remove_duplicates(string2))  # Output: "cbad"
