def is_prime(n: int) -> bool:
    # Check if the number is less than 2 (not prime)
    if n < 2:
        return False
    # Check for factors from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test cases
num1 = 29
num2 = 16

print(f"Is {num1} prime? {is_prime(num1)}")  # Output: True
print(f"Is {num2} prime? {is_prime(num2)}")  # Output: False
