def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"  # Optional case

# Example usage:
n1 = 5
n2 = -6

print(f"Input: n={n1} -> Output: {check_number(n1)}")
print(f"Input: n={n2} -> Output: {check_number(n2)}")
