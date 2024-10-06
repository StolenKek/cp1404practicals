import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
What did you see on line 1?
What was the smallest number you could have seen, what was the largest?
"""
# The number that generated for me was 19. The smallest number that could come up is 5 and the largest would be 20.

"""
What did you see on line 2?
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?
"""
# The number that generated for me was 9. The smallest number that could come up is 3 and the largest would be 9.
# 4 cannot come up because the step count is a 2

"""
What did you see on line 3?
What was the smallest number you could have seen, what was the largest?
"""
# The number that generated for me was 3.974754794767607.
# The smallest would be a float number slightly more than 2.5 and the largest would be slightly less than 5.5.

"""
Write code, not a comment, to produce a random number between 1 and 100 inclusive.
"""
import random

random_number = random.randint(1, 100)
print(random_number)