def is_palindrome(n: int) -> bool:
    # Convert the number to a string and check if it reads the same forward and backward
    return str(n) == str(n)[::-1]

def find_palindromes_in_range(min_val: int, max_val: int) -> list:
    # List to store palindrome numbers
    palindrome_numbers = []
    
    # Iterate over each number in the given range
    for num in range(min_val, max_val + 1):
        if is_palindrome(num):
            palindrome_numbers.append(num)
    
    return palindrome_numbers

# Example 1
min_val1 = 10
max_val1 = 50
result1 = find_palindromes_in_range(min_val1, max_val1)
print(f"Palindromes between {min_val1} and {max_val1}: {result1}")

# Example 2
min_val2 = 100
max_val2 = 150
result2 = find_palindromes_in_range(min_val2, max_val2)
print(f"Palindromes between {min_val2} and {max_val2}: {result2}")
