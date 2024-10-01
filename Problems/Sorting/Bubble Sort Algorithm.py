def bubble_sort(arr):
    N = len(arr)
    for i in range(N):
        swapped = False
        for j in range(0, N - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped, the array is sorted
        if not swapped:
            break
    return arr

# Example usage:
print(bubble_sort([13, 46, 24, 52, 20, 9]))  # Output: [9, 13, 20, 24, 46, 52]
print(bubble_sort([5, 4, 3, 2, 1]))          # Output: [1, 2, 3, 4, 5]
