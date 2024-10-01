def insertion_sort(arr):
    N = len(arr)
    for i in range(1, N):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0...i-1] that are greater than key to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage:
print(insertion_sort([13, 46, 24, 52, 20, 9]))  # Output: [9, 13, 20, 24, 46, 52]
print(insertion_sort([5, 4, 3, 2, 1]))          # Output: [1, 2, 3, 4, 5]
