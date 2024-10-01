import math

def is_strong_number(N):
    # Convert the number to string to extract digits
    digits = [int(digit) for digit in str(N)]
    
    # Calculate the sum of factorials of the digits
    sum_of_factorials = sum(math.factorial(digit) for digit in digits)
    
    # Check if the sum of factorials is equal to the original number
    if sum_of_factorials == N:
        print("YES")
    else:
        print("NO")

# Example usage:
N1 = 145
N2 = 26

print(f"Is {N1} a strong number?")
is_strong_number(N1)  # Output: YES

print(f"\nIs {N2} a strong number?")
is_strong_number(N2)  # Output: NO
