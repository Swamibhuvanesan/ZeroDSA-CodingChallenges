def num_to_words(num):
    # Define words for ones, tens, and unique numbers
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    def convert_hundreds(n):
        if n == 0:
            return ""
        elif n < 10:
            return ones[n]
        elif n < 20:
            return teens[n - 10]
        elif n < 100:
            return tens[n // 10] + ("" if n % 10 == 0 else " " + ones[n % 10])
        else:
            return ones[n // 100] + " hundred" + ("" if n % 100 == 0 else " " + convert_hundreds(n % 100))

    if num == 0:
        return "zero"

    result = ""

    # Handle thousands
    if num >= 1000:
        result += ones[num // 1000] + " thousand"
        num %= 1000
        if num > 0:
            result += " "

    # Handle hundreds, tens, and ones
    result += convert_hundreds(num)

    return result

# Example usage:
print(num_to_words(7824))  # Output: seven thousand eight hundred twenty four
print(num_to_words(370))   # Output: three hundred seventy
