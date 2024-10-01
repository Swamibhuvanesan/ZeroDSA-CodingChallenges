def reverse_words(s: str) -> str:
    # Split the string into words, reverse the list of words, and join them back into a string
    return ' '.join(s.split()[::-1])

# Example 1
input_str1 = "this is an amazing program"
output_str1 = reverse_words(input_str1)
print(f"Input: {input_str1}")
print(f"Output: {output_str1}")

# Example 2
input_str2 = "This is decent"
output_str2 = reverse_words(input_str2)
print(f"Input: {input_str2}")
print(f"Output: {output_str2}")
