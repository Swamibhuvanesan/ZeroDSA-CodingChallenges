def word_both_cap(s):

    # lambda function for capitalizing the
    # first and last letter of words in
    # the string
    return ' '.join(map(lambda s: s[:-1]+s[-1].upper(),
                        s.title().split()))


# Driver's code
s = input("Enter a string:")
print(word_both_cap(s))
