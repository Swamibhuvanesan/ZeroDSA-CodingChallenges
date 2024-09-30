def is_subset(arr1, arr2):
    # Convert arr2 to a set for faster lookup
    set_arr2 = set(arr2)
    
    # Check if every element in arr1 exists in arr2
    for elem in arr1:
        if elem not in set_arr2:
            return False  # If any element is missing, it's not a subset
    
    return True  # All elements are present, so arr1 is a subset

# Test with the provided examples
arr1 = [1, 3, 4, 5, 2]
arr2 = [2, 4, 3, 1, 7, 5, 15]
print(is_subset(arr1, arr2))  # Output: True (subset)

arr1 = [1, 3, 4, 5, 2]
arr2 = [4, 5, 2]
print(is_subset(arr1, arr2))  # Output: False (not a subset)

arr1 = [1, 3, 4, 5, 2]
arr2 = [11, 12, 13, 15, 16]
print(is_subset(arr1, arr2))  # Output: False (not a subset)
