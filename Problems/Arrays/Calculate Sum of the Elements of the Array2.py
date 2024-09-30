n = int(input())
arr = list(range(1, n+1))
print(arr)

def array_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total
print(array_sum(arr))