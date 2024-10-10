"""
CP1404/CP5632 Practical
List exercises

Write a program that prompts the user for 5 numbers and then stores each of these in a list called numbers.
The program should then output information about these numbers, as in the output below.
You can use the functions min, max, sum and len, and you can use the append method to add a number to a list.

   Number: 5
   Number: 20
   Number: 1
   Number: 2
   Number: 3
   The first number is 5
   The last number is 3
   The smallest number is 1
   The largest number is 20
   The average of the numbers is 6.2
"""
def main():
    """Main function to run code"""
    numbers = get_numbers()  # Get the list of numbers from the user
    print_results(numbers)

def get_numbers():
    """Prompt the user for 5 numbers and validate each one."""
    numbers = []  # List to store valid numbers
    for i in range(5):
        valid_input = False  # Flag to track if the input is valid
        while not valid_input:
            try:
                number = int(input(f"Enter number: "))
                numbers.append(number)  # Add the valid number to the list
                valid_input = True
            except ValueError:
                print("Invalid input; please enter a valid number.")
    return numbers

def print_results(numbers):
    first_number = numbers[0]
    last_number = numbers[-1]
    smallest_number = min(numbers)
    largest_number = max(numbers)
    average = sum(numbers) / len(numbers)

    print(f"The first number is {first_number}")
    print(f"The last number is {last_number}")
    print(f"The smallest number is {smallest_number}")
    print(f"The largest number is {largest_number}")
    print(f"The average of the numbers is {average:.1f}")

main()