"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

get sales
while sales >= 0
    calculate bonus (this line is intentionally incomplete pseudocode)
    print bonus
    get sales
do next thing
"""
MINIMUM_THRESHOLD = 0
BONUS_THRESHOLD = 1000
UNDER_BONUS = 0.1
MET_BONUS = 0.15

sales = float(input("Enter sales: $"))

while sales <= 0:
    print("Enter a valid amount.")
    sales = float(input("Enter sales: $"))

if sales >= MINIMUM_THRESHOLD:
    bonus = sales * UNDER_BONUS

if sales >= BONUS_THRESHOLD:
    bonus = sales * MET_BONUS

print(f"Your bonus is ${bonus:.2f}")


