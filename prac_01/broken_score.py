"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

MINIMUM_THRESHOLD = 0
MAXIMUM_THRESHOLD = 100
PASSABLE_THRESHOLD = 50
EXCELLENT_THRESHOLD = 90

score = float(input("Enter score: "))

while score < MINIMUM_THRESHOLD or score > MAXIMUM_THRESHOLD:
    print("Invalid score")
    score = float(input("Enter score: "))

if score >= EXCELLENT_THRESHOLD:
    print("Excellent")
elif score >= PASSABLE_THRESHOLD:
    print("Passable")
else:
    print("Bad")