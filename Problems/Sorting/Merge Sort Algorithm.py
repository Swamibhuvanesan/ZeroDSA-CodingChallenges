def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle of the array
        mid = len(arr) // 2
        # Divide the array into two halves
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the two halves
        i = j = k = 0

        # Copy data to temp arrays left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any element was left in left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Check if any element was left in right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Example usage:
print(merge_sort([4, 2, 1, 6, 7]))  # Output: [1, 2, 4, 6, 7]
print(merge_sort([3, 2, 8, 5, 1, 4, 23]))  # Output: [1, 2, 3, 4, 5, 8, 23]
