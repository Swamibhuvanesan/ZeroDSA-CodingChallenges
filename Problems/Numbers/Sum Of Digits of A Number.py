def sum_of_digits(N):
    # Step 1: Convert the number to a string
    N_str = str(N)
    
    # Step 2: Initialize the sum variable to store the total sum of digits
    digit_sum = 0
    
    # Step 3: Loop through each character in the string
    for digit in N_str:
        # Step 4: Convert the character (which represents a digit) back to an integer
        digit_int = int(digit)
        
        # Step 5: Add the integer value of the digit to the sum
        digit_sum += digit_int
    
    # Step 6: Return the total sum of digits
    return digit_sum

# Example
N = 472
print(sum_of_digits(N))  # Output: 13
