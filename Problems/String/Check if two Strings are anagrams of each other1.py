def are_anagrams(str1: str, str2: str) -> bool:
    # Step 1: Check if lengths are the same
    if len(str1) != len(str2):
        return False

    # Step 2: Create dictionaries to count the frequency of each character
    frequency1 = {}
    frequency2 = {}

    # Step 3: Count the frequency of each character in str1
    for char in str1:
        if char in frequency1:
            frequency1[char] += 1
        else:
            frequency1[char] = 1

    # Step 4: Count the frequency of each character in str2
    for char in str2:
        if char in frequency2:
            frequency2[char] += 1
        else:
            frequency2[char] = 1

    # Step 5: Compare both frequency dictionaries
    return frequency1 == frequency2

# Test examples
print(are_anagrams("CAT", "ACT"))  # Output: True
print(are_anagrams("RULES", "LESRT"))  # Output: False
