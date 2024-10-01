def reverse_number(N):
    # Convert the number to a string, reverse it, and convert back to an integer to remove leading zeros
    reversed_number = int(str(N)[::-1])
    return reversed_number

# Example usage:
N1 = 472
N2 = 470

print(f"Input: {N1} -> Output: {reverse_number(N1)}")
print(f"Input: {N2} -> Output: {reverse_number(N2)}")
