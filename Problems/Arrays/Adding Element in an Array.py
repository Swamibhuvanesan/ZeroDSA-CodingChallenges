def AddEle(arr):
    arr.append(99)   # Appends 99 to the end of the array. #can also create a new new list and use extend()
    arr.insert(0, 0) # Inserts 0 at the beginning of the array. #use insert() for adding elements at specific index position.

# Example usage:
arr = [1, 2, 3, 4, 5]
AddEle(arr)
print(arr)  # Output will be [0, 1, 2, 3, 4, 5, 99]


