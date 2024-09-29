'''
CP1404/CP5632 - Practical
Menu-driven number sequence generator

A school teacher requires a small program that would allow primary school students to learn about various number
sequences. The teacher is interested in a simple menu-driven program that has the following choices (where x and y are
inputs the user enters once at the start of the program):

1. Show the even numbers from x to y
2. Show the odd numbers from x to y
3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)
4. Exit the program
'''
# User-input start and end numbers
user_start_number = int(input("Enter the number you want to start the sequence with: "))
user_end_number = int(input("Enter the number you want to end the sequence with: "))

# Menu and choices
print("\nWhat would you like to try today? (1-4)\n1. Show the even numbers from x to y\n2. Show the odd numbers from x to y\n3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)\n4. Exit the program")
user_choice = str(input(">>> "))

while user_choice != "4":
    if user_choice == "1":
        for i in range (user_start_number, user_end_number + 1):
            if i % 2 == 0:
                print(i, end=" ")
    elif user_choice == "2":
        for i in range (user_start_number, user_end_number + 1):
            if i % 2 == 1:
                print(i, end=" ")
    elif user_choice == "3":
        for i in range(user_start_number, user_end_number + 1):
            user_squared = i ** 2
            print(user_squared, end=' ')
    else:
        print("Invalid choice, choose from 1-4.")
    print("\nWhat would you like to try today? (1-4)\n1. Show the even numbers from x to y\n2. Show the odd numbers from x to y\n3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)\n4. Exit the program")
    user_choice = input(">>> ").upper()
print("Goodbye!")