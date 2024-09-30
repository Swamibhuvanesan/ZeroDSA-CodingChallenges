def find_median(arr):
    arr.sort()  # Sort the array
    n = len(arr)
    mid = n // 2
    
    if n % 2 == 0:  # If even number of elements
        return (arr[mid - 1] + arr[mid]) / 2
    else:  # If odd number of elements
        return arr[mid]

# Example usage:
arr = [1,2,3,4,5,6,8,9]
median = find_median(arr)
print("Median:", median)
