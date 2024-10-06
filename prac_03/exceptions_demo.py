"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    A ValueError will occur when a user enters something that cannot be converted to an integer, such as a string
2. When will a ZeroDivisionError occur?
    A ZeroDivisionError will occur when a user enters 0 as the denominator.
    Dividing any number by zero is mathematically undefined, so Python will raise this error to prevent the operation.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Yes, so we need to check if the denominator is 0 before dividing.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:  # Ask until the user enters a non-zero denominator
        print("Denominator cannot be zero, enter another number.")
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")