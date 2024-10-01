def prime_factors(N):
    # Initialize an empty list to store prime factors
    factors = []
    
    # Step 1: Divide N by 2 until it's no longer divisible by 2
    while N % 2 == 0:
        factors.append(2)
        N //= 2
    
    # Step 2: Now check for odd numbers starting from 3
    for i in range(3, int(N**0.5) + 1, 2):
        while N % i == 0:
            factors.append(i)
            N //= i
    
    # Step 3: If N is still greater than 2, then it must be a prime number
    if N > 2:
        factors.append(N)
    
    # Remove duplicates from the list (since we want unique prime factors)
    unique_factors = list(set(factors))
    
    # Print the prime factors
    print(", ".join(map(str, unique_factors)))

# Example usage:
N1 = 60
N2 = 35

print(f"Prime factors of {N1}:")
prime_factors(N1)  # Output: 2, 3, 5

print(f"\nPrime factors of {N2}:")
prime_factors(N2)  # Output: 5, 7
