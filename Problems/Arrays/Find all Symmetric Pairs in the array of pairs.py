def find_symmetric_pairs(pairs):
    # Dictionary to store the pairs
    pair_dict = {}
    symmetric_pairs = []

    # Iterate through each pair
    for a, b in pairs:
        # Check if (b, a) exists in the dictionary
        if pair_dict.get(b) == a:
            symmetric_pairs.append((a, b))
        else:
            # Add the current pair to the dictionary
            pair_dict[a] = b
    
    return symmetric_pairs

# Example 1:
pairs = [(1, 2), (2, 1), (3, 4), (4, 5), (5, 4)]
result = find_symmetric_pairs(pairs)
print("Symmetric pairs:", result)  # Output: [(2, 1), (5, 4)]

# Example 2:
pairs = [(1, 5), (2, 3), (4, 2), (5, 1), (2, 4)]
result = find_symmetric_pairs(pairs)
print("Symmetric pairs:", result)  # Output: [(5, 1), (2, 4)]
