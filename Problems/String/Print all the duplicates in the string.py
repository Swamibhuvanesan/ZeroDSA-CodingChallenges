def print_duplicate_characters(s):
    # Create a dictionary to store character counts
    frequency = {}
    
    # Iterate through each character in the input string
    for char in s:
        # Increment the count of the character in the dictionary
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    # Print the characters that occur more than once
    for char, count in frequency.items():
        if count > 1:
            print(f"{char} - {count}")

# Example 1
s = "sinstriiintng"
print_duplicate_characters(s)

# Example 2
s = "abcdefg"
print_duplicate_characters(s)
