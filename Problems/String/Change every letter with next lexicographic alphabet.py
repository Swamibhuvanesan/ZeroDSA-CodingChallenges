def next_lexicographic_string(s):
    result = ""
    
    for char in s:
        # Check if the character is a lowercase letter between 'a' and 'z'
        if 'a' <= char <= 'z':
            # For 'z', wrap around to 'a'
            if char == 'z':
                result += 'a'
            else:
                result += chr(ord(char) + 1)
        # Check if the character is an uppercase letter between 'A' and 'Z'
        elif 'A' <= char <= 'Z':
            # For 'Z', wrap around to 'A'
            if char == 'Z':
                result += 'A'
            else:
                result += chr(ord(char) + 1)
        else:
            # If the character is not a letter, keep it unchanged
            result += char
    
    return result

# Example usage
s = "hello world! Zebra"
output = next_lexicographic_string(s)
print(output)  # Output: "ifmmp xpsme! Afcsb"
