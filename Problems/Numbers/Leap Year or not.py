def is_leap_year(year):
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        return "Yes"
    else:
        return "No"

# Example usage:
year1 = 1996
year2 = 2000

print(f"Input: {year1} -> Output: {is_leap_year(year1)}")
print(f"Input: {year2} -> Output: {is_leap_year(year2)}")
