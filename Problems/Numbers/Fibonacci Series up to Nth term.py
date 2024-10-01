def fibonacci_series(N):
    a, b = 0, 1  # Initialize the first two terms
    
    for i in range(N+1):
        print(a, end=" ")  # Print the current term
        a, b = b, a + b    # Update a and b for the next term

# Example usage:
N1 = 5
N2 = 6

print(f"Fibonacci series up to {N1}th term:")
fibonacci_series(N1)
print("\n")  # To separate the outputs

print(f"Fibonacci series up to {N2}th term:")
fibonacci_series(N2)
