def remove_characters(str1, str2):
    # Create a set of characters from the second string for efficient lookup
    chars_to_remove = set(str2)
    
    # Initialize an empty result string
    result = ""
    
    # Iterate through each character in the first string
    for char in str1:
        # Check if the character is not in the set of characters to remove
        if char not in chars_to_remove:
            # Append the character to the result if it's not in the second string
            result += char
    
    return result

# Example usage
str1 = "hello world"
str2 = "lod"
result = remove_characters(str1, str2)
print(result)  # Output: "he wr"
