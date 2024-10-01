def binary_to_decimal(N):
    # Convert binary string to decimal integer
    return int(str(N), 2)

# Example 1
N1 = 1011
print(f"Input: N = {N1}")
print(f"Output: {binary_to_decimal(N1)}")  # Output: 11

# Example 2
N2 = 100
print(f"Input: N = {N2}")
print(f"Output: {binary_to_decimal(N2)}")  # Output: 4
