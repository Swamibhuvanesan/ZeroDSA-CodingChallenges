def remove_whitespaces(s):
    result = ""
    
    for char in s:
        if not char.isspace():
            result += char
    
    return result

# Input string
s = input("Enter a string: ")

# Output the string after removing whitespaces
print(f"String after removing whitespaces: {remove_whitespaces(s)}")
