def remove_brackets(expression):
    result = ""
    
    for char in expression:
        if char not in "()":  # Ignore brackets
            result += char
    
    return result

# Input expression
expression = input("Enter an algebraic expression: ")

# Output the expression after removing brackets
print(f"Expression after removing brackets: {remove_brackets(expression)}")
