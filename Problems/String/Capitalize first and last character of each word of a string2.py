def Caps_workFL(s):
# Creating an empty string
    result = ""

# Using for loop + the functions to capitalize
    for i in s.title().split():
        result += (i[:-1] + i[-1].upper()) + ' '
    return result
    
s = input("Enter a string:")
print(Caps_workFL(s).strip()) # To remove the space at the end
