def find_largest_word(s):
    # Split the string into words
    words = s.split()
    
    # Initialize variables to store the largest word
    largest_word = ""
    
    # Iterate through the list of words
    for word in words:
        # Update the largest word if the current word is longer
        if len(word) > len(largest_word):
            largest_word = word
    
    return largest_word

# Example 1
s1 = "Google Doc"
print(find_largest_word(s1))  # Output: "Google"

# Example 2
s2 = "Microsoft Teams"
print(find_largest_word(s2))  # Output: "Microsoft"
