def count_vowels_consonants_spaces(s):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    space_count = 0
    
    for char in s:
        if char in vowels:
            vowel_count += 1
        elif char.isalpha() and char not in vowels:
            consonant_count += 1
        elif char.isspace():
            space_count += 1
    
    return vowel_count, consonant_count, space_count

# Input string
s = input("Enter a string: ")

vowels, consonants, spaces = count_vowels_consonants_spaces(s)

print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Spaces: {spaces}")
