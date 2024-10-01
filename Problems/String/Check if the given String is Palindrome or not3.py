def palindrome(str):
    for i in range(0,len(str)):
        if str[i] != str[len(str) -i -1]:
            return False
    return True
    
str = "MalayayalaM"
haha = palindrome(str)
print("The given string is palindrome?",haha)
