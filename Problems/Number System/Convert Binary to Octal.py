def binary_to_octal(N):
    # Step 1: Convert binary string to decimal integer
    decimal_num = int(str(N), 2)
    
    # Step 2: Convert decimal integer to octal string
    octal_num = oct(decimal_num)[2:]  # Remove the '0o' prefix from the octal representation
    
    return octal_num

# Example 1
N1 = 1100110
print(f"Input: N = {N1}")
print(f"Output: {binary_to_octal(N1)}")  # Output: 146

# Example 2
N2 = 11111
print(f"Input: N = {N2}")
print(f"Output: {binary_to_octal(N2)}")  # Output: 37
