def power(x, n):
    result = 1  # Initialize result to 1
    
    # Multiply x, n times
    for _ in range(n):
        result *= x
    
    return result

# Example usage:
x1, n1 = 2, 5
x2, n2 = 21, 2

print(f"{x1}^{n1} = {power(x1, n1)}")  # Output: 32
print(f"{x2}^{n2} = {power(x2, n2)}")  # Output: 441
