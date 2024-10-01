def octal_to_binary(octal_str):
    # Convert octal to decimal
    decimal_num = int(octal_str, 8)
    # Convert decimal to binary and remove "0b" prefix
    binary_num = bin(decimal_num).replace("0b", "")
    # Add leading zeros to match the length of the octal equivalent
    return binary_num.zfill(len(octal_str) * 3)

# Example usage:
print(octal_to_binary("345"))  # Output: 011100101
print(octal_to_binary("170"))  # Output: 001111000
