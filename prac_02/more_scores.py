"""
CP1404 - Practical 2
Scores program

"""

import random

MINIMUM_THRESHOLD = 0
MAXIMUM_THRESHOLD = 100
PASSABLE_THRESHOLD = 50
EXCELLENT_THRESHOLD = 90

# Determine_result function from score.py
def determine_result(score):
    """Determine the result based on the score."""
    if score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score >= PASSABLE_THRESHOLD:
        return "Passable"
    else:
        return "Bad"

def main():
    """Main program to generate random scores and write results to a file."""
    # Ask the user for the number of scores to generate
    number_of_scores = int(input("Enter the number of scores: "))

    # Open a file to write results
    with open("results.txt", "w") as file:
        # Generate random scores and write the results to the file
        for _ in range(number_of_scores):
            score = random.randint(MINIMUM_THRESHOLD, MAXIMUM_THRESHOLD)  # Generate random score
            result = determine_result(score)  # Determine the result for this score
            file.write(f"{score} is {result}\n")  # Write to file

    print(f"{number_of_scores} scores written to results.txt")

if __name__ == "__main__":
    main()