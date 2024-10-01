def count_common_subsequences(s1: str, s2: str, i: int, j: int) -> int:
    # Base case: If we've reached the end of either string
    if i == len(s1) or j == len(s2):
        return 1  # The empty subsequence is always a common subsequence

    # If characters match, we can either include or exclude them in the subsequence
    if s1[i] == s2[j]:
        # Add up subsequences by either including or excluding the matched character
        return count_common_subsequences(s1, s2, i + 1, j) + count_common_subsequences(s1, s2, i, j + 1)
    else:
        # If characters don't match, move to the next character in one or both strings
        return count_common_subsequences(s1, s2, i + 1, j) + count_common_subsequences(s1, s2, i, j + 1) - count_common_subsequences(s1, s2, i + 1, j + 1)

# Test cases
string1 = "abc"
string2 = "abc"
print(count_common_subsequences(string1, string2, 0, 0))  # Output: 8

string3 = "abc"
string4 = "def"
print(count_common_subsequences(string3, string4, 0, 0))  # Output: 1
