def max_occurrence_char(s: str) -> str:
    # Dictionary to store the frequency of each character
    frequency = {}
    
    # Count the frequency of each character
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    # Find the character with the maximum frequency
    max_char = ''
    max_count = 0
    for char, count in frequency.items():
        if count > max_count:
            max_char = char
            max_count = count
    
    return max_char

# Test cases
str1 = "takeuforward"
str2 = "apple"

print("Input:", str1)
print("Output:", max_occurrence_char(str1))  # Output: 'a' or 'r'

print("Input:", str2)
print("Output:", max_occurrence_char(str2))  # Output: 'p'
