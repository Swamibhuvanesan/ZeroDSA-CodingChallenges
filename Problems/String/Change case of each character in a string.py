def change_case(s: str) -> str:
    # Using list comprehension and str.swapcase() to change case
    return s.swapcase()

# Example 1
input_str1 = "javA"
output_str1 = change_case(input_str1)
print(f"Input: {input_str1}")
print(f"Output: {output_str1}")

# Example 2
input_str2 = "take u forward IS Awesome"
output_str2 = change_case(input_str2)
print(f"Input: {input_str2}")
print(f"Output: {output_str2}")
