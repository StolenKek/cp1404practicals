"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
Let's write a program that gets an integer from the user and does not crash when a non-number is entered.
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True # Changes is_finished to True when valid
    except ValueError: # Catch non-integer inputs
        print("Please enter a valid integer.")
print("Valid result is:", result)