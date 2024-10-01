def word_with_highest_repeated_letters(input_str):
    # Split the input string into words
    words = input_str.split()
    
    max_repeats = 0
    word_with_max_repeats = -1  # Default return value in case no word has repeated letters
    
    # Iterate through each word
    for word in words:
        # Create a dictionary to count occurrences of each letter
        letter_count = {}
        
        # Count the occurrences of each letter in the word
        for letter in word:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
        
        # Find the highest occurrence of any letter in the word
        most_repeated = max(letter_count.values())
        
        # If a word has more than 1 occurrence of any letter and it has the most repeats so far
        if most_repeated > 1 and most_repeated > max_repeats:
            max_repeats = most_repeated
            word_with_max_repeats = word
    
    return word_with_max_repeats

# Example 1
str1 = "abcdefghij google microsoft"
print(word_with_highest_repeated_letters(str1))  # Output: google

# Example 2
str2 = "cameron blue"
print(word_with_highest_repeated_letters(str2))  # Output: -1
