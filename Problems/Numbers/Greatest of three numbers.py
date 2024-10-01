def find_greatest_of_three(num1, num2, num3):
    # Compare all three numbers and return the greatest one
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Example usage:
num1_1, num1_2, num1_3 = 1, 3, 5
num2_1, num2_2, num2_3 = 1.123, 1.124, 1.125

print(f"Input: {num1_1} {num1_2} {num1_3} -> Output: {find_greatest_of_three(num1_1, num1_2, num1_3)}")
print(f"Input: {num2_1} {num2_2} {num2_3} -> Output: {find_greatest_of_three(num2_1, num2_2, num2_3)}")
