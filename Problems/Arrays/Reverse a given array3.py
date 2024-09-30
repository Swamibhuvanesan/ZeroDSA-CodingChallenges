arr = [1, 2, 3, 4, 5]
n = len(arr)

# Loop from the start to the middle of the list
for i in range(n // 2):
    # Swap the elements at index i and n-i-1
    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]

print(arr)
