def gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

def find_lcm(num1, num2):
    return abs(num1 * num2) // gcd(num1, num2)

# Example 1
num1, num2 = 4, 8
print("LCM of", num1, "and", num2, "is", find_lcm(num1, num2))  # Output: 8

# Example 2
num1, num2 = 3, 6
print("LCM of", num1, "and", num2, "is", find_lcm(num1, num2))  # Output: 6
