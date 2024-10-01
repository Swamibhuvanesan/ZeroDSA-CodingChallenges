def palindrome(str):
    reverse = str[::-1]
    if str == reverse:
        return True
    else:
        return False
    
str = "swami"
haha = palindrome(str)
print("The given string is palindrome?",haha)
