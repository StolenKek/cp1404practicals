# Practice 1

total_age = 0
user_count = 0

user_age = int(input("Enter Age: "))

while user_age >= 0:
    total_age = total_age + user_age
    user_count = user_count + 1
    user_age = int(input("Enter Age: "))

print(f"The total age of everyone is {total_age}")
print(f"The average age is {total_age / user_count}")

# Practice 2

'''
get number of gifts
get number of students

while number of gifts >= 0
    gifted gifts = number of gifts / number of students
    remainder = number of gifts - (gifted gifts * number of students)

print gifted gifts
print remainder
'''

gift_count = int(input("Enter number of gifts: "))
student_count = int(input("Enter number of students: "))

while gift_count >= 0:
    gifted_gifts = gift_count // student_count
    remaining_gifts = gift_count % student_count
    gift_count = int(input("Enter number of gifts: "))
    student_count = int(input("Enter number of students: "))

print(f"Each student gets {gifted_gifts} gifts.")
print(f"There will be {remaining_gifts} gifts left.")

# Practice 3

GST = 0.09

item_price = float(input("Enter item price: "))
has_gst = str(input("Does it have GST? (Y/N): ")).upper()

if has_gst == "Y":
    new_price = item_price + (item_price * GST)

print(f"Your item price is ${new_price:.2f}")

# Practice 4

# a. Using While loop
number = 0

number_limit = int(input("Enter the limit: "))

while number <= number_limit:
    print(f"{number}")
    number +=1


# b. Using For loop
number = 0

number_limit = int(input("Enter the limit: "))

for number in range(1, number_limit + 1):
    print(f"{number}")

# Practice 5
NUMBER = 1

guess = int(input("Guess a number (1-10): "))

while guess != NUMBER:
    print("Guess again :P")
    guess = int(input("Guess a number (1-10): "))

print("You got it! :D")

# Practice 6

user_name = input("Enter name: ").upper()

while user_name == "":
    print("Enter name again.")
    user_name = input("Enter name: ").upper()

user_salary = float(input("Enter salary: "))

while user_salary < 0:
    print("Enter salary again.")
    user_salary = float(input("Enter salary: "))

print(f"Hello {user_name}. Your salary is ${user_salary:.2f}")

# Practice 7a
total_age = 0
age_count = int(input("Enter how many ages you want: "))

for n in range(age_count):
    age = int(input("Enter age: "))
    total_age += age
    average_age = total_age/age_count

print(f"The total of the ages is {total_age} and the average of the ages is {average_age}.")

# Practice 7b
total_age = 0
age_count = 0

age = int(input("Enter age: "))

while age > -1:
    total_age += age
    age_count += 1
    age = int(input("Enter age: "))

average_age = total_age/age_count

print(f"The total of the ages is {total_age} and the average of the ages is {average_age}.")

