def area_of_circle(radius):
    # Approximate value of pi
    pi = 3.14
    
    # Formula to calculate area of the circle
    area = pi * radius * radius
    return area

# Example 1
N1 = 5
print(f"Input: N = {N1}")
print(f"Output: {area_of_circle(N1):.1f}")  # Output: 78.5

# Example 2
N2 = 4
print(f"Input: N = {N2}")
print(f"Output: {area_of_circle(N2):.1f}")  # Output: 50.2
