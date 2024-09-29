'''
CP1404/CP5632 - Practical
A shop requires a small program that would allow them to quickly work out the total
price for a number of items, each with different prices.

The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the screen.

Sample output:
The output should look like the sample below (where bold text represents user input).
This uses f-string formatting to set the currency to 2 decimal places.

Number of items: 3
Price of item: 100
Price of item: 35.56
Price of item: 3.24
Total price for 3 items is $124.92
'''

DISCOUNT_THRESHOLD = 100
DISCOUNT_AMOUNT = 0.1

item_count = int(input("Number of items: "))

# Error checking for item_count
while item_count < 0:
    print("Invalid number of items!")
    item_count = int(input("Number of items "))

total_price = 0

# Loop to enter price and calculate total price
for i in range(1, item_count + 1):
    item_price = float(input(f"Price of item:: $"))

    # Error checking for item_price
    while item_price < 0:
        print("Invalid price!")
        item_price = float(input(f"Price of item:: $"))

    total_price += item_price

# Apply a 10% discount when total price > $100
if total_price > DISCOUNT_THRESHOLD:
    discounted_price = total_price * DISCOUNT_AMOUNT
    total_price -= discounted_price

# Display the total price (2 decimal places)
print(f"Total price for {item_count} items is ${total_price:.2f}")
