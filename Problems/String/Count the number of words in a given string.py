def count_words(s):
    # Split the string by spaces to get a list of words
    words = s.split()
    
    # Return the length of the list, which is the number of words
    return len(words)

# Example usage
str1 = "Hello, how are you?"
print(count_words(str1))  # Output: 4

str2 = "This is a test string."
print(count_words(str2))  # Output: 5
