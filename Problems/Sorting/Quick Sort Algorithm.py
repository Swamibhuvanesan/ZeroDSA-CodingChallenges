def quicksort(arr):
    # Base case: if the array has 0 or 1 element, it is already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Select the pivot element (in this case, the middle element)
        pivot = arr[len(arr) // 2]
        # Partition the array into three parts:
        # less than pivot, equal to pivot, greater than pivot
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        # Recursively sort the left and right partitions and concatenate results
        return quicksort(left) + middle + quicksort(right)

# Example usage:
print(quicksort([4, 1, 7, 9, 3]))  # Output: [1, 3, 4, 7, 9]
print(quicksort([4, 6, 2, 5, 7, 9, 1, 3]))  # Output: [1, 2, 3, 4, 5, 6, 7, 9]
