# Input the value of n
n = int(input("Enter a number: "))

# Create the array with elements from 1 to n
arr = list(range(1, n + 1))
print("Array:", arr)

# Function to calculate the sum of the array
def array_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

# Calculate the sum of the array
total_sum = array_sum(arr)

# Calculate the average
average = total_sum / n if n > 0 else 0  # Avoid division by zero

# Print the result
print("Sum:", total_sum)
print("Average:", average)
