"""
CP1404/CP5632 Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.

Things To Do:
1) Get the word format from the user so that they can customise it. Convert it to lowercase using a string method.

2) Try and make the program more interesting. For example:
    a. Use wildcards for the vowels (#) and consonants (%) or either (*) and make alphabetical characters use that actual character - e.g. the format "%re#l" might produce a word like "greatly" or "breuzla"
    b. Automatically (randomly) generate the word_format variable.

"""

import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

word_format = input("Enter your word format ('%' for consonants & '#' for vowels): ").lower()
word = ""
for kind in word_format:
    if kind == "%":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)

print(word)