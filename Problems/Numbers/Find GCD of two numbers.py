def gcd(N1, N2):
    while N2 != 0:
        N1, N2 = N2, N1 % N2
    return N1

# Example usage:
N1_1, N2_1 = 9, 12
N1_2, N2_2 = 20, 15

print(f"GCD of {N1_1} and {N2_1} is: {gcd(N1_1, N2_1)}")  # Output: 3
print(f"GCD of {N1_2} and {N2_2} is: {gcd(N1_2, N2_2)}")  # Output: 5
