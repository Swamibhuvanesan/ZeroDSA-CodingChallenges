def is_automorphic(N):
    # Calculate the square of N
    square = N * N
    
    # Convert both N and the square to strings
    str_N = str(N)
    str_square = str(square)
    
    # Check if the square ends with N
    if str_square.endswith(str_N):
        print("Automorphic Number")
    else:
        print("Not an Automorphic Number")

# Example usage:
N1 = 76
N2 = 25
N3 = 7

print(f"Is {N1} an Automorphic Number?")
is_automorphic(N1)  # Output: Automorphic Number

print(f"\nIs {N2} an Automorphic Number?")
is_automorphic(N2)  # Output: Automorphic Number

print(f"\nIs {N3} an Automorphic Number?")
is_automorphic(N3)  # Output: Not an Automorphic Number
