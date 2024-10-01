def char_frequency(s: str) -> None:
    # Dictionary to store frequency of each character
    frequency = {}

    # Iterate through each character in the string
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # Print the frequency of each character
    for key, value in frequency.items():
        print(f"{key}{value}", end=" ")

# Test examples
string1 = "takeuforward"
string2 = "articles"

char_frequency(string1)  # Output: "t1 a2 k1 e1 u1 f1 o1 r2 w1 d1"
print()  # For better readability in output
char_frequency(string2)  # Output: "a1 r1 t1 i1 c1 l1 e1 s1"
