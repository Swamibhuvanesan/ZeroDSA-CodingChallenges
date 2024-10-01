def find_greatest(num1, num2):
    # Compare the two numbers and return the greater one
    if num1 > num2:
        return num1
    else:
        return num2

# Example usage:
num1_1, num1_2 = 1, 3
num2_1, num2_2 = 1.123, 1.124

print(f"Input: {num1_1} {num1_2} -> Output: {find_greatest(num1_1, num1_2)}")
print(f"Input: {num2_1} {num2_2} -> Output: {find_greatest(num2_1, num2_2)}")
