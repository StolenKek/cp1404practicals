"""
Write a program to read a file and print only the lines that start with #
The user should enter the filename()
"""
# user_file = input("Enter file name: ")
#
# with open(user_file, "r") as in_file:
#     for line in in_file:
#         if line.startswith("#"):
#             print(line.strip())

"""
Write code that creates files from a list of strings
Each file should be named with the value of the string with .txt extension. 
If the string is "Bob", create a file called "Bob.txt".
Write the string to the file.
"""

FILENAME = ["Adam", "Bob", "Cathy"]

# for name in FILENAME:
#     current_file = open(name + ".txt", "w")
#     current_file.write(name)
#     current_file.close()

# for name in FILENAME:
#     with open(f"{name}.txt", "w") as current_file:
#         current_file.write(name)

"""
Write code to read a file like this and print each data pair, like "Bob was born in NZ"
Bob\n
NZ\n
Jane\n
Myannmar\n
Derek\n
Austrailia\n
"""

# with open("names.txt", "r") as in_file:
#     lines = in_file.readlines()
#
# print()
#
# for i in range(0, len(lines)-1, 2):
#     name = lines[i].strip()
#     country = lines[i + 1].strip()
#     print(f"{name} was born in {country}.")

