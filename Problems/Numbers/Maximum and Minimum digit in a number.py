def find_max_min_digit(N):
    # Convert the number to a string to access each digit
    # Step 1: Convert the number N to a string
    str_N = str(N)

    # Step 2: Initialize an empty list to store the digits
    digits = []

    # Step 3: Iterate over each character (digit) in the string
    for digit in str_N:
    # Convert the character back to an integer and append to the list
        digits.append(int(digit))

    # Find the maximum and minimum digit
    max_digit = max(digits)
    min_digit = min(digits)
    
    return max_digit, min_digit

# Example usage:
N1 = 472
N2 = 839245

max_digit1, min_digit1 = find_max_min_digit(N1)
max_digit2, min_digit2 = find_max_min_digit(N2)

print(f"Input: {N1} -> Max Digit: {max_digit1}, Min Digit: {min_digit1}")
print(f"Input: {N2} -> Max Digit: {max_digit2}, Min Digit: {min_digit2}")
