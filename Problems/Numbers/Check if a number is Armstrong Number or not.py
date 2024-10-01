def is_armstrong(number: int) -> bool:
    # Convert the number to a string to easily access each digit
    digits = str(number)
    num_digits = len(digits)
    
    # Initialize the sum of powers to 0
    sum_of_powers = 0
    
    # Loop through each digit
    for digit in digits:
        # Convert the digit to an integer and raise it to the power of the number of digits
        power_value = int(digit) ** num_digits
        # Add the result to the sum
        sum_of_powers += power_value
    
    # Check if the sum equals the original number
    return sum_of_powers == number

# Test cases
num1 = 153
num2 = 9474
num3 = 123

print(f"Is {num1} an Armstrong number? {is_armstrong(num1)}")  # Output: True
print(f"Is {num2} an Armstrong number? {is_armstrong(num2)}")  # Output: True
print(f"Is {num3} an Armstrong number? {is_armstrong(num3)}")  # Output: False
