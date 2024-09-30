def search_element(array, k):
    # Loop through the array
    for i in range(len(array)):
        if array[i] == k:
            return i  # Return the index if element is found
    
    return -1  # Return -1 if the element is not found

# Test with the provided examples
print(search_element([1, 2, 3, 4, 5], 3))  # Output: 2
print(search_element([6, 7, 9, 5, 3, 10], 10))  # Output: 5
