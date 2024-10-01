def selection_sort(arr):
    N = len(arr)
    for i in range(N):
        # Assume the current element is the smallest
        min_index = i
        for j in range(i + 1, N):
            # Find the index of the smallest element in the remaining unsorted part
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found smallest element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example usage:
print(selection_sort([13, 46, 24, 52, 20, 9]))  # Output: [9, 13, 20, 24, 46, 52]
print(selection_sort([5, 4, 3, 2, 1]))          # Output: [1, 2, 3, 4, 5]
