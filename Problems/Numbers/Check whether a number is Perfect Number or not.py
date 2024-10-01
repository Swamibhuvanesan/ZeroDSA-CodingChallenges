def is_perfect_number(n: int) -> bool:
    # Initialize sum of divisors
    sum_of_divisors = 0
    
    # Find divisors of n (excluding n itself)
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    
    # If the sum of divisors equals the number, it's a perfect number
    return sum_of_divisors == n

# Test cases
n1 = 6
n2 = 15
n3 = 28

print(f"{n1} is a perfect number? {is_perfect_number(n1)}")  # Output: True
print(f"{n2} is a perfect number? {is_perfect_number(n2)}")  # Output: False
print(f"{n3} is a perfect number? {is_perfect_number(n3)}")  # Output: True
