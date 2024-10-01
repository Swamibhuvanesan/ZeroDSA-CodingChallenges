def non_repeating_characters(s: str) -> str:
    # Dictionary to store the frequency of each character
    frequency = {}
    result = []
    # First loop: Count the frequency of each character
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # Second loop: Collect characters that appear only once
    for char in s:
        if frequency[char] == 1:
            result.append(char)
            
    # Return the non-repeating characters as a comma-separated string
    return ','.join(result)

# Test examples
string1 = "google"
string2 = "yahoo"

print(non_repeating_characters(string1))  # Output: "l,e"
print(non_repeating_characters(string2))  # Output: "y,a,h"
