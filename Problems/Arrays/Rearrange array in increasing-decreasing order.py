#Problem Statement: Rearrange the array such that the first half is arranged in increasing order, and the second half is arranged in decreasing order
def rearrange_array(arr):
    # Sort the array in ascending order
    arr.sort()

    # Find the middle index
    mid = len(arr) // 2

    # First half: increasing order
    first_half = arr[:mid]

    # Second half: decreasing order (reverse the second half)
    second_half = arr[mid:][::-1]

    # Combine the two halves
    result = first_half + second_half
    
    return result

# Example usage
arr = [1, 3, 2, 7, 5, 4, 6]
result = rearrange_array(arr)
print(result)
