def is_prime(n: int) -> bool:
    # Check if the number is less than 2 (not prime)
    if n < 2:
        return False
    # Check for factors from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(a: int, b: int) -> list:
    # List to store prime numbers in the range
    prime_numbers = []
    
    # Iterate through each number in the range [a, b]
    for num in range(a, b + 1):
        if is_prime(num):
            prime_numbers.append(num)
    
    return prime_numbers

# Example 1
a1, b1 = 2, 10
primes1 = find_primes_in_range(a1, b1)
print(f"Prime numbers between {a1} and {b1}: {primes1}")

# Example 2
a2, b2 = 10, 16
primes2 = find_primes_in_range(a2, b2)
print(f"Prime numbers between {a2} and {b2}: {primes2}")
