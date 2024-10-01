def sum_of_gp(a, r, n):
    # If common ratio is 1, the sum is just n times the first term
    if r == 1:
        return n * a
    else:
        # Using the formula for sum of G.P. when r != 1
        return a * (1 - r**n) / (1 - r)

# Example usage:
a1, r1, n1 = 1, 0.5, 3
a2, r2, n2 = 3, 5, 2

print(f"Sum of the G.P. Series for Input 1: {sum_of_gp(a1, r1, n1)}")
print(f"Sum of the G.P. Series for Input 2: {sum_of_gp(a2, r2, n2)}")
