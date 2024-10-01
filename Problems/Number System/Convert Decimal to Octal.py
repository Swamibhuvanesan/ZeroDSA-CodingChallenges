def decimal_to_octal(N):
    return oct(N).replace("0o", "")

# Example usage:
print(decimal_to_octal(17))  # Output: 21
print(decimal_to_octal(45))  # Output: 55
