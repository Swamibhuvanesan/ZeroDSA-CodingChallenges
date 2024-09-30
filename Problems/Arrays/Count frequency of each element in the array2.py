arr = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
elements_count = {}

for element in arr:
    if element in elements_count:
        elements_count[element] += 1
    else:
        elements_count[element] = 1

for key, value in elements_count.items():
    print(f"{key}: {value}")