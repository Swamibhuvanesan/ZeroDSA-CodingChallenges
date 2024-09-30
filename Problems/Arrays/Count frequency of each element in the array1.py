import collections
arr = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
elements_count = collections.Counter(arr)

for key, value in elements_count.items():
    print(f"{key}: {value}")