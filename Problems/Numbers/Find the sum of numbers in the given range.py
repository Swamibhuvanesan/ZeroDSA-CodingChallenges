def sum_of_range(l, r):
    # Step 1: Use a loop to calculate the sum of numbers from l to r
    total_sum = sum(range(l, r + 1))
    return total_sum

# Example 1
l1, r1 = 2, 7
print(f"Input: l={l1}, r={r1}")
print(f"Output: {sum_of_range(l1, r1)}")  # Output: 27

# Example 2
l2, r2 = 5, 9
print(f"Input: l={l2}, r={r2}")
print(f"Output: {sum_of_range(l2, r2)}")  # Output: 35
