"""
CP1404/CP5632 - Practical
Starter code for cumulative total income program

Accountant Annie wants you to write a program to calculate the monthly cumulative totals for incomes.
The program should ask for the number of monthly incomes to enter, then get and store the incomes in a list.

When the incomes have been entered, the program should display a list of the month's income with cumulative totals.
Here's some sample output (for 5 months in this case):

How many months? 5

Enter income for month 1: 120
Enter income for month 2: 245.4
Enter income for month 3: 900
Enter income for month 4: 1205.56
Enter income for month 5: 12.35

Income Report
-------------
Month  1 - Income: $    120.00         Total: $    120.00
Month  2 - Income: $    245.40         Total: $    365.40
Month  3 - Income: $    900.00         Total: $   1265.40
Month  4 - Income: $   1205.56         Total: $   2470.96
Month  5 - Income: $     12.35         Total: $   2483.31
Think about how to do this before reading on...

We need a list to store the incomes.
How do you add values to a list?

We need a counter variable (int) for the month number.
Remember that list indexes start at 0, but we want to print from 1.

How many loops will we need? What kind of loops?

We need a cumulative total to update as we loop through the list to display the incomes.

And lastly we need to format the output nicely, which we can use f-strings for.
----------------------------
Things to do:
Copy the starter code from total_income.py (remember to use Raw mode) and commit it to your own prac repo:

Study it to see how this code answers those questions so far.
Change the line that gets the income input so that it uses an f-string instead of string concatenation (+).

Problem: We have two variables that sound very similar: incomes and months.
They're both plural, so they sound like they're both lists. incomes is a list of incomes, so we might assume that months is a list of months, but it's actually a scalar value that stores the number of months - an int not a list.

Refactor the months variable to a better name.
DO NOT just change it in 3 places or use find and replace... but use refactoring in PyCharm by clicking anywhere on the variable and pressing Shift+F6 (or use the context menu).
Then rename it to something more meaningful, that sounds like a number not a list.
When naming variables, we can say, "This variable stores..." and the completion of that statement is usually a good name.
In this case, "This variable stores the... number of months". :)

Run the program again with some sample data and make sure it still works.
This kind of "regression testing" is important. Make sure you don't break anything!

Now, let's refactor (move) the report printing into its own function. Select those 6 lines and turn them into a new function with a good name.
When naming functions, we can say, "This function will..." and the completion of that statement is usually a good name for the function.
In this case, "This function will... print report". :)

Test again and make sure it's all good.

Double-check the report printing function you just wrote. Is it well-designed according to SRP? Does it take in _ only_ what it needs to know? Refactor it if you can make it better.
"""

def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    month_count = int(input("How many months? ")) # This variable stores the number of months

    for month in range(1, month_count + 1):
        income = float(input(f"Enter income for month {str(month)}: "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, month_count + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()