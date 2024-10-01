def check_even_or_odd(n: int) -> str:
    # Check if the number is divisible by 2
    if n % 2 == 0:
        return "even"
    else:
        return "odd"

# Test cases
n1 = 5
n2 = 6

print(f"{n1} is {check_even_or_odd(n1)}")  # Output: odd
print(f"{n2} is {check_even_or_odd(n2)}")  # Output: even
