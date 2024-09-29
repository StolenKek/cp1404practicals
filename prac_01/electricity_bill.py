'''
CP1404/CP5632 - Practical
Create an electricity bill estimator.

Inputs should be:
price per kWh in cents,
daily use in kWh, and
number of days in the billing period.

Example use:
Electricity bill estimator
Enter cents per kWh: 35
Enter daily use in kWh: 4.5
Enter number of billing days: 90
Estimated bill: $141.75
====================================
(in the same file) Modify your bill estimator by asking the user to choose which tariff they are using - then use the
appropriate stored value for cents per kWh.
Start by defining two constants like below.
Constants in Python are just variables written in ALL_CAPITALS.

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
=====================================
Example use:

Electricity bill estimator 2.0
Which tariff? 11 or 31: 11
Enter daily use in kWh: 13.4
Enter number of billing days: 90
Estimated bill: $295.01
'''
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
tariff_choice = str(input("Which tariff? 11 or 31: "))


while tariff_choice != '11' and tariff_choice != '31':
    print("Enter a valid choice.")
    tariff_choice = input("Which tariff? 11 or 31: ")

daily_use_per_kilowatthour = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))

# Tariff calculation for TARIFF_11
if tariff_choice == '11':
    estimated_bill_11 = TARIFF_11 * daily_use_per_kilowatthour * billing_days
    print(f"Estimated bill: ${estimated_bill_11:.2f}")
# Tariff calculation for TARIFF_31
elif tariff_choice == '13':
    estimated_bill_31 = TARIFF_31 * daily_use_per_kilowatthour * billing_days
    print(f"Estimated bill: ${estimated_bill_31:.2f}")
