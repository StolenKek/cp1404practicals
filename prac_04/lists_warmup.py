"""
CP1404/CP5632 - Practical
Warming up on using lists

What values do the following expressions have? Without running the code, record your answers to these questions in your Python file as a comment.
Then use the Python console to see if you were correct.

In the same Python file, write statements to achieve the following:

Change the first element of numbers to "ten" (the string, not the number 10)
Change the last element of numbers to 1
Print all the elements from numbers except the first two (slice)
Print whether 9 is an element of numbers
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

numbers[0] # The value is 3
numbers[-1] # The value is 2
numbers[3] # The value is 1
numbers[:-1] # The values are 3, 1, 4, 1, 5, 9 which is everything before position -1, but not including it
numbers[3:4] # The value is 1, which is the number starting at position 3 and ending at position 4, but not including it
5 in numbers # True, because it exists in the list
7 in numbers # False, because it does not exist in the list
"3" in numbers # False, because it does not exist in the list as a string, but as an integer
numbers + [6, 5, 3] # The values are 3, 1, 4, 1, 5, 9, 6, 5, 3 which is everything in the list, but now 6, 5, 3 are added to it

# Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"

# Change the last element of numbers to 1
numbers[-1] = 1

# Print all the elements from numbers except the first two (slice)
print(numbers[2:])

# Print whether 9 is an element of numbers
print(9 in numbers)

