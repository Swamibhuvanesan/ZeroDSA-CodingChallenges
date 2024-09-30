arr = [1, 2, 4, 7, 7, 5]
# Remove duplicates by converting to a set and back to a list
arr = list(set(arr))
arr.sort()
print(arr[1])
arr.sort(reverse=True)
print(arr[1])