def reverse_string(s):
    result = ""
    
    for char in s:
        result = char + result  # Prepend each character to the result
    
    return result

# Input string
s = input("Enter a string: ")

# Output the reversed string
print(f"Reversed string: {reverse_string(s)}")
