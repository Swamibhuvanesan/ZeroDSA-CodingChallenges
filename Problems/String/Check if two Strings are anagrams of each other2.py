from collections import Counter

def are_anagrams(str1: str, str2: str) -> bool:
    # Step 1: Compare the character counts of both strings using Counter
    return Counter(str1) == Counter(str2)

# Test examples
print(are_anagrams("CAT", "ACT"))  # Output: True
print(are_anagrams("RULES", "LESRT"))  # Output: False
