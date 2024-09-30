def remove_duplicates(arr):
    if not arr:
        return 0
    # Pointer to place the next unique element
    unique_idx = 0 # it's set to the first element's index

    for i in range(1, len(arr)): #The loop starts from the second element (index 1) because the first element is already considered as unique.
        if arr[i] != arr[unique_idx]: #For each element, we check if it’s different from the last unique element found (which is at arr[unique_idx]). If it’s different, it means it's a unique element.
            unique_idx += 1
            arr[unique_idx] = arr[i]
    
    # Return the length of the array with unique elements
    return unique_idx + 1 #After the loop completes, unique_idx will point to the last unique element's position. Since indices are 0-based, the length of the unique part of the array is unique_idx + 1.

# Example usage:
arr = [1, 1, 2, 2, 3, 4, 4, 5]
new_length = remove_duplicates(arr)
print("Array after removing duplicates:", arr[:new_length])
print("New length:", new_length)
