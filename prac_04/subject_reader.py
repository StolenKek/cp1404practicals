"""
CP1404/CP5632 Practical
Data file -> lists program

A common way of storing data is in files, which means the data is in string form. Even numbers are stored as string.
So, a data file storing subjects, lecturer and student numbers might look like:

CP1401,Ada Lovelace,192
CP1404,Alan Turing,98

We can read a file like this line-by-line (for line in file) but we also need to process each line to get the parts. A good way to do that is with the string split method.
So, line.split(',') would give us a list that contained the parts of this line... but each part would still be a string.

Things to do:
Copy the starter code and data file from subject_reader.py and subject_data.txt
Remember to commit these before modifying them any further.
Study the starter code and run it. There are comments and print calls to show you what's happening.

The code reads the file data and processes it into the parts variable, but we want the load_data function to return the data as a list of lists (nested list), like:
[['CP1401', 'Ada Lovelace', 192],['CP1404', 'Alan Turing', 98]]
Modify the function so that it does this.

Currently, main just prints data. Add a new function to display subject details that produces something like the following:

CP1401 is taught by Ada Lovelace and has 192 students
CP1404 is taught by Alan Turing  and has  98 students
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
    input_file.close()
    return subject

def display_subjects():
    """Display subject details formatted like: subject + is taught by + lecturer + and has + number of students"""
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]:3} students")

main()

