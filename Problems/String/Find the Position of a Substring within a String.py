def find_first_occurrence(text: str, pattern: str) -> int:
    # Using the find() method to get the first occurrence
    index = text.find(pattern)
    return index

# Example 1
text1 = "HelloWorld"
pattern1 = "World"
result1 = find_first_occurrence(text1, pattern1)
print(f"Input: text = {text1}, pattern = {pattern1}")
print(f"Output: {result1}")

# Example 2
text2 = "hello"
pattern2 = "az"
result2 = find_first_occurrence(text2, pattern2)
print(f"Input: text = {text2}, pattern = {pattern2}")
print(f"Output: {result2}")
