'''
Write a program that asks the user for a low and high number, ensuring the high is higher than the low.
Then print n smiley faces where n is a random number between the low and high numbers inclusive
'''
from random import randint

# Enter high and low numbers
user_low_number = int(input("Enter the minimum number: "))
user_high_number = int(input("Enter the maximum number: "))

# Make sure high
while user_high_number <= user_low_number:
    print(f"It must be higher than {user_low_number}.")
    user_high_number = int(input("Enter the maximum number: "))

# Generate a random number between low and high (inclusive)
random_number = randint(user_low_number, user_high_number)

# Print n smiley faces
print(":)" * random_number, end=" ")

'''
Use a main menu:
1) Get a valid non-empty name
2) Print a line of asterisks
3) Print a random number
4) Quit (and say goodbye + name)
'''
from random import randint

def main():
    user_name = ""
    print("1. Get a valid non-empty name")
    print("2. Print a line of asterisks")
    print("3. Print a random number")
    print("4. Quit (and say goodbye + name)")

    while True:
        user_choice = input(">>> ")

        if user_choice == "1":
            user_name = get_name()
        elif user_choice == "2":
            asterisk_line()
        elif user_choice == "3":
            print("Random number:", random_number())
        elif user_choice == "4":
            quit(user_name)
            break
        else:
            print("Invalid choice. Please try again.")

def get_name():
    user_name = input("Enter name: ")
    while user_name == "":  # Ensure the name is not empty
        print("Name cannot be empty.")
        user_name = input("Enter name: ")
    return user_name

def asterisk_line():
    print("*" * 10)

def random_number():
    return randint(1, 100)

def quit(user_name):
    print(f"Farewell {user_name}")

main()

