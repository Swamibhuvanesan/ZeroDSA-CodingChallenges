def find_repeating_elements(arr):
    element_count = {}  # Dictionary to store the count of each element
    repeating_elements = []  # List to store the repeating elements
    
    # Count occurrences of each element
    for elem in arr:
        if elem in element_count:
            element_count[elem] += 1
        else:
            element_count[elem] = 1
    
    # Identify repeating elements
    for elem, count in element_count.items():
        if count > 1:  # Here, we check if an element's count is greater than 1. This means the element is repeated.
            repeating_elements.append(elem)
    
    return repeating_elements

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 2, 4, 6, 6, 3]
repeats = find_repeating_elements(arr)
print("Repeating elements:", repeats)
