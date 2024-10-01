def solve(a: str, b: str) -> bool:
    n, m = len(a), len(b)
    
    # Base case: Both strings are empty
    if n == 0 and m == 0:
        return True
    
    # If pattern has '*' but no characters left in b, it's a mismatch
    if n > 1 and a[0] == '*' and m == 0:
        return False
    
    # If current characters match or pattern has '?' at the first position
    if (n > 0 and m > 0 and (a[0] == '?' or a[0] == b[0])):
        return solve(a[1:], b[1:])
    
    # If pattern contains '*' at the first position
    if n > 0 and a[0] == '*':
        # '*' can match an empty sequence (skip '*' in a) or
        # '*' can match one character from b (move to the next character in b)
        return solve(a[1:], b) or solve(a, b[1:])
    
    # If no match, return False
    return False

# Test cases
str1 = "Prepins*a"
str2 = "Prepinsta"

print("First string with wild characters:", str1)
print("Second string without wild characters:", str2)
print(solve(str1, str2))  # Output: True
