def sum_of_numbers_in_string(s: str) -> int:
    # Initialize sum to 0
    total_sum = 0
    current_number = ''
    
    # Iterate over each character in the string
    for char in s:
        # If the character is a digit, add it to the current number
        if char.isdigit():
            current_number += char
        else:
            # If a non-digit is encountered, add the current number (if any) to the total sum
            if current_number:
                total_sum += int(current_number)
                current_number = ''
    
    # Add the last number (if any) after the loop ends
    if current_number:
        total_sum += int(current_number)
    
    return total_sum

# Test cases
s1 = "abc123xyz"
s2 = "5abc10de15"

print("Input:", s1)
print("Sum of numbers:", sum_of_numbers_in_string(s1))  # Output: 123
print("Input:", s2)
print("Sum of numbers:", sum_of_numbers_in_string(s2))  # Output: 30
