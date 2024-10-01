def find_factors(n):
    # Initialize an empty set to store factors (using set to avoid duplicates)
    factors = set()
    
    # Loop through all numbers from 1 to sqrt(n)
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.add(i)        # Add the divisor
            factors.add(n // i)   # Add its corresponding divisor
    
    # Sort the factors to print them in order
    sorted_factors = sorted(factors)
    
    # Print the factors
    print(", ".join(map(str, sorted_factors)))

# Example usage:
n1 = 6
n2 = 9

print(f"Factors of {n1}:")
find_factors(n1)  # Output: 1, 2, 3, 6

print(f"\nFactors of {n2}:")
find_factors(n2)  # Output: 1, 3, 9
