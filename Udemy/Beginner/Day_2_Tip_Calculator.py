# #!/bin/python

# ################################################################################
# # Programmer: Allie
# # File: Day_2_Tip_Calculator.py
# Coding Exercise 2.1: Sum of Double Digits
# Coding Exercise 2.2: BMI Calculator
# Coding Exercise 2.3: Life in weeks
# Coding Project 2.A: Tip Calculator
# # Subjects: Data Types (Strings, Integers, Float, Booleans), Rounding function, and f-Strings
# # Date: February 28, 2022
# ################################################################################

# Large Integers: writing large numbers with commas like 123,456,789 you put '_' like 123_456_789

# Coding Exercise 2.1: Add the sum of a double digit number together
# (i.e. 26 = 8; 13 = 4)
two_digit_number = input("Type a two digit number.\n")
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
sum_of_digits = first_digit + second_digit
print("The sum of the two digits is " + str(sum_of_digits))


# Coding Exercise 2.2: BMI Calculator
height = input("enter your height in m:")
weight = input("enter your height in kg:")
bmi_equation1 = float(weight) / (float(height)**2)
# or
bmi_equation2 = float(weight) / (float(height) * float(height))
print(bmi_equation1)
# Rounding function:
# (Item we are rounding, # of decimal places)
# (8/3, 2) -> 2.67
# Calculating for an integer:
# Using two forward slashes will save as an integer rather than a float
# (4 / 2 ) -> float
# (4 // 2 ) -> Integer
# F-Strings:
# Purpose: Concatenate different data types such as a string, float, integer, etc.
# 1. The letter 'f' needs to be in front of the single or double quotes
#       print(f"Your score is")
# 2. Use curly brackets to enter the other data types
#       print(f"Your score is {score}, your height is {height}, your age is {age}")

# Coding Exercise 2.3: Life in Weeks
age = input("What is your current age ? \n")
# 1 year = 365 days = 52 weeks = 12 months
age_remaining = 90 - int(age)
print(age_remaining)
x = age_remaining * 365
y = age_remaining * 52
z = age_remaining * 12
print(f"You have {x} days, {y} weeks, and {z} months left")


# Coding Project 2.A: Tip Calculator
# 1. Create a greeting
print("Welcome to the Tip Calculator.")
# 2. Ask the User for the total bill
total_bill = input("What was the total bill ? \n")
# 3. Ask the user how many people the bill will be split by
total_individuals = input("How many people to split the bill \n")
# 4. Ask the user what percentage would they like to give
tip_percentage = input(
    "What percentage tip would you like to give ? 10, 12, or 15? \n")
# 5. Calculate the amount each person should pay including tip percentage
before_tip = float(total_bill) / float(total_individuals)
tip_only = before_tip * float(tip_percentage) / 100
total_pp = before_tip + tip_only
print("Each person should pay: $" + str(round(total_pp, 2)))
