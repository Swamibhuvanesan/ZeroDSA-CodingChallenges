def factorial(X):
    result = 1  # Initialize result to 1
    
    # Loop to multiply all numbers from 1 to X
    for i in range(1, X + 1):
        result *= i
    
    return result

# Example usage:
X1 = 5
X2 = 3

print(f"Factorial of {X1} is: {factorial(X1)}")  # Output: 120
print(f"Factorial of {X2} is: {factorial(X2)}")  # Output: 6
