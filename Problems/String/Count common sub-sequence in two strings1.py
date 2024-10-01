def count_common_subsequences(s1: str, s2: str) -> int:
    n = len(s1)
    m = len(s2)
    
    # Create a 2D DP table to store counts of common subsequences
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Base case: An empty string has exactly 1 subsequence (the empty subsequence)
    for i in range(n + 1):
        dp[i][0] = 1
    for j in range(m + 1):
        dp[0][j] = 1
    
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:  # Matching characters
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            else:  # Non-matching characters
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

    # The answer is the total number of common subsequences
    return dp[n][m]

# Test examples
string1 = "abc"
string2 = "abc"
print(count_common_subsequences(string1, string2))  # Output: 8

string3 = "abc"
string4 = "def"
print(count_common_subsequences(string3, string4))  # Output: 1
