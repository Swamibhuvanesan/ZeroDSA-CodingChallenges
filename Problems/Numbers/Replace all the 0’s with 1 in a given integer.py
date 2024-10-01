def replace_zeros_with_ones(N):
    # Convert the integer to a string
    N_str = str(N)
    
    # Replace all occurrences of '0' with '1'
    N_str_replaced = N_str.replace('0', '1')
    
    # Convert the string back to an integer
    return int(N_str_replaced)

# Example 1
N1 = 102003
print(f"Input: N = {N1}")
print(f"Output: {replace_zeros_with_ones(N1)}")  # Output: 112113

# Example 2
N2 = 204
print(f"Input: N = {N2}")
print(f"Output: {replace_zeros_with_ones(N2)}")  # Output: 214
