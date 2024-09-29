'''
CP1404/CP5632 - Practical
Various loops

Create a file called loops.py and add the following for loop that displays all the odd numbers between
1 and 20 with a space between each one.

Write more for loops (using range) to do the following:

For marking, we expect to see a complete file with each loop still in it.
Label each of your questions (a, b, c, d)

a. count in 10s from 0 to 100: 0 10 20 30 40 50 60 70 80 90 100

b. count down from 20 to 1: 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1

c. print n stars. Ask the user for a number, then print that many stars (*), all on one line.

d. print n lines of increasing stars. Using the same number as above, print lines of increasing stars, starting at 1 with no blank line.
'''

for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a. count in 10s from 0 to 100: 0 10 20 30 40 50 60 70 80 90 100
for i in range (0, 110, 10):
    print(i, end=' ')
print()

# b. count down from 20 to 1: 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c. print n stars. Ask the user for a number, then print that many stars (*), all on one line.
stars_line = int(input("Enter your number of stars: "))

for i in range(stars_line):
    print("*", end='')
print()

# d. print n lines of increasing stars. Using the same number as above, print lines of increasing stars, starting at
# 1 with no blank line.
stars_stack = int(input("Enter your number of stars: "))

for i in range(stars_stack + 1):
    print("*" * i)
