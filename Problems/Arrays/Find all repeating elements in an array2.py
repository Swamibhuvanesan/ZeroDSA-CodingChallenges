from collections import Counter

def find_repeating_elements(arr):
    element_count = Counter(arr)  # Count the occurrences of each element
    return [elem for elem, count in element_count.items() if count > 1]

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 2, 4, 6, 6, 3]
repeats = find_repeating_elements(arr)
print("Repeating elements:", repeats)
