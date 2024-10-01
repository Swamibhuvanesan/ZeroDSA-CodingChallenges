def sort_characters(s):
    # Initialize an empty list to store alphabetic characters
    letters_only = []
    
    # Iterate through each character in the input string
    for char in s:
        # Check if the character is an alphabetic letter
        if char.isalpha():
            # Append the alphabetic character to the list
            letters_only.append(char)
    
    # Sort the alphabetic characters
    sorted_letters = sorted(letters_only)
    
    # Join the sorted characters into a string
    sorted_str = ''.join(sorted_letters)
    
    return sorted_str

# Example 1
str1 = "zxcbg"
print(sort_characters(str1))  # Output: "bcgxz"

# Example 2
str2 = "edcba"
print(sort_characters(str2))  # Output: "abcde"
