def sum_of_ap(a, d, n):
    # Using the formula to calculate the sum of the A.P.
    return (n / 2) * (2 * a + (n - 1) * d)

# Example usage:
a = 2  # First term
d = 3  # Common difference
n = 5  # Number of terms

print(f"Sum of the A.P. Series: {sum_of_ap(a, d, n)}")
